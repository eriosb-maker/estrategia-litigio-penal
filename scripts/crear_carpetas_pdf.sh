#!/usr/bin/env bash
# Crea la estructura de carpetas recomendada para organizar PDFs legales
# antes de importarlos al vault de Obsidian.
#
# Uso:
#   ./scripts/crear_carpetas_pdf.sh              # usa ~/Documentos/PDFs-Legales
#   ./scripts/crear_carpetas_pdf.sh /otro/path   # destino personalizado

set -euo pipefail

DESTINO="${1:-$HOME/Documentos/PDFs-Legales}"

echo "📁 Creando estructura de carpetas en: $DESTINO"
echo ""

crear() {
    local ruta="$DESTINO/$1"
    mkdir -p "$ruta"
    printf "  ✓ %s\n" "$1"
}

# Códigos y cuerpos legales principales
crear "01-Codigos"

# Leyes especiales (Ley 20.066, Ley 18.216, etc.)
crear "02-Leyes-Especiales"

# Jurisprudencia organizada por año
crear "03-Jurisprudencia/2026"
crear "03-Jurisprudencia/2025"
crear "03-Jurisprudencia/2024"
crear "03-Jurisprudencia/2023"
crear "03-Jurisprudencia/Anteriores"

# Manuales y libros académicos
crear "04-Manuales-y-Libros"

# Artículos académicos y papers
crear "05-Papers"

# Estrategia procesal, negociación, teoría
crear "06-Estrategia"

# PDFs de causas específicas (no van al vault general)
crear "07-Causas-Especificas"

echo ""
echo "─────────────────────────────────────────────"

# Crear READMEs explicativos en cada carpeta
cat > "$DESTINO/01-Codigos/LEEME.txt" <<'TXT'
CÓDIGOS Y CUERPOS LEGALES PRINCIPALES
======================================
Qué poner aquí:
  - Código Penal (versión actualizada)
  - Código Procesal Penal (CPP)
  - Código Civil
  - Código de Procedimiento Civil
  - Código del Trabajo
  - Código Tributario
  - Constitución Política

Nomenclatura sugerida:
  codigo-penal-2024.pdf
  cpp-2024.pdf
  codigo-civil-2024.pdf

Comando de importación:
  ./scripts/litigio.sh importar ~/Documentos/PDFs-Legales/01-Codigos/
TXT

cat > "$DESTINO/02-Leyes-Especiales/LEEME.txt" <<'TXT'
LEYES ESPECIALES
================
Qué poner aquí:
  - Ley 20.066 (Violencia Intrafamiliar)
  - Ley 20.084 (Responsabilidad Penal Adolescente)
  - Ley 18.216 (Penas Sustitutivas)
  - Ley 20.931 (Agenda Corta Antidelincuencia)
  - Ley 19.968 (Tribunales de Familia)
  - Ley 19.496 (Protección al Consumidor)
  - Cualquier ley especial relevante para tus causas

Nomenclatura sugerida:
  ley-20066-vif.pdf
  ley-18216-penas-sustitutivas.pdf
TXT

cat > "$DESTINO/03-Jurisprudencia/LEEME.txt" <<'TXT'
JURISPRUDENCIA
==============
Organiza los fallos por año en las subcarpetas.

Qué poner aquí:
  - Sentencias Corte Suprema
  - Sentencias Cortes de Apelaciones
  - Fallos TOP / TJOP relevantes

Nomenclatura sugerida:
  CS-2024-rol-12345-homicidio.pdf
  CA-santiago-2023-rol-456-estafa.pdf
  TOP-antofagasta-2024-absolucion-robo.pdf

Tip: Los fallos de la Corte Suprema puedes bajarlos de:
  https://www.pjud.cl → Jurisprudencia → Consulta en línea
TXT

cat > "$DESTINO/04-Manuales-y-Libros/LEEME.txt" <<'TXT'
MANUALES Y LIBROS ACADÉMICOS
=============================
Qué poner aquí:
  - Manuales de derecho penal (Politoff, Matus, Ramírez)
  - Tratados de derecho civil (Alessandri, Somarriva)
  - Libros de derecho procesal (Mosquera, Piedrabuena)
  - Cualquier libro académico en PDF

