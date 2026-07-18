# Aprendizajes acumulados de la skill

> **Instrucción de uso**: Este archivo es la memoria de mejora continua de la skill. Debe ser **leído siempre al inicio** de cualquier análisis, inmediatamente después del SKILL.md. Contiene correcciones, criterios y preferencias capturados en usos anteriores, que prevalecen sobre las reglas generales del SKILL.md en caso de conflicto (salvo las prohibiciones expresas y el principio epistémico rector, que son inderogables).
>
> **Instrucción de actualización**: Al cierre de cada análisis, ejecuta el Protocolo de Cierre y Aprendizaje (sección «Auto-aprendizaje» del SKILL.md). Si de él surgen lecciones nuevas, agrégalas aquí con el formato estandarizado. Si el entorno no permite escribir en el directorio de la skill (Claude.ai), genera el bloque de aprendizaje en el chat y ofrece al usuario reempaquetar la skill actualizada.

---

## Formato estandarizado de cada entrada

```
### A-0NN — [AAAA-MM-DD] — [Categoría] — Título breve
- **Estado**: propuesto | aprobado | rechazado | derogado
- **Naturaleza**: corrección de manifiesto | cambio de criterio
- **Contexto**: caso o situación en que surgió (sin datos identificatorios de clientes; usar RUC solo si el usuario lo autoriza).
- **Lección**: qué se corrigió, aprendió o prefirió.
- **Regla operativa**: instrucción concreta y accionable para análisis futuros.
- **Vigencia**: permanente / hasta verificación / hasta subsanación / derogada el [fecha].
```

**Identificador estable.** El campo `ID` se asigna en orden de ingreso, de la forma `A-0NN`, y **jamás se reasigna**. Las entradas derogadas conservan su identificador. Se proscribe la numeración ordinal en todo catálogo acumulativo del repositorio, por su fragilidad ante inserciones y consolidaciones (regla A-013).

**Estado.** Ninguna entrada rige mientras figure como `propuesto`. Conforme a la sección 15.3 del `SKILL.md`, las correcciones de manifiesto se aplican de inmediato y se informan; los cambios de criterio requieren aprobación expresa del titular.

**Categorías admitidas**: `Criterio-jurídico` · `Estilo-redacción` · `Metodología` · `Normativa` · `Jurisprudencia` · `Preferencia-usuario` · `Error-corregido` · `Fuente-verificada` · `Tipología-LAFT` · `Tributario`.

---

## Reglas de higiene de la memoria

1. Máximo 50 entradas activas. Superado el límite, consolida entradas afines en una sola regla operativa y archiva las originales en la sección «Histórico consolidado».
2. Ninguna entrada puede contener datos personales de imputados, víctimas, testigos o clientes, ni contenido amparado por secreto profesional. Se registran **criterios**, no hechos de casos.
3. Toda entrada de categoría `Normativa` o `Jurisprudencia` debe indicar su fuente de verificación (texto legal, rol de causa, fecha). Si no fue verificada, se marca «pendiente de verificación» y no puede fundar conclusiones hasta ser confirmada.
4. Las entradas derogadas no se borran: se marcan `Vigencia: derogada` con la fecha, para preservar trazabilidad.

---

## Aprendizajes activos

### A-001 — [2026-07-05] — Metodología — Entrada fundacional
- **Estado**: aprobado
- **Naturaleza**: cambio de criterio
- **Contexto**: creación del mecanismo de auto-aprendizaje (versión 3.1 de la skill).
- **Lección**: la skill debe capturar sistemáticamente las correcciones del usuario en lugar de perderlas al cierre de cada conversación.
- **Regla operativa**: ejecutar el Protocolo de Cierre y Aprendizaje al término de todo análisis; ofrecer siempre al usuario la incorporación de las lecciones detectadas.
- **Vigencia**: permanente.

### A-002 — [2026-07-09] — Fuente-verificada — El aparato axiomático de von Neumann y Morgenstern no funda el criterio de valor esperado
- **Estado**: aprobado
- **Naturaleza**: corrección de manifiesto
- **Contexto**: examen del texto primario *Theory of Games and Economic Behavior*, sección 3.7.1.
- **Lección**: el aparato axiomático no deriva el criterio de valor esperado: lo presupone por vía de definición. Las invocaciones previas del texto como su fundamento eran circulares.
- **Regla operativa**: prohibido citar a von Neumann y Morgenstern como fundamento del criterio de valor esperado. Si el criterio se emplea, se funda en otra parte o se declara como supuesto.
- **Vigencia**: permanente.

