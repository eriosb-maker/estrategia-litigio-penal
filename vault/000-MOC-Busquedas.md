---
tipo: moc
etiquetas: [moc, busqueda]
---

# 🔍 MOC de Búsquedas Guardadas

> Queries Dataview reutilizables para encontrar lo que necesites en segundos.
> Si necesitas búsqueda por texto libre, ver [[Busqueda|Guía completa de búsqueda]].

---

## 📋 Pendientes Globales

### 🔴 Todas las tareas abiertas en causas (ordenadas por fecha)

```dataview
TASK
FROM "01-Causas"
WHERE !completed
SORT due ASC, file.name ASC
```

### 🟡 PDFs importados sin procesar (#importado)

```dataview
TABLE WITHOUT ID
  file.link AS "Nota",
  tipo AS "Tipo",
  num-paginas AS "Páginas"
FROM #importado
SORT tipo ASC, file.name ASC
```

---

## ⚖️ Causas

### Causas activas

```dataview
TABLE WITHOUT ID
  file.link AS "Causa",
  materia AS "Materia",
  rol-abogado AS "Rol",
  tribunal AS "Tribunal",
  proxima-audiencia AS "Próxima audiencia",
  probabilidad-condena AS "P(condena)"
FROM "01-Causas"
WHERE tipo = "causa" AND estado = "en-proceso"
SORT proxima-audiencia ASC
```

### Causas con audiencia en los próximos 14 días

```dataview
TABLE WITHOUT ID
  file.link AS "Causa",
  proxima-audiencia AS "Audiencia",
  tribunal,
  juez
FROM "01-Causas"
WHERE tipo = "causa"
  AND proxima-audiencia >= date(today)
  AND proxima-audiencia <= date(today) + dur(14 days)
SORT proxima-audiencia ASC
```

### Causas penales con P(condena) > 70% (urgente negociar)

```dataview
TABLE WITHOUT ID
  file.link AS "Causa",
  probabilidad-condena AS "P(C)",
  imputado,
  recomendacion-estrategia AS "Estrategia"
FROM "01-Causas"
WHERE tipo = "causa" AND materia = "penal" AND probabilidad-condena > 0.7
SORT probabilidad-condena DESC
```

### Causas cerradas el último año (análisis post-mortem)

```dataview
TABLE WITHOUT ID
  file.link AS "Causa",
  materia,
  rol-abogado AS "Rol",
  probabilidad-condena AS "P(C) final"
FROM "01-Causas"
WHERE tipo = "causa" AND estado = "cerrada"
  AND fecha-inicio >= date(today) - dur(365 days)
SORT fecha-inicio DESC
```

---

## 📜 Marco Legal

### Normas más citadas en mis causas

```dataview
TABLE WITHOUT ID
  file.link AS "Norma",
  cuerpo-legal AS "Código",
  length(file.inlinks) AS "Veces citada"
FROM "02-Marco-Legal"
WHERE tipo = "norma"
SORT length(file.inlinks) DESC
LIMIT 20
```

### Jurisprudencia favorable a defensa

```dataview
TABLE WITHOUT ID
  file.link AS "Fallo",
  tribunal,
  rol AS "Rol",
  fecha-fallo AS "Fecha",
  relevancia
FROM "02-Marco-Legal"
WHERE tipo = "jurisprudencia" AND favorece = "defensa"
SORT fecha-fallo DESC
```

### Jurisprudencia favorable a acusación

```dataview
TABLE WITHOUT ID
  file.link AS "Fallo",
  tribunal,
  rol AS "Rol",
  fecha-fallo AS "Fecha",
  relevancia
FROM "02-Marco-Legal"
WHERE tipo = "jurisprudencia" AND favorece = "acusacion"
SORT fecha-fallo DESC
```

### Normas vigentes vs derogadas

```dataview
TABLE WITHOUT ID
  file.link AS "Norma",
  cuerpo-legal,
  articulo
FROM "02-Marco-Legal"
WHERE tipo = "norma" AND !vigente
```

---

## 📚 Biblioteca

### Lecturas pendientes (no leídas) por relevancia

```dataview
TABLE WITHOUT ID
  file.link AS "Obra",
  autor,
  año,
  relevancia
FROM "03-Biblioteca"
WHERE tipo = "libro" OR tipo = "paper" OR tipo = "lectura"
WHERE leido != true
SORT relevancia ASC, año DESC
```

### Lecturas marcadas como Alta relevancia

```dataview
TABLE WITHOUT ID
  file.link AS "Obra",
  autor,
  tipo
FROM "03-Biblioteca"
WHERE relevancia = "alta"
SORT autor ASC
```

