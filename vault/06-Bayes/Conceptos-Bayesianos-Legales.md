---
tipo: concepto
titulo: Análisis Bayesiano en el Litigio
materia: teoria
etiquetas: [bayes, probabilidad, evidencia, litigio]
---

# 📊 Análisis Bayesiano para Abogados Litigantes

> *El teorema de Bayes describe cómo actualizar creencias ante nueva evidencia. En litigio, es la herramienta formal para razonar sobre probabilidades de condena o responsabilidad.*

---

## El Teorema de Bayes

```
P(H|E) = P(E|H) × P(H) / P(E)
```

Donde:
- `P(H)` = Probabilidad **a priori** de la hipótesis (antes de ver evidencia)
- `P(E|H)` = **Verosimilitud**: probabilidad de la evidencia si H es verdadera
- `P(H|E)` = Probabilidad **a posteriori**: probabilidad de H después de ver E
- `P(E)` = Probabilidad marginal de E (constante normalizadora)

### En términos legales

```
P(Culpable | Evidencia) = P(Evidencia | Culpable) × P(Culpable a priori)
                          ───────────────────────────────────────────────
                                       P(Evidencia)
```

---

## El Estándar de Prueba como Umbral Bayesiano

| Estándar | Umbral Bayesiano | Aplicación |
|----------|-----------------|-----------|
| **Más allá de toda duda razonable** | P(Culpable\|E) > 0.90-0.95 | Penal (condena) |
| **Preponderancia de la evidencia** | P(Responsable\|E) > 0.50 | Civil |
| **Probabilidad suficiente** | P(H\|E) > 0.70 | Formalización/Acusación |
| **Indicio** | P(H\|E) > 0.30 | Medidas cautelares |

**Implicación estratégica**: En penal, no necesitas probar inocencia. Solo necesitas que P(Culpable|E) no supere el umbral del tribunal (en la práctica, ~0.85-0.90).

---

## La Razón de Verosimilitud (Likelihood Ratio)

La forma más práctica del teorema de Bayes para evaluar evidencia individual:

```
LR = P(E | Culpable) / P(E | Inocente)
```

| LR | Interpretación |
|----|---------------|
| > 100 | Evidencia decisiva para culpabilidad |
| 10-100 | Evidencia fuerte |
| 2-10 | Evidencia moderada |
| 1 | Evidencia neutral (no ayuda ni a culpabilidad ni inocencia) |
| < 1 | Evidencia favorable a inocencia |
| < 0.1 | Evidencia fuerte de inocencia |

### Ejemplo: Test de ADN
- P(Match en muestra | Culpable) = 0.999
- P(Match en muestra | Inocente) = 0.0001 (error de laboratorio)
- **LR = 0.999 / 0.0001 = 9,990** → Evidencia muy fuerte de culpabilidad

### Ejemplo: Testigo Ocular
- P(ID positiva | Culpable) = 0.80 (testigos son 80% precisos en condiciones ideales)
- P(ID positiva | Inocente) = 0.20 (error de identificación)
- **LR = 0.80 / 0.20 = 4.0** → Evidencia moderada (no decisiva)

---

## Actualización Secuencial de Probabilidades

Cuando tenemos múltiples piezas de evidencia (E1, E2, E3...), actualizamos secuencialmente:

```
P(C|E1) → actualizar con E2 → P(C|E1,E2) → actualizar con E3 → P(C|E1,E2,E3)
```

**Asumiendo independencia** entre las pruebas:
```
P(C|E1,E2) ∝ LR_1 × LR_2 × P(C_prior)
```

**Advertencia sobre independencia**: Si E1 y E2 provienen de la misma fuente (ej: dos testigos que hablaron entre sí), no son independientes y no puedes multiplicar sus LRs.

---

## Aplicación Práctica: Análisis de una Causa

### Paso 1: Establecer Probabilidad A Priori

Considera:
- Tasa base de condenas para este tipo de delito en este tribunal
- Experiencia del abogado con este fiscal y juez
- Contexto social y mediático del caso

**Ejemplo**: En delitos de robo con intimidación en Chile, la tasa de condena en TOP es ~72%. P(C_prior) = 0.72.

