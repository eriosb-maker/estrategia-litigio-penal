# Razonamiento probatorio — Catálogo de falacias y protocolo de contraexamen cuantitativo

> Módulo de referencia condicional. Cárgalo cuando el caso presente prueba pericial con contenido estadístico o probabilístico (ADN, coincidencias de rasgos, peritajes financieros con cifras de probabilidad, instrumentos predictivos), o cuando deba impugnarse una valoración probatoria que agregue indicios.

## 0. Declaración de procedencia y estado epistémico

Este módulo fue construido en la sesión de 9-10 de julio de 2026 y quedó en estado `no_propagado` (el archivo no se instaló; su texto sobrevivió solo en la transcripción). La presente versión es una **reconstrucción de sesión de 10 de julio de 2026**, con la siguiente disciplina de procedencia: las secciones marcadas **[R-VERBATIM]** reproducen texto recuperado literalmente de la transcripción original; las marcadas **[R-SÍNTESIS]** reconstruyen contenido cuya existencia consta en la transcripción o en el resumen de sesión, pero cuyo tenor literal no fue recuperado. El hash del archivo original es irrecuperable; esta reconstrucción genera hash propio y sustituye al original en el índice maestro, dejando constancia. Ninguna sección [R-SÍNTESIS] se cita en escrito ni informe sin revisión previa del abogado responsable.

Rige la regla de traducción del repositorio: **ninguna probabilidad, matriz, razón de verosimilitud ni equilibrio ingresa a un escrito judicial**; hacia adentro se calcula, hacia afuera se traduce a las fórmulas prudenciales establecidas.

## 1. La pregunta previa: la probabilidad a priori [R-VERBATIM]

De ello se sigue la pregunta que este módulo antepone a cualquier otra ante un peritaje que exhiba cifras de naturaleza probabilística: no cómo se calculó la verosimilitud, sino **cuál fue la previa empleada y quién autorizó al perito a fijarla**. Esta pregunta, y no la escala de decibanes, constituye el instrumento de mayor rendimiento forense de todo el módulo, y debe encabezar cualquier preparación de contraexamen pericial.

## 2. Catálogo de falacias

### 2.1 Transposición del condicional (falacia del fiscal) [R-VERBATIM]

Consiste en confundir la probabilidad de la prueba dado que el imputado es inocente con la probabilidad de que el imputado sea inocente dada la prueba. Son magnitudes distintas que solo coinciden bajo el supuesto —casi nunca verificado ni verificable— de que la probabilidad previa de culpabilidad es exactamente 50%. Su detección exige exigir del perito o del persecutor la explicitación de cuál de las dos magnitudes está afirmando.

### 2.2 Negligencia de la tasa base [R-VERBATIM]

Consiste en valorar la fuerza de un indicio —por ejemplo, una coincidencia de rasgos poco frecuentes— sin ponderarla contra la tasa base de ocurrencia de ese rasgo en la población relevante de sospechosos posibles. Un indicio con razón de verosimilitud alta puede producir una probabilidad posterior baja si la tasa base de culpabilidad previa es suficientemente reducida, y el catálogo debe emplearse para exigir que toda cifra de «probabilidad de coincidencia» se acompañe de la tasa base efectivamente aplicada.

### 2.3 Adición indebida de indicios condicionalmente dependientes [R-VERBATIM]

Consiste en sumar los pesos de distintos indicios como si fueran independientes entre sí, cuando en realidad comparten una causa común que los correlaciona condicionalmente a cada hipótesis. La corrección metodológica es precisa: lo que impide sumar los pesos no es que los indicios estén correlacionados entre sí de manera marginal, sino que lo estén *condicionalmente a cada hipótesis en examen*; dos hechos marginalmente asociados pueden, no obstante, ser condicionalmente independientes, y dos hechos marginalmente inconexos pueden ser condicionalmente dependientes. La sola invocación de «independencia» sin esa precisión es, en sí misma, un indicio de manejo técnico deficiente por parte de quien la invoca.

### 2.4 Cuantificación indebida del estándar del artículo 340 del Código Procesal Penal [R-VERBATIM, cierre R-SÍNTESIS]

Es la falacia de mayor gravedad detectada en el corpus auditado, y merece desarrollo separado por su potencial de volverse contra quien la emplea.

El estándar de convicción del artículo 340 CPP —más allá de toda duda razonable— no admite reducción a un umbral numérico de probabilidad posterior sin incurrir en un error matemático identificable. El decibán, unidad de medida de razones de verosimilitud, no mide la probabilidad final de culpabilidad: mide el *cambio* que un conjunto de indicios produce sobre la razón de probabilidades previa. Sostener que un acumulado probatorio inferior a determinado peso neto «impide lógicamente condenar» omite la probabilidad a priori, que es el término que el teorema de Bayes en forma de *odds* exige multiplicar. La misma cifra de peso probatorio produce probabilidades finales radicalmente distintas según la previa; quien afirma lo contrario incurre en una variante de la falacia del fiscal. La defensa no invoca umbrales numéricos del art. 340 CPP: los detecta y los desarma cuando la acusación o el perito los emplea.

## 3. Protocolo de contraexamen [R-SÍNTESIS]

1. Exigir la explicitación de la magnitud afirmada (¿P(prueba|hipótesis) o P(hipótesis|prueba)?).
2. Exigir la probabilidad a priori empleada, su fuente y la autoridad del perito para fijarla.
3. Exigir la tasa base de la población relevante para toda cifra de coincidencia.
4. Ante agregación de indicios, exigir la justificación de independencia condicional a cada hipótesis, no meramente marginal.
5. Ante instrumentos predictivos, remitir a `fiscalizacion-algoritmica.md` (defectos estructurales: etiquetas corruptas, sesgo de selección, contrafáctico inobservable).

## 4. Cierre operativo

El rendimiento real del razonamiento cuantitativo en la sala no es afirmativo sino crítico: sirve para desarmar la prueba estadística de cargo, no para construir la propia. Todo hallazgo de este módulo se traduce, antes de ingresar a un escrito, al lenguaje prudencial del repositorio (acreditado / indiciario / hipótesis).
