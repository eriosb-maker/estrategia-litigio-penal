#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
curar_norma.py — Motor de curatoría normativa para la skill analisis-penal-chile.

Procesa el XML oficial de una norma chilena obtenido del servicio de la
Biblioteca del Congreso Nacional (LeyChile), conforme al esquema
EsquemaIntercambioNorma-v1-0.xsd documentado en
https://www.leychile.cl/esquemas/accesoLeyesChilenas4.pdf, y extrae los
artículos indicados en formato Markdown de curatoría, con trazabilidad
completa: idNorma, idParte, fecha de versión de cada artículo, estado de
derogación y fecha de verificación.

Obtención del XML de origen (a cargo del abogado, desde la fuente oficial):
    https://www.leychile.cl/Consulta/obtxml?opt=7&idNorma=1984      (Código Penal)
    https://www.leychile.cl/Consulta/obtxml?opt=7&idNorma=176595    (Código Procesal Penal)
    (parámetro opcional &notaPIE=1 para incluir notas al pie de la BCN)

Uso:
    python curar_norma.py --xml codigo_penal.xml \
        --articulos "1-18,50-78,93-105" \
        --sigla "CP" --idnorma 1984 \
        --out extracto_cp_nucleo.md

    python curar_norma.py --xml codigo_penal.xml --listar
        (inventaría los artículos disponibles sin generar extracto)

    python curar_norma.py --resolver "Ley 21595"
    python curar_norma.py --resolver "Codigo Tributario"
        (resuelve el idNorma de una norma a partir de su identificador;
        ver sección «Resolución automática de idNorma» más abajo)

    python curar_norma.py --descargar 1195119 --out ley-21595.xml
        (descarga el XML oficial desde obtxml, calcula su SHA-256 y lo
        deja registrado en la consola para trazabilidad)

Resolución automática de idNorma:
    El identificador interno (idNorma) que exige `--idnorma` no coincide con
    el número de la ley o decreto ley. `--resolver` lo obtiene por dos vías:
    (a) un registro local de normas ya verificadas en esta skill (Código
    Penal, Código Procesal Penal, Código Tributario, Leyes de Renta e IVA,
    y las cinco leyes especiales curadas), y (b) para normas del tipo «Ley
    N°» no registradas, consulta en línea el servicio de LeyChile
    `nuevo.leychile.cl/servicios/Navegar?idLey=<N>` y extrae el idNorma del
    enlace canónico de la página — mecanismo NO documentado oficialmente
    por la BCN (el servicio `obtxml` sí admite `idLey` directamente para
    normas de tipo «Ley», conforme al accesoLeyesChilenas4.pdf, pero ese
    parámetro no resuelve decretos leyes ni códigos). Para decretos leyes,
    decretos con fuerza de ley o normas ambiguas no registradas, el
    resolver así lo advierte: no existe un servicio de búsqueda oficial
    documentado por número+tipo, y la identificación del idNorma requiere
    verificación manual del abogado (o del asistente mediante herramientas
    de búsqueda web, con registro expreso de la fuente) antes de curar.
    Requiere conexión a internet; no se ejecuta como parte de la suite
    pytest (las pruebas de red se omiten mediante mocks).

Reglas del motor:
  1. Los rangos numéricos (p. ej. "229-241") incluyen por defecto las
     variantes bis/ter/quáter/quinquies/sexies de los números comprendidos,
     salvo que se invoque --sin-variantes.
  2. Los artículos derogados se incluyen SOLO con la marca [DEROGADO] y sin
     texto, para preservar la advertencia sin engrosar el módulo.
  3. Los artículos transitorios se excluyen salvo --incluir-transitorios.
  4. Todo extracto queda encabezado con los metadatos de la norma y la fecha
     de verificación, condición de validez de la curatoría conforme a la
     regla de cita normativa rigurosa del SKILL.md (sección 7).

