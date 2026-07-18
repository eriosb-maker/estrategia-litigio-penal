#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
curar_jurisprudencia.py — Motor de curatoría jurisprudencial para la skill
analisis-penal-chile (línea IV del plan de mejoras, v4.6, 2026-07-12).

OBJETO. Administrar el registro `references/jurisprudencia-curada.md`
conforme a su protocolo: asignación de identificadores estables J-0NN
(jamás reasignados), cómputo del SHA-256 del texto normalizado del
considerando, verificación copulativa de las condiciones del estado [V]
y auditoría de consistencia del registro completo.

LIMITACIÓN ESTRUCTURAL. No existe fuente oficial estructurada de
jurisprudencia chilena accesible desde este entorno. Este motor NO
descarga sentencias ni valida su existencia ante el Poder Judicial: el
texto del considerando lo aporta el titular desde la fuente que tiene a
la vista. El motor fija, sella y audita; no verifica la realidad externa
del fallo. Esa verificación es acto humano del abogado responsable.

USO:
    python curar_jurisprudencia.py --plantilla > ficha.json
    python curar_jurisprudencia.py --validar ficha.json
    python curar_jurisprudencia.py --agregar ficha.json \
        --registro references/jurisprudencia-curada.md
    python curar_jurisprudencia.py --verificar references/jurisprudencia-curada.md
    python curar_jurisprudencia.py --listar references/jurisprudencia-curada.md

