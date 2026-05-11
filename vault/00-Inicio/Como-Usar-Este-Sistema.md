---
tipo: guia
titulo: Cómo Usar Este Segundo Cerebro Legal
fecha-creacion: 2026-01-01
etiquetas: [guia, inicio, sistema, karpathy]
---

# 🧠 Cómo Usar Este Segundo Cerebro Legal

## El Principio Karpathy

Andrej Karpathy describe el segundo cerebro como un sistema externo de procesamiento cognitivo donde:
- **No memorizas**: almacenas y enlazas
- **No buscas**: navegas por conexiones
- **No repites trabajo**: reutilizas y actualizas nodos

Aplicado al litigio: cada causa, ley, argumento y observación es un **nodo** en una red de conocimiento que crece con cada caso.

---

## 📁 Estructura del Vault

```
vault/
├── 000-MOC-Principal.md       ← Dashboard (empieza aquí)
├── 00-Inicio/                 ← Guías del sistema
├── 01-Causas/                 ← Una subcarpeta por causa
│   └── RUC-XXXX-YYYY/
│       ├── 00-Resumen-Causa.md
│       ├── 01-Hechos.md
│       ├── 02-Pruebas.md
│       ├── 03-Testigos.md
│       ├── 04-Analisis-Bayes.md
│       └── 05-Estrategia-TJ.md
├── 02-Marco-Legal/            ← Normas y jurisprudencia
├── 03-Biblioteca/             ← Libros y papers
├── 04-Estrategias/            ← Estrategias reutilizables
├── 05-Teoria-Juegos/          ← Modelos estratégicos
├── 06-Bayes/                  ← Análisis probabilísticos
├── 07-Conceptos/              ← Notas atómicas de conceptos
└── 08-Actores/                ← Jueces, fiscales, peritos
```

---

## 🔄 Flujo para una Causa Nueva

### Paso 1: Crear la causa
```bash
python scripts/nueva_causa.py --ruc "2024-1234" --nombre "Caso Ejemplo" --tipo "penal"
```
Esto crea automáticamente la carpeta con todas las notas base.

### Paso 2: Cargar los hechos
En `01-Causas/RUC-2024-1234/01-Hechos.md`:
- Descripción cronológica de los hechos
- Fuentes de cada hecho (declaración, video, pericia, etc.)
- Nivel de certeza (alto / medio / bajo)

### Paso 3: Registrar pruebas
En `01-Causas/RUC-2024-1234/02-Pruebas.md`:
- Cada prueba con su peso probatorio
- Enlazar a [[02-Marco-Legal/]] para normas de admisibilidad
- Marcar si es favorable/desfavorable

### Paso 4: Análisis Bayesiano
```bash
python scripts/analizar_causa.py --ruc "2024-1234" --modo bayes
```
Genera `04-Analisis-Bayes.md` con probabilidades actualizadas por evidencia.

### Paso 5: Modelar con Teoría de Juegos
```bash
python scripts/analizar_causa.py --ruc "2024-1234" --modo juegos
```
Genera `05-Estrategia-TJ.md` con matriz de pagos y equilibrios.

### Paso 6: Cruzar con Biblioteca
Usar el buscador de Obsidian (`Ctrl+Shift+F`) para encontrar:
- Papers sobre el tipo de delito
- Jurisprudencia similar
- Estrategias probadas en el área

---

## 🏷️ Sistema de Etiquetas

| Etiqueta | Uso |
|----------|-----|
| `#penal` | Materia penal |
| `#civil` | Materia civil |
| `#defensa` | Perspectiva defensora |
| `#acusacion` | Perspectiva fiscal/demandante |
| `#urgente` | Requiere atención inmediata |
| `#bayes` | Tiene análisis bayesiano |
| `#tj` | Tiene análisis de teoría de juegos |
| `#revisar` | Pendiente de revisión |
| `#precedente` | Caso con valor de precedente |

---

## 🔗 Convenciones de Enlace

- `[[Nombre de Nota]]` → Enlace directo
- `[[Nota|Texto visible]]` → Enlace con alias
- `[[02-Marco-Legal/Art-XX-CP|Art. XX CP]]` → Enlace a norma específica

### Tipos de relaciones a documentar:
- `> Véase también:` → Notas relacionadas
- `> Contrargumento:` → Posición contraria
- `> Fuente:` → Origen del dato
- `> Aplica en:` → Causas donde aplica este concepto

---

## 📊 Plugins Recomendados de Obsidian

| Plugin | Función |
|--------|---------|
| **Dataview** | Consultas dinámicas (como SQL) para el vault |
| **Templater** | Plantillas con lógica y fechas automáticas |
| **Graph View** | Visualizar conexiones entre notas |
| **Calendar** | Vista de calendario con audiencias |
| **QuickAdd** | Captura rápida de ideas y hechos |
| **Tasks** | Gestión de tareas y deadlines |
| **Excalidraw** | Diagramas de estrategia y relaciones |
| **Natural Language Dates** | Fechas en lenguaje natural |

---

## 💡 Principios del Sistema

### 1. Nota Atómica
Cada nota cubre **una sola idea**. Si tienes dos ideas, crea dos notas y enlázalas.

### 2. Enlace Bidireccional
Si la Nota A menciona la Nota B, Obsidian automáticamente muestra en B que A la menciona. Explota esto.

### 3. Progressive Summarization (Karpathy)
- **Nivel 1**: Copia textual del fuente
- **Nivel 2**: Highlight de lo importante (negrita)
- **Nivel 3**: Resumen propio al inicio
- **Nivel 4**: Solo el resumen con links a detalles

### 4. Evergreen Notes
Las notas deben ser **atemporales**: actualiza la nota existente en vez de crear una nueva cuando cambias de opinión.

### 5. Retrieval Practice
Antes de buscar en el vault, intenta recordar. Esto refuerza el aprendizaje y revela lagunas.

---

*[[000-MOC-Principal|← Volver al Dashboard]]*
