---
tipo: doc
etiquetas: [doc, pdf, importacion]
---

# 📚 Importar PDFs al Segundo Cerebro

> Si tienes legislación, manuales, papers o jurisprudencia en PDF,
> este sistema los convierte en notas Markdown enlazables manteniendo los PDFs originales como adjuntos.

---

## 🧠 Cómo funciona el modelo

```
┌─────────────────┐      ┌──────────────────────────┐
│   PDF original  │ ───→ │  vault/_pdfs/Archivo.pdf │  (adjunto, abrible)
│   (en tu PC)    │      └──────────────────────────┘
└─────────────────┘                  ↑ enlace
                          ┌──────────────────────────┐
                          │  02-Marco-Legal/         │
                          │    Codigo-Penal.md       │  (nota indexable)
                          └──────────────────────────┘
                              ↓ frontmatter, tags, enlaces
                          ┌──────────────────────────┐
                          │  Dataview, búsqueda,     │
                          │  cross-referencias       │
                          └──────────────────────────┘
```

**Por qué este modelo**:
- Los PDFs no son indexables nativamente por Dataview ni se pueden cruzar con `[[wikilinks]]`.
- La nota Markdown es liviana, enlazable y permite agregar tu análisis manual.
- El PDF queda intacto: se abre con un clic desde la nota.

---

## 🚀 Setup (una sola vez)

```bash
./scripts/litigio.sh setup
```

Esto instala `pypdf` y las demás dependencias.

---

## 📥 Importar un PDF

### Modo asistido (recomendado para PDFs sueltos)

```bash
./scripts/litigio.sh importar /ruta/a/tu/archivo.pdf
```

El sistema:
1. Lee el PDF.
2. Detecta automáticamente el tipo (norma, jurisprudencia, libro, paper, doctrina).
3. Te muestra su sugerencia y te pide confirmación.
4. Crea la nota en la carpeta correcta (`02-Marco-Legal/` o `03-Biblioteca/`).
5. Copia el PDF a `vault/_pdfs/`.

### Modo automático (batch de carpetas)

```bash
./scripts/litigio.sh importar ~/Documentos/PDFs-Legales/ --auto
```

Procesa **todos los PDFs** dentro de la carpeta (recursivamente, incluyendo subcarpetas) sin preguntar nada. Útil cuando tienes 50, 100 o 500 archivos.

### Forzar un tipo específico

Si sabes que toda la carpeta son normas (ej: descargaste todos los Códigos):

```bash
./scripts/litigio.sh importar ~/Codigos-Chile/ --tipo norma --auto
```

Tipos disponibles: `norma`, `jurisprudencia`, `sentencia`, `libro`, `paper`, `doctrina`, `otro`.

---

## 🎯 Clasificación automática — cómo lo detecta

El sistema escanea las primeras páginas buscando patrones:

| Patrón detectado | Clasificación |
|------------------|--------------|
| "CORTE SUPREMA", "ROL N°", "SENTENCIA", "FALLO" | `jurisprudencia` |
| "CÓDIGO PENAL", "LEY N°", "ARTÍCULO 1.-" | `norma` |
| "ISBN", "EDITORIAL", "CAPÍTULO I" | `libro` |
| "abstract", "DOI:", "keywords:" | `paper` |
| Nada de lo anterior | `otro` (→ va a `03-Biblioteca/`) |

> La detección no es perfecta. Para colecciones grandes, conviene organizar los PDFs en carpetas por tipo y usar `--tipo` para forzar la clasificación.

---

## 📂 Organización recomendada antes de importar

Estructura tu carpeta de PDFs así para batch eficiente:

```
~/Mis-PDFs-Legales/
├── Codigos/                ← ./litigio.sh importar Codigos/ --tipo norma --auto
│   ├── Codigo-Penal.pdf
│   ├── CPP.pdf
│   └── Codigo-Civil.pdf
├── Jurisprudencia/         ← --tipo jurisprudencia --auto
│   ├── SCS-12345-2023.pdf
│   └── ICA-Stgo-678-2024.pdf
├── Libros/                 ← --tipo libro --auto
│   ├── Mauricio-Duce-Proceso-Penal.pdf
│   └── Politoff-Lecciones.pdf
└── Papers/                 ← --tipo paper --auto
    └── ...
```

