#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Vigilancia de plazos de revalidación normativa (protocolo de curatoría).

Cada extracto curado declara, en su encabezado, una fecha de vencimiento de
revalidación semestral («vence el AAAA-MM-DD»), conforme a la regla 4 del
protocolo de curatoría de `marco-legal.md`. Este script no reemplaza el
juicio del abogado sobre si la norma cambió: solo evita que el vencimiento
del plazo declarado pase inadvertido, mediante detección textual de la
fecha y comparación contra la fecha de ejecución.

Uso: `python3 scripts/vigilar_revalidacion.py [--umbral-dias 60] [--fecha AAAA-MM-DD]`
Salida: 0 siempre que la ejecución sea correcta (el vencimiento próximo no
es un error de CI, es una alerta informativa); código 2 solo ante error de
ejecución del propio script. El detalle de alertas se imprime a stdout y,
si `GITHUB_STEP_SUMMARY` está definido, se añade también allí.
"""

import argparse
import os
import re
import sys
from datetime import date, datetime, timedelta
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
PATRON = re.compile(r"vence el[\s>]*\**(\d{4}-\d{2}-\d{2})\**", re.MULTILINE)

RUTAS_A_REVISAR = [
    RAIZ / "skill" / "references" / "marco-legal.md",
    RAIZ / "skill" / "references" / "leyes-especiales.md",
    RAIZ / "skill" / "references" / "tributario.md",
    RAIZ / "curatoria" / "encabezado-leyes-especiales.md",
]


def extraer_vencimientos(ruta: Path):
    if not ruta.exists():
        return []
    texto = ruta.read_text(encoding="utf-8", errors="replace")
    hallazgos = []
    for m in PATRON.finditer(texto):
        try:
            fecha = datetime.strptime(m.group(1), "%Y-%m-%d").date()
        except ValueError:
            continue
        numero_linea = texto.count("\n", 0, m.start()) + 1
        hallazgos.append((ruta.relative_to(RAIZ), numero_linea, fecha))
    return hallazgos


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--umbral-dias", type=int, default=60)
    ap.add_argument("--fecha", type=str, default=None, help="AAAA-MM-DD; por defecto, hoy")
    args = ap.parse_args()

    hoy = datetime.strptime(args.fecha, "%Y-%m-%d").date() if args.fecha else date.today()
    umbral = timedelta(days=args.umbral_dias)

    todos = []
    for ruta in RUTAS_A_REVISAR:
        todos.extend(extraer_vencimientos(ruta))

    if not todos:
        print("No se hallaron marcas «vence el AAAA-MM-DD» en los archivos vigilados.")
        return 0

    lineas_reporte = [f"# Vigilancia de revalidación normativa — ejecutado el {hoy.isoformat()}\n"]
    hay_alerta = False
    for ruta, linea, fecha in sorted(todos, key=lambda x: x[2]):
        dias = (fecha - hoy).days
        if dias < 0:
            estado = f"⛔ VENCIDO hace {-dias} días"
            hay_alerta = True
        elif timedelta(days=dias) <= umbral:
            estado = f"⚠️  vence en {dias} días"
            hay_alerta = True
        else:
            estado = f"ok — vence en {dias} días"
        fila = f"- `{ruta}:{linea}` — {fecha.isoformat()} — {estado}"
        print(fila)
        lineas_reporte.append(fila)

    resumen_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if resumen_path:
        with open(resumen_path, "a", encoding="utf-8") as f:
            f.write("\n".join(lineas_reporte) + "\n")

    if hay_alerta:
        print(
            "\nAtención: uno o más extractos normativos vencen dentro del umbral "
            f"de {args.umbral_dias} días o ya está vencido. Ejecute la re-curación "
            "conforme al protocolo de `marco-legal.md` (sección 1, regla 4)."
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
