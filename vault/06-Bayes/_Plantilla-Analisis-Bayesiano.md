---
tipo: analisis-bayes
causa: "{{NOMBRE_CAUSA}}"
ruc: "{{RUC}}"
fecha: {{YYYY-MM-DD}}
probabilidad-prior: {{0.0}}
probabilidad-posterior: {{0.0}}
etiquetas: [bayes, analisis, {{ruc}}]
umbral-condena: 0.90
recomendacion: "{{juicio | negociar | salida-alternativa}}"
---

# 📊 Análisis Bayesiano — {{NOMBRE_CAUSA}}

> Análisis generado el {{FECHA}} | Causa: [[01-Causas/|{{RUC}}]]

---

## Probabilidad A Priori

**P(Condena_inicial)** = {{%}}

**Base para esta estimación**:
- Tasa histórica de condenas para {{tipo delito}} en {{tribunal}}: {{%}}
- Ajuste por factores del caso: {{descripción}}
- Fuente: [[08-Actores/]] (historial del juez), estadísticas del CEAD

---

## Inventario de Evidencias

### Evidencias de Cargo (aumentan P(Condena))

| N° | Evidencia | P(E\|Culpable) | P(E\|Inocente) | LR | Peso |
|----|-----------|---------------|----------------|-----|------|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |

### Evidencias de Descargo (reducen P(Condena))

| N° | Evidencia | P(E\|Culpable) | P(E\|Inocente) | LR | Peso |
|----|-----------|---------------|----------------|-----|------|
| 1 | | | | | |
| 2 | | | | | |

---

## Cálculo Bayesiano

### Odds A Priori
```
Odds_prior = P / (1-P) = {{P}} / {{1-P}} = {{ODDS_PRIOR}}
```

### Multiplicación de LRs
```
LR_total = LR_1 × LR_2 × ... × LR_n = {{CALCULO}}
         = {{LR_TOTAL}}
```

### Odds A Posteriori
```
Odds_posterior = Odds_prior × LR_total = {{ODDS_PRIOR}} × {{LR_TOTAL}} = {{ODDS_POST}}
```

### Probabilidad A Posteriori
```
P(Condena | Evidencia) = Odds_post / (1 + Odds_post) = {{RESULTADO}}
```

**P(Condena | Evidencia) = {{PORCENTAJE}}%**

---

## Análisis de Sensibilidad

¿Qué pasa si excluimos cada evidencia clave?

| Evidencia Excluida | P(Condena) Resultante | Diferencia |
|-------------------|----------------------|------------|
| Sin evidencia N°1 | {{%}} | {{±%}} |
| Sin evidencia N°2 | {{%}} | {{±%}} |
| **Evidencia más crítica** | | |

---

## Escenarios

| Escenario | P(Condena) | Descripción |
|-----------|-----------|-------------|
| Pesimista | {{%}} | Si toda la evidencia se valora en nuestra contra |
| Base | **{{%}}** | Análisis central |
| Optimista | {{%}} | Si logramos excluir/impugnar evidencias clave |

---

## Comparación con Umbral del Estándar de Prueba

```
P(Condena | E) = {{%}}
Umbral "más allá de duda razonable" ≈ 90%

Margen: {{% - 90%}} → {"peligro" si positivo, "margen favorable" si negativo}
```

---

## Recomendación

### Decisión: **{{JUICIO / NEGOCIAR / SALIDA ALTERNATIVA}}**

**Razonamiento Bayesiano**:

Si P(Condena) = {{%}}:
- Valor esperado del juicio para el imputado = {{-p × pena - costos}} = **{{VALUE}}**
- Valor del acuerdo ofrecido = **{{ACUERDO}}**
- → {{Comparación y decisión}}

### Qué necesitaríamos para cambiar la recomendación

Para que "ir a juicio" sea preferible, necesitaríamos bajar P(Condena) a < {{%}}.
Esto requeriría: {{descripción de acciones}}

---

## Notas y Advertencias

⚠️ **Limitaciones de este análisis**:
- Los valores de LR son estimaciones subjetivas del abogado
- Se asume independencia entre evidencias (puede no ser correcto)
- No captura todos los factores cualitativos (ej: lenguaje corporal del imputado)

---

*Análisis complementario: [[05-Teoria-Juegos/_Plantilla-Analisis-TJ|Análisis Teoría de Juegos]]*
*[[06-Bayes/MOC-Bayes|← Análisis Bayesiano]]*
