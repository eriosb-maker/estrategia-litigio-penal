# 📊 Análisis Bayesiano — Estafa Inmobiliaria - Caso González

**RUC**: 2024-DEMO-002 | **Materia**: penal | **Generado**: automático

---

## Resultado Principal

| Métrica | Valor |
|---------|-------|
| **Probabilidad A Priori** | 55.0% |
| **Probabilidad A Posteriori** | **14.2%** |
| **Umbral del estándar de prueba** | 90% |
| **¿Supera el umbral?** | ✅ NO |
| **Recomendación** | `ir-a-juicio` |

---

## Evidencias Analizadas

| N° | Evidencia | LR | Interpretación |
|----|-----------|-----|----------------|
| 1 | Transferencia $50M sin contrato firme | 2.12 | Evidencia moderada de culpabilidad |
| 2 | Informe PDI patrón estafa | 1.57 | Evidencia débil / neutral |
| 3 | Promesa firmada como vendedor | 1.50 | Evidencia débil / neutral |
| 4 | Restitución voluntaria $30M pre-querella | 0.27 | Evidencia moderada de inocencia |
| 5 | WhatsApp con mandato verbal del dueño | 0.19 | Evidencia moderada de inocencia |
| 6 | Sin antecedentes penales | 0.54 | Evidencia débil / neutral |

---

## Cálculo Detallado

```
Odds Prior       = 1.2222
LR Total         = 0.1349
Odds Posterior   = 0.1648
P(Condena|E)     = 0.1415 (14.2%)
```

## Escenarios

| Escenario | P(Condena) |
|-----------|-----------|
| 🔴 Pesimista | 86.0% |
| 🟡 Base | **14.1%** |
| 🟢 Optimista | 3.2% |

---

## Análisis de Sensibilidad

*(Impacto de excluir cada evidencia)*

| Evidencia | LR | P(Condena) sin ella | Impacto | ¿Crítica? |
|-----------|-----|---------------------|---------|-----------|
| WhatsApp con mandato verbal del dueño | 0.187 | 46.8% | -32.6% | 🔴 Sí |
| Restitución voluntaria $30M pre-querella | 0.267 | 38.2% | -24.1% | 🔴 Sí |
| Sin antecedentes penales | 0.538 | 23.4% | -9.3% | No |
| Transferencia $50M sin contrato firme | 2.125 | 7.2% | +7.0% | No |
| Informe PDI patrón estafa | 1.571 | 9.5% | +4.7% | No |
| Promesa firmada como vendedor | 1.5 | 9.9% | +4.2% | No |

---

## Recomendación: `IR-A-JUICIO`

> ✅ La probabilidad de condena es suficientemente baja. Ir a juicio es la estrategia recomendada.