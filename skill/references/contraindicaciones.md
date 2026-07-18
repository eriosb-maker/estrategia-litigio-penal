# Contraindicaciones — Catálogo de prohibiciones de exhibición

> **ESTADO: RECUPERACIÓN CORREGIDA (10 de julio de 2026).** Este módulo sustituye a la versión que declaró pérdida total de las catorce entradas (`estado: perdido`, sesión de recuperación del 10 de julio de 2026). Esa declaración fue prematura: la transcripción original de la sesión del 9 de julio de 2026 (fragmento de inserción, Atlas de Economías Ilícitas v1.0.0), localizada en exportación local aportada por el titular, contiene el texto **íntegro y verbatim** de C-012, C-013 y C-014, sin truncamiento. Se deja sin efecto, en consecuencia, la marca `[R-S — texto original truncado]` que una reconstrucción intermedia había asignado al fundamento de C-012. C-001 a C-011 permanecen sin rastro textual en toda fuente examinada hasta esta fecha.

## Prevención sobre la numeración [R-V]

La numeración ordinal es un identificador frágil en un catálogo acumulativo: basta la inserción de una prohibición anterior, o la consolidación de dos entradas afines, para que toda cita externa a «la contraindicación N° 7» quede desplazada y apunte a una regla distinta de la invocada. Se adoptan identificadores estables `C-0NN`, asignados en orden de ingreso y jamás reasignados; las entradas derogadas conservan su identificador con la marca correspondiente, conforme a la regla de higiene vigente en `aprendizajes.md`. *(Cambio de criterio propuesto en la sesión de origen; su aprobación no consta.)*

## C-001 a C-011 — [PERDIDAS]

- **Estado**: perdido. **Texto**: no recuperado en ninguna transcripción examinada, incluida la exportación local aportada el 10 de julio de 2026.
- **Constancia**: la existencia de las entradas consta en el índice maestro v3.6 a v3.8; su contenido no consta en los antecedentes examinados.
- **Remedio disponible**: si el titular conserva otra sesión de origen o exportación adicional, el texto puede reingresarse conservando sus identificadores originales.

## C-012 — Prohibición de citar centralidad no acreditada [R-V]

**Regla.** No se cita en escrito, informe pericial, minuta de alegato ni exhibición ante tribunal métrica alguna de centralidad calculada sobre un grafo que incorpore aristas de estatuto indiciario o hipotético. Únicamente las métricas de sufijo `_acreditada`, computadas sobre el subgrafo de aristas acreditadas, son citables.

**Fundamento.** Una medida de centralidad es una función de las aristas del grafo. Si el grafo incorpora aristas que el propio estudio ha clasificado como hipótesis, la centralidad resultante es, ella misma, una hipótesis, y arrastra ese estatuto a toda conclusión que se funde en ella. Afirmar que un actor «ocupa la posición central de la red» sobre la base de un cómputo que incluye conjeturas equivale a presentar como acreditado el producto de lo no acreditado. El vicio es de la misma especie que el que este catálogo ya proscribe respecto de la reducción escalar de la exposición penal: una operación aritméticamente correcta que transporta hacia su resultado una certeza que sus insumos no poseen.

**Alcance.** Cubre las centralidades de grado, de intermediación, de cercanía y de vector propio, así como cualquier medida derivada, y se extiende a las formulaciones verbales que las traduzcan sin nombrarlas —«actor articulador», «nodo central», «posición de bisagra»—.

**Detección.** El informe emitido por `atlas-aristas.js` marca cada actor con los campos `sensible_a_hipotesis` y `articulacion_solo_hipotetica`. Toda afirmación referida a un actor con el segundo campo en `true` es una infracción a esta contraindicación, sin excepción posible.

**Excepción.** Ninguna en sede de exhibición. En sede de análisis interno, la métrica total puede emplearse como orientación investigativa, siempre que su carácter hipotético conste en el documento de trabajo.

**Vigencia.** Permanente.

## C-013 — Prohibición de inferir jerarquía de la posición topológica [R-V]

