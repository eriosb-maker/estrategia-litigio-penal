---
tipo: moc
titulo: Marco Legal
etiquetas: [moc, marco-legal]
---

# 📜 Marco Legal

## Normas por Materia

### Derecho Penal Sustantivo
```dataview
LIST FROM "02-Marco-Legal"
WHERE tipo = "norma" AND materia = "penal"
SORT titulo ASC
```

### Derecho Procesal Penal
```dataview
LIST FROM "02-Marco-Legal"
WHERE tipo = "norma" AND materia = "procesal"
SORT titulo ASC
```

### Derecho Civil
```dataview
LIST FROM "02-Marco-Legal"
WHERE tipo = "norma" AND materia = "civil"
SORT titulo ASC
```

## Jurisprudencia

### Corte Suprema
```dataview
TABLE fecha-fallo AS "Fecha", favorece AS "Favorece", titulo AS "Resumen"
FROM "02-Marco-Legal"
WHERE tipo = "jurisprudencia" AND tribunal = "CS"
SORT fecha-fallo DESC
```

### Cortes de Apelaciones
```dataview
TABLE fecha-fallo AS "Fecha", tribunal AS "Tribunal", favorece AS "Favorece"
FROM "02-Marco-Legal"
WHERE tipo = "jurisprudencia" AND tribunal = "CA"
SORT fecha-fallo DESC
```

### TOP / TJOP
```dataview
TABLE fecha-fallo AS "Fecha", tribunal AS "Tribunal"
FROM "02-Marco-Legal"
WHERE tipo = "jurisprudencia" AND (tribunal = "TOP" OR tribunal = "TJOP")
SORT fecha-fallo DESC
```

---
*[[000-MOC-Principal|← Dashboard]]*