### A-003 — [2026-07-09] — Criterio-jurídico — La utilidad es vectorial sin comparabilidad plena de preferencias
- **Estado**: aprobado
- **Naturaleza**: corrección de manifiesto
- **Contexto**: *Theory of Games and Economic Behavior*, sección 3.7.2.
- **Lección**: los propios autores conceden que, ausente la comparabilidad plena, la utilidad es vectorial y multidimensional. Ello corrobora, desde la fuente misma, la regla contra la reducción escalar de la exposición penal.
- **Regla operativa**: la exposición penal no se reduce a un escalar. Sus dimensiones —privación de libertad, pena accesoria, consecuencia patrimonial, inhabilitación, registro— se exhiben separadamente y no se agregan en una cifra única.
- **Vigencia**: permanente.

### A-004 — [2026-07-09] — Metodología — Prohibición de comparaciones interpersonales de utilidad
- **Estado**: aprobado
- **Naturaleza**: corrección de manifiesto
- **Contexto**: *Theory of Games and Economic Behavior*, sección 3.7.3. La regla se formuló al advertirse que un prototipo previo en Python promediaba valores esperados del Ministerio Público y del imputado.
- **Lección**: la fuente excluye expresamente la comparación interpersonal de utilidades. Promediar el valor esperado del fiscal con el del imputado carece de sentido, aun cuando la operación aritmética sea posible.
- **Regla operativa**: prohibido agregar, promediar o compensar utilidades entre partes con intereses contrapuestos. Cada parte se modela por separado.
- **Vigencia**: permanente.

### A-005 — [2026-07-09] — Error-corregido — Regla de rotulación de fuentes
- **Estado**: aprobado
- **Naturaleza**: corrección de manifiesto
- **Contexto**: McNamee y Celona fueron contabilizados como voces separadas y en conflicto, siendo coautores de una sola obra. El error, originado en una rotulación por apellido único, infló una contradicción de tres voces a cuatro. Se repitió en un segundo caso.
- **Lección**: la rotulación por apellido único produce duplicación de autoría y falsas contradicciones en la auditoría de fuentes.
- **Regla operativa**: toda entrada del repositorio consigna autor o autores completos, título, edición y sección. Ninguna fuente ingresa rotulada por apellido único.
- **Vigencia**: permanente.

### A-006 — [2026-07-09] — Criterio-jurídico — El valor esperado no es criterio aplicable a la defensa penal
- **Estado**: aprobado
- **Naturaleza**: corrección de manifiesto
- **Contexto**: McNamee y Celona, *Decision Analysis for the Professional*, cuarta edición.
- **Lección**: los propios autores declaran el criterio de valor esperado apropiado únicamente para decisiones repetidas, no correlacionadas y de baja consecuencia. La decisión sobre procedimiento abreviado no reúne ninguna de las tres condiciones. El destilado invocaba la fuente para justificar precisamente aquello que la fuente condiciona.
- **Regla operativa**: la decisión estratégica en materia penal se resuelve por acotamiento del peor escenario y no por maximización del valor esperado. Toda invocación del valor esperado declara las tres condiciones y verifica su concurrencia.
- **Vigencia**: permanente.

### A-007 — [2026-07-09] — Criterio-jurídico — Asimetría abogado/cliente con respaldo doctrinal
- **Estado**: aprobado
- **Naturaleza**: cambio de criterio
- **Contexto**: Alexandre Morais da Rosa, *A Teoria dos Jogos Aplicada ao Processo Penal*, sección 1.4.1.9.
- **Lección**: la observación del doble régimen de pagos corrobora, desde fuente doctrinal independiente, la asimetría entre quien calcula la decisión y quien soporta su resultado. La regla asciende de inferencia propia del estudio a regla con respaldo doctrinal.
- **Regla operativa**: toda recomendación estratégica identifica expresamente quién soporta el peor escenario. La asimetría se declara al cliente antes de la decisión.
- **Vigencia**: permanente. La cita textual exige colación contra original impreso; véase A-009.

