---
tipo: actor
subtipo: fiscal
nombre: "{{NOMBRE COMPLETO}}"
fiscalia: "{{FISCALÍA LOCAL}}"
region: "{{REGIÓN}}"
especialidad: "{{crimen organizado | VIF | delitos economicos | general}}"
etiquetas: [actor, fiscal, {{fiscalia}}]
---

# 👮 {{NOMBRE}} — Fiscal {{FISCALÍA}}

> ⚠️ *Uso interno del estudio. Confidencial.*

---

## Perfil

| Campo | Valor |
|-------|-------|
| **Fiscalía** | {{FISCALÍA}} |
| **Años como fiscal** | {{N}} |
| **Especialidad** | {{ESPECIALIDAD}} |
| **Estilo negociador** | Flexible / Moderado / Duro |

---

## Estilo de Litigación

### Manejo de Investigación
- **Calidad de la investigación**: Exhaustiva / Estándar / Deficiente
- **Uso de peritos**: Frecuente / Ocasional
- **Respeto plazos CPP**: Riguroso / Variable

### En Juicio
- **Estructura del alegato de apertura**: Clara / Compleja / Simple
- **Contraexamen**: Agresivo / Técnico / Débil
- **Uso del estándar de prueba**: Bien argumentado / Mecánico

### En Negociación
- **Apertura a salidas alternativas**: Alta / Media / Baja
- **Factores que usa para negociar**: Carga de trabajo / Presión de víctimas / Político
- **Máxima rebaja de pena observada**: {{%}}

---

## Causas Donde Actúa

```dataview
TABLE causa AS "Causa", estado AS "Estado", resultado-final AS "Resultado"
FROM "01-Causas"
WHERE tipo = "causa" AND fiscal = this.nombre
SORT fecha-inicio DESC
```

---

## Notas de Interacción

### {{FECHA}} — {{CAUSA}}
*Observaciones de la negociación/audiencia*:

---

## Estrategia para Enfrentar a este Fiscal

- **Fortalezas que tendrá**: 
- **Debilidades que suele mostrar**: 
- **Cómo negociar con él/ella**: 

---

*[[08-Actores/MOC-Actores|← Actores]]*
