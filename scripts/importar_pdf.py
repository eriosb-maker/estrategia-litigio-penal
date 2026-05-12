#!/usr/bin/env python3
"""
Importador de PDFs al segundo cerebro legal.

Toma un PDF (o carpeta de PDFs), extrae texto y metadata, lo clasifica,
copia el PDF a vault/_pdfs/ y crea una nota Markdown con frontmatter
en la carpeta correcta del vault (02-Marco-Legal, 03-Biblioteca, etc.).

Uso:
    python scripts/importar_pdf.py archivo.pdf
    python scripts/importar_pdf.py carpeta_con_pdfs/
    python scripts/importar_pdf.py archivo.pdf --tipo norma
    python scripts/importar_pdf.py carpeta/ --tipo libro --auto
"""

import argparse
import re
import shutil
import sys
from pathlib import Path

try:
    from pypdf import PdfReader
except ImportError:
    print("❌ Falta pypdf. Instala con: pip install pypdf")
    sys.exit(1)

VAULT = Path(__file__).parent.parent / "vault"
PDFS_DIR = VAULT / "_pdfs"

TIPOS = {
    "norma": ("02-Marco-Legal", "norma", ["norma"]),
    "jurisprudencia": ("02-Marco-Legal", "jurisprudencia", ["jurisprudencia"]),
    "libro": ("03-Biblioteca", "libro", ["libro", "lectura"]),
    "paper": ("03-Biblioteca", "paper", ["paper", "lectura"]),
    "sentencia": ("02-Marco-Legal", "jurisprudencia", ["jurisprudencia", "sentencia"]),
    "doctrina": ("03-Biblioteca", "lectura", ["doctrina", "lectura"]),
    "otro": ("03-Biblioteca", "lectura", ["lectura"]),
}

PATRONES_AUTO = [
    (re.compile(r"\b(?:CORTE SUPREMA|CORTE DE APELACIONES|TRIBUNAL ORAL|JUZGADO|FALLO|SENTENCIA|ROL\s+(?:N°|Nº)?\s*\d+)", re.I), "jurisprudencia"),
    (re.compile(r"\b(?:CÓDIGO\s+(?:PENAL|PROCESAL|CIVIL|DEL TRABAJO)|LEY\s+(?:N°|Nº)?\s*\d+|ARTÍCULO\s+\d+\.-)", re.I), "norma"),
    (re.compile(r"\b(?:ISBN|EDITORIAL|CAPÍTULO\s+[IVX0-9])", re.I), "libro"),
    (re.compile(r"\b(?:abstract|doi:|keywords:|recibido el|aceptado el)", re.I), "paper"),
]


def slugify(s: str, max_len: int = 80) -> str:
    s = re.sub(r"[^\w\sáéíóúñÑÁÉÍÓÚ\-]", "", s)
    s = re.sub(r"\s+", "-", s.strip())
    return s[:max_len].rstrip("-") or "Documento-Sin-Titulo"


def extraer_pdf(pdf_path: Path, paginas_preview: int = 3) -> dict:
    """Lee el PDF y devuelve {titulo, autor, num_paginas, texto_preview, texto_completo}."""
    reader = PdfReader(str(pdf_path))
    meta = reader.metadata or {}
    num_pag = len(reader.pages)

    texto_completo_partes = []
    for p in reader.pages:
        try:
            texto_completo_partes.append(p.extract_text() or "")
        except Exception:
            texto_completo_partes.append("")
    texto_completo = "\n".join(texto_completo_partes)

    texto_preview_partes = texto_completo_partes[:paginas_preview]
    texto_preview = "\n\n".join(texto_preview_partes).strip()

    titulo = (meta.get("/Title") or "").strip()
    if not titulo:
        # primera línea no vacía del PDF como fallback
        for linea in texto_completo.splitlines():
            linea = linea.strip()
            if len(linea) > 5:
                titulo = linea[:120]
                break
    if not titulo:
        titulo = pdf_path.stem

    autor = (meta.get("/Author") or "").strip()

    return {
        "titulo": titulo,
        "autor": autor,
        "num_paginas": num_pag,
        "texto_preview": texto_preview,
        "texto_completo": texto_completo,
    }


def clasificar_auto(texto: str) -> str:
    """Detecta el tipo de documento por patrones en el texto."""
    primeras_palabras = texto[:3000]
    for patron, tipo in PATRONES_AUTO:
        if patron.search(primeras_palabras):
            return tipo
    return "otro"