### A-008 — [2026-07-09] — Error-corregido — Rectificación sobre la fuente Henderson
- **Estado**: aprobado
- **Naturaleza**: corrección de manifiesto
- **Contexto**: Henderson, Chugg, Anderson y Ho, CSLAW '22. El destilado describía la obra con dirección argumental inversa a la real y con autoría incompleta.
- **Lección**: la obra es una agenda de investigación en aprendizaje automático que promueve el perfeccionamiento de sistemas algorítmicos en contextos de fiscalización administrativa, y no una crítica a su uso en justicia penal. Su aporte de mayor valor forense es la tesis de la sección 4.6: la exactitud de un instrumento predictivo no constituye motivación del acto que en él se funda.
- **Regla operativa**: ninguna fuente se caracteriza por el destilado que de ella se hizo; la dirección argumental se verifica contra el original antes de citarla. El módulo `fiscalizacion-algoritmica.md` permanece en versión 0.1 y no gradúa mientras se sostenga en fuente única.
- **Vigencia**: permanente.

### A-009 — [2026-07-09] — Metodología — Advertencia permanente de calidad de OCR
- **Estado**: aprobado
- **Naturaleza**: corrección de manifiesto
- **Contexto**: los archivos de Morais da Rosa (interlineado de dos columnas) y de von Neumann y Morgenstern (símbolos matemáticos corrompidos) presentan reconocimiento óptico defectuoso.
- **Lección**: la transcripción mecánica desde estos archivos produce citas textuales inexactas.
- **Regla operativa**: ninguna cita textual proveniente de dichos archivos se transcribe sin colación previa contra el original impreso.
- **Vigencia**: permanente.

### A-010 — [2026-07-09] — Error-corregido — Los artefactos entregados no se instalan
- **Estado**: aprobado
- **Naturaleza**: corrección de manifiesto
- **Contexto**: cinco módulos construidos en sesión anterior no constaban en el paquete instalado. El contenedor de ejecución se reinicia y el directorio de salida no propaga hacia la instalación de la skill.
- **Lección**: lo construido en una sesión no existe en la siguiente salvo reinstalación del paquete por el usuario.
- **Regla operativa**: rigen las reglas R-1 a R-5 de la sección 0.1 del `SKILL.md`. Ninguna sesión presume instalado lo construido en otra. Ante duda, se presume `no_propagado`.
- **Vigencia**: permanente.

### A-011 — [2026-07-09] — Error-corregido — El SKILL.md invocaba módulos inexistentes
- **Estado**: aprobado; remedio decidido y ejecutado el 2026-07-10
- **Naturaleza**: corrección de manifiesto (la constatación) / cambio de criterio (el remedio)
- **Contexto**: la tabla de triage de la sección 5 ordenaba cargar `metodologia-detallada.md`, `prueba-digital.md`, `calculo-penas.md` y `leyes-especiales.md`. Ninguno existía en el disco.
- **Lección**: el instrumento se instruía a sí mismo para leer archivos inexistentes, sin advertencia alguna.
- **Regla operativa**: antes de invocar un módulo, verificar su existencia; si falta, declararlo al usuario y no suponer su contenido (Paso 2 de la sección 0). **Remedio elegido por el titular: construcción de los cuatro módulos** (instrucción de 2026-07-10, «dejar operativa la skill», única opción que subsana el defecto N° 1 del CHANGELOG tal como fue formulado). Ejecutado en la versión 3.7. Las citas normativas de `leyes-especiales.md` y `calculo-penas.md` no cotejadas contra LeyChile quedan en estado [C], conforme a la regla 3 de higiene, hasta su curación con `curar_norma.py`.
- **Vigencia**: cumplida en cuanto al remedio (v3.7); la regla operativa de verificación previa es permanente.

### A-012 — [2026-07-09] — Metodología — Verificación de métricas contra topologías de valor conocido
- **Estado**: aprobado
- **Naturaleza**: corrección de manifiesto
- **Contexto**: una implementación propia del algoritmo de Brandes dividía dos veces por dos y arrojaba centralidades de intermediación normalizadas de 2,0, siendo 1,0 el máximo teórico. El defecto se detectó por control sobre un grafo en estrella.
- **Lección**: una métrica implementada y no verificada contra un valor conocido es una afirmación no acreditada, aunque provenga de código propio.
- **Regla operativa**: toda métrica cuantitativa que ingrese al repositorio se verifica contra topologías o casos de valor analítico conocido antes de su uso. El control se documenta.
- **Vigencia**: permanente.

