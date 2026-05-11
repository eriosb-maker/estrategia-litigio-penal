---
tipo: moc
titulo: Mapa de Causas
etiquetas: [moc, causas]
---

# 📁 Mapa de Causas

## Causas Activas

```dataview
TABLE WITHOUT ID
  link(file.link, causa) AS "Causa",
  ruc AS "RUC",
  tribunal AS "Tribunal",
  materia AS "Materia",
  round(probabilidad-condena * 100, 0) + "%" AS "P(Cond.)",
  proxima-audiencia AS "Próx. Audiencia",
  estado AS "Estado"
FROM "01-Causas"
WHERE tipo = "causa" AND estado = "en-proceso"
SORT proxima-audiencia ASC
```

## Causas Cerradas

```dataview
TABLE WITHOUT ID
  link(file.link, causa) AS "Causa",
  ruc AS "RUC",
  materia AS "Materia",
  resultado-final AS "Resultado",
  fecha-cierre AS "Cierre"
FROM "01-Causas"
WHERE tipo = "causa" AND (estado = "cerrada" OR estado = "archivada")
SORT fecha-cierre DESC
```

## Nueva Causa

Usar plantilla: [[_Plantilla-Causa]] o ejecutar:
```bash
python scripts/nueva_causa.py --ruc "YYYY-NNNN" --nombre "Nombre del Caso" --tipo penal
```

---
*[[000-MOC-Principal|← Dashboard]]*
