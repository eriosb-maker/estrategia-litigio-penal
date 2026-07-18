# Fiscalización algorítmica — Protocolo de objeción metodológica a instrumentos predictivos (v0.2-reconstruida)

> Módulo condicional. Cárgalo cuando la causa involucre prueba o decisión fundada en instrumentos predictivos, scoring, algoritmos de asignación (p. ej. SITCI), modelos de riesgo o analítica de fiscalización (SII, UAF, policías). Derivado del destilado de decisión secuencial (Henderson), identificado en la auditoría de julio de 2026 como el de mayor rendimiento del corpus, precisamente porque su valor es crítico y no constructivo.

## 0. Declaración de procedencia y cláusula de no graduación

Versión 0.1 construida en sesión de 9-10 de julio de 2026, `no_propagado`; la presente v0.2 es reconstrucción de 10 de julio de 2026 desde la transcripción de la sesión de auditoría **[R-SÍNTESIS con núcleo R-VERBATIM]**. **Este módulo no gradúa a versión 1.0 mientras no se coteje contra una segunda fuente independiente del destilado de origen.** Sus proposiciones se emplean como protocolo de preguntas de contraexamen, no como afirmaciones periciales propias.

## 1. Los tres defectos estructurales de los instrumentos predictivos

1. **Etiquetas corruptas.** El instrumento se entrena sobre etiquetas que no miden el fenómeno de interés sino un subrogado administrativo (detención en lugar de comisión; denuncia en lugar de ocurrencia). La objeción exige la definición operativa exacta de la etiqueta y su distancia con el hecho que el tribunal debe establecer.

2. **Sesgo de selección en los datos de entrenamiento.** La muestra de entrenamiento no es aleatoria respecto de la población sobre la que el instrumento predice; refleja las prioridades históricas de fiscalización. La objeción exige la descripción del proceso generador de los datos y de las poblaciones sub y sobrerrepresentadas.

3. **Bucle de retroalimentación — formulación corregida [R-VERBATIM en su corrección].** El problema no es que el algoritmo interprete la prisión como predicción exitosa, sino que **el contrafáctico es inobservable** —el problema de las etiquetas selectivas—, de modo que la predicción no puede ser evaluada ni confirmada. Un perito contrainterrogado explotaría la formulación imprecisa; la corregida es la única que ingresa a preparación de audiencia.

## 2. Protocolo de preguntas

1. ¿Qué mide exactamente la etiqueta de entrenamiento y quién la asignó?
2. ¿Cómo se generaron los datos y qué decisiones humanas previas los filtraron?
3. ¿Cómo se validó el instrumento si el contrafáctico —lo que habría ocurrido sin la intervención— no es observable?
4. ¿Qué tasa de error declara el proveedor, sobre qué población, y quién la auditó?
5. ¿Puede el perito reproducir el resultado del instrumento para el caso concreto, con los insumos del caso concreto?

## 3. Cierre operativo

Este módulo se coordina con `razonamiento-probatorio.md` (sección 3, punto 5) y con `prueba-digital.md`. Su producto es siempre una línea de contraexamen o una solicitud de exhibición de metodología; nunca una afirmación pericial propia de la defensa.