### A-013 — [2026-07-09] — Metodología — Identificadores estables en catálogos acumulativos
- **Estado**: aprobado
- **Naturaleza**: cambio de criterio
- **Contexto**: `contraindicaciones.md` numeraba sus entradas de modo ordinal. La inserción o consolidación de una entrada anterior desplaza toda cita externa.
- **Lección**: la numeración ordinal es un identificador frágil en un catálogo que crece y se consolida.
- **Regla operativa**: todo catálogo acumulativo del repositorio emplea identificadores estables (`A-0NN`, `C-0NN`), asignados en orden de ingreso y jamás reasignados. Las entradas derogadas conservan su identificador con la marca correspondiente.
- **Vigencia**: permanente.

---

## Lagunas consignadas

**Primera.** No consta el texto de las tres entradas pendientes de aprobación desde las versiones 3.1 a 3.4 de la skill. No se reconstruyen. Si el titular conserva su formulación, se incorporan como `A-021` y siguientes (el identificador `A-014` quedó asignado el 2026-07-10), sin alterar la numeración precedente.

**Segunda.** Las entradas `A-002` a `A-009` son **reconstrucción** de las lecciones formuladas en la sesión de examen de fuentes primarias, efectuada desde el registro de la sesión y no desde este archivo, que no las contenía. La correspondencia uno a uno con las ocho lecciones originales no está verificada.

**Tercera.** No consta el texto de las entradas `C-001` a `C-011` de `contraindicaciones.md`, módulo que figura como `no_propagado`. El fragmento `C-012` a `C-014` no se integra mientras aquellas no se recuperen.

---

### A-014 — [2026-07-10] — Fuente-verificada — Verificación de la Ley 21.595 detectó dos errores en el módulo recién construido
- **Estado**: aprobado
- **Naturaleza**: corrección de manifiesto
- **Contexto**: cotejo del módulo `leyes-especiales.md` (v3.7) contra la exportación oficial de LeyChile de la Ley 21.595 (idNorma 1195119, versión única 17-AGO-2023) y contra el catálogo oficial de la UAF para la Ley 19.913.
- **Lección**: el módulo construido de conocimiento profesional, con sus citas honestamente marcadas [C], contenía dos errores sustantivos: situaba el lavado de activos en la tercera categoría, siendo de la cuarta (art. 4), y atribuía al catálogo de sustitutivas propias la libertad vigilada intensiva, siendo el catálogo del art. 20 la remisión condicional, la reclusión parcial en domicilio y la reclusión parcial en establecimiento especial. La disciplina [C] funcionó exactamente para lo que fue diseñada: ninguna de esas citas podía fundar conclusión ni escrito antes del cotejo.
- **Regla operativa**: todo módulo normativo nuevo se coteja contra fuente oficial antes de su primer uso en caso real, aunque provenga de conocimiento profesional consolidado; las etiquetas [C] no se degradan a mera formalidad. Fuente de verificación: LeyChile idNorma 1195119 (13-03-2024) y uaf.cl.
- **Vigencia**: permanente.

---

## Entradas incorporadas en la reconciliación v4.3 (2026-07-12)

Las entradas A-015 a A-020 provienen del linaje del repositorio `estrategia-litigio-penal` (sesiones de curatoría del 2026-07-06 y 2026-07-07, aprobadas por el titular en su oportunidad). La bifurcación de linajes posterior a la v3.7 impidió su traslado a esta memoria hasta la presente reconciliación. Se asignan identificadores estables conforme a A-013, respetando el orden de ingreso.