**Regla.** No se afirma jefatura, dirección, mando, articulación ni rol organizativo alguno de un actor sobre la base de su posición en el grafo, ni aun cuando esa posición se calcule sobre el subgrafo íntegramente acreditado.

**Fundamento.** Una centralidad de intermediación elevada identifica a quien conecta subgrupos que, sin él, quedarían desconectados. Esa propiedad es topológica y no jerárquica. Puede corresponder al jefe; corresponde con igual frecuencia al chofer, al contador externo, al corredor de propiedades o a la secretaria que agenda las reuniones. Ninguna de las medidas de centralidad de uso corriente distingue a quien imparte la orden de quien transporta el recado, por la razón elemental de que ambos ocupan el mismo lugar en el trazado de las relaciones.

De ello se desprende que la métrica, correctamente calculada, puede a lo sumo señalar dónde mirar. No puede sustituir la prueba de aquello que se mire.

**Alcance.** Comprende tanto la afirmación directa como la insinuación estructural, esto es, la disposición gráfica que sitúa a un actor en el centro del lienzo o le asigna un tamaño de nodo proporcional a su centralidad. El tamaño es una afirmación.

**Excepción.** Ninguna.

**Vigencia.** Permanente.

## C-014 — Prohibición de exhibir centralidad sin declaración de perímetro [R-V]

**Regla.** No se exhibe métrica alguna de red, ni representación gráfica del Atlas, sin la declaración de perímetro exigida por `perimetro.md`, completa y suscrita.

**Fundamento.** El grafo es una función de dónde se trazó la frontera de la observación. Los actores no observados no existen en él, y su ausencia no deja un vacío: redistribuye la centralidad hacia los observados. Un actor puede exhibir el grado más alto del grafo por el solo hecho de que la investigación partió de él y se expandió desde su entorno, con lo cual la densidad de aristas en torno suyo mide cuánto se lo vigiló y no cuánto operó.

En consecuencia, y sin la declaración de qué fuentes se incorporaron, cuáles se conocían y no se incorporaron, desde qué nodo semilla se expandió la construcción y a qué fecha se cortó, ninguna centralidad del Atlas es interpretable. Corresponde advertir que esta es también la primera pregunta que un contraexamen competente formularía sobre el propio instrumento, y que la ausencia de respuesta preparada constituye un riesgo procesal del estudio antes que un defecto metodológico.

**Alcance.** Cubre la exhibición ante tribunal, la incorporación a informe institucional y la entrega a cliente o a autoridad. No cubre el uso interno de trabajo.

**Detección.** El informe de `atlas-aristas.js` emite el campo `perimetro_declarado`. Mientras su valor sea `false`, toda exhibición infringe esta contraindicación.

**Excepción.** Ninguna.

**Vigencia.** Permanente.

## Candidata C-015 — No incorporada como entrada; cuestión de ubicación pendiente

Existe una cuarta regla, de índole normativa y no técnica, cuyo lugar en la arquitectura del repositorio no está resuelto: **una arista no es un concierto**. El grafo registra contacto, coocurrencia o transferencia; el tipo penal exige acuerdo de voluntades orientado a la comisión de delitos, con permanencia y estructura. Entre el contacto y el concierto media exactamente la prueba que el grafo no aporta.

No se propone como contraindicación, porque no es una prohibición de uso de un instrumento, sino una tesis de derecho penal sustantivo que pertenece al módulo de razonamiento probatorio. Se deja aquí constancia de su existencia y de la decisión pendiente sobre su ubicación.

Su desarrollo se encuentra obstruido por una constatación material: los artículos 292 y siguientes del Código Penal no integran el perímetro curado de `marco-legal.md`. `[VERIFICAR-LEYCHILE]`

## C-016 en adelante — Numeración corriente

La primera entrada nueva que no corresponda a una recuperación de las aquí tratadas se numera `C-016`, en aplicación de la regla de no reasignación: C-001 a C-015 quedan reservados aun cuando parte de ellos permanezca sin texto.