---

## 👤 Actores (jueces, fiscales, peritos)

### Jueces con más causas observadas

```dataview
TABLE WITHOUT ID
  file.link AS "Juez/a",
  institucion AS "Tribunal"
FROM "08-Actores"
WHERE rol = "juez"
SORT length(file.inlinks) DESC
```

### Fiscales con más causas

```dataview
TABLE WITHOUT ID
  file.link AS "Fiscal",
  institucion AS "Institución"
FROM "08-Actores"
WHERE rol = "fiscal"
SORT length(file.inlinks) DESC
```

---

## 🧠 Conceptos

### Conceptos huérfanos (sin enlaces — candidatos a borrar o conectar)

```dataview
LIST FROM "07-Conceptos"
WHERE length(file.outlinks) = 0 AND length(file.inlinks) = 0
```

### Conceptos más conectados (importantes en el sistema)

```dataview
TABLE WITHOUT ID
  file.link AS "Concepto",
  length(file.inlinks) AS "Veces referenciado"
FROM "07-Conceptos"
SORT length(file.inlinks) DESC
LIMIT 20
```

---

## 🏛️ Audiencias

### Próximas audiencias (todas las causas)

```dataview
TABLE WITHOUT ID
  file.link AS "Audiencia",
  causa-ruc AS "Causa",
  fecha AS "Fecha",
  tipo-audiencia AS "Tipo",
  juez
FROM #audiencia
WHERE fecha >= date(today)
SORT fecha ASC
```

### Audiencias recientes con resultado favorable

```dataview
TABLE WITHOUT ID
  file.link AS "Audiencia",
  causa-ruc,
  fecha,
  resultado
FROM #audiencia
WHERE resultado = "favorable"
  AND fecha >= date(today) - dur(90 days)
SORT fecha DESC
```

### Audiencias desfavorables (para aprender)

```dataview
TABLE WITHOUT ID
  file.link AS "Audiencia",
  causa-ruc,
  fecha,
  juez,
  fiscal
FROM #audiencia
WHERE resultado = "desfavorable"
SORT fecha DESC
LIMIT 20
```

---

## 📥 Inbox y Bandeja

### Ideas capturadas (Ctrl+Shift+I) — pendientes de procesar

```dataview
TABLE WITHOUT ID
  file.link AS "Nota",
  file.mtime AS "Última modificación"
FROM "00-Inbox"
SORT file.mtime DESC
```

---

## 📊 Métricas del estudio

### Resumen general

| Métrica | Valor |
|---------|-------|
| Total causas | `$= dv.pages('"01-Causas"').where(p => p.tipo === 'causa').length` |
| Causas activas | `$= dv.pages('"01-Causas"').where(p => p.estado === 'en-proceso').length` |
| Total normas | `$= dv.pages('"02-Marco-Legal"').where(p => p.tipo === 'norma').length` |
| Total jurisprudencia | `$= dv.pages('"02-Marco-Legal"').where(p => p.tipo === 'jurisprudencia').length` |
| Total libros | `$= dv.pages('"03-Biblioteca"').where(p => p.tipo === 'libro').length` |
| Total conceptos | `$= dv.pages('"07-Conceptos"').length` |
| PDFs importados pendientes | `$= dv.pages('#importado').length` |

### P(condena) promedio en mis causas activas

```dataviewjs
const causas = dv.pages('"01-Causas"').where(p => p.tipo === 'causa' && p.estado === 'en-proceso');
const probs = causas.map(c => c['probabilidad-condena']).filter(p => p !== undefined);
if (probs.length > 0) {
  const avg = probs.reduce((a, b) => a + b, 0) / probs.length;
  dv.paragraph(`**P(condena) promedio**: ${(avg * 100).toFixed(1)}% (sobre ${probs.length} causas)`);
} else {
  dv.paragraph("Sin datos.");
}
```

---

## 🆕 Plantillas para nuevas búsquedas

¿Necesitas una búsqueda nueva? Copia uno de estos esqueletos:

### Lista simple

````markdown
```dataview
LIST FROM "CARPETA"
WHERE CONDICION
```
````

### Tabla con propiedades

````markdown
```dataview
TABLE prop1, prop2, prop3
FROM "CARPETA"
WHERE CONDICION
SORT prop1 ASC
```
````

### Tareas

````markdown
```dataview
TASK
FROM "CARPETA"
WHERE !completed
```
````

---

*[[000-MOC-Principal|← Dashboard]] · [[Busqueda|Guía de búsqueda completa]]*