Nomenclatura sugerida:
  politoff-matus-ramirez-dp-parte-general.pdf
  alessandri-somarriva-vodanovic-civil-t1.pdf
TXT

cat > "$DESTINO/05-Papers/LEEME.txt" <<'TXT'
ARTÍCULOS ACADÉMICOS Y PAPERS
==============================
Qué poner aquí:
  - Artículos de Revista de Derecho (U. Austral, UDP, etc.)
  - Papers de derecho comparado
  - Artículos de criminología y prueba
  - Publicaciones del Ministerio Público / Defensoría

Nomenclatura sugerida:
  autor-apellido-2024-titulo-corto.pdf
  horvitz-2023-garantias-procesal-penal.pdf
TXT

cat > "$DESTINO/06-Estrategia/LEEME.txt" <<'TXT'
ESTRATEGIA PROCESAL Y NEGOCIACIÓN
===================================
Qué poner aquí:
  - Libros de teoría del litigio
  - Manuales de negociación y mediación
  - Guías de valoración de la prueba
  - Material sobre teoría del caso
  - Papers de game theory aplicada al derecho

Nomenclatura sugerida:
  teoria-del-caso-baytelman-duce.pdf
  negociacion-fisher-ury-getting-to-yes.pdf
TXT

cat > "$DESTINO/07-Causas-Especificas/LEEME.txt" <<'TXT'
PDFs DE CAUSAS ESPECÍFICAS
===========================
Qué poner aquí:
  - Carpetas por causa (usando el RUC como nombre)
  - Escritos, resoluciones, actas de tu causa
  - Informes periciales
  - Documentos del cliente

Nomenclatura sugerida (crear subcarpeta por causa):
  07-Causas-Especificas/
  └── 2024-001-RIT-O-12345/
      ├── acusacion.pdf
      ├── informe-pericial-dna.pdf
      └── resolucion-apertura-juicio.pdf

NOTA: Estos PDFs son confidenciales. No los importes al vault general
con ./litigio.sh importar — agrégatelos manualmente al directorio
01-Causas/{ruc}/ dentro del vault.
TXT

# Crear README principal
cat > "$DESTINO/README.txt" <<'TXT'
SEGUNDO CEREBRO LEGAL — Carpetas de PDFs
==========================================

Esta estructura organiza tus PDFs *antes* de importarlos al vault de Obsidian.

WORKFLOW:
  1. Baja el PDF y guárdalo en la carpeta correspondiente
  2. Usa el importador para procesarlo:
       ./scripts/litigio.sh importar <ruta-al-pdf>
       ./scripts/litigio.sh importar <ruta-a-carpeta>   ← importa todos
  3. El importador crea una nota Markdown en el vault y copia el PDF a vault/_pdfs/
  4. Abre la nota en Obsidian y completa los campos que el importador no pudo detectar

CARPETAS:
  01-Codigos/           → Códigos legales (Penal, Civil, Procesal…)
  02-Leyes-Especiales/  → Leyes especiales (Ley 20.066, 18.216…)
  03-Jurisprudencia/    → Fallos por año
  04-Manuales-y-Libros/ → Libros académicos
  05-Papers/            → Artículos de revista
  06-Estrategia/        → Material de estrategia procesal
  07-Causas-Especificas/→ Documentos de causas propias (NO importar al vault general)

AYUDA:
  ./scripts/litigio.sh importar --help
TXT

echo "✅ Estructura creada exitosamente."
echo ""
echo "📂 $DESTINO/"
find "$DESTINO" -type d | sort | sed "s|$DESTINO||" | grep -v "^$" | awk '{print "   " $0}'
echo ""
echo "👉 Siguiente paso:"
echo "   Copia tus PDFs a las carpetas correspondientes y luego ejecuta:"
echo "   ./scripts/litigio.sh importar $DESTINO/01-Codigos/"
