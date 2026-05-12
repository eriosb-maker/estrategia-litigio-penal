<%*
const nombre = await tp.system.prompt("Nombre de la norma (ej: Robo con fuerza en las cosas)");
const cuerpo = await tp.system.suggester(
  ["Código Penal", "Código Procesal Penal", "Código Civil", "Código del Trabajo", "CPR", "Ley especial"],
  ["CP", "CPP", "CC", "CT", "CPR", "Ley"]
);
const articulo = await tp.system.prompt("Artículo (solo número, ej: 440)");
const materia = await tp.system.suggester(
  ["penal", "civil", "procesal", "constitucional", "laboral"],
  ["penal", "civil", "procesal", "constitucional", "laboral"]
);
const favorece = await tp.system.suggester(
  ["Defensa", "Acusación", "Neutral"],
  ["defensa", "acusacion", "neutral"]
);
const hoy = tp.date.now("YYYY-MM-DD");
const nombreSlug = nombre.replace(/[^a-zA-Z0-9áéíóúñÑ ]/g, "").replace(/\s+/g, "-");
await tp.file.rename(`${cuerpo}-Art-${articulo}-${nombreSlug}`);
-%>
---
tipo: norma
titulo: "<% nombre %>"
cuerpo-legal: "<% cuerpo %>"
articulo: "Art. <% articulo %>"
materia: "<% materia %>"
favorece: "<% favorece %>"
vigente: true
fecha-captura: <% hoy %>
etiquetas: [norma, <% materia %>, <% cuerpo.toLowerCase() %>]
---

# 📜 <% nombre %> — <% cuerpo %> Art. <% articulo %>

> *Capturada: <% hoy %> | Favorece: <% favorece %>*

---

## Texto Legal

> *"Pegar aquí el texto literal del artículo"*

---

## Análisis del Tipo / Requisitos

### Elementos
1. 
2. 
3. 

### Bien Jurídico Protegido


### Sujeto Activo


### Sujeto Pasivo


### Verbo Rector


### Pena / Consecuencia Jurídica


---

## Interpretación Doctrinaria

### Posición Mayoritaria


### Posición Minoritaria / Crítica


### Fuentes Doctrinarias
- [[03-Biblioteca/]]

---

## Jurisprudencia Relacionada

```dataview
LIST FROM "02-Marco-Legal"
WHERE tipo = "jurisprudencia" AND contains(normas-aplicadas, this.file.name)
```

---

## Causas Donde Aplica

```dataview
LIST FROM "01-Causas"
WHERE tipo = "causa" AND contains(file.outlinks, this.file.link)
```

---

## Estrategias Asociadas

### Para la Defensa
- 

### Para la Acusación
- 

---

## Notas

*Añadida: <% hoy %>*
*[[02-Marco-Legal/MOC-Marco-Legal|← Marco Legal]]*
