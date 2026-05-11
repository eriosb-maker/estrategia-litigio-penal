---
tipo: moc
titulo: Análisis Bayesiano
etiquetas: [moc, bayes]
---

# 📊 Análisis Bayesiano

## Conceptos
- [[Conceptos-Bayesianos-Legales]] — Fundamentos y aplicación al litigio

## Análisis por Causa
```dataview
TABLE causa AS "Causa", fecha AS "Fecha", probabilidad-posterior AS "P(Condena)", recomendacion AS "Recomendación"
FROM "06-Bayes"
WHERE tipo = "analisis-bayes"
SORT fecha DESC
```

## Plantilla
- [[_Plantilla-Analisis-Bayesiano]] — Para generar análisis nuevo

---
*[[000-MOC-Principal|← Dashboard]]*