def crear_nota(pdf_path: Path, tipo: str, datos: dict, auto: bool) -> Path:
    """Genera la nota Markdown en la carpeta correcta del vault."""
    carpeta, tipo_frontmatter, etiquetas = TIPOS[tipo]
    destino_carpeta = VAULT / carpeta
    destino_carpeta.mkdir(parents=True, exist_ok=True)
    PDFS_DIR.mkdir(parents=True, exist_ok=True)

    # Copiar PDF a _pdfs/
    pdf_destino = PDFS_DIR / pdf_path.name
    if not pdf_destino.exists():
        shutil.copy2(pdf_path, pdf_destino)

    slug = slugify(datos["titulo"])
    nota_path = destino_carpeta / f"{slug}.md"

    # Si ya existe, sufijar
    i = 2
    while nota_path.exists():
        nota_path = destino_carpeta / f"{slug}-{i}.md"
        i += 1

    etiquetas_yaml = ", ".join(etiquetas)
    extracto = datos["texto_preview"][:2500].replace("\n", "\n> ")

    contenido = f"""---
tipo: {tipo_frontmatter}
titulo: "{datos['titulo']}"
autor: "{datos['autor']}"
num-paginas: {datos['num_paginas']}
pdf-origen: "_pdfs/{pdf_path.name}"
clasificado-como: "{tipo}"
clasificacion-auto: {str(auto).lower()}
etiquetas: [{etiquetas_yaml}, importado]
---

# 📄 {datos['titulo']}

> **Tipo**: {tipo} | **Páginas**: {datos['num_paginas']} | **Autor**: {datos['autor'] or "(no detectado)"}

📎 **PDF original**: [[_pdfs/{pdf_path.name}|Abrir PDF]]

---

## Resumen Manual (3 puntos)

> *Llenar después de leer — Progressive Summarization Nivel 3*

1.
2.
3.

---

## Por qué importa

> *¿En qué causas, estrategias o argumentos aplica?*

---

## Conceptos clave a extraer

- [[07-Conceptos/]]
- [[07-Conceptos/]]

---

## Causas donde aplica

```dataview
LIST FROM "01-Causas"
WHERE contains(file.outlinks, this.file.link)
```

---

## Extracto Automático (primeras páginas)

> *Texto extraído del PDF. Editar/limpiar manualmente cuando se procese la nota.*

> {extracto}

---

*Importado: {Path(__file__).stem} · PDF en `_pdfs/{pdf_path.name}`*
"""
    nota_path.write_text(contenido, encoding="utf-8")
    return nota_path


def preguntar_tipo(titulo: str, sugerencia: str) -> str:
    print(f"\n📄 PDF: {titulo}")
    print(f"   Sugerencia automática: {sugerencia}")
    print("   Tipos: norma, jurisprudencia, sentencia, libro, paper, doctrina, otro")
    print("   (enter para usar sugerencia, 's' para saltar este PDF)")
    r = input(f"   Tipo [{sugerencia}]: ").strip().lower()
    if r == "s":
        return "skip"
    return r or sugerencia


def importar_pdf(pdf_path: Path, tipo_forzado: str | None, auto: bool) -> Path | None:
    print(f"  → Leyendo {pdf_path.name}...")
    try:
        datos = extraer_pdf(pdf_path)
    except Exception as e:
        print(f"  ⚠️  Error leyendo: {e}")
        return None

    if tipo_forzado:
        tipo = tipo_forzado
    else:
        sugerencia = clasificar_auto(datos["texto_completo"])
        if auto:
            tipo = sugerencia
            print(f"  → Clasificado automáticamente como: {tipo}")
        else:
            tipo = preguntar_tipo(datos["titulo"], sugerencia)
            if tipo == "skip":
                return None
            if tipo not in TIPOS:
                print(f"  ⚠️  Tipo desconocido '{tipo}', usando 'otro'")
                tipo = "otro"

    nota = crear_nota(pdf_path, tipo, datos, auto)
    print(f"  ✅ Creada: {nota.relative_to(VAULT)}")
    return nota


def main():
    parser = argparse.ArgumentParser(description="Importa PDFs al segundo cerebro legal")
    parser.add_argument("ruta", help="Archivo PDF o carpeta con PDFs")
    parser.add_argument("--tipo", choices=list(TIPOS), help="Forzar tipo (sin preguntar)")
    parser.add_argument("--auto", action="store_true",
                        help="Clasificación automática sin preguntas (batch mode)")
    args = parser.parse_args()

    ruta = Path(args.ruta).expanduser().resolve()
    if not ruta.exists():
        print(f"❌ No existe: {ruta}")
        sys.exit(1)

    if ruta.is_file():
        pdfs = [ruta] if ruta.suffix.lower() == ".pdf" else []
    else:
        pdfs = sorted(ruta.rglob("*.pdf"))

    if not pdfs:
        print(f"❌ No se encontraron PDFs en {ruta}")
        sys.exit(1)

    print(f"\n📚 Importando {len(pdfs)} PDF(s) al vault...\n")
    creadas = []
    for pdf in pdfs:
        nota = importar_pdf(pdf, args.tipo, args.auto)
        if nota:
            creadas.append(nota)

    print(f"\n✅ {len(creadas)} nota(s) creada(s) en el vault.")
    if creadas:
        print(f"📎 PDFs en: {PDFS_DIR}")
        print("\nPróximos pasos:")
        print("  1. Abre Obsidian — verás las notas nuevas con etiqueta #importado")
        print("  2. Para cada nota: llena 'Resumen Manual' y enlaza a causas/conceptos")
        print("  3. (Opcional) instala plugin 'Omnisearch' para buscar dentro del texto del PDF")


if __name__ == "__main__":
    main()
