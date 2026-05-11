---
tipo: moc
titulo: Actores del Sistema
etiquetas: [moc, actores]
---

# 👥 Actores del Sistema

## Jueces
```dataview
TABLE tribunal AS "Tribunal", materia AS "Materia"
FROM "08-Actores"
WHERE tipo = "actor" AND subtipo = "juez"
SORT tribunal ASC
```

## Fiscales
```dataview
TABLE fiscalia AS "Fiscalía", especialidad AS "Especialidad"
FROM "08-Actores"
WHERE tipo = "actor" AND subtipo = "fiscal"
SORT fiscalia ASC
```

## Peritos de Confianza
```dataview
TABLE especialidad AS "Especialidad"
FROM "08-Actores"
WHERE tipo = "actor" AND subtipo = "perito"
SORT nombre ASC
```

---
*[[000-MOC-Principal|← Dashboard]]*
