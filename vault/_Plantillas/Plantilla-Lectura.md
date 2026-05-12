<%*
const titulo = await tp.system.prompt("Título de la obra");
const autor = await tp.system.prompt("Autor/a");
const año = await tp.system.prompt("Año", tp.date.now("YYYY"));
const tipoFuente = await tp.system.suggester(
  ["Libro", "Paper / Artículo", "Sentencia comentada", "Manual", "Tesis"],
  ["libro", "paper", "sentencia", "manual", "tesis"]
);
const materia = await tp.system.suggester(
  ["penal", "civil", "procesal", "teoria-juegos", "bayes", "criminologia", "filosofia-derecho"],
  ["penal", "civil", "procesal", "teoria-juegos", "bayes", "criminologia", "filosofia"]
);
const relevancia = await tp.system.suggester(["Alta", "Media", "Baja"], ["alta", "media", "baja"]);
const hoy = tp.date.now("YYYY-MM-DD");
const slug = titulo.replace(/[^a-zA-Z0-9áéíóúñÑ ]/g, "").replace(/\s+/g, "-");
await tp.file.rename(slug);
-%>
---
tipo: lectura
titulo: "<% titulo %>"
autor: "<% autor %>"
año: <% año %>
tipo-fuente: "<% tipoFuente %>"
materia: "<% materia %>"
relevancia: "<% relevancia %>"
leido: false
fecha-captura: <% hoy %>
etiquetas: [lectura, <% tipoFuente %>, <% materia %>]
---

# 📚 <% titulo %>

**<% autor %>** (<% año %>) — <% tipoFuente %>

> *Relevancia: <% relevancia %> | Capturada: <% hoy %>*

---

## Resumen en 3 Puntos

> *Progressive Summarization Nivel 3 — Lo más importante*

1. 
2. 
3. 

---

## Tesis Central

> *¿Cuál es el argumento principal?*

---

## Citas y Notas de Lectura

### Cita — p. 

> *""*

**Por qué importa**:

**Conceptos relacionados**: [[]]

---

## Conceptos Clave Extraídos

- [[07-Conceptos/]]
- [[07-Conceptos/]]

---

## Aplicación Práctica

### Causas donde aplica
```dataview
LIST FROM "01-Causas"
WHERE contains(file.outlinks, this.file.link)
```

### Estrategias que fundamenta
- [[04-Estrategias/]]

### Normas que ilumina
- [[02-Marco-Legal/]]

---

## Crítica

> *¿Limitaciones? ¿Contextos donde no aplica?*

---
*Añadida: <% hoy %>*
*[[03-Biblioteca/MOC-Biblioteca|← Biblioteca]]*
