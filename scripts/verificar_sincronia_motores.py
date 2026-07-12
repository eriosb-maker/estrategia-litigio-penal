#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verificación de sincronía de motores deterministas (aprendizaje A-022).

La skill instalada (`skill/scripts/`) debe ser un espejo exacto de la ruta
canónica del repositorio (`scripts/` para `curar_norma.py`; `src/` para
`prescripcion.py`). Una divergencia de hash entre ambos ejemplares es,
precisamente, el defecto que motivó los 22 fallos detectados en la
reconciliación de linajes de la sesión 2026-07-12 (v4.3): el paquete
empaquetado operaba con un motor desincronizado del real.

Este script no verifica corrección jurídica ni de código: verifica
IDENTIDAD BINARIA entre cada par de rutas declaradas. Se ejecuta en cada
push como paso independiente de la suite pytest, para que la divergencia
se detecte de forma automática y no dependa de que un abogado la note por
inspección manual.

Uso: `python3 scripts/verificar_sincronia_motores.py`
Salida: 0 si todos los pares coinciden; 1 si algún par diverge (con detalle
de los archivos y hashes en conflicto).
"""

import hashlib
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent

# Pares (ruta canónica, ruta empaquetada) que deben ser binariamente idénticos.
PARES = [
    (RAIZ / "scripts" / "curar_norma.py", RAIZ / "skill" / "scripts" / "curar_norma.py"),
    (RAIZ / "src" / "prescripcion.py", RAIZ / "skill" / "scripts" / "prescripcion.py"),
]


def sha256(ruta: Path) -> str:
    return hashlib.sha256(ruta.read_bytes()).hexdigest()


def main() -> int:
    defectos = []
    for canonica, empaquetada in PARES:
        if not canonica.exists():
            defectos.append(f"ruta canónica ausente: {canonica.relative_to(RAIZ)}")
            continue
        if not empaquetada.exists():
            defectos.append(f"ruta empaquetada ausente: {empaquetada.relative_to(RAIZ)}")
            continue
        h1, h2 = sha256(canonica), sha256(empaquetada)
        if h1 != h2:
            defectos.append(
                f"DIVERGENCIA — {canonica.relative_to(RAIZ)} ({h1[:12]}…) "
                f"≠ {empaquetada.relative_to(RAIZ)} ({h2[:12]}…)"
            )
        else:
            print(f"[ok] {canonica.relative_to(RAIZ)} ≡ {empaquetada.relative_to(RAIZ)} ({h1[:12]}…)")

    if defectos:
        print("\n== RESULTADO: no conforme (A-022) ==", file=sys.stderr)
        for d in defectos:
            print(f"  - {d}", file=sys.stderr)
        print(
            "\nProhibición vigente: ninguna copia empaquetada puede divergir de su "
            "ruta canónica. Regenere `skill/scripts/` a partir de la ruta canónica "
            "antes de reempaquetar.",
            file=sys.stderr,
        )
        return 1

    print("\n== RESULTADO: conforme. ==")
    return 0


if __name__ == "__main__":
    sys.exit(main())
