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
import re
import sys
import unicodedata
import xml.etree.ElementTree as ET

NS = {"lc": "http://www.leychile.cl/esquemas"}

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
                nombre_parte = np.text.strip()
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
    p.add_argument("--xml", required=True, help="Ruta al XML oficial de LeyChile")
    p.add_argument("--articulos", help="Especificación: '1-18,50-78,97 bis,FINAL'")
    p.add_argument("--sigla", default="NORMA", help="Sigla del cuerpo (CP, CPP, CT)")
    p.add_argument("--idnorma", help="idNorma esperado, para validar la fuente")
    p.add_argument("--out", help="Archivo de salida Markdown")
    p.add_argument("--sin-variantes", action="store_true",
                   help="Los rangos NO incluyen artículos bis/ter/quáter")
    p.add_argument("--incluir-transitorios", action="store_true")
    p.add_argument("--fecha-verificacion", help="AAAA-MM-DD (por defecto, hoy)")
    p.add_argument("--listar", action="store_true",
                   help="Solo inventaría los artículos del XML")
    args = p.parse_args(argv)

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
