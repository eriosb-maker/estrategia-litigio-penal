---
tipo: concepto
titulo: Equilibrio de Nash en Litigios - Aplicación Práctica
materia: teoria
etiquetas: [teoria-juegos, nash, negociacion, litigio]
---

# ⚖️ Equilibrio de Nash en Litigios

> El Equilibrio de Nash (John Nash, 1950) es el punto donde ningún jugador puede mejorar su situación cambiando unilateralmente de estrategia.

---

## El Juego de Negociación Penal

### Jugadores y Estrategias

**Defensa**: {Ir a Juicio (J), Negociar (N)}
**Fiscalía**: {Ir a Juicio (J), Negociar (N)}

### Matriz de Pagos General

```
                    FISCALÍA
                  Juicio    Negociar
DEFENSA  Juicio │ (d_j, f_j) │ (d_jn, f_jn) │
         Negocia│ (d_nj, f_nj)│ (d_n, f_n)  │
```

### Llenando la Matriz (Caso Penal)

Los pagos se expresan como **utilidad** (no solo dinero), incorporando:
- Probabilidad de condena `p`
- Severidad de la pena `s` (en años o equivalente monetario)
- Costos del juicio `c_D` (defensa) y `c_F` (fiscalía)
- Costo reputacional `r`

**Para la Defensa:**
- Juicio vs. Juicio: `-p × s - c_D`
- Negociar (llegar a acuerdo): `-s_acordada` (pena negociada, menor que la máxima)

**Para la Fiscalía:**
- Juicio vs. Juicio: `p × beneficio_condena - c_F - riesgo_derrota`
- Negociar: `beneficio_acuerdo - c_F × 0.2` (costos reducidos)

---

## Ejemplo Numérico: Caso de Robo con Intimidación

### Datos del caso
- **Pena máxima**: 10 años (valor = -100 para el imputado)
- **Probabilidad de condena** según análisis Bayesiano: p = 0.65
- **Costos del juicio** para la defensa: c_D = 5 (unidades arbitrarias)
- **Costos del juicio** para la fiscalía: c_F = 3
- **Oferta de la fiscalía**: Procedimiento Abreviado con 4 años (valor = -40 para imputado)

### Cálculo de Pagos (imputado)

| Situación | Cálculo | Valor |
|-----------|---------|-------|
| Juicio y pierde (p=0.65) | -100 × 0.65 | **-65** |
| Juicio y gana (1-p=0.35) | 0 | **0** |
| **Valor esperado del juicio** | -65 × 0.65 + 0 × 0.35 - 5 (costos) | **-47.25** |
| Procedimiento abreviado | -40 (fijo, sin riesgo) | **-40** |

**Conclusión para el imputado**: Valor esperado del juicio (-47.25) < Acuerdo (-40).
→ **El imputado prefiere negociar**.

### Cálculo de Pagos (fiscalía)

| Situación | Cálculo | Valor |
|-----------|---------|-------|
| Juicio y gana (p=0.65) | +80 (condena lograda) | **+80** |
| Juicio y pierde (1-p=0.35) | -20 (derrota) | **-20** |
| **Valor esperado del juicio** | 80 × 0.65 + (-20 × 0.35) - 3 | **+46** |
| Acuerdo abreviado | +30 (condena menor pero segura) | **+30** |

**Conclusión para la fiscalía**: Valor esperado del juicio (+46) > Acuerdo (+30).
→ **La fiscalía prefiere ir a juicio**.

### Equilibrio Nash en este Caso

```
                      FISCALÍA
                   Juicio   Negociar
DEFENSA  Juicio │ (-47, 46)│ (-60, 30)│
         Negocia│ (-20, 46)│ (-40, 30)│
                                      
Nash: (Defensa: Negocia, Fiscalía: Juicio)
→ La Fiscalía tiene estrategia dominante: Juicio
→ La Defensa responde con: Negociar (mejor respuesta dado Juicio de Fiscalía)
```

**Interpretación**: La Fiscalía irá a juicio. La Defensa debería explorar cómo cambiar los parámetros para modificar el equilibrio.

---

## Cómo Cambiar el Equilibrio a tu Favor

### Si eres la Defensa y el equilibrio te desfavorece:

**1. Aumentar los costos del juicio para la Fiscalía (c_F)**
- Anunciar testigos numerosos
- Preparar un contraexamen devastador del perito fiscal
- Cuestionar cada pieza de prueba en audiencias previas

**2. Reducir p (probabilidad de condena percibida por la Fiscalía)**
- Presentar contraperitos sólidos
- Obtener jurisprudencia favorable
- Hacer creíble la exclusión de prueba ilícita

**3. Mejorar tu BATNA (lo que obtienes si no hay acuerdo)**
- Si crees que la probabilidad real es menor que la que percibe la Fiscalía, hacer más juicios para actualizar esa percepción

**4. Señalizar credibilidad**
- Rechazar ofertas claramente malas (señal de que crees en tu caso)
- Invertir en prueba técnica costosa (señal de seriedad)

---

## Modelo de Litigio Civil: Teorema de Coase

### La "Zona de Acuerdo" (ZOPA)

```
Mínimo que aceptaría el Demandante:
    BATNA_D = P(ganar) × Monto - Costos_litigio

Máximo que pagaría el Demandado:
    BATNA_F = P(perder) × Monto + Costos_litigio

ZOPA existe si: BATNA_D < BATNA_F
```

### Ejemplo Civil

| Parámetro | Valor |
|-----------|-------|
| Monto demandado | $100M |
| P(ganar) según demandante | 70% |
| P(perder) según demandado | 60% |
| Costos del juicio (c/u) | $5M |

**BATNA del demandante** (mínimo que acepta):
```
0.70 × $100M - $5M = $65M
```

**BATNA del demandado** (máximo que paga):
```
0.60 × $100M + $5M = $65M
```

**ZOPA = [$65M, $65M]** → Un solo punto de acuerdo. Si la estimación de la Fiscalía sube a 65%, la ZOPA se abre.

**Divergencia de estimaciones**: Si el demandante cree que P=70% y el demandado cree que P=50%, el demandante no acepta menos de $65M y el demandado no paga más de $55M → **No hay ZOPA → Juicio inevitable**.

---

## Juegos Repetidos: La Reputación como Activo

Si litigas repetidamente ante los mismos tribunales y contra los mismos abogados/fiscales, el juego es **repetido**.

En juegos repetidos:
- La cooperación puede sostenerse (si el "shadow of the future" es suficientemente grande)
- La reputación de ser "duro" o "flexible" afecta los equilibrios futuros
- **Trampa**: ser siempre blando te hace un objetivo de demandas/acusaciones

**Regla del "Tit for Tat"** (Robert Axelrod):
1. Comienza con cooperación (oferta razonable)
2. Si la contraparte no coopera, responde igual (rechaza la próxima vez)
3. Si la contraparte vuelve a cooperar, también tú
→ En el largo plazo, genera el mejor resultado promedio

---

## Template de Análisis para una Causa

Ver: [[05-Teoria-Juegos/_Plantilla-Analisis-TJ]]
Herramienta Python: `python scripts/analizar_causa.py --ruc YYYY-NNNN --modo juegos`

---

*[[05-Teoria-Juegos/MOC-Teoria-Juegos|← Teoría de Juegos]]*
