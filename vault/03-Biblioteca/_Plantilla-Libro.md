---
tipo: libro
titulo: "{{TÍTULO}}"
autor: "{{AUTOR}}"
año: {{YYYY}}
editorial: "{{EDITORIAL}}"
isbn: "{{ISBN}}"
materia: "{{penal | civil | procesal | teoria}}"
etiquetas: [libro, {{materia}}, {{autor}}]
relevancia: "{{alta | media | baja}}"
leido: false
---

# 📖 {{TÍTULO}}
**{{AUTOR}}** ({{AÑO}}) — {{EDITORIAL}}

---

## Resumen en 3 Puntos

> *Progressive Summarization Nivel 3 — Lo más importante del libro*

1. 
2. 
3. 

---

## Tesis Central

> *¿Cuál es el argumento principal del autor?*

---

## Conceptos Clave

### {{Concepto 1}}
> *Definición o idea principal*

Ver: [[07-Conceptos/]]

### {{Concepto 2}}
> *Definición o idea principal*

---

## Citas Destacadas

> *"{{CITA TEXTUAL}}"* (p. {{N}})

> *"{{CITA TEXTUAL}}"* (p. {{N}})

---

## Tabla de Contenidos Relevante

| Capítulo | Tema | Páginas | Utilidad |
|----------|------|---------|---------|
| | | | Alta/Media/Baja |

---

## Aplicación Práctica

### Casos donde aplica
```dataview
LIST FROM "01-Causas"
WHERE tipo = "causa" AND contains(fuentes-biblioteca, this.file.name)
```

### Estrategias que fundamenta
- [[04-Estrategias/]]

### Normas que ilumina
- [[02-Marco-Legal/]]

---

## Crítica y Limitaciones


---

## Notas de Lectura

### Capítulo {{N}}: {{TÍTULO}}
*p. {{N}}-{{N}}*

**Idea principal**:

**Cita clave**:
> *""*

**Conexiones**:
- [[]]

---

*Añadido: {{FECHA}} | Completado: {{FECHA}}*
*[[03-Biblioteca/MOC-Biblioteca|← Biblioteca]]*
