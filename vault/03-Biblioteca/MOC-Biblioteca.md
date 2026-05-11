---
tipo: moc
titulo: Biblioteca
etiquetas: [moc, biblioteca]
---

# 📚 Biblioteca

## Libros por Materia

### Derecho Penal
```dataview
TABLE autor AS "Autor", año AS "Año", relevancia AS "Relevancia"
FROM "03-Biblioteca"
WHERE tipo = "libro" AND materia = "penal"
SORT relevancia ASC, año DESC
```

### Derecho Procesal Penal
```dataview
TABLE autor AS "Autor", año AS "Año"
FROM "03-Biblioteca"
WHERE tipo = "libro" AND materia = "procesal"
SORT año DESC
```

### Teoría General / Teoría de Juegos / Probabilidad
```dataview
TABLE autor AS "Autor", año AS "Año"
FROM "03-Biblioteca"
WHERE tipo = "libro" AND (materia = "teoria" OR materia = "economia")
SORT año DESC
```

## Papers Destacados
```dataview
TABLE autores AS "Autores", año AS "Año", revista AS "Revista", relevancia AS "Relevancia"
FROM "03-Biblioteca"
WHERE tipo = "paper" AND relevancia = "alta"
SORT año DESC
```

## Pendientes de Leer
```dataview
LIST FROM "03-Biblioteca"
WHERE (tipo = "libro" OR tipo = "paper") AND leido = false
```

---
*[[000-MOC-Principal|← Dashboard]]*
