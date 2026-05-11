---
tipo: moc
titulo: Mapa de Estrategias
etiquetas: [moc, estrategias]
---

# ♟️ Mapa de Estrategias

## Colecciones Principales
- [[Estrategias-Defensa-Penal]] — Estrategias para la defensa en causas penales
- [[Estrategias-Acusacion-Civil]] — Estrategias para litigio civil

## Estrategias Individuales

### Por Materia
```dataview
TABLE rol AS "Rol", efectividad-estimada AS "Efectividad", tipo-caso AS "Tipo de Caso"
FROM "04-Estrategias"
WHERE tipo = "estrategia"
SORT materia ASC, efectividad-estimada ASC
```

### Más Efectivas
```dataview
LIST FROM "04-Estrategias"
WHERE tipo = "estrategia" AND efectividad-estimada = "alta"
```

---
*[[000-MOC-Principal|← Dashboard]]*