### A-015 — [2026-07-06] — Fuente-verificada — Servicio XML oficial de LeyChile (`obtxml opt=7`)
- **Estado**: aprobado *(aprobación original del titular: 2026-07-06; incorporada a este archivo en la reconciliación v4.3 del 2026-07-12 desde el linaje del repositorio `estrategia-litigio-penal`, acta en `docs/APROBACIONES-PENDIENTES.md`)*
- **Naturaleza**: fuente verificada
- **Contexto**: sesión de curatoría normativa que pobló `references/marco-legal.md` (248 artículos CP/CPP) desde los XML oficiales de la Biblioteca del Congreso Nacional.
- **Lección**: el servicio `https://www.leychile.cl/Consulta/obtxml?opt=7&idNorma=<ID>` (opcionalmente `&notaPIE=1`) entrega el texto consolidado y vigente de la norma en esquema `EsquemaIntercambioNorma-v1-0`, con metadatos de versión por artículo (idParte y fecha de versión). Identificadores verificados: Código Penal → idNorma **1984**; Código Procesal Penal (Ley 19.696) → idNorma **176595**; Código Tributario (DL 830) → idNorma **6374**.
- **Regla operativa**: toda cita normativa de la skill se verifica contra XML descargado desde ese servicio, identificando la norma por su idNorma verificado. Queda prohibido el uso de mirrors privados, agregadores o versiones sin fecha.
- **Vigencia**: permanente. *(Aprobada por el abogado el 2026-07-07.)*

### A-016 — [2026-07-06] — Metodología — Curatoría normativa exclusivamente vía `curar_norma.py` sobre XML descargado por el abogado
- **Estado**: aprobado *(aprobación original del titular: 2026-07-06; incorporada a este archivo en la reconciliación v4.3 del 2026-07-12 desde el linaje del repositorio `estrategia-litigio-penal`, acta en `docs/APROBACIONES-PENDIENTES.md`)*
- **Naturaleza**: cambio de criterio aprobado
- **Contexto**: misma sesión de curatoría. Se constató que la transcripción manual o reconstruida de memoria introduce riesgo de texto desactualizado o inexacto, incompatible con el estándar del estudio.
- **Lección**: la única cadena admisible para poblar módulos normativos es: (1) el abogado descarga personalmente el XML desde LeyChile; (2) el XML se procesa con `scripts/curar_norma.py`, que valida idNorma, extrae el perímetro, marca derogados, excluye transitorios y advierte artículos no hallados; (3) el extracto se inserta íntegro, sin edición manual del texto legal.
- **Regla operativa**: ninguna curatoría normativa se ejecuta por transcripción manual ni desde la memoria del modelo. Si no hay XML aportado por el abogado, el artículo conserva la marca «cita pendiente de verificación».
- **Vigencia**: permanente. *(Aprobada por el abogado el 2026-07-07.)*

### A-017 — [2026-07-06] — Fuente-verificada — La marca «2222-02-02» en el XML de LeyChile denota vigencia diferida, no error de fuente
- **Estado**: aprobado *(aprobación original del titular: 2026-07-06; incorporada a este archivo en la reconciliación v4.3 del 2026-07-12 desde el linaje del repositorio `estrategia-litigio-penal`, acta en `docs/APROBACIONES-PENDIENTES.md`)*
- **Naturaleza**: fuente verificada
- **Contexto**: al procesar el XML del Código Penal (idNorma 1984) se observó que el atributo de versión de la norma reporta la fecha «2222-02-02», coexistiendo con artículos cuya fecha de versión individual es real (la más reciente del perímetro: 17-09-2025).
- **Lección**: LeyChile utiliza la fecha centinela «2222-02-02» para señalar que el cuerpo normativo contiene al menos una disposición con **vigencia diferida** (aún no vigente); no constituye error del servicio ni invalida la descarga.
- **Regla operativa**: cuando el XML reporte versión de norma «2222-02-02», la curatoría debe (a) dejar constancia de la marca en el encabezado del extracto, y (b) verificar la fecha de versión **artículo por artículo**, identificando cuáles disposiciones del perímetro tienen vigencia diferida antes de citarlas como derecho vigente.
- **Vigencia**: permanente. *(Aprobada por el abogado el 2026-07-07.)*