La salida es un INSUMO para `references/marco-legal.md`; su incorporación
definitiva queda sujeta a revisión del abogado responsable.
"""

import argparse
import datetime
import hashlib
import re
import sys
import unicodedata
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET

NS = {"lc": "http://www.leychile.cl/esquemas"}

OBTXML_URL = "https://www.leychile.cl/Consulta/obtxml?opt=7&idNorma={idnorma}"
NAVEGAR_IDLEY_URL = "https://nuevo.leychile.cl/servicios/Navegar?idLey={numero}"
USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/126.0 Safari/537.36"
)

# Registro local de normas ya verificadas por esta skill (idNorma confirmado
# mediante descarga real y cotejo del atributo normaId del XML). Se amplía
# cada vez que una curatoría nueva confirma un idNorma; no reemplaza la
# verificación documentada en `references/marco-legal.md` y
# `references/leyes-especiales.md`, que es la fuente de trazabilidad
# canónica.
REGISTRO_IDNORMA = {
    "CP": (1984, "Código", "Código Penal"),
    "CODIGO PENAL": (1984, "Código", "Código Penal"),
    "CPP": (176595, "Ley", "Código Procesal Penal (Ley 19.696)"),
    "CODIGO PROCESAL PENAL": (176595, "Ley", "Código Procesal Penal (Ley 19.696)"),
    "CT": (6374, "Decreto Ley", "Código Tributario (DL 830)"),
    "CODIGO TRIBUTARIO": (6374, "Decreto Ley", "Código Tributario (DL 830)"),
    "DL 830": (6374, "Decreto Ley", "Código Tributario"),
    "DECRETO LEY 830": (6374, "Decreto Ley", "Código Tributario"),
    "DL 824": (6368, "Decreto Ley", "Ley sobre Impuesto a la Renta"),
    "DECRETO LEY 824": (6368, "Decreto Ley", "Ley sobre Impuesto a la Renta"),
    "LEY DE RENTA": (6368, "Decreto Ley", "Ley sobre Impuesto a la Renta (DL 824)"),
    "LIR": (6368, "Decreto Ley", "Ley sobre Impuesto a la Renta (DL 824)"),
    "DL 825": (6369, "Decreto Ley", "Ley sobre Impuesto a las Ventas y Servicios"),
    "DECRETO LEY 825": (6369, "Decreto Ley", "Ley sobre Impuesto a las Ventas y Servicios"),
    "LEY DE IVA": (6369, "Decreto Ley", "Ley sobre Impuesto a las Ventas y Servicios (DL 825)"),
    "IVA": (6369, "Decreto Ley", "Ley sobre Impuesto a las Ventas y Servicios (DL 825)"),
    "LEY 21595": (1195119, "Ley", "Ley de Delitos Económicos"),
    "LEY 20393": (1008668, "Ley", "Responsabilidad Penal de las Personas Jurídicas"),
    "LEY 19913": (219119, "Ley", "UAF y lavado de activos"),
    "LEY 21459": (1177743, "Ley", "Delitos Informáticos"),
    "LEY 20000": (235507, "Ley", "Tráfico Ilícito de Estupefacientes"),
}


def _normalizar_clave_registro(texto):
    t = unicodedata.normalize("NFD", texto.upper())
    t = "".join(c for c in t if unicodedata.category(c) != "Mn")
    # Elimina el indicador ordinal «N°»/«Nº» (p. ej. "LEY N° 21595" ->
    # "LEY 21595"), exigiendo el símbolo de grado para no arrasar con
    # cualquier "N" de una palabra ordinaria (p. ej. "PENAL", "RENTA").
    t = re.sub(r"\bN[°º]\s*", "", t)
    t = re.sub(r"[°ºª]", "", t)
    return re.sub(r"\s+", " ", t).strip()


def resolver_desde_registro(consulta):
    """Busca la consulta en REGISTRO_IDNORMA (normas ya verificadas)."""
    clave = _normalizar_clave_registro(consulta)
    if clave in REGISTRO_IDNORMA:
        idnorma, tipo, descripcion = REGISTRO_IDNORMA[clave]
        return {
            "idnorma": idnorma, "tipo": tipo, "descripcion": descripcion,
            "fuente": "registro local (idNorma verificado en curatoría previa)",
        }
    return None


def resolver_por_idley(numero, _opener=None):
    """Resuelve el idNorma de una norma tipo «Ley N°» consultando LeyChile.

    Consulta `nuevo.leychile.cl/servicios/Navegar?idLey=<numero>` (mecanismo
    NO documentado oficialmente; server-side rendering observado
    empíricamente) y extrae el idNorma del `<link rel="canonical">`. Lanza
    ValueError si la norma no es de tipo «Ley» o no se encuentra.

    `_opener` permite inyectar un abridor de URL alternativo en pruebas,
    evitando tráfico de red real.
    """
    abrir = _opener or (lambda req: urllib.request.urlopen(req, timeout=30))
    url = NAVEGAR_IDLEY_URL.format(numero=numero)
    solicitud = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with abrir(solicitud) as respuesta:
        html = respuesta.read().decode("utf-8", errors="replace")
    m = re.search(r'<link rel="canonical" href="[^"]*idNorma=(\d+)', html)
    if not m:
        raise ValueError(
            f"No fue posible resolver el idNorma para «Ley {numero}»: la "
            "norma podría no ser de tipo Ley (el parámetro idLey solo "
            "resuelve normas tipo «Ley»; para decretos leyes, DFL o "
            "códigos, verifique el idNorma manualmente en leychile.cl y "
            "regístrelo con --idnorma)."
        )
    idnorma = int(m.group(1))
    tm = re.search(r"<title>([^<]+)</title>", html)
    titulo = tm.group(1).strip() if tm else "s/d"
    return {
        "idnorma": idnorma, "tipo": "Ley", "descripcion": titulo,
        "fuente": f"resolución en línea vía idLey={numero} (no oficial/no documentada)",
    }


def resolver_norma(consulta, _opener=None):
    """Resuelve el idNorma de `consulta` (sigla, «Ley N°» o descripción).

    Orden: (1) registro local de normas ya verificadas; (2) si la consulta
    contiene un número y no fue hallada en el registro, intenta resolución
    en línea asumiendo tipo «Ley». Lanza ValueError si ninguna vía resuelve.
    """
    hallazgo = resolver_desde_registro(consulta)
    if hallazgo:
        return hallazgo
    m = re.search(r"(\d{3,6})", consulta)
    if m:
        return resolver_por_idley(int(m.group(1)), _opener=_opener)
    raise ValueError(
        f"No fue posible resolver «{consulta}»: no consta en el registro "
        "local ni contiene un número identificable. Verifique manualmente "
        "en leychile.cl y use --idnorma con el valor confirmado."
    )


def descargar_xml(idnorma, destino, nota_pie=False, _opener=None):
    """Descarga el XML oficial de `idnorma` desde el servicio obtxml,
    lo guarda en `destino` y devuelve (bytes_descargados, sha256_hex).

    Requiere conexión a internet; `_opener` permite mockear en pruebas.
    """
    abrir = _opener or (lambda req: urllib.request.urlopen(req, timeout=60))
    url = OBTXML_URL.format(idnorma=idnorma)
    if nota_pie:
        url += "&notaPIE=1"
    solicitud = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with abrir(solicitud) as respuesta:
        contenido = respuesta.read()
    if b'normaId="' not in contenido[:2000]:
        raise ValueError(
            f"La respuesta de idNorma={idnorma} no parece un XML válido de "
            "LeyChile (falta el atributo normaId); verifique el idNorma."
        )
    with open(destino, "wb") as f:
        f.write(contenido)
    return len(contenido), hashlib.sha256(contenido).hexdigest()

SUFIJOS_VALIDOS = (
    "", "BIS", "TER", "QUATER", "QUÁTER", "QUINQUIES", "SEXIES",
    "SEPTIES", "OCTIES",
)


def _normalizar(texto):
    """Mayúsculas sin tildes, para comparar sufijos (QUÁTER == QUATER).

    Elimina además los indicadores ordinales que algunas leyes recientes
    usan en la numeración de sus artículos («Art. 1°», «Art. 8º»), de modo
    que '1°' y '1' se comparen como el mismo número."""
    t = unicodedata.normalize("NFD", texto.upper())
    t = "".join(c for c in t if unicodedata.category(c) != "Mn")
    return t.replace("°", "").replace("º", "").replace("ª", "").strip()


def parsear_nombre_parte(nombre):
    """Descompone NombreParte ('24 BIS', '97', 'FINAL') en (número, sufijo).

    Devuelve (None, nombre_normalizado) cuando la parte no es numérica
    (p. ej. 'FINAL', 'UNICO').
    """
    limpio = _normalizar(nombre)
    m = re.match(r"^(\d+)\s*([A-Z]+(?:\s+[A-Z]+)*)?$", limpio)
    if not m:
        return None, limpio
    numero = int(m.group(1))
    sufijo = re.sub(r"\s+", " ", m.group(2) or "").strip()
    return numero, sufijo


def parsear_especificacion(spec):
    """Convierte '1-18,50-78,97 bis,FINAL' en una lista de criterios.

    Cada criterio es:
      ('rango', a, b)           → números a..b (con o sin variantes según flag)
      ('exacto', numero, suf)   → artículo puntual, p. ej. (97, 'BIS')
      ('nombre', texto)         → parte no numérica, p. ej. 'FINAL'
    """
    criterios = []
    for token in spec.split(","):
        token = token.strip()
        if not token:
            continue
        t = _normalizar(token)
        m_rango = re.match(r"^(\d+)\s*-\s*(\d+)$", t)
        if m_rango:
            a, b = int(m_rango.group(1)), int(m_rango.group(2))
            if a > b:
                a, b = b, a
            criterios.append(("rango", a, b))
            continue
        m_exacto = re.match(r"^(\d+)\s*([A-Z]+(?:\s+[A-Z]+)*)?$", t)
        if m_exacto:
            criterios.append(
                ("exacto", int(m_exacto.group(1)), re.sub(r"\s+", " ", m_exacto.group(2) or "").strip()))
            continue
        criterios.append(("nombre", t))
    return criterios


def articulo_seleccionado(numero, sufijo, nombre_crudo, criterios,
                          con_variantes=True):
    for c in criterios:
        if c[0] == "rango" and numero is not None:
            if c[1] <= numero <= c[2]:
                if con_variantes or sufijo == "":
                    return True
        elif c[0] == "exacto" and numero is not None:
            if numero == c[1] and sufijo == c[2]:
                return True
        elif c[0] == "nombre" and numero is None:
            if nombre_crudo == c[1]:
                return True
    return False


def _limpiar_disambiguador_articulado(nombre):
    """Quita el sufijo parentético «(DEL ART. 1)» / «(DEL ART 1)» / «(ART 1)»
    que la BCN antepone a los artículos internos de normas con estructura de
    «Doble Articulado» (p. ej. el Código Tributario, DL 830, cuyo art. 97
    figura en el XML como NombreParte «97 (DEL ART. 1)»). El sufijo identifica
    el artículo promulgatorio contenedor, no el número del artículo citable;
    se elimina para que la selección numérica y la etiqueta de salida
    reflejen la cita real («art. 97 CT», no «art. 97 (DEL ART. 1) CT»)."""
    return re.sub(r"\s*\(\s*DEL\s+ART\.?\s+\d+\s*\)\s*$", "", nombre,
                  flags=re.IGNORECASE).strip()


def recorrer_articulos(elemento, ruta=()):
    """Recorre recursivamente EstructurasFuncionales y rinde cada artículo
    junto con la ruta de agrupadores (Libro/Título/Párrafo) que lo contiene."""
    for ef in elemento.findall("lc:EstructurasFuncionales/lc:EstructuraFuncional", NS):
        tipo = ef.get("tipoParte", "")
        meta = ef.find("lc:Metadatos", NS)
        titulo_parte = ""
        nombre_parte = ""
        if meta is not None:
            tp = meta.find("lc:TituloParte", NS)
            np = meta.find("lc:NombreParte", NS)
            if tp is not None and tp.get("presente") == "si" and tp.text:
                titulo_parte = " ".join(tp.text.split())
            if np is not None and np.get("presente") == "si" and np.text:
                nombre_parte = _limpiar_disambiguador_articulado(np.text.strip())
        if tipo == "Artículo" or tipo == "Artículo Transitorio":
            yield ef, nombre_parte, ruta
            # Normas promulgatorias con articulado anidado («Doble
            # Articulado», p. ej. Ley 20.393: el Artículo PRIMERO contiene
            # el estatuto completo): se desciende también al interior del
            # artículo para inventariar y extraer los artículos internos.
            nueva_ruta = ruta + ((f"Artículo {nombre_parte}".strip(),)
                                 if nombre_parte else (tipo,))
            yield from recorrer_articulos(ef, nueva_ruta)
        else:
            nueva_ruta = ruta + ((titulo_parte or tipo),) if (titulo_parte or tipo) else ruta
            yield from recorrer_articulos(ef, nueva_ruta)


def limpiar_texto(texto):
    """Normaliza el texto del artículo: quita sangría fija y marcas marginales
    de referencia interna del visor ('VER NOTA n') sin alterar el contenido."""
    lineas = []
    for linea in texto.splitlines():
        linea = re.sub(r"\s+(VER\s+)?NOTA\s*:?\s*\d*\s*$", "", linea.rstrip())
        lineas.append(linea)
    cuerpo = "\n".join(lineas)
    cuerpo = re.sub(r"\n{3,}", "\n\n", cuerpo).strip("\n")
    return cuerpo


def cargar_norma(ruta_xml):
    arbol = ET.parse(ruta_xml)
    raiz = arbol.getroot()
    metadatos = {
        "normaId": raiz.get("normaId", "s/d"),
        "fechaVersion": raiz.get("fechaVersion", "s/d"),
        "derogado": raiz.get("derogado", "s/d"),
        "titulo": "s/d",
        "tipo_numero": "",
        "fechaPublicacion": "s/d",
    }
    tit = raiz.find("lc:Metadatos/lc:TituloNorma", NS)
    if tit is not None and tit.text:
        metadatos["titulo"] = " ".join(tit.text.split())
    ident = raiz.find("lc:Identificador", NS)
    if ident is not None:
        metadatos["fechaPublicacion"] = ident.get("fechaPublicacion", "s/d")
        tn = ident.find("lc:TiposNumeros/lc:TipoNumero", NS)
        if tn is not None:
            tipo = tn.find("lc:Tipo", NS)
            numero = tn.find("lc:Numero", NS)
            metadatos["tipo_numero"] = " ".join(
                x.text.strip() for x in (tipo, numero)
                if x is not None and x.text)
    return raiz, metadatos


def generar_extracto(ruta_xml, spec, sigla, idnorma_esperado=None,
                     con_variantes=True, incluir_transitorios=False,
                     fecha_verificacion=None):
    raiz, meta = cargar_norma(ruta_xml)
    if idnorma_esperado and str(meta["normaId"]) != str(idnorma_esperado):
        raise SystemExit(
            f"ERROR: el XML corresponde a la norma id {meta['normaId']}, "
            f"no a la esperada ({idnorma_esperado}). Verifique la fuente.")
    criterios = parsear_especificacion(spec)
    fecha_verificacion = fecha_verificacion or datetime.date.today().isoformat()

    encontrados, faltantes = [], []
    vistos = set()
    for ef, nombre, ruta in recorrer_articulos(raiz):
        if ef.get("transitorio") == "transitorio" and not incluir_transitorios:
            continue
        numero, sufijo = parsear_nombre_parte(nombre or "")
        if sufijo not in SUFIJOS_VALIDOS and numero is not None:
            sufijo_cmp = sufijo
        else:
            sufijo_cmp = sufijo
        if not articulo_seleccionado(numero, sufijo_cmp, _normalizar(nombre or ""),
                                     criterios, con_variantes):
            continue
        texto_el = ef.find("lc:Texto", NS)
        texto = limpiar_texto(texto_el.text or "") if texto_el is not None else ""
        etiqueta = (nombre or "").strip() or "s/n"
        clave = (numero, sufijo_cmp, etiqueta)
        if clave in vistos:
            continue
        vistos.add(clave)
        encontrados.append({
            "numero": numero,
            "sufijo": sufijo_cmp,
            "etiqueta": etiqueta,
            "idParte": ef.get("idParte", "s/d"),
            "fechaVersion": ef.get("fechaVersion", "s/d"),
            "derogado": ef.get("derogado") == "derogado",
            "ruta": " › ".join(ruta),
            "texto": texto,
        })

    # Verificación de completitud: números pedidos por rango o exactos que no aparecieron.
    presentes = {(a["numero"], a["sufijo"]) for a in encontrados if a["numero"]}
    for c in criterios:
        if c[0] == "rango":
            for n in range(c[1], c[2] + 1):
                if (n, "") not in presentes:
                    faltantes.append(f"Art. {n}")
        elif c[0] == "exacto":
            if (c[1], c[2]) not in presentes:
                faltantes.append(f"Art. {c[1]} {c[2]}".strip())

    encontrados.sort(key=lambda a: (a["numero"] if a["numero"] is not None else 10**9,
                                    SUFIJOS_VALIDOS.index(a["sufijo"].split(" ")[0])
                                    if a["sufijo"].split(" ")[0] in SUFIJOS_VALIDOS else 99,
                                    a["sufijo"]))

    lineas = []
    lineas.append(f"## {meta['titulo']} ({sigla})")
    lineas.append("")
    lineas.append(f"> **Fuente oficial**: Biblioteca del Congreso Nacional — LeyChile, "
                  f"servicio XML `obtxml opt=7`, idNorma {meta['normaId']} "
                  f"({meta['tipo_numero'] or 'norma'}), publicada el {meta['fechaPublicacion']}.")
    lineas.append(f"> **Versión de la norma**: {meta['fechaVersion']} · "
                  f"**Estado**: {meta['derogado']}.")
    lineas.append(f"> **Fecha de verificación de esta curatoría**: {fecha_verificacion}. "
                  f"Todo uso posterior debe cotejar la vigencia en LeyChile.")
    lineas.append("")
    for a in encontrados:
        encabezado = f"### {sigla} — Art. {a['etiqueta']}"
        lineas.append(encabezado)
        ubic = f"*{a['ruta']}*" if a["ruta"] else ""
        traz = (f"`idParte {a['idParte']} · versión del artículo: "
                f"{a['fechaVersion']}`")
        lineas.append(" ".join(x for x in (ubic, "—", traz) if x).strip(" —"))
        lineas.append("")
        if a["derogado"]:
            lineas.append("**[DEROGADO]** — El texto se omite deliberadamente; "
                          "verificar la norma derogatoria en LeyChile.")
        else:
            lineas.append("```")
            lineas.append(a["texto"])
            lineas.append("```")
        lineas.append("")
    if faltantes:
        lineas.append("---")
        lineas.append("**Advertencia de completitud** — Los siguientes artículos del "
                      "perímetro solicitado no constan en el XML procesado (pueden no "
                      "existir en la numeración del cuerpo, estar refundidos o requerir "
                      "verificación manual): " + ", ".join(faltantes) + ".")
        lineas.append("")
    return "\n".join(lineas), encontrados, faltantes


def listar_inventario(ruta_xml):
    raiz, meta = cargar_norma(ruta_xml)
    print(f"# {meta['titulo']} — idNorma {meta['normaId']} — "
          f"versión {meta['fechaVersion']}")
    n = 0
    for ef, nombre, ruta in recorrer_articulos(raiz):
        marca = " [DEROGADO]" if ef.get("derogado") == "derogado" else ""
        marca += " [TRANSITORIO]" if ef.get("transitorio") == "transitorio" else ""
        print(f"Art. {nombre or 's/n':<12} v.{ef.get('fechaVersion','s/d')}"
              f"{marca}  ({' › '.join(ruta)})")
        n += 1
    print(f"\nTotal de artículos inventariados: {n}")


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--xml", help="Ruta al XML oficial de LeyChile")
    p.add_argument("--articulos", help="Especificación: '1-18,50-78,97 bis,FINAL'")
    p.add_argument("--sigla", default="NORMA", help="Sigla del cuerpo (CP, CPP, CT)")
    p.add_argument("--idnorma", help="idNorma esperado, para validar la fuente")
    p.add_argument("--out", help="Archivo de salida Markdown, o de destino con --descargar")
    p.add_argument("--sin-variantes", action="store_true",
                   help="Los rangos NO incluyen artículos bis/ter/quáter")
    p.add_argument("--incluir-transitorios", action="store_true")
    p.add_argument("--fecha-verificacion", help="AAAA-MM-DD (por defecto, hoy)")
    p.add_argument("--listar", action="store_true",
                   help="Solo inventaría los artículos del XML")
    p.add_argument("--resolver",
                   help="Resuelve el idNorma de una norma (sigla, «Ley N°» o "
                        "descripción registrada); requiere conexión a internet "
                        "para normas no registradas localmente")
    p.add_argument("--descargar", type=int, metavar="IDNORMA",
                   help="Descarga el XML oficial del idNorma indicado hacia "
                        "--out; requiere conexión a internet")
    p.add_argument("--nota-pie", action="store_true",
                   help="Con --descargar: incluye notas al pie de la BCN (notaPIE=1)")
    args = p.parse_args(argv)

    if args.resolver:
        try:
            hallazgo = resolver_norma(args.resolver)
        except ValueError as e:
            print(f"ERROR: {e}", file=sys.stderr)
            return 1
        print(f"idNorma: {hallazgo['idnorma']}")
        print(f"Tipo: {hallazgo['tipo']}")
        print(f"Descripción: {hallazgo['descripcion']}")
        print(f"Fuente de la resolución: {hallazgo['fuente']}")
        print(f"URL de descarga: {OBTXML_URL.format(idnorma=hallazgo['idnorma'])}")
        return 0

    if args.descargar is not None:
        if not args.out:
            p.error("--descargar requiere --out con la ruta de destino")
        try:
            tamano, sha256 = descargar_xml(args.descargar, args.out,
                                           nota_pie=args.nota_pie)
        except (ValueError, urllib.error.URLError) as e:
            print(f"ERROR: {e}", file=sys.stderr)
            return 1
        print(f"Descargado: {args.out} — {tamano} bytes")
        print(f"SHA-256: {sha256}")
        print("Registre este hash en el módulo de referencia correspondiente, "
              "conforme al protocolo de curatoría.")
        return 0

    if not args.xml:
        p.error("--xml es obligatorio salvo en modo --resolver o --descargar")

    if args.listar:
        listar_inventario(args.xml)
        return 0
    if not args.articulos:
        p.error("--articulos es obligatorio salvo en modo --listar")

    md, encontrados, faltantes = generar_extracto(
        args.xml, args.articulos, args.sigla, args.idnorma,
        con_variantes=not args.sin_variantes,
        incluir_transitorios=args.incluir_transitorios,
        fecha_verificacion=args.fecha_verificacion)

    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(md)
        print(f"Extracto generado: {args.out} — {len(encontrados)} artículos"
              + (f"; {len(faltantes)} no hallados" if faltantes else ""))
    else:
        print(md)
    return 0


if __name__ == "__main__":
    sys.exit(main())