SALIDA: 0 conforme · 1 defectos o ficha inválida · 2 error de uso o E/S.
"""

import argparse
import hashlib
import json
import re
import sys
import unicodedata
from datetime import date

ESTADOS = ("[V]", "[PV]", "[NU]", "[S]")

CAMPOS_OBLIGATORIOS = (
    "estado",
    "tribunal",
    "rol",
    "fecha_sentencia",
    "considerandos",
    "tesis",
    "materia",
)

# Copulativos para [V] (además de los obligatorios generales):
CAMPOS_V = ("texto_considerando", "fuente_texto", "fecha_verificacion")

MARCA_INICIO = "<!-- INICIO-REGISTRO-FICHAS -->"
MARCA_FIN = "<!-- FIN-REGISTRO-FICHAS -->"

RE_FECHA = re.compile(r"^\d{4}-\d{2}-\d{2}$")
RE_ID = re.compile(r"^### (J-\d{3,})\b")


# ---------------------------------------------------------------- utilidades
def normalizar(texto: str) -> str:
    """Normaliza el texto del considerando antes del hash: Unicode NFC,
    recorte de extremos y colapso de todo espacio interno a un único
    espacio. Diferencias tipográficas irrelevantes no alteran el hash;
    cualquier alteración de contenido, sí."""
    t = unicodedata.normalize("NFC", texto)
    return re.sub(r"\s+", " ", t).strip()


def hash_texto(texto: str) -> str:
    return hashlib.sha256(normalizar(texto).encode("utf-8")).hexdigest()


def _err(msg: str) -> None:
    print(f"  [DEFECTO] {msg}")


def _ok(msg: str) -> None:
    print(f"  [ok     ] {msg}")


# ---------------------------------------------------------------- plantilla
def plantilla() -> dict:
    return {
        "_instrucciones": (
            "Complete los campos y elimine este campo. El texto del "
            "considerando debe transcribirse fielmente desde la fuente "
            "que el titular tiene a la vista (Oficina Judicial Virtual, "
            "copia en carpeta, base identificada). Estados admitidos: "
            "[V] [PV] [NU] [S]. Para [V] son copulativos: "
            "texto_considerando, fuente_texto y fecha_verificacion."
        ),
        "estado": "[PV]",
        "tribunal": "",
        "sala": "",
        "tipo_recurso": "",
        "rol": "",
        "ruc_rit_origen": "",
        "fecha_sentencia": "",
        "redactor": "",
        "considerandos": "",
        "tesis": "",
        "alcance_limites": "",
        "materia": "",
        "firmeza": "",
        "fuente_texto": "",
        "fecha_verificacion": "",
        "texto_considerando": "",
        "motivo_ingreso": "",
    }


# ---------------------------------------------------------------- validación
def validar_ficha(f: dict) -> list:
    """Devuelve la lista de defectos; vacía si la ficha es conforme."""
    defectos = []
    estado = f.get("estado", "")
    if estado not in ESTADOS:
        defectos.append(
            f"estado «{estado}» no admitido; use uno de {', '.join(ESTADOS)}"
        )
    for c in CAMPOS_OBLIGATORIOS:
        if not str(f.get(c, "")).strip():
            defectos.append(f"campo obligatorio vacío: {c}")
    fs = str(f.get("fecha_sentencia", "")).strip()
    if fs and not RE_FECHA.match(fs):
        defectos.append("fecha_sentencia debe tener formato AAAA-MM-DD")
    if estado == "[V]":
        for c in CAMPOS_V:
            if not str(f.get(c, "")).strip():
                defectos.append(
                    f"estado [V] exige el campo «{c}» (condición copulativa); "
                    "en su defecto, degrade a [PV] (regla R-5)"
                )
        fv = str(f.get("fecha_verificacion", "")).strip()
        if fv and not RE_FECHA.match(fv):
            defectos.append("fecha_verificacion debe tener formato AAAA-MM-DD")
    if estado in ("[NU]", "[S]") and not str(f.get("alcance_limites", "")).strip():
        defectos.append(
            f"estado {estado} exige consignar en «alcance_limites» la razón "
            "(búsqueda negativa, doctrina no contenida o fallo que la supera)"
        )
    if "_instrucciones" in f:
        defectos.append("elimine el campo _instrucciones de la plantilla")
    return defectos


# ---------------------------------------------------------------- registro
def leer_registro(ruta: str) -> str:
    with open(ruta, encoding="utf-8") as fh:
        contenido = fh.read()
    if MARCA_INICIO not in contenido or MARCA_FIN not in contenido:
        raise ValueError(
            "el registro no contiene las marcas de sección de fichas; "
            "verifique que corresponde a references/jurisprudencia-curada.md"
        )
    return contenido


def ids_existentes(contenido: str) -> list:
    return RE_ID.findall("\n".join(
        ln for ln in contenido.splitlines() if ln.startswith("### J-")
    )) or re.findall(r"### (J-\d{3,})", contenido)


def siguiente_id(contenido: str) -> str:
    usados = [int(i.split("-")[1]) for i in ids_existentes(contenido)]
    n = (max(usados) + 1) if usados else 1
    return f"J-{n:03d}"


def ficha_a_markdown(fid: str, f: dict) -> str:
    estado = f["estado"]
    lineas = [
        f"### {fid} — [{f['materia']}] — {f['tribunal']}, "
        f"Rol N° {f['rol']}, de {f['fecha_sentencia']}",
        f"- **Estado**: {estado}",
        f"- **Tribunal y sala**: {f['tribunal']}"
        + (f", {f['sala']}" if f.get("sala") else ""),
    ]
    if f.get("tipo_recurso"):
        lineas.append(f"- **Tipo de recurso o procedimiento**: {f['tipo_recurso']}")
    lineas.append(f"- **Rol**: {f['rol']}")
    if f.get("ruc_rit_origen"):
        lineas.append(f"- **RUC/RIT de origen**: {f['ruc_rit_origen']}")
    lineas.append(f"- **Fecha de la sentencia**: {f['fecha_sentencia']}")
    if f.get("redactor"):
        lineas.append(f"- **Redactor**: {f['redactor']}")
    lineas.append(f"- **Considerando(s) invocado(s)**: {f['considerandos']}")
    lineas.append(f"- **Tesis que sostiene**: {f['tesis']}")
    if f.get("alcance_limites"):
        lineas.append(f"- **Alcance y límites**: {f['alcance_limites']}")
    lineas.append(f"- **Materia**: {f['materia']}")
    if f.get("firmeza"):
        lineas.append(f"- **Firmeza**: {f['firmeza']}")
    if estado == "[V]":
        h = hash_texto(f["texto_considerando"])
        lineas += [
            f"- **Fuente del texto**: {f['fuente_texto']}",
            f"- **Fecha de verificación**: {f['fecha_verificacion']}",
            f"- **SHA-256 del texto**: `{h}`",
        ]
    if f.get("motivo_ingreso"):
        lineas.append(f"- **Motivo de ingreso**: {f['motivo_ingreso']}")
    lineas.append(f"- **Fecha de ingreso al registro**: {date.today().isoformat()}")
    if str(f.get("texto_considerando", "")).strip():
        lineas.append("- **Texto del considerando**:")
        lineas.append("")
        for parr in f["texto_considerando"].strip().splitlines():
            lineas.append(f"> {parr}" if parr.strip() else ">")
    lineas.append("")
    return "\n".join(lineas)


def agregar(ruta_ficha: str, ruta_registro: str) -> int:
    with open(ruta_ficha, encoding="utf-8") as fh:
        f = json.load(fh)
    defectos = validar_ficha(f)
    if defectos:
        print("== FICHA INVÁLIDA; no se ingresa al registro:")
        for d in defectos:
            _err(d)
        return 1
    contenido = leer_registro(ruta_registro)
    fid = siguiente_id(contenido)
    bloque = ficha_a_markdown(fid, f)
    nuevo = contenido.replace(MARCA_FIN, bloque + "\n" + MARCA_FIN)
    with open(ruta_registro, "w", encoding="utf-8") as fh:
        fh.write(nuevo)
    print(f"== Ficha ingresada con identificador {fid} (estado {f['estado']}).")
    if f["estado"] == "[V]":
        print(f"   SHA-256: {hash_texto(f['texto_considerando'])}")
    print("   Recuerde: el identificador queda quemado y jamás se reasigna.")
    return 0


# ---------------------------------------------------------------- verificación
def extraer_fichas(contenido: str) -> list:
    """Extrae las fichas del registro como diccionarios mínimos para
    auditoría: id, estado, hash declarado y texto transcrito."""
    seccion = contenido.split(MARCA_INICIO, 1)[1].split(MARCA_FIN, 1)[0]
    bloques = re.split(r"(?=^### J-)", seccion, flags=re.M)
    fichas = []
    for b in bloques:
        m = re.match(r"### (J-\d{3,})", b)
        if not m:
            continue
        estado = re.search(r"\*\*Estado\*\*:\s*(\[\w+\])", b)
        hdecl = re.search(r"\*\*SHA-256 del texto\*\*:\s*`([0-9a-f]{64})`", b)
        texto = "\n".join(
            ln[2:] if ln.startswith("> ") else ""
            for ln in b.splitlines()
            if ln.startswith(">")
        )
        fichas.append(
            {
                "id": m.group(1),
                "estado": estado.group(1) if estado else None,
                "hash_declarado": hdecl.group(1) if hdecl else None,
                "texto": texto.strip(),
            }
        )
    return fichas


def verificar(ruta_registro: str) -> int:
    contenido = leer_registro(ruta_registro)
    fichas = extraer_fichas(contenido)
    defectos = 0
    ids = [f["id"] for f in fichas]
    duplicados = {i for i in ids if ids.count(i) > 1}
    for d in sorted(duplicados):
        _err(f"identificador duplicado: {d}")
        defectos += 1
    nums = sorted(int(i.split("-")[1]) for i in set(ids))
    for a, b in zip(nums, nums[1:]):
        if b != a + 1:
            print(
                f"  [aviso  ] salto de numeración J-{a:03d} → J-{b:03d} "
                "(admisible solo si media identificador quemado documentado)"
            )
    for f in fichas:
        if f["estado"] not in ESTADOS:
            _err(f"{f['id']}: estado ausente o no admitido")
            defectos += 1
            continue
        if f["estado"] == "[V]":
            if not f["hash_declarado"]:
                _err(f"{f['id']}: estado [V] sin SHA-256 declarado")
                defectos += 1
            elif not f["texto"]:
                _err(f"{f['id']}: estado [V] sin texto del considerando")
                defectos += 1
            elif hash_texto(f["texto"]) != f["hash_declarado"]:
                _err(
                    f"{f['id']}: el hash del texto no coincide con el "
                    "declarado; el texto fue alterado tras su sellado o el "
                    "hash es espurio. Degrade a [PV] y reverifique."
                )
                defectos += 1
            else:
                _ok(f"{f['id']} [V] — hash conforme")
        else:
            _ok(f"{f['id']} {f['estado']}")
    if not fichas:
        print("  (registro sin fichas; primer identificador disponible: J-001)")
    print(
        f"\n== RESULTADO: {'conforme' if defectos == 0 else str(defectos) + ' defecto(s)'}."
    )
    return 0 if defectos == 0 else 1


def listar(ruta_registro: str) -> int:
    contenido = leer_registro(ruta_registro)
    fichas = extraer_fichas(contenido)
    if not fichas:
        print("Registro sin fichas. Primer identificador disponible: J-001.")
        return 0
    for f in fichas:
        print(f"  {f['id']}  {f['estado'] or '[?]'}")
    print(f"\nTotal: {len(fichas)} ficha(s).")
    return 0


# ---------------------------------------------------------------- main
def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--plantilla", action="store_true")
    g.add_argument("--validar", metavar="FICHA_JSON")
    g.add_argument("--agregar", metavar="FICHA_JSON")
    g.add_argument("--verificar", metavar="REGISTRO_MD")
    g.add_argument("--listar", metavar="REGISTRO_MD")
    p.add_argument("--registro", metavar="REGISTRO_MD")
    a = p.parse_args(argv)

    try:
        if a.plantilla:
            print(json.dumps(plantilla(), ensure_ascii=False, indent=2))
            return 0
        if a.validar:
            with open(a.validar, encoding="utf-8") as fh:
                defectos = validar_ficha(json.load(fh))
            if defectos:
                print("== FICHA INVÁLIDA:")
                for d in defectos:
                    _err(d)
                return 1
            print("== Ficha conforme.")
            return 0
        if a.agregar:
            if not a.registro:
                print("--agregar exige --registro", file=sys.stderr)
                return 2
            return agregar(a.agregar, a.registro)
        if a.verificar:
            return verificar(a.verificar)
        if a.listar:
            return listar(a.listar)
    except (OSError, ValueError, json.JSONDecodeError) as e:
        print(f"[FATAL] {e}", file=sys.stderr)
        return 2
    return 2


if __name__ == "__main__":
    sys.exit(main())