Luego ejecutas 4 comandos y tienes tu biblioteca completa en el vault.

---

## ✏️ Qué hace por ti / qué te toca a ti

### 🤖 Hace por ti

- ✅ Extrae el título (de metadata o primera línea)
- ✅ Cuenta páginas
- ✅ Genera el frontmatter (tipo, etiquetas, ruta al PDF)
- ✅ Inserta extracto de las primeras 3 páginas
- ✅ Pone la nota en la carpeta correcta
- ✅ Copia el PDF a `vault/_pdfs/`
- ✅ Marca con etiqueta `#importado` para que sepas qué falta procesar

### ✋ Te toca a ti

- ⬜ **Resumen en 3 puntos** (Progressive Summarization)
- ⬜ **Por qué importa** para tu práctica
- ⬜ Extraer **conceptos clave** a notas atómicas en `07-Conceptos/`
- ⬜ Enlazar con causas, estrategias y normas relacionadas
- ⬜ Quitar la etiqueta `#importado` cuando termines de procesarla

---

## 🔍 Buscar dentro del texto de los PDFs

Obsidian nativo **no busca dentro de PDFs**. El extracto generado por el importador queda en la nota, así que la búsqueda global encontrará coincidencias ahí. Pero para PDFs largos solo se extraen las primeras 3 páginas.

### Solución: plugin Omnisearch (recomendado para colecciones grandes)

1. **Settings → Community plugins → Browse → Omnisearch → Install → Enable**.
2. **Settings → Omnisearch → Options**:
   - ✅ "Index PDF files" — activado.
3. La primera vez tarda un minuto en indexar.
4. Abre Omnisearch con `Ctrl+Shift+F` y busca cualquier cosa: encuentra coincidencias **dentro** del texto de los PDFs.

---

## 🗂️ Cómo procesar la avalancha de importados

Cuando importas 500 PDFs de golpe, todos quedan con `#importado`. Para procesarlos sistemáticamente:

### Dashboard de pendientes (Dataview)

Agrega esto a tu MOC o crea una nota nueva:

````markdown
## 📥 PDFs Pendientes de Procesar

```dataview
TABLE WITHOUT ID
  file.link AS "Nota",
  tipo AS "Tipo",
  num-paginas AS "Páginas"
FROM #importado
SORT tipo, file.name
```
````

Cada vez que termines de procesar una nota, quita la etiqueta `importado` del frontmatter y desaparece del listado.

---

## ⚠️ PDFs escaneados (OCR)

Si el PDF es una **imagen escaneada** (no texto seleccionable), `pypdf` no podrá extraer nada útil. El importador igual genera la nota con título y enlace al PDF, pero sin extracto.

### Solución: OCR antes de importar

**Mac/Linux** — usa `ocrmypdf` para convertir escaneos en PDFs con texto buscable:

```bash
brew install ocrmypdf   # Mac
# o: sudo apt install ocrmypdf  # Linux

ocrmypdf input-escaneado.pdf input-con-texto.pdf -l spa
```

Luego importas el PDF resultante normalmente.

**Windows** — usa Adobe Acrobat Pro o ABBYY FineReader para OCR antes de importar.

---

## 🧹 Limitaciones conocidas

| Problema | Estado |
|----------|--------|
| PDFs escaneados sin OCR | Genera nota vacía. Hacer OCR antes |
| PDFs encriptados/protegidos | Falla con error claro. Quitar protección antes |
| Extracción rompe el formato de columnas | Esperado — el extracto es solo preview, el original queda intacto |
| Caracteres especiales mal codificados | Frecuente en PDFs antiguos. Editar manualmente |
| Detección de título falla con PDFs sin metadata | Usa la primera línea — puede quedar raro |

---

## 🧪 Verificar que funciona

```bash
# 1. Setup (si no lo has hecho)
./scripts/litigio.sh setup

# 2. Importar un PDF de prueba
./scripts/litigio.sh importar /ruta/a/un-pdf-cualquiera.pdf

# 3. Abrir Obsidian — verás la nota nueva en 02-Marco-Legal/ o 03-Biblioteca/
# 4. La etiqueta #importado marca que está pendiente de procesar
```

---

*[[000-MOC-Principal|← Dashboard]] · [[Integracion-Python|Integración Python]] · [[Como-Usar-Este-Sistema|Cómo usar]]*