### Paso 2: Listar Evidencias y Calcular LRs

| Evidencia | P(E\|Culpable) | P(E\|Inocente) | LR |
|-----------|---------------|----------------|-----|
| Testigo ocular A (condiciones malas) | 0.60 | 0.30 | **2.0** |
| Huella dactilar (parcial) | 0.70 | 0.05 | **14.0** |
| Sin coartada verificable | 0.65 | 0.35 | **1.9** |
| Historia previa (antecedentes) | 0.80 | 0.50 | **1.6** |

### Paso 3: Actualizar con Odds Ratio

Convertir probabilidad a odds:
```
Odds_prior = P/(1-P) = 0.72/0.28 = 2.57
```

Multiplicar por todos los LRs:
```
Odds_posterior = 2.57 × 2.0 × 14.0 × 1.9 × 1.6 = 219
```

Convertir de vuelta a probabilidad:
```
P(C|E) = Odds/(1+Odds) = 219/220 = 0.995
```

**Conclusión**: Con esta evidencia, la probabilidad de condena es ~99.5%. **Definitivamente recomendar salida alternativa.**

### Paso 4: Evaluar Qué Pasa si Excluimos Evidencia Clave

Si excluimos la huella dactilar (LR = 14):
```
Odds_posterior = 2.57 × 2.0 × 1.9 × 1.6 = 15.6
P(C|E sin huella) = 15.6/16.6 = 0.94
```

Aún alto, pero la diferencia importa para la negociación.

---

## La Falacia del Fiscal (Prosecutor's Fallacy)

**Error común**: Confundir P(E|Inocente) con P(Inocente|E).

Ejemplo: "La probabilidad de esta coincidencia de ADN en un inocente es de 1 en 1,000,000. Por lo tanto, hay 1 en 1,000,000 de probabilidad de que sea inocente."

**¿Por qué es un error?** Porque ignora la probabilidad a priori (cuántas personas viven en la ciudad, cuántos tienen esta característica de ADN).

**Cómo atacarlo en juicio**: "Señor fiscal, si en Santiago viven 6 millones de personas y la probabilidad de este perfil es 1/1M, estadísticamente hay 6 personas con este perfil en la ciudad. ¿Cuál es la base para identificar a mi cliente entre esos 6?"

---

## La Falacia de la Defensa (Defense Attorney's Fallacy)

**Error contrario**: Argumentar que "hay millones de personas que podrían ser culpables" ignorando que otras evidencias ya limitaron sustancialmente el grupo de sospechosos.

Ambas falacias son errores de razonamiento bayesiano que los abogados deben evitar (o aprovechar si la comete la contraparte).

---

## Evidencia que Actualiza vs. Evidencia que No Actualiza

### ¿Cuándo una pieza de evidencia NO actualiza P(Culpable)?

Cuando LR = 1, es decir:
```
P(E | Culpable) = P(E | Inocente)
```

**Ejemplo**: El imputado estaba nervioso durante el interrogatorio.
- ¿Las personas culpables se ponen nerviosas? Sí.
- ¿Las personas inocentes también se ponen nerviosas cuando son interrogadas? Igualmente sí.
- LR ≈ 1 → Esta evidencia no debería influir en la probabilidad de culpabilidad.

---

## Herramienta Python

```bash
python scripts/analizar_causa.py --ruc 2024-1234 --modo bayes
```

El script calcula y genera automáticamente la nota `04-Analisis-Bayes.md` para la causa.

Ver: [[06-Bayes/_Plantilla-Analisis-Bayesiano]]

---

## Referencias

- [[03-Biblioteca/]] — Kahneman, "Thinking Fast and Slow" (razonamiento probabilístico)
- [[03-Biblioteca/]] — Tillers & Green (eds.), "Probability and Inference in the Law of Evidence" (1988)
- [[03-Biblioteca/]] — Gigerenzer, "Calculated Risks" (2002) — cómo comunicar probabilidades al jurado/juez

---

*[[06-Bayes/MOC-Bayes|← Análisis Bayesiano]]*