### A-018 — [2026-07-07] — Metodología — Enmienda: descarga del XML ejecutable por el asistente desde el servicio oficial, por instrucción del abogado
- **Estado**: aprobado *(aprobación original del titular: 2026-07-07; incorporada a este archivo en la reconciliación v4.3 del 2026-07-12 desde el linaje del repositorio `estrategia-litigio-penal`, acta en `docs/APROBACIONES-PENDIENTES.md`)*
- **Naturaleza**: cambio de criterio aprobado
- **Contexto**: sesión de curatoría de las cinco leyes especiales (21.595, 20.393, 19.913, 21.459 y 20.000). El abogado instruyó expresamente que el asistente descargara los XML, lo que enmienda la regla que exigía descarga personal del abogado.
- **Lección**: la finalidad de la regla es la autenticidad de la fuente, no la identidad del descargador. La descarga directa por el asistente preserva la cadena de custodia si se ejecuta contra el servicio oficial `obtxml opt=7`, con idNorma resuelto desde el enlace canónico de LeyChile, validación de idNorma por `curar_norma.py` y hash SHA-256 registrado en el módulo.
- **Regla operativa**: la descarga del XML puede ejecutarla el asistente, dentro de la sesión de trabajo y previa instrucción del abogado, únicamente desde `https://www.leychile.cl/Consulta/obtxml?opt=7&idNorma=<ID>`, dejando registro de: URL, idNorma canónico, fecha de descarga y SHA-256. Sigue prohibida toda fuente distinta del servicio oficial y toda transcripción de memoria.
- **Vigencia**: permanente. *(Aprobada por el abogado el 2026-07-07.)*

### A-019 — [2026-07-07] — Fuente-verificada — La Ley 20.393 usa estructura «Doble Articulado» en el XML de LeyChile
- **Estado**: aprobado *(aprobación original del titular: 2026-07-07; incorporada a este archivo en la reconciliación v4.3 del 2026-07-12 desde el linaje del repositorio `estrategia-litigio-penal`, acta en `docs/APROBACIONES-PENDIENTES.md`)*
- **Naturaleza**: fuente verificada
- **Contexto**: el inventario inicial de la Ley 20.393 (idNorma 1008668) arrojó solo tres artículos (PRIMERO/SEGUNDO/TERCERO): su estatuto completo (arts. 1 a 29, con variantes bis a quinquies) está anidado dentro del Artículo PRIMERO bajo un nodo `tipoParte="Doble Articulado"`.
- **Lección**: las leyes promulgatorias con articulado aprobado «como texto» requieren que el motor de curatoría descienda al interior de los artículos; de lo contrario la extracción queda vacía sin advertencia.
- **Regla operativa**: usar la versión de `curar_norma.py` del repositorio `estrategia-litigio-penal` (con recursión en articulado anidado y prueba de regresión); ante toda norma nueva, cotejar el total inventariado contra la estructura visible en LeyChile antes de extraer.
- **Vigencia**: permanente. *(Aprobada por el abogado el 2026-07-07.)*

### A-020 — [2026-07-07] — Fuente-verificada — Numeración ordinal («Art. 1°») en leyes recientes
- **Estado**: aprobado *(aprobación original del titular: 2026-07-07; incorporada a este archivo en la reconciliación v4.3 del 2026-07-12 desde el linaje del repositorio `estrategia-litigio-penal`, acta en `docs/APROBACIONES-PENDIENTES.md`)*
- **Naturaleza**: fuente verificada
- **Contexto**: la extracción de la Ley 21.459 (idNorma 1177743) omitió los arts. 1° a 9° porque su `NombreParte` incluye el indicador ordinal («1°», «8º»), que el parser no reconocía como número.
- **Lección**: LeyChile registra la numeración ordinal de forma heterogénea (con ° u º); la comparación numérica debe normalizar esos indicadores.
- **Regla operativa**: `curar_norma.py` normaliza los indicadores ordinales (°, º, ª) antes de comparar; en toda curatoría, verificar que el número de artículos extraídos coincida con el perímetro y tratar la «Advertencia de completitud» como bloqueo hasta esclarecer su causa.
- **Vigencia**: permanente. *(Aprobada por el abogado el 2026-07-07.)*

### A-021 — [2026-07-12] — Fuente-verificada — El servicio `obtxml` de LeyChile exige cabecera `User-Agent` de navegador
- **Estado**: aprobado *(aprobación del titular: 2026-07-12, sesión de reconciliación v4.3)*
- **Naturaleza**: cambio de criterio aprobado
- **Contexto**: re-curación de la Ley 21.459 en la sesión de reconciliación. La solicitud a `https://nuevo.leychile.cl/servicios/Consulta/obtxml?opt=7&idNorma=1177743` sin cabecera `User-Agent` fue rechazada por la capa CloudFront del servicio con HTTP 401 y cuerpo vacío; la misma solicitud con `User-Agent` de navegador respondió HTTP 200 con el XML oficial íntegro (esquema EsquemaIntercambioNorma-v1-0).
- **Lección**: el rechazo 401 sin cabecera de navegador no denota falta de autorización sobre la fuente ni bloqueo de red: es un filtro de la infraestructura del servicio. Diagnosticarlo como «bloqueo de entorno» conduce a diferir curatorías que son ejecutables.
- **Regla operativa**: toda descarga desde `obtxml` se ejecuta con cabecera `User-Agent` de navegador y `Accept: application/xml`. Ante respuesta vacía o 401, se verifica primero la cabecera antes de declarar bloqueo de red; la declaración de bloqueo exige constancia del encabezado de respuesta (código y, si existe, `x-deny-reason`). Se mantiene íntegro el registro de trazabilidad: URL, idNorma, fecha y SHA-256 del XML.
- **Vigencia**: permanente.

