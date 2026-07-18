#!/usr/bin/env bash
# =============================================================================
# verificar-integridad.sh — Auditoría de integridad y propagación
# Skill: analisis-penal-chile · Versión 1.1.0
#
# OBJETO. Contrastar el árbol de archivos efectivamente instalado contra
# `index-maestro.json`, y contra las invocaciones que `SKILL.md` hace de sus
# propios módulos. Detecta cuatro defectos:
#
#   (a) módulo indexado como `instalado` que no existe en el disco;
#   (b) módulo instalado cuyo hash no corresponde al indexado;
#   (c) archivo presente en el disco y ausente del índice;
#   (d) módulo invocado por SKILL.md que no existe en el disco Y NO ESTÁ
#       DECLARADO como ausente o no propagado en el índice. La invocación de un
#       módulo cuya falta consta en el índice es un aviso, no un defecto: el
#       vicio reside en la invocación silenciosa, no en la invocación.
#
# LIMITACIÓN ESTRUCTURAL. Este script reside dentro del paquete que audita.
# Si el paquete se instala incompleto, puede no existir para autoinvocarse. Su
# modo operativo es la auditoría PREVIA a la entrega del `.skill`, no la
# verificación posterior a la instalación, que queda entregada a la Cláusula
# de Propagación del SKILL.md.
#
# USO:  ./verificar-integridad.sh [directorio_de_la_skill]
# SALIDA: 0 conforme · 1 defectos detectados · 2 índice ausente o ilegible
# =============================================================================

set -uo pipefail

RAIZ="${1:-.}"
INDICE="$RAIZ/index-maestro.json"
DEFECTOS=0

rojo()  { printf '  [DEFECTO] %s\n' "$1"; DEFECTOS=$((DEFECTOS+1)); }
gris()  { printf '  [aviso  ] %s\n' "$1"; }
ok()    { printf '  [ok     ] %s\n' "$1"; }

command -v python3 >/dev/null || { echo "python3 requerido"; exit 2; }
[ -f "$INDICE" ] || { echo "[FATAL] No existe $INDICE"; exit 2; }
python3 -c "import json,sys;json.load(open(sys.argv[1]))" "$INDICE" 2>/dev/null \
  || { echo "[FATAL] $INDICE ilegible"; exit 2; }

echo "== Auditoría de integridad: $RAIZ"
echo

# --- (a) y (b): archivos indexados como instalados ---------------------------
echo "-- Módulos indexados como instalados"
while IFS=$'\t' read -r ruta sha; do
  f="$RAIZ/$ruta"
  if [ ! -f "$f" ]; then
    rojo "ausente en disco pese a estar indexado como instalado: $ruta"
  else
    real=$(sha256sum "$f" | cut -d' ' -f1)
    if [ "$real" != "$sha" ]; then
      rojo "hash alterado: $ruta"
    else
      ok "$ruta"
    fi
  fi
done < <(python3 -c "
import json,sys
d=json.load(open(sys.argv[1]))
for a in d['archivos']:
    if a['estado']=='instalado':
        print(a['ruta']+'\t'+a['sha256'])
" "$INDICE")

# --- (c): archivos en disco no indexados -------------------------------------
echo
echo "-- Archivos presentes y no indexados"
INDEXADOS=$(python3 -c "
import json,sys
d=json.load(open(sys.argv[1]))
print('\n'.join(a['ruta'] for a in d['archivos']))
" "$INDICE")
HALLADO=0
while read -r f; do
  rel="${f#"$RAIZ"/}"
  [ "$rel" = "index-maestro.json" ] && continue
  [ "$rel" = "verificar-integridad.sh" ] && continue
  if ! printf '%s\n' "$INDEXADOS" | grep -qxF "$rel"; then
    rojo "no indexado: $rel"
    HALLADO=1
  fi
done < <(find "$RAIZ" -type f | sort)
[ "$HALLADO" -eq 0 ] && ok "ninguno"

# --- (d): módulos invocados por SKILL.md e inexistentes ----------------------
echo
echo "-- Módulos invocados por SKILL.md"
if [ -f "$RAIZ/SKILL.md" ]; then
  DECLARADOS=$(python3 -c "
import json,sys
d=json.load(open(sys.argv[1]))
print('\n'.join(a['ruta'] for a in d['archivos'] if a['estado']!='instalado'))
" "$INDICE")
  while read -r m; do
    if [ -f "$RAIZ/$m" ]; then
      ok "$m"
    elif printf '%s\n' "$DECLARADOS" | grep -qxF "$m"; then
      gris "invocado y no instalado, pero declarado en el índice: $m"
    else
      rojo "SKILL.md invoca un módulo inexistente y no declarado: $m"
    fi
  done < <(grep -oE '(references|scripts|assets/templates)/[a-z0-9_-]+\.(md|py)' "$RAIZ/SKILL.md" | sort -u)
else
  rojo "no existe SKILL.md"
fi

# --- Estados declarados ------------------------------------------------------
echo
echo "-- Estados declarados en el índice"
python3 -c "
import json,sys
d=json.load(open(sys.argv[1]))
for a in d['archivos']:
    if a['estado'] != 'instalado':
        print('  [%s] %s — %s' % (a['estado'], a['ruta'], a.get('origen','')))
" "$INDICE"

echo
if [ "$DEFECTOS" -gt 0 ]; then
  echo "== RESULTADO: $DEFECTOS defecto(s). El paquete NO se entrega ni se declara instalado."
  exit 1
fi
echo "== RESULTADO: conforme."
exit 0
