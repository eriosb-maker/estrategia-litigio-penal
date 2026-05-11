---
tipo: actor
subtipo: juez
nombre: "{{NOMBRE COMPLETO}}"
tribunal: "{{TRIBUNAL}}"
sala: "{{SALA}}"
cargo: "{{Juez | Ministro | Presidente}}"
materia: "{{penal | civil | ambos}}"
etiquetas: [actor, juez, {{tribunal}}]
---

# 👨‍⚖️ {{NOMBRE}} — {{TRIBUNAL}}

> ⚠️ *Esta nota contiene observaciones profesionales para uso interno del estudio. Tratar con absoluta confidencialidad.*

---

## Perfil

| Campo | Valor |
|-------|-------|
| **Tribunal** | {{TRIBUNAL}} |
| **Cargo** | {{CARGO}} |
| **Años en el cargo** | {{N}} |
| **Formación** | {{Universidad, posgrados}} |
| **Antigüedad** | {{Escalafón}} |

---

## Estilo Judicial Observado

### En Audiencias
- **Manejo del tiempo**: Puntual / Flexible / Impredecible
- **Tolerancia a incidentes**: Alta / Media / Baja
- **Intervención espontánea**: Frecuente / Ocasional / Escasa

### Valoración de la Prueba
- **Prueba pericial**: Depende mucho / Medianamente / Poco del perito
- **Prueba testimonial**: Pesa mucho la credibilidad / Analiza lógicamente / Formalista
- **Prueba documental**: Riguroso / Flexible

### Posición sobre Estándares
- **Umbral para condena observado**: Alto (exige mucho) / Estándar / Bajo
- **Tendencia en penal**: Pro-defensa / Neutral / Pro-fiscalía (estadística)

---

## Posiciones Jurídicas Conocidas

| Tema | Posición | Caso de Referencia |
|------|---------|-------------------|
| Exclusión de prueba ilícita | | [[02-Marco-Legal/]] |
| Legítima defensa | | |
| Valoración de testigo único | | |

---

## Historial de Causas

```dataview
TABLE causa AS "Causa", resultado-final AS "Resultado", materia AS "Materia"
FROM "01-Causas"
WHERE tipo = "causa" AND juez = this.nombre
SORT fecha-cierre DESC
```

**Estadísticas personales**:
- Causas ante este juez: {{N}}
- Resultados favorables: {{N}} ({{%}})

---

## Notas de Observación

### Audiencia: {{FECHA}} — {{CAUSA}}
*Observaciones de comportamiento y estilo*:

---

## Cómo Maximizar Resultados ante este Juez

- ✅ **Hacer**: 
- ❌ **Evitar**: 

---

*[[08-Actores/MOC-Actores|← Actores]]*