### A-022 — [2026-07-12] — Metodología — Prohibición de copias duales de motores deterministas
- **Estado**: aprobado *(aprobación del titular: 2026-07-12, sesión de reconciliación v4.3)*
- **Naturaleza**: cambio de criterio aprobado
- **Contexto**: la reconciliación v4.3 constató que el linaje del repositorio v4.2 mantenía dos copias de `curar_norma.py` —`scripts/` de nivel superior (motor real, con `--resolver` y `--descargar`, ejercitado por la suite de 54 pruebas) y `skill/scripts/` (copia empaquetada, desincronizada en 240 líneas, contra la cual fallaban 22 pruebas)—, mientras el catálogo del SKILL.md atribuía a la copia empaquetada capacidades que no poseía.
- **Lección**: la copia dual de un motor determinista crea una certeza falsa de la misma especie que un índice que declara instalado lo inexistente (R-1): el paquete promete lo que solo el repositorio cumple. La suite que pasa contra una ruta no acredita nada respecto de la otra.
- **Regla operativa**: todo script determinista existe en una sola ruta canónica dentro del paquete de la skill (`scripts/`). Si el repositorio conserva una copia de trabajo fuera del paquete, el Deber de Cierre (R-3) comprende el cotejo de hash entre ambas rutas; ante discrepancia, la copia del paquete se regenera desde la canónica probada por la suite, jamás a la inversa sin nueva ejecución íntegra de las pruebas.
- **Vigencia**: permanente.


### A-023 — [2026-07-17] — Fuente-verificada — Las tablas normativas del XML de LeyChile constan como imágenes embebidas (`aem:ArchivoBinario`), no como texto
- **Estado**: aprobado *(propuesta y texto del titular, 2026-07-17, Protocolo de Cierre de la sesión v4.8; su autoría directa constituye la aprobación expresa que exige la sección 15.3.3.b, conservando el titular la facultad de revertirla)*
- **Naturaleza**: cambio de criterio aprobado
- **Contexto**: cotejo único de la TABLA DEMOSTRATIVA del art. 56 CP (sesión v4.8, 2026-07-17). El extracto textual del 2026-07-06 carecía de la tabla pese a provenir del XML oficial íntegro; se constató que el XML del Código Penal (idNorma 1984, SHA-256 `21fd760b…78e18`) la incorpora como imagen embebida en un nodo `aem:ArchivoBinario` (`Art56CP.jpeg`, 294.054 bytes, SHA-256 `eb7441aa…3ac0fa`), fuera del flujo textual que procesa `curar_norma.py`.
- **Lección**: el XML oficial de LeyChile incorpora las tablas normativas (v.gr., la TABLA DEMOSTRATIVA del art. 56 CP) como imágenes embebidas en `aem:ArchivoBinario`, no como texto. Un motor de curatoría limitado al flujo textual produce extractos silenciosamente incompletos respecto de toda disposición cuyo contenido operativo resida en una tabla, sin advertencia alguna de completitud.
- **Regla operativa**: la curatoría de todo artículo cuyo contenido normativo comprenda una tabla exige: (a) inventariar los nodos `aem:ArchivoBinario` del XML descargado; (b) extraer el binario y registrar su SHA-256 propio, además del hash del XML de origen; (c) practicar cotejo visual del binario contra la transcripción que se incorpore al módulo, dejando constancia del resultado en el registro de curatoría; y (d) conservar el binario en `assets/fuentes/` e indexarlo. `curar_norma.py` solo captura el flujo textual: su salida no acredita, por sí sola, la completitud de artículos con tablas.
- **Vigencia**: permanente.


---

## Histórico consolidado

*(vacío)*
