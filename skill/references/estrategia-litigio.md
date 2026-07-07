# Estrategia de litigio — Marco de decisión cuantitativo

> Módulo de referencia asociado al script `scripts/estrategia_litigio.py`. Cárgalo cuando el caso exija comparar juicio oral con salidas alternativas o negociadas (suspensión condicional, acuerdo reparatorio, procedimiento abreviado), o cuando el usuario solicite un análisis costo-beneficio de la decisión de litigar.

## 1. Naturaleza y límites del análisis

El análisis cuantitativo de estrategia es un **insumo auxiliar**, no un sustituto del juicio profesional. Formaliza lo que el litigante experimentado hace intuitivamente —ponderar probabilidad de condena, magnitud de la pena probable, valor de las salidas disponibles y costos del proceso—, con dos ventajas: hace explícitos los supuestos y permite examinar cuán sensible es la conclusión a errores de estimación. Sus límites deben declararse siempre en el informe: (a) la probabilidad de condena es una estimación subjetiva informada, no un dato; (b) el modelo no captura factores cualitativos decisivos (efecto reputacional, precedente, situación familiar del imputado, interés de la víctima, política de persecución del fiscal regional); (c) la decisión corresponde exclusivamente al abogado y su cliente, debidamente informado.

## 2. Variables del modelo

1. **Probabilidad de condena en juicio oral**: estimada a partir del análisis probatorio de las fases 4 a 6 (matriz de contradicciones y ACH). Debe fundarse en la suficiencia probatoria respecto de cada elemento del tipo, no en impresión general. Consigna expresamente el fundamento de la estimación.
2. **Pena concreta probable en caso de condena**: determinada conforme al régimen aplicable (Código Penal o sistema especial de la Ley 21.595 para delitos económicos), considerando atenuantes y agravantes verosímiles. Si existe `references/calculo-penas.md`, úsalo; en su defecto, aplica la regla de degradación controlada.
3. **Probabilidad de pena sustitutiva** (Ley 18.216) en el escenario de condena, que reduce la exposición privativa efectiva. En delitos económicos, atiende al régimen restrictivo introducido por la Ley 21.595.
4. **Salidas disponibles y su costo**: pena ofrecida o esperable en procedimiento abreviado; condiciones de una suspensión condicional; monto y términos de un acuerdo reparatorio.
5. **Costos del proceso**: honorarios, pericias, duración, exposición pública.

## 3. Métricas producidas por el script

- **Exposición penal esperada del juicio**: probabilidad de condena × pena probable (años-equivalentes). Se reporta también la exposición **privativa** esperada, descontada la probabilidad de sustitutiva.
- **Punto de equilibrio**: la probabilidad de condena que iguala la exposición del juicio con la oferta negociada. Es la métrica más útil en la práctica: en lugar de discutir si la probabilidad "real" es 0,60 o 0,70, la pregunta se reduce a si está por sobre o por debajo del umbral de indiferencia.
- **Análisis de sensibilidad**: exposición esperada ante variaciones de ±10 y ±20 puntos en la probabilidad de condena. Si la conclusión se invierte dentro de ese rango, la decisión es frágil y debe reforzarse el análisis probatorio antes de decidir.
- **Viabilidad prima facie de salidas procesales**: filtros de procedencia de la suspensión condicional (art. 237 CPP), el acuerdo reparatorio (art. 241 CPP) y el procedimiento abreviado (art. 406 y ss. CPP). Son filtros preliminares: **todo umbral debe verificarse contra el texto legal vigente y el delito concreto**, incluyendo las reglas especiales de la Ley 20.931 y de la Ley 21.595.

## 4. Reglas de uso en el informe

1. El resultado del script se integra en el capítulo de teoría del caso o de riesgos procesales, en prosa, presentando los supuestos, las métricas y su lectura estratégica; la salida JSON cruda va en anexo.
2. Nunca presentes la recomendación del modelo como conclusión del informe: preséntala como «el análisis cuantitativo sugiere, bajo los supuestos declarados, que…», seguida de los factores cualitativos que podrían alterarla.
3. Si la perspectiva es acusadora (fiscal o querellante), el mismo modelo se lee en espejo: sirve para anticipar los incentivos de la defensa a negociar y calibrar la posición propia.
4. Consigna en el archivo de estado del caso los parámetros utilizados y su fecha, para que la evolución de la estimación quede trazada entre sesiones.
