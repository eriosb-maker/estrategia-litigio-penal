---
tipo: pruebas
causa: "Estafa Inmobiliaria - Caso González"
ruc: "2024-DEMO-002"
etiquetas: [pruebas, penal, estafa]
---

# 🔬 Pruebas — Caso González

## Pruebas de Cargo (Fiscalía)

| # | Tipo | Descripción | Peso | Cuestionamiento Defensa |
|---|------|-------------|------|-------------------------|
| 1 | Documental | Certificado de dominio CBR — confirma que el imputado nunca fue dueño | 🔴 Alto | No discutible (es hecho objetivo) |
| 2 | Documental | Promesa de compraventa firmada por imputado como "vendedor" | 🔴 Alto | Atacar: faltó cláusula de mandato. Pedir lectura completa del contrato |
| 3 | Bancaria | Cartola Banco Santander: transferencia $50M de víctima → cuenta personal del imputado | 🔴 Alto | Sin cuestionamiento posible (objetiva) |
| 4 | Testimonial | Declaración víctima: "Me dijo que era el dueño" | 🟡 Medio | Atacar credibilidad: contradicción con audio donde dice "es de un familiar" |
| 5 | Testimonial | Corredora propiedades — vio interacción imputado/víctima | 🟡 Medio | Atacar: ella escuchó parcialmente, hay 30 min sin testigos |
| 6 | Documental | Publicación Portal Inmobiliario sin mencionar mandato | 🟡 Medio | Estándar del mercado: nadie publica mandatos |
| 7 | Pericial | Informe pericial de la PDI sobre patrón "estafa inmobiliaria" | 🔴 Alto | **CONTRAPERITAJE URGENTE** — el patrón no aplica a caso único sin reincidencia |

---

## Pruebas de Descargo (Defensa)

| # | Tipo | Descripción | Peso | Observación |
|---|------|-------------|------|-------------|
| 1 | Documental | Mensajes WhatsApp imputado ↔ verdadero dueño (familiar) — promesa de venta | 🟢 Alto | **PRUEBA REINA** — debe ser autenticada |
| 2 | Bancaria | Cartola: imputado restituye $30M antes de la querella (sin presión) | 🟢 Alto | Demuestra rectificación voluntaria |
| 3 | Testimonial | Verdadero dueño (familiar): confirmará promesa verbal | 🟡 Medio | Riesgo: parentesco puede afectar credibilidad |
| 4 | Documental | Sin antecedentes penales — extracto de filiación limpio | 🟢 Medio | Primer ofensor |
| 5 | Documental | Contratos anteriores de corretaje exitosos del imputado | 🟡 Medio | Demuestra que tiene experiencia legítima en el rubro |
| 6 | Pericial | Informe contable: los $20M restantes están en inversión recuperable | 🟡 Medio | Capacidad de restitución total → posible salida alternativa |

---

## Pruebas Pendientes de Obtener

- [ ] 📅 2026-05-19 — Solicitar peritaje informático para autenticar WhatsApp
- [ ] 📅 2026-05-26 — Obtener declaración escrita del verdadero dueño
- [ ] 📅 2026-06-02 — Solicitar contraperitaje sobre informe PDI

---

## Análisis de Likelihood Ratios para Bayes

> Estos valores se usan en el análisis Bayesiano (`./scripts/litigio.sh bayes`)

| Evidencia | P(E\|culpable) | P(E\|inocente) | LR | Tipo |
|-----------|---------------|----------------|----|----- |
| Certificado dominio (no era dueño) | 0.95 | 0.95 | ~1.0 | Neutral (es solo el hecho) |
| Transferencia $50M sin contrato firme | 0.85 | 0.40 | 2.13 | Cargo (más probable si engañó) |
| Restitución voluntaria de $30M | 0.20 | 0.75 | 0.27 | **Descargo fuerte** |
| WhatsApp con mandato verbal del dueño | 0.15 | 0.80 | 0.19 | **Descargo decisivo** si se autentica |
| Sin antecedentes penales previos | 0.35 | 0.65 | 0.54 | Descargo leve |
| Informe PDI patrón estafa (genérico) | 0.55 | 0.35 | 1.57 | Cargo débil (no específico) |

---
*[[00-Resumen|← Resumen de la Causa]]*
