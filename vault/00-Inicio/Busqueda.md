---
tipo: doc
etiquetas: [doc, busqueda, productividad]
---

# 🔍 Buscar en el Segundo Cerebro

> El sistema tiene **4 capas de búsqueda** complementarias. Saber cuándo usar cada una es la diferencia entre encontrar lo que necesitas en 5 segundos o en 5 minutos.

---

## 🎯 Decisión rápida: ¿qué uso?

| Lo que quiero encontrar | Herramienta | Atajo |
|-------------------------|-------------|-------|
| Un nombre exacto, un RUC, un artículo | **Quick Switcher** | `Ctrl+O` |
| Una palabra dentro de una nota o PDF | **Omnisearch** | `Ctrl+Shift+F` |
| Todas las causas que citan una norma | **Dataview** | (en MOC) |
| Patrón complejo / regex / muchos archivos | **Terminal (ripgrep)** | `./scripts/litigio.sh buscar` |

---

## 1️⃣ Quick Switcher — saltar a una nota por nombre

**Atajo**: `Ctrl+O` (Mac: `Cmd+O`)

Para cuando ya sabes cómo se llama la nota:
- `Cmd+O` → escribes `Art 468` → enter → ahí está.
- `Cmd+O` → escribes `2024-001` → llegas a tu causa.

> Es lo más rápido. Acostumbra los dedos a este atajo.

---

## 2️⃣ Omnisearch — el motor de búsqueda completo

**Atajo**: `Ctrl+Shift+F` (en todo el vault, incluyendo PDFs)
**Atajo alterno**: `Ctrl+Alt+F` (solo vault, sin PDFs — más rápido)

### Qué busca

- ✅ Texto dentro de notas Markdown
- ✅ Texto dentro de **PDFs** (gracias a configuración pre-activada)
- ✅ Títulos, encabezados, frontmatter
- ✅ Tolera errores de tipeo (fuzziness: 1)
- ❌ No busca en imágenes ni en archivos Office (por configuración por defecto)

### Cómo está configurado

| Aspecto | Valor |
|---------|-------|
| Indexación de PDFs | ✅ Activada |
| Tolerancia a errores | 1 carácter |
| Peso del nombre de archivo | 10 (alto) |
| Peso del RUC en frontmatter | 9 (muy alto) |
| Peso del título y causa | 8-6 |
| Excerpts en resultados | ✅ |
| Cache para rapidez | ✅ |

### Trucos de búsqueda

| Lo que escribes | Lo que hace |
|-----------------|-------------|
| `dolo eventual` | Busca esas dos palabras (no necesariamente juntas) |
| `"dolo eventual"` | Frase exacta |
| `dolo -culposo` | Tiene "dolo" pero NO "culposo" |
| `Art 468` | Encuentra notas con ese artículo |
| `path:02-Marco-Legal` | Solo busca en esa carpeta |
| `path:_pdfs` | Solo busca dentro de PDFs |
| `ext:pdf` | Solo archivos PDF |
| `tag:#jurisprudencia` | Solo notas con ese tag |

### Ejemplos reales del segundo cerebro

```
"presunción de inocencia"
→ Encuentra el concepto, las normas que la consagran y los fallos que la aplican

estafa path:02-Marco-Legal
→ Solo normas/jurisprudencia sobre estafa, ignora libros y causas

prueba ilícita path:_pdfs
→ Busca dentro de tus libros PDF sobre prueba ilícita

ruc:2024-001
→ Va directo a esa causa
```

---

## 3️⃣ Búsqueda nativa de Obsidian

**Atajo**: `Ctrl+Shift+S` (Mac: `Cmd+Shift+F`)

Es la búsqueda original. Más rápida que Omnisearch para queries simples pero **no indexa PDFs**.

### Cuándo usarla
- Cuando quieres operadores específicos (`line:`, `block:`, `section:`)
- Para regex avanzados
- Cuando Omnisearch tarda mucho indexando

### Operadores útiles

| Operador | Ejemplo | Función |
|----------|---------|---------|
| `tag:` | `tag:#causa tag:#penal` | Múltiples tags |
| `line:` | `line:(dolo culpa)` | Ambas en la misma línea |
| `section:` | `section:("Pruebas de Cargo")` | Dentro de una sección |
| `task:` | `task:"audiencia"` | En tareas pendientes |
| `task-todo:` | `task-todo:""` | Tareas no completadas |
| `file:` | `file:.pdf` | Solo archivos PDF |
| `/regex/` | `/Art\.\s+\d+/` | Expresiones regulares |

