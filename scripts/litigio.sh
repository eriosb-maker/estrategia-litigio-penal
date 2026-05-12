#!/usr/bin/env bash
# Wrapper único para todas las operaciones del segundo cerebro legal.
#
# Uso:
#   ./scripts/litigio.sh nueva              # Crear nueva causa (modo interactivo)
#   ./scripts/litigio.sh bayes <RUC>        # Análisis Bayesiano de causa
#   ./scripts/litigio.sh juegos <RUC>       # Análisis Teoría de Juegos
#   ./scripts/litigio.sh completo <RUC>     # Bayes + TJ encadenados (recomendado)
#   ./scripts/litigio.sh conexiones <RUC>   # Reporte de cross-referencias
#   ./scripts/litigio.sh buscar "término"   # Buscar en el vault
#   ./scripts/litigio.sh demo               # Ejecutar demo con caso ficticio
#   ./scripts/litigio.sh setup              # Instalar dependencias Python

set -e
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
PY="${PYTHON:-python3}"

cd "${ROOT_DIR}"

cmd="${1:-help}"
shift || true

case "${cmd}" in
  nueva)
    ${PY} scripts/nueva_causa.py --interactivo "$@"
    ;;
  bayes)
    [[ -z "$1" ]] && { echo "Uso: litigio.sh bayes <RUC>"; exit 1; }
    ${PY} scripts/analizar_causa.py --ruc "$1" --modo bayes --guardar
    ;;
  juegos)
    [[ -z "$1" ]] && { echo "Uso: litigio.sh juegos <RUC>"; exit 1; }
    ${PY} scripts/analizar_causa.py --ruc "$1" --modo juegos --guardar
    ;;
  completo)
    [[ -z "$1" ]] && { echo "Uso: litigio.sh completo <RUC>"; exit 1; }
    ${PY} scripts/analizar_causa.py --ruc "$1" --modo completo --guardar
    ;;
  conexiones)
    [[ -z "$1" ]] && { echo "Uso: litigio.sh conexiones <RUC>"; exit 1; }
    ${PY} scripts/analizar_causa.py --ruc "$1" --modo conexiones
    ;;
  buscar)
    [[ -z "$1" ]] && { echo "Uso: litigio.sh buscar <término>"; exit 1; }
    ${PY} scripts/buscar.py "$@"
    ;;
  demo)
    ${PY} scripts/analizar_causa.py --demo
    ;;
  setup)
    ${PY} -m pip install -r requirements.txt
    echo "✅ Dependencias instaladas"
    ;;
  help|--help|-h|"")
    grep '^#' "$0" | sed 's/^# \?//'
    ;;
  *)
    echo "❌ Comando desconocido: ${cmd}"
    echo "Ejecuta: litigio.sh help"
    exit 1
    ;;
esac
