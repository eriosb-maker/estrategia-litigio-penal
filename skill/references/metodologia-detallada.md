# Metodología detallada — Quince fases del análisis forense

> **Estado del módulo**: OPERATIVO. Expande las quince fases del SKILL.md v3.5,
> sección 4. Las citas al CPP marcadas como verificadas constan en
> `references/marco-legal.md` (curatoría 2026-07-06); las restantes conservan
> la marca «cita pendiente de verificación».

Consulta este archivo cuando la complejidad del caso amerite el desarrollo
extenso de una fase determinada.

---

## Fase 1 — Reconocimiento inicial y metacognición

Antes del análisis sustantivo, formula explícitamente:

1. ¿Qué tipo de caso es éste? Delitos potenciales, complejidad y etapa
   procesal (investigación desformalizada, formalizada, cierre, acusación,
   preparación de juicio oral, juicio).
2. ¿Qué información tengo disponible? Inventario sumario: declaraciones,
   documentos, pericias, evidencia digital, evidencia material.
3. ¿Qué evidencia digital y financiera está presente?
4. ¿Qué información crítica podría estar faltando?
5. ¿Cuál es la perspectiva del análisis? (fiscal, defensiva, querellante).
6. ¿Qué hipótesis preliminares emergen del primer cotejo?
7. ¿Qué sesgos cognitivos podrían estar afectando la lectura inicial?
8. ¿Cuál es el estado de la cadena de custodia de la evidencia?

Si el usuario adjunta un archivo `estado-del-caso-[RUC].md`, léelo antes que
cualquier otro documento y respeta las decisiones estratégicas allí
consignadas. El propósito de esta fase es prevenir el sesgo de anclaje.

---

## Fase 2 — Extracción de hechos investigados

Lee exhaustivamente los documentos y construye la cronología con la plantilla
`assets/templates/cronologia-hechos.md`. Para cada evento consigna fecha y
hora, lugar, descripción objetiva, fuente (con folio), tipo de evidencia
(física, digital, testimonial) y nivel de certeza (acreditado, probable,
alegado, en disputa).

La distinción entre tipos de evidencia es relevante porque su ponderación
difiere: el registro con marca temporal automática prevalece sobre la memoria
del testigo; el testimonio sin corroboración es alegación, no acreditación.

Cierra la fase con la calificación jurídica preliminar: tipos potencialmente
configurados, iter criminis (arts. 7 a 9 CP, verificados) y forma de autoría o
participación (arts. 14 a 17 CP, verificados).

---

## Fase 3 — Identificación de participantes

Construye la matriz de actores: nombre y RUT, rol procesal, rol material,
declaraciones rendidas (con folio), presencia digital, vínculos (laborales,
familiares, societarios, financieros) y antecedentes conocidos.

Los vínculos digitales son particularmente reveladores: frecuencia y horario
de las comunicaciones, contenido coordinatorio, ubicaciones coincidentes.
Cuando un interviniente niega conocimiento que sus registros documentan, la
contradicción pasa a la matriz de la Fase 5 con severidad crítica.

---

## Fase 4 — Análisis comparativo de versiones

Para cada tema controvertido, coteja las versiones con la plantilla
`assets/templates/matriz-contradicciones.md`, examinando coherencia interna,
corroboración externa y convergencia con evidencia objetiva. La contradicción
entre declaración y evidencia digital íntegra es la de mayor valor: las marcas
temporales automáticas no admiten modificación retroactiva sin comprometer la
cadena de integridad.

---

## Fase 5 — Matriz de coincidencias y contradicciones

Sistematiza: **coincidencias** (hechos en que convergen fuentes múltiples e
independientes, con su nivel de certeza) y **contradicciones**, clasificadas
por severidad (crítica, importante, menor). Para cada contradicción crítica:
versiones en pugna, evidencia objetiva que favorece a una u otra, implicancia
probatoria (dolo, conocimiento, falso testimonio) y valor para la teoría del
caso.

---

## Fase 6 — Análisis metacognitivo y ACH

Usa la plantilla `assets/templates/ach-hipotesis-competitivas.md`. Enumera al
menos tres hipótesis (principal y dos alternativas plausibles) y, para cada
una, la evidencia que la apoya, la que la refuta y su probabilidad estimada.
Consigna fortalezas y debilidades de la investigación, los sesgos a controlar
(confirmación, anclaje, disponibilidad, retrospección, autoridad) y las
preguntas críticas sin responder, que alimentan la Fase 11.

---

## Fase 7 — Análisis financiero forense integral *(condicional)*

Solo si hay flujo de fondos, criptoactivos o componente tributario. Carga
`references/forense-financiero.md` y aplica su método de tres capas: fiat
(cartolas), criptoactivos e información tributaria chilena (F22, F29, BHE,
facturación), con la matriz de coherencia entre lo declarado al SII y los
flujos reales y la distinción obligatoria entre elusión, evasión y posible
lavado de activos.

---

## Fase 8 — Análisis de prueba digital *(condicional)*

Solo si hay evidencia digital. Carga `references/prueba-digital.md`
(tipificación, cadena de custodia, autenticación, reconstrucción temporal y
cotejo digital-físico).