---

## 4️⃣ Dataview — búsquedas estructuradas

Dataview es búsqueda **por propiedades** (frontmatter), no por texto. Perfecto para encontrar **conjuntos** de notas.

### Ejemplos integrados en el vault

Ver: [[000-MOC-Busquedas|MOC de Búsquedas Guardadas]]

### Patrón común: causas que citan una norma

````markdown
```dataview
LIST FROM "01-Causas"
WHERE contains(file.outlinks, [[Art-440-CP]])
```
````

### Patrón: jurisprudencia favorable a defensa por año

````markdown
```dataview
TABLE rol AS "Rol", tribunal, fecha-fallo AS "Fecha"
FROM "02-Marco-Legal"
WHERE tipo = "jurisprudencia" AND favorece = "defensa"
SORT fecha-fallo DESC
```
````

### Patrón: pendientes globales

````markdown
```dataview
TASK
FROM "01-Causas"
WHERE !completed
SORT due ASC
```
````

---

## 5️⃣ Terminal — `litigio.sh buscar`

Para búsquedas masivas (cientos de archivos) o regex complejas, el terminal es más rápido:

```bash
./scripts/litigio.sh buscar "dolo eventual"
./scripts/litigio.sh buscar "Art\. 4[0-9]{2}"   # regex
./scripts/litigio.sh buscar "presunción" --en 02-Marco-Legal
```

---

## 🧠 Estrategias prácticas

### Estrategia 1: encontrar precedentes para tu causa

1. `Ctrl+Shift+F` → describe el problema jurídico: `legítima defensa exceso`
2. Filtras los resultados para quedarte con tipo `jurisprudencia`
3. Lees los holdings
4. En la nota de tu causa actual, agregas enlaces `[[]]` a los precedentes encontrados

### Estrategia 2: ¿qué dije sobre este juez en otras causas?

1. `Ctrl+O` → `Juez-López` → abre la ficha del juez
2. Bajo "Causas Donde Aparece" (Dataview) aparecen todas las causas con este juez
3. Bajo "Audiencias Donde Participó" aparecen todas las audiencias documentadas
4. → Acumulas inteligencia operacional sobre ese juez

### Estrategia 3: ¿qué dice mi biblioteca sobre este tema?

1. `Ctrl+Shift+F` → `path:_pdfs` + tu término
2. Omnisearch te muestra el extracto del PDF donde aparece
3. Clic en el resultado → abre el PDF en la página relevante
4. Si vale la pena, copias la cita a la nota correspondiente en `03-Biblioteca/`

### Estrategia 4: auditoría rápida de una causa

1. Abre el `00-Resumen.md` de la causa
2. En el panel derecho, abre la pestaña **"Backlinks"** (Ctrl+Shift+B)
3. Ves todas las notas (conceptos, jurisprudencia, otras causas) que enlazan a esta
4. Eso te dice qué tan "conectada" está la causa: si tiene 0 backlinks, probablemente le falta análisis

---

## ⚡ Ajustar Omnisearch a tu uso

Si después de usar el plugin notas que algo no funciona como esperas:

1. **Settings → Community plugins → Omnisearch → Options**
2. Tres ajustes que suelen pedir cambio:

| Opción | Recomendado | Cuándo cambiarlo |
|--------|-------------|------------------|
| **Fuzziness** | 1 | Subirlo a 2 si tipeas con muchos errores |
| **Excerpt length** | default | Bajarlo si los resultados se ven muy largos |
| **Display title** | (vacío) | Poner `{{title}}` si quieres títulos largos |

---

## 🆘 Problemas comunes

| Problema | Solución |
|----------|----------|
| Omnisearch no encuentra contenido nuevo | Reabre Obsidian. Indexa al arrancar |
| Los PDFs no aparecen en resultados | Verifica: Omnisearch → Options → "PDF Indexing" ON |
| Mac dice "Cmd+Shift+F está ocupado" | Settings → Hotkeys → reasignar a `Cmd+Shift+G` o similar |
| Búsqueda lenta con miles de PDFs | Activa "useCache" (ya está activado por defecto) |

---

## 📚 Referencias

- [[Importar-PDFs|Importar PDFs al vault]] — para llenar la biblioteca
- [[Integracion-Python|Integración Python]] — para análisis de causas
- [[000-MOC-Busquedas|MOC de Búsquedas guardadas]] — queries listas para usar

---

*[[000-MOC-Principal|← Dashboard]]*