---

## Fase 9 — Evaluación de elementos del tipo penal

Respecto de cada delito investigado, verifica elemento por elemento:
**estado** (acreditado, parcialmente acreditado, no acreditado), **prueba que
lo respalda** (con folio) y **prueba faltante**. Consulta
`references/marco-legal.md` para el texto verificado; si el hecho es posterior
al 17-08-2023 y califica como delito económico, consulta además
`references/leyes-especiales.md` *(módulo pendiente de curatoría; rige la
regla de degradación controlada)*.

La conclusión es expresa: «todos los elementos están acreditados», «faltan los
siguientes elementos» o «el tipo no se configura». Esa conclusión sostiene o
desbarata la teoría del caso.

---

## Fase 10 — Cálculo de penas y marco punitivo *(condicional)*

Solo si se requiere estimación de pena. Carga `references/calculo-penas.md` y
aplica su algoritmo de seis pasos; para prescripción, ejecuta el motor
`prescripcion.py` del repositorio `estrategia-litigio-penal`.

---

## Fase 11 — Propuesta de diligencias de investigación

Sobre los vacíos y preguntas críticas de la Fase 6, propone diligencias con:
objetivo específico, fundamento legal, plazo sugerido, riesgo de omisión y
preguntas que debe responder. Prioriza en tres niveles (alta: urgencia, alto
impacto o riesgo de pérdida de evidencia; media: complementarias; baja:
exploratorias). Incluye las diligencias digitales de
`references/prueba-digital.md`, sección VI, cuando el caso lo amerite.

---

## Fase 12 — Teoría del caso dual

Construye el relato acusador (proposiciones fácticas sostenidas por prueba
específica, con refutación anticipada de los argumentos defensivos) y, en
sección separada, la teoría defensiva esperable (estrategia de negación,
justificación, atenuación o vía procesal; debilidades de la acusación;
contraexamen; temas de alegato).

Cuando el caso exija comparar juicio oral con salidas alternativas o
negociadas, ejecuta `scripts/estrategia_litigio.py` conforme al marco de
`references/estrategia-litigio.md` e integra sus métricas (exposición
esperada, punto de equilibrio, sensibilidad) como insumo auxiliar, nunca como
conclusión. La teoría fiscal solo es robusta si sobrevive al contraataque
defensivo simulado.

---

## Fase 13 — Análisis de riesgos procesales

- **Prescripción**: computa con el motor `prescripcion.py` (arts. 93 a 105 CP
  verificados). La formalización suspende la prescripción (art. 233 letra a)
  CPP, verificado); la decisión de no perseverar la deja continuar «como si
  nunca se hubiere interrumpido» (art. 248 letra c) CPP, verificado).
- **Nulidad por prueba ilícita**: examina la licitud de obtención de cada
  pieza. El recurso de nulidad consta verificado (arts. 372 a 387 CPP); la
  nulidad procesal (arts. 159 y siguientes) y la exclusión de prueba en la
  audiencia de preparación (art. 276) quedan *(cita pendiente de
  verificación)*.
- **Sobreseimiento y no perseverar**: riesgo de cierre sin acusación
  (arts. 247 a 258 CPP, verificados, incluido el forzamiento de la acusación
  del art. 258).
- **Salidas alternativas**: suspensión condicional (arts. 237 a 240 CPP,
  verificados) y acuerdo reparatorio (art. 241 CPP, verificado; arts. 242 a
  244 *(cita pendiente de verificación)*).
- **Procedimiento abreviado**: presupuestos y límites (arts. 406 a 415 CPP,
  verificados).
- **Cautelares**: prisión preventiva y personales menos intensas (arts. 139 a
  156 bis CPP, verificados); cautelares reales *(art. 157 CPP — cita
  pendiente de verificación)* ante riesgo de insolvencia provocada.

---

## Fase 14 — Producción de borradores *(opcional)*

A petición del usuario, produce borradores con las plantillas de
`assets/templates/` (querella *(art. 113 CPP — cita pendiente de
verificación)*, matriz de contradicciones, cronología, ACH). Todo borrador
lleva advertencia expresa de revisión humana por el abogado responsable.

---

## Fase 15 — Cierre y aprendizaje *(obligatoria en análisis sustantivos)*

Ejecuta el Protocolo de Cierre y Aprendizaje (SKILL.md, sección 15.3):
detección de correcciones, preferencias, fuentes validadas y errores;
formulación de reglas operativas en el formato de
`references/aprendizajes.md`; propuesta al usuario (nada se incorpora sin su
aprobación); persistencia según el entorno, y generación del archivo
`estado-del-caso-[RUC].md` conforme a la plantilla
`assets/templates/estado-del-caso.md`. Si no surgió lección alguna, decláralo
expresamente.

---

## Cierre metodológico

Las quince fases no son rígidas: el orden se adapta al caso. Lo innegociable
son los principios rectores: distinción epistémica obligatoria,
verificabilidad de toda afirmación, precisión nominativa, perspectiva dual
cuando proceda y resguardo del secreto profesional. La metodología existe para
servir al criterio jurídico del abogado, no para sustituirlo.
