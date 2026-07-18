# Registro de cambios — `analisis-penal-chile`

## v4.11 — 17 de julio de 2026

**Versión exclusivamente registral: rectificación de manifiesto (15.3.3.a) y constancia de cierre del Defecto N° 6 en el ciclo v4.10.**

1. **Rectificación de la entrada v4.10.** El apartado *«Pendientes que subsisten»* de la entrada v4.10 consignó que el directorio `skill/` del repositorio `estrategia-litigio-penal` se encontraba «en v4.2». La constancia era inexacta: a la fecha de ese cierre, `skill/` se encontraba ya en **v4.9**, por efecto del commit `e154c54` («Subsana Defecto N° 6: incorpora linaje reconciliado v4.3 → v4.9»), publicado por el titular vía bundle el 2026-07-17, con verificación posterior por clon independiente. El texto arrastró el estado de un ciclo anterior. La entrada v4.10 se conserva sin alteración, conforme a la regla de inmutabilidad del registro histórico; la presente entrada constituye su fe de erratas.

2. **Cierre del Defecto N° 6 respecto del ciclo v4.10.** En sesión del 2026-07-17 se incorporó al repositorio la cadena reconciliada **v4.3 → v4.10** mediante el commit `c70d2ae` («Actualiza skill/ al linaje reconciliado v4.3 → v4.10»), publicado por el titular vía bundle (`defecto6-v410.bundle`, SHA-256 `566380c92861a8812107fea7350bb8680c217184389749634901062366037686`) y verificado por clon independiente: `skill/SKILL.md` en versión 4.10, verificador de sincronía de motores conforme, 62 pruebas conformes. Los linajes instalado y publicado convergen; **el Defecto N° 6 queda cerrado**, sin perjuicio de su reapertura natural cada vez que se cierre una versión nueva sin propagarla al repositorio.

3. **Constancia de curatoría de sincronía (A-022).** La operación del numeral anterior advirtió una divergencia triple de `prescripcion.py` —tres hashes distintos entre `src/`, `skill/scripts/` y la instalación v4.10, por diferencias exclusivamente cosméticas de formato—. Se adoptó el ejemplar de la instalación v4.10 como texto único para ambas rutas del repositorio (hash convergente `f949afc81c3ad07609b991810b6606363277ead0e2f9298537eb3fa4424f7dac`), con verificador de identidad binaria conforme y suite completa conforme. Ningún cambio funcional.

4. Versión incrementada a 4.11; índice maestro regenerado conforme a R-4; paquete auditado con `verificar-integridad.sh` conforme a R-3. Esta versión no altera módulo sustantivo alguno: solo `CHANGELOG.md`, `SKILL.md` (número de versión y registro) e `index-maestro.json`.

*Pendientes que subsisten*: instalación del paquete v4.11 en Claude.ai (acto del titular); incorporación de la cadena v4.3 → v4.11 al directorio `skill/` del repositorio, cuyo commit acompaña esta misma sesión.


## v4.10 — 17 de julio de 2026

**Protocolo de Cierre y Aprendizaje de la sesión de curatoría histórica.**

1. **A-024 incorporada** a `references/aprendizajes.md` en estado **aprobado** (categoría Fuente-verificada; naturaleza corrección de manifiesto sometida además a aprobación expresa, obtenida del titular el 2026-07-17). Contenido: el manual oficial `accesoLeyesChilenas.pdf` (descargado desde `www.leychile.cl/esquemas/`), sección 6, establece que el servicio `obtxml` entrega siempre la versión actualizada de la norma —integración de las últimas versiones de cada una de sus partes— sin contemplar parámetro alguno de consulta histórica; la sintaxis `idVersion=<fecha>` ensayada en sesión anterior era una hipótesis del asistente desmentida por la propia fuente oficial y se descarta de plano como método futuro. Regla operativa: las consultas históricas se canalizan por el protocolo de degradación de A-025 o por descarga humana desde la interfaz web de LeyChile.
2. **A-025 incorporada** a `references/aprendizajes.md` en estado **aprobado** (categoría Metodología; naturaleza cambio de criterio, aprobación expresa del titular el 2026-07-17). Contenido: protocolo de degradación controlada para consultas normativas históricas cuando la vía primaria de LeyChile es *estructuralmente* inviable —no meramente bloqueada o demorada—, con cinco condiciones copulativas: (1) constancia expresa de la inviabilidad y su causa; (2) pluralidad de fuentes doctrinarias o profesionales identificadas y concordantes; (3) rotulación [C] expresa con indicación de cada fuente; (4) declaración del grado de certeza y sujeción a cotejo con el texto oficial si deviene accesible; (5) prohibición de fundar un escrito judicial en la sola cita [C] sin advertencia de su estatuto. Se deja constancia expresa de que la regla A-016 permanece plenamente vigente para toda curatoría de texto normativo actual: A-025 no la excepciona, sino que regula un supuesto distinto (consulta histórica sin vía primaria disponible), diverso del error que A-016 sanciona (transcripción normativa desde la memoria del modelo sin XML de respaldo alguno).
3. Versión de la skill incrementada a 4.10; índice maestro regenerado conforme a R-4; paquete reempaquetado y auditado con `verificar-integridad.sh` conforme a R-3.

*Pendientes que subsisten*: instalación del paquete v4.10 en Claude.ai (acto del titular); **Defecto N° 6** del repositorio `estrategia-litigio-penal` (directorio `skill/` en v4.2), cuya subsanación exige ahora incorporar la cadena reconciliada **v4.3 → v4.10**.

## v4.9 — 17 de julio de 2026

**Protocolo de Cierre y Aprendizaje de la sesión v4.8 (línea VI).**

1. **A-023 incorporada** a `references/aprendizajes.md` en estado **aprobado** (categoría Fuente-verificada; naturaleza cambio de criterio; propuesta redactada por el propio titular el 2026-07-17, lo que constituye la aprobación expresa del 15.3.3.b, con facultad de reversión). Contenido: las tablas normativas del XML oficial de LeyChile constan como imágenes embebidas en `aem:ArchivoBinario` (caso constatado: TABLA DEMOSTRATIVA del art. 56 CP, `Art56CP.jpeg`, SHA-256 `eb7441aa…3ac0fa`, dentro del XML del CP SHA-256 `21fd760b…78e18`), no como texto; regla operativa de curatoría en cuatro pasos (inventario de nodos binarios, extracción con hash propio, cotejo visual con constancia, conservación indexada en `assets/fuentes/`), con la advertencia de que `curar_norma.py` solo captura el flujo textual.
2. **Corrección de manifiesto** (15.3.3.a, aplicada e informada): se elimina la sección «Histórico consolidado» duplicada al cierre de `references/aprendizajes.md`, defecto material introducido en una consolidación anterior.
3. Índice maestro regenerado conforme a R-4; paquete reempaquetado y auditado con `verificar-integridad.sh` conforme a R-3.

*Pendientes que subsisten*: instalación del paquete v4.9 en Claude.ai (acto del titular); **Defecto N° 6** del repositorio `estrategia-litigio-penal` (directorio `skill/` en v4.2), cuya subsanación exige ahora incorporar la cadena reconciliada **v4.3 → v4.9** sobre esta versión y no sobre el linaje publicado.

## v4.8 — 17 de julio de 2026

**Cierre de las marcas pendientes del módulo de cálculo (diligencia derivada subsistente de v4.7).**

1. **Art. 351 CPP curado.** Descarga oficial vía `curar_norma.py --descargar 176595` (SHA-256 del XML `c7a5b75858a0ab0a3857f9e7a3f5706fd31ac3ab5cb720bd123de067e16e6469`, idéntico al registrado en la curatoría del 2026-07-12: la norma no ha variado desde la versión 2026-04-02). Artículo insertado en `references/marco-legal.md` como nueva subsección **3.7 «Sentencia definitiva: reiteración de delitos de una misma especie»** (idParte 8646929, versión del artículo 2000-10-12), con renumeración de la antigua 3.7 (nulidad y abreviado) a 3.8. Corpus verificado: **282 artículos**.
2. **Cotejo único de la tabla del art. 56 CP: conforme.** Hallazgo de curatoría: el XML oficial incorpora la TABLA DEMOSTRATIVA como **imagen embebida** (`aem:ArchivoBinario`, `Art56CP.jpeg`, 294.054 bytes, SHA-256 `eb7441aa9c1684e51fcc1a121c210852ca825ac2d1f5b2d31918a373753ac0fa`, extraída del XML del CP descargado el 2026-07-17, idNorma 1984, SHA-256 `21fd760b636b573ee524b0903289ad994aeb2a212c89a21b29abc7e0eb578e18`), lo que explicaba la ausencia de la tabla en el extracto del 2026-07-06. El cotejo visual contra el binario oficial resultó **íntegramente conforme** con la tabla de la sección III de `calculo-penas.md`; la transcripción verificada de las cinco filas quedó anotada como nota de curatoría del art. 56 en `marco-legal.md`, sección 2.2.
3. **`calculo-penas.md` sin marcas pendientes.** Sección III: marca sustituida por constancia de cotejo conforme. Sección IV: el art. 351 CPP pasa de «alternativa a cotejar» a **base de cálculo habilitada**, con su régimen verificado (dos hipótesis de exasperación, cláusula de favorabilidad hacia el art. 74 CP, identidad de especie por bien jurídico afectado).
4. **Capa doctrinal habilitada para cita textual.** `determinacion-penas-doctrina.md`: regla 0.2 y nota de gobernanza de la sección 2.5 actualizadas; la cita textual del art. 351 CPP procede con remisión al extracto verificado.
5. Registro de curatoría de `marco-legal.md` ampliado con las dos operaciones del 2026-07-17.

## v4.7 — 17 de julio de 2026

**Capa doctrinal del cálculo de penas** (fuente aportada por el titular).

*Fuente*: *Guía aplicada para la determinación de penas*, Academia Judicial de Chile, © 2026, 137 pp., autores Javier Wilenmann von Bernath, Francisco Maldonado Fuentes y Sebastián Valenzuela Agüero, validada por comité de jueces de garantía y orales en lo penal; PDF sellado SHA-256 `04a388ce92b4280920d7a66785868eccc4d507f7718ffcbd0d68dc7ce6fe6c81`; curatoría del 2026-07-17 sobre extracción íntegra del texto.

*Módulo nuevo*: `references/determinacion-penas-doctrina.md` v1.0 — capa de criterios de aplicación judicial complementaria (no sustitutiva) de `calculo-penas.md`, con regla de jerarquía expresa (prevalece siempre el texto verificado; no releva las marcas pendientes del art. 56 CP ni del art. 351 CPP). Contenido: dos alternativas de efecto del art. 103 CP en concurrencia con atenuantes simples (aplicación única vs. acumulativa, con el precedente RIT 5081-2014 y la nota táctica principal/subsidiaria para tesis de media prescripción); disparidad jurisprudencial sobre la subida del marco del art. 68 inc. 4° CP (en bloque vs. desde el grado superior, adoptando la guía la segunda) y facultatividad del «podrá»; art. 68 ter CP tras la Ley 21.694 (derogación del art. 449 N° 2) con adecuación del art. 18 CP y disidencia de congruencia interna (CS Rol 2885-2025, Ministro Llanos); algoritmo concursal en cuatro operaciones y criterios de aplicación del art. 351 CPP (misma especie por bien jurídico predominante en delitos pluriofensivos; exasperación sobre marcos sin agotar la individualización; cotejo de favorabilidad con el art. 74 CP); LDE: calificación previa, graduación bidimensional obligatoria perjuicio/culpabilidad, tabla de decisión de sustitutivas (arts. 19–26) y multa obligatoria de mayor cuantía, con el ejercicio Nova Austral como referencia de capacidad económica real; personas jurídicas Ley 20.393: tres operaciones, prelación de la multa proporcional sobre el sistema de días-multa (art. 12), punto medio como default (art. 16) corregido por modificatorias y reproche organizacional, conversión por utilidad anual/365 (ejercicio Penta); RPA: determinación desde el grado inferior sin art. 69 CP ni art. 351 CPP, y prohibición de subir de tramo del art. 23 LRPA (CS Roles 57.252-2021, 2442-2025 y 4757-2025).

*Jurisprudencia*: lote de 12 resoluciones individualizadas por la fuente, ingresadas al módulo como **candidatas** para `references/jurisprudencia-curada.md` en estado pendiente de verificación primaria; ninguna se ingresa al registro J-0NN ni se cita como verificada sin cotejo del titular contra el texto del fallo, conforme a la regla rectora de la línea IV. Doctrina referida por la fuente: Parra (2019), *Revista de Derecho* U. de Concepción, Vol. 87, N° 246 (no verificada).

*Propagación*: `SKILL.md` v4.7 — fila nueva en la tabla de triage (sección 5, carga conjunta con `calculo-penas.md`) y entrada de catálogo (sección 14). Índice regenerado conforme a R-4.

*Diligencia derivada*: programar curatoría del art. 351 CPP vía `curar_norma.py` sobre el XML del CPP (idNorma 176595) y cotejo único de la tabla del art. 56 CP, únicas marcas que esta versión deja subsistentes en `calculo-penas.md`.

*Pendientes que subsisten*: instalación del paquete v4.7 en Claude.ai (acto del titular); incorporación del linaje reconciliado al directorio `skill/` del repositorio `estrategia-litigio-penal`, que permanece en v4.2 (defecto N° 6), debiendo efectuarse sobre esta v4.7 y no sobre el linaje publicado.

## v4.6 — 12 de julio de 2026

**Protocolo de jurisprudencia verificada** (línea IV del plan de mejoras, aprobada por el titular).

*Diseño*: no se construye un repositorio de fallos —inviable sin fuente oficial estructurada de jurisprudencia chilena accesible desde el entorno—, sino un protocolo de curatoría análogo al normativo: el texto de todo considerando lo aporta el titular desde la fuente que tiene a la vista (Oficina Judicial Virtual, copia en carpeta, base identificada); la skill lo fija, identifica, sella con hash y somete a reglas de estado. La verificación de la realidad externa del fallo permanece como acto humano del abogado responsable.

*Módulo nuevo*: `references/jurisprudencia-curada.md` v1.0 — regla rectora que prohíbe de modo absoluto e inderogable el ingreso o cita como verificada de jurisprudencia proveniente de la memoria del modelo (en línea con la prohibición N° 2 de la sección 12 del `SKILL.md`); formato estandarizado de ficha con campos de individualización (tribunal, sala, tipo de recurso, rol, fecha, redactor, considerando), de contenido (tesis, alcance y límites, materia, firmeza) y de verificación (fuente del texto, fecha de verificación, SHA-256 del texto normalizado); cuatro estados —[V] verificada con condiciones copulativas, [PV] pendiente, [NU] no ubicable/rechazada como antecedente negativo, [S] superada— con regla de degradación conforme a R-5; identificadores estables `J-0NN` jamás reasignados (regla A-013); reglas de higiene (omisión de datos personales no indispensables, una ficha por considerando, trazabilidad de ingreso, crecimiento causa a causa, remisión cruzada a `aprendizajes.md` categoría `Jurisprudencia`); índice temático inicial de diez categorías. Registro creado sin fichas; primer identificador disponible: J-001.

*Motor nuevo*: `scripts/curar_jurisprudencia.py` — plantilla JSON (`--plantilla`), validación de ficha con verificación copulativa del estado [V] (`--validar`), ingreso con asignación del identificador siguiente y sellado SHA-256 del texto normalizado —Unicode NFC, colapso de espacios— (`--agregar`), auditoría del registro con detección de identificadores duplicados, saltos de numeración, fichas [V] sin texto y hashes no coincidentes (`--verificar`, código de salida 0/1/2), e inventario (`--listar`). Sin acceso a red por diseño. Suite `test_curar_jurisprudencia.py`: 17 pruebas pytest con datos íntegramente ficticios, todas conformes; entregada para su incorporación al directorio `tests/` del repositorio.

*Propagación*: `SKILL.md` v4.6 — fila nueva en la tabla de triage (sección 5); regla de cita jurisprudencial reforzada en el formato de entrega (solo cita verificada la que conste en estado [V], con remisión `J-0NN`); punto de verificación final actualizado (sección 13); entradas de catálogo del módulo y del motor (sección 14). Índice regenerado conforme a R-4.

*Pendientes que subsisten*: incorporación del linaje reconciliado (v4.5/v4.6) al directorio `skill/` del repositorio `estrategia-litigio-penal`, que permanece en v4.2 (defecto N° 6 del registro de v4.3); incorporación del motor y su suite al repositorio con las adecuaciones de CI (sincronía de motores y lint).

## v4.5 — 12 de julio de 2026

**Módulo de audiencia de preparación y exclusión probatoria** (línea III del plan de mejoras, aprobada por el titular).

*Curatoría normativa*: descarga del XML oficial del CPP (idNorma 176595, versión de la norma 2026-04-02, 806.351 bytes, SHA-256 `c7a5b75858a0ab0a3857f9e7a3f5706fd31ac3ab5cb720bd123de067e16e6469`) mediante `curar_norma.py --descargar`, conforme a A-021; extracción verificada de 26 artículos (260–280 bis, 295–297 y 340) e inserción en `marco-legal.md` como subsecciones 3.5 y 3.6, con renumeración de la antigua 3.5 («Nulidad y procedimiento abreviado») a 3.7 y nueva fila en el registro de curatoría. Corpus verificado: 281 artículos.

*Módulo nuevo*: `references/audiencia-preparacion.md` v1.0 — naturaleza estratégica de la fase intermedia; calendario procesal con tabla de preclusiones; control de congruencia, vicios formales (sanción de sobreseimiento del art. 270) y excepciones del art. 264 con su régimen recursivo asimétrico (art. 271); las cuatro categorías de exclusión del art. 276 con protocolo de construcción de la solicitud en cinco pasos y regla de subsidiariedad escalonada; asimetría recursiva del art. 277 (apelación exclusiva del MP, preconstitución del agravio del art. 373 a) para la defensa, palanca del sobreseimiento por exclusión de prueba esencial); convenciones probatorias con el hallazgo del inciso final del art. 275 (atenuante 11 N° 9 CP, versión 2024-09-04) y regla de prudencia de peor caso; herramientas complementarias (arts. 273, 274, 278, 280 y 280 bis); encuadre de los tres momentos probatorios (arts. 295–297 y 340); checklists por rol y test de fallo. Conexiones declaradas con `prueba-digital.md` (VII.a), `razonamiento-probatorio.md`, `calculo-penas.md`, `tributario.md`, `estrategia-litigio.md` y la skill `argumentacion-forense`. Sin citas jurisprudenciales; criterios de práctica marcados [criterio práctico].

*Propagación*: SKILL.md v4.5 (fila de triage, entrada de catálogo, corpus 255→281), índice regenerado conforme a R-4.

## v4.4 — 12 de julio de 2026

Incorporación, con aprobación expresa del titular, de las entradas **A-021** (cabecera `User-Agent` obligatoria ante `obtxml`; el 401 de CloudFront no constituye bloqueo de red y su declaración exige constancia del encabezado de respuesta) y **A-022** (ruta canónica única para los motores deterministas y cotejo de hash entre paquete y repositorio como acto del Deber de Cierre R-3). Sin cambios normativos ni de módulos; índice regenerado conforme a R-4.

## v4.3 — 12 de julio de 2026 (reconciliación de linajes)

**Reconciliación de linajes.** Unifica el linaje local (v3.8→v3.11: gobernanza, recuperaciones, curación normativa del 2026-07-11) y el linaje del repositorio (v4.0→v4.2: módulos reconstruidos sobre marco verificado, `tributario.md`, `prescripcion.py`, motor `curar_norma.py` ampliado, ejemplo pedagógico), conforme al acta de reconciliación aprobada por el titular (D-1 a D-4). Resoluciones: `marco-legal.md` local prevalece (255 artículos, incluidos arts. 292–295 CP); `leyes-especiales.md` local como módulo analítico y extracto verbatim del repositorio como `leyes-especiales-extractos.md`; `calculo-penas.md` base repositorio con la sección de la Ley 18.216 **[V]** del linaje local; `prueba-digital.md` base repositorio con inyección del mapa de licitud local (VII.a); `metodologia-detallada.md` base repositorio con la regla de proporcionalidad y el paso de verificación de gobernanza; `aprendizajes.md` en unión (A-001 a A-020, incorporando las seis lecciones de curatoría del repositorio como A-015 a A-020 y reubicando A-014); re-curación de la Ley 21.459 el 2026-07-12 (XML oficial, SHA-256 registrado, resultado concordante: arts. 9° y 16 derogados, art. 11 en vigencia diferida). Restituye la Cláusula de Integridad y Propagación (sección 0, R-1 a R-5), la calificación dual del Protocolo de Cierre (15.3.3.a/b), el índice maestro, `verificar-integridad.sh` y el CHANGELOG, ausentes del linaje del repositorio. Subsana la laguna documental de los cinco módulos locales no catalogados en la sección 14.

**Defectos que subsisten** (heredados y actualizados):
1. Texto de C-001 a C-011 y de las tres entradas pendientes de las versiones 3.1 a 3.4: perdido salvo reingreso por el titular.
2. `errata-acta-auditoria.md` en reconstrucción de síntesis; tenor literal de las ocho erratas pendiente.
3. `fiscalizacion-algoritmica.md` no gradúa a 1.0 sin segunda fuente.
4. Revalidaciones: `marco-legal.md` enero de 2027; `leyes-especiales-extractos.md` 2027-01-07 (salvo Ley 21.459, re-curada el 2026-07-12); módulos analíticos julio de 2027 o ante noticia de reforma.
5. Candidata C-015 (arista/concierto): desbloqueada; pendiente de decisión del titular.
6. La divergencia de linajes queda **cerrada**: el repositorio `estrategia-litigio-penal` debe recibir esta v4.3 como fuente única (commit pendiente, acto del titular).

**Corrección de manifiesto adicional (v4.3).** Se constató que el linaje del repositorio v4.2 empaquetaba en `skill/scripts/curar_norma.py` una versión desincronizada del motor —carente de `--resolver` y `--descargar`, funciones que el propio catálogo declaraba y que la suite de 54 pruebas ejercita contra `scripts/curar_norma.py` de nivel superior (22 pruebas fallaban contra la copia empaquetada). La v4.3 adopta el motor completo (SHA-256 `a0f8a434…`), verificado con la suite íntegra.

## Linaje del repositorio (v4.0 → v4.2)

**Versión 4.2** — Julio de 2026. Construye `references/tributario.md`, con 52 artículos verificados del Código Tributario (DL 830), la Ley de IVA (DL 825) y la Ley de Renta (DL 824) —catálogo de infracciones y delitos del art. 97 CT, requisito de procesabilidad exclusiva del Director del SII (art. 162 CT), atenuantes/agravantes tributarias (arts. 111 y 111 bis CT), prescripción tributaria (arts. 200–202 CT), crédito fiscal IVA y justificación de inversiones de la Ley de Renta (art. 70)—, e integra sus citas verificadas a `references/forense-financiero.md` y `references/calculo-penas.md`. Incorpora a `scripts/curar_norma.py` la resolución automática de idNorma (`--resolver`, con registro local de normas verificadas y resolución en línea para normas tipo «Ley») y la descarga con verificación de hash (`--descargar`), además de corregir dos defectos descubiertos en esta curatoría: el disambiguador «(DEL ART. N)» que la BCN antepone a los artículos internos de los decretos leyes con estructura de Doble Articulado (Código Tributario, Ley de Renta), y un error de normalización que eliminaba toda letra «N» de las consultas del registro de normas. Suite ampliada a 54 pruebas.

**Versión 4.1** — Julio de 2026. Construye `examples/ejemplo-estafa-empresarial.md`, el caso pedagógico ficticio anunciado desde la versión 3.0, con lo que se completa el catálogo íntegro de la skill (todos los archivos de `references/`, `assets/templates/`, `scripts/` y `examples/` pasan a **[disponible]**). El ejemplo recorre las quince fases, aplica el catálogo verificado de las Leyes 21.595/20.393/19.913 con sus consecuencias reales (incluida la conclusión de que un caso de estafa/administración desleal corriente no activa el sistema especial de la Ley 21.595) y ejecuta con parámetros de trabajo los motores `prescripcion.py` y `estrategia_litigio.py`, incorporando su salida real al informe.

**Versión 4.0** — Julio de 2026. Completa la construcción de los módulos de referencia anunciados desde la versión 3.0 e incorpora los motores deterministas al paquete. Nuevos disponibles: `references/metodologia-detallada.md` (quince fases), `references/prueba-digital.md` (Ley 21.459 verificada; depurados dos roles de la Corte Suprema y un oficio FN no verificables del borrador 3.0), `references/calculo-penas.md` (algoritmo común sobre arts. 50–78 bis CP verificados y sistema especial de la Ley 21.595 verificado) y `references/leyes-especiales.md` (177 artículos de las Leyes 21.595, 20.393, 19.913, 21.459 y 20.000, curatoría del 2026-07-07 con registro de hashes; revalidación al 2027-01-07). Se incorporan `scripts/prescripcion.py` (calculadora de prescripción, 24 pruebas) y la versión corregida de `scripts/curar_norma.py` (Doble Articulado y numeración ordinal). Publicada junto al repositorio `estrategia-litigio-penal` v2.0.0. Pendiente: `examples/ejemplo-estafa-empresarial.md` (paso 6 del plan de trabajo).

## Linaje local (v3.6 → v3.11)

## v3.11 — 11 de julio de 2026

**Curación normativa completa (subsanación del defecto N° 1 de las versiones 3.7 a 3.10).** Levantado el bloqueo de red sobre LeyChile (el servicio `obtxml opt=7` responde desde `nuevo.leychile.cl`), se descargaron los seis XML oficiales y se ejecutó la curación pendiente, en el orden dispuesto por el titular:

1. **CP arts. 292 a 295 (Ley 21.577)**: siete artículos (292, 293, 293 bis, 294, 294 bis, 294 ter y 295, § 10 «De las asociaciones delictivas y criminales», versión de artículos 2023-06-15) curados con `curar_norma.py` e insertados en `marco-legal.md`, con nueva subsección 2.2 de perímetro y asiento en el registro de curatoría. El art. 295 bis no consta en el XML oficial vigente y así se declara. Queda desbloqueado el desarrollo de la Candidata C-015 (arista/concierto).
2. **Ley 21.459** (idNorma 1177743): catálogo de los arts. 1° a 8°, fraude informático (art. 7°) y régimen procesal (arts. 12 a 14) convertidos de [C] a **[V]**. Hallazgos incorporados: reforma del art. 2° (versión 2024-04-08) que exige superar barreras técnicas y crea la exención por investigación de vulnerabilidades ante la ANCI; **derogación del art. 9°** (versión 2024-09-04) y del art. 16.
3. **Ley 18.216** (idNorma 29636): sección 3 de `calculo-penas.md` convertida a **[V]**, con umbrales verificados por artículo (arts. 4, 8, 11, 15, 15 bis y 34), precisión de la expulsión (extensión al residente legal por la Ley 21.325, tope de cinco años, prohibición de regreso decenal) y constancia del catálogo de exclusiones del art. 1° en su versión 2025-02-12, que comprende el art. 293 CP.
4. **Ley 19.913** (idNorma 219119, versión de norma 2026-05-30; art. 27 en versión 2023-11-23): **figura culposa localizada** (inciso cuarto del art. 27, rebaja de dos grados) y convertida a [V]; **autolavado zanjado por texto expreso** del propio art. 27 (antes «pendiente de verificación»), con reserva de irretroactividad para hechos anteriores; tope de pena por referencia al delito base consignado; catálogo de la letra a) transcrito en lo relevante, incluido el Título I de la Ley 21.459 y el § 10 del Título VI del Libro II CP. La modificación de norma de 2026 no altera los arts. 27 y 28.
5. **Ley 20.393** (idNorma 1008668, versión 2023-08-17): cotejo íntegro de los arts. 3, 4, 6 a 15, 17, 18, 18 bis, 19 bis y 20 bis contra el XML. Las afirmaciones del módulo resultaron conformes (multa siempre, art. 15; publicación del extracto siempre, arts. 13 y 14 inciso final; supervisión de seis meses a dos años, art. 11 bis; extinción restringida, art. 9; cautelar del art. 20 bis; solidaridad por reorganización, arts. 18 y 18 bis); no hubo correcciones que efectuar.
6. **Ley 21.595** (idNorma 1195119): revalidación contra la versión de norma **2025-09-29**. Hallazgo material: los **arts. 2 y 3 fueron reformados** con vigencia de artículo al 29-09-2025 (incorporación de numerales referidos a la Ley Marco de Autorizaciones Sectoriales; el art. 2 N° 2 comprende hoy también el inciso cuarto del art. 8 ter CT); las categorías del módulo fueron actualizadas con advertencia de vigencia temporal. Las disposiciones «transitorias» [C] de la sección 0.2 se resolvieron: la ley no las contiene como articulado separado; la vigencia diferida del régimen RPPJ consta en el art. 60 N° 1 (**desde el 01-09-2024**) y el derecho intertemporal en los arts. 66 a 68, incluida la prohibición expresa de fraccionamiento (art. 67), todo [V]. Se incorporaron además la cooperación eficaz del art. 63 (tratamiento como art. 14 circunstancia 1.ª con rebaja de un grado adicional), la regla de colusión del art. 65 y la constancia de derogación del art. 64.

**Método declarado.** La curación no es reconstrucción de memoria: cada conversión [C] → [V] proviene de cotejo contra el texto del XML oficial descargado en la sesión y procesado con el motor del repositorio. Los tres módulos afectados (`leyes-especiales.md`, `calculo-penas.md`, `prueba-digital.md`) declaran fecha y fuente en sus secciones de estado; `marco-legal.md` registra la inserción en su registro de curatoría.

**Sincronización.** `SKILL.md` (versión 3.11, nota de triage y descripción de `marco-legal.md` actualizadas), `index-maestro.json` y este registro quedan consistentes conforme a R-4.

### Defectos que subsisten

1. Texto de C-001 a C-011 y de las tres entradas pendientes de las versiones 3.1 a 3.4: perdido salvo reingreso por el titular desde otra exportación o sesión de origen.
2. `errata-acta-auditoria.md` en estado de reconstrucción de síntesis; pendiente examinar si la exportación local de la v3.10 contiene su tenor literal.
3. `fiscalizacion-algoritmica.md` no gradúa a 1.0 sin segunda fuente.
4. Revalidación de `marco-legal.md`: enero de 2027; la de `leyes-especiales.md`, `calculo-penas.md` y `prueba-digital.md`: julio de 2027 o ante noticia de reforma, lo que ocurra primero.
5. Ubicación y desarrollo de la Candidata C-015 (arista/concierto): ahora desbloqueada por la incorporación de los arts. 292 y siguientes; pendiente de decisión del titular.
6. La numeración mayor (2.0.0) diferida en la v3.7 queda desbloqueada en cuanto a la curación normativa; su publicación permanece sujeta a la resolución de los defectos 1 y 2.

## v3.10 — 10 de julio de 2026

**Corrección de manifiesto: reversión de la declaración de pérdida total de `contraindicaciones.md` (v3.9).** La v3.9 declaró que el texto de las catorce entradas C-001 a C-014 era irrecuperable. La constatación era exacta respecto de C-001 a C-011, pero errónea respecto de C-012 a C-014: una exportación local de conversaciones aportada por el titular contiene el texto **verbatim** del fragmento de inserción de la sesión de 9 de julio de 2026 (Atlas de Economías Ilícitas v1.0.0), sin el truncamiento que la v3.9 le había atribuido por prudencia epistémica ante la falta de la fuente.

Conforme a la sección 15.3.a del `SKILL.md` — corrección de manifiesto, aplicable de inmediato y sin aprobación previa por tratarse de constatación y no de decisión —, se sustituyó `references/contraindicaciones.md` por la versión que restituye C-012, C-013 y C-014 con marca **[R-V]** (recuperación verbatim), conserva C-001 a C-011 en estado `perdido`, y preserva la nota "Candidata C-015" sobre la distinción entre arista y concierto, remitida al futuro módulo de razonamiento probatorio en materia de organización criminal.

El índice maestro fue actualizado: nuevo `sha256` de `contraindicaciones.md` (8.150 bytes; el anterior, de 2.030 bytes, correspondía a la versión de pérdida total) y campo `origen` reformulado para declarar la reversión y su fuente. `verificar-integridad.sh` confirma conformidad de hash tras la corrección.

**Advertencia de procedencia.** El texto recuperado no proviene de reconstrucción de memoria ni de síntesis: es transcripción localizada de la sesión de origen. No se alteró una sola palabra de la regla, el fundamento, el alcance, la detección, la excepción ni la vigencia de C-012, C-013 y C-014 respecto de lo que consta en esa transcripción.

### Defectos que subsisten

1. Curación automatizada pendiente de las Leyes 21.595, 20.393, 19.913, 21.459 y 18.216, y de los arts. 292 y siguientes del CP (bloqueo de entorno declarado en v3.9).
2. Texto de C-001 a C-011 y de las tres entradas pendientes de las versiones 3.1 a 3.4: perdido salvo reingreso por el titular desde otra exportación o sesión de origen.
3. `errata-acta-auditoria.md` en estado de reconstrucción de síntesis (tenor literal de las ocho erratas no recuperado); no se ha verificado si la exportación local que permitió esta corrección contiene también su texto — pendiente de examen.
4. `fiscalizacion-algoritmica.md` no gradúa a 1.0 sin segunda fuente.
5. Revalidación de `marco-legal.md`: enero de 2027.
6. Ubicación pendiente de la Candidata C-015 (arista/concierto) en la arquitectura del repositorio; su desarrollo depende de la incorporación de los arts. 292 y siguientes del CP a `marco-legal.md` (defecto N° 1).

## v3.9 — 10 de julio de 2026

**Sesión de recuperación de los cinco módulos `no_propagado` (subsanación parcial del defecto N° 2 de la v3.8).** Los cinco módulos fueron reconstruidos desde las transcripciones de las sesiones de 9-10 de julio de 2026 e instalados con **disciplina de procedencia declarada por sección**: [R-VERBATIM] para texto recuperado literal, [R-SÍNTESIS] para contenido reconstruido desde resumen o fragmentos. Resultado por módulo:

- `razonamiento-probatorio.md` — fidelidad alta: secciones 1 y 2 (catálogo de falacias 2.1 a 2.4) recuperadas verbatim; secciones 3 y 4 en síntesis.
- `decision-estrategica.md` — fidelidad alta: encabezado y regla rectora verbatim; secciones 2 a 4 en síntesis con respaldo en las entradas A-002, A-003, A-005 y A-006 de `aprendizajes.md`.
- `fiscalizacion-algoritmica.md` — v0.2-reconstruida; mantiene la cláusula de no graduación sin segunda fuente; corrección del bucle de retroalimentación recuperada verbatim.
- `errata-acta-auditoria.md` — reconstrucción de síntesis; el tenor literal de las ocho erratas numeradas no fue recuperado y así se declara.
- `contraindicaciones.md` — **pérdida documentada**: no fue posible recuperar el texto de C-001 a C-014, incluido el fragmento C-012 a C-014 que el índice daba por pendiente de integración. Los identificadores quedan quemados; la primera entrada nueva será C-015.

Los hashes originales son irrecuperables; el índice maestro registra los hashes de las reconstrucciones con campo `origen` explícito. Remedio superior disponible: reingreso de los textos originales desde exportación del titular, conservando identificadores.

**Curación de los arts. 292 y siguientes del Código Penal (defecto N° 3): BLOQUEADA en este entorno.** El dominio leychile.cl no integra la lista de red permitida (denegación verificada: `x-deny-reason: host_not_allowed`) y no consta XML cargado. `curar_norma.py` está operativo; falta el insumo. Remedios: (a) cargar el XML oficial (idNorma 1984, opt=7) a la sesión, o (b) incorporar www.leychile.cl a los dominios de red permitidos.

### Defectos que subsisten

1. Curación automatizada pendiente de las Leyes 21.595, 20.393, 19.913, 21.459 y 18.216, y de los arts. 292 y siguientes del CP (bloqueo de entorno declarado supra).
2. Texto original de C-001 a C-014 y de las tres entradas pendientes de las versiones 3.1 a 3.4: perdido salvo reingreso por el titular.
3. `errata-acta-auditoria.md` en estado de reconstrucción de síntesis (tenor literal de las ocho erratas no recuperado).
4. `fiscalizacion-algoritmica.md` no gradúa a 1.0 sin segunda fuente.
5. Revalidación de `marco-legal.md`: enero de 2027.

## v3.8 — 10 de julio de 2026

**Verificación normativa de la Ley 21.595 y de la Ley 19.913 (art. 27).** Las citas del módulo `leyes-especiales.md` y de la sección 4 de `calculo-penas.md` fueron cotejadas contra la exportación oficial de LeyChile (idNorma 1195119, versión única de 17-AGO-2023, documento generado el 13-03-2024) y contra el catálogo oficial de la UAF. Las citas verificadas llevan etiqueta **[V]** con fuente y fecha; subsisten en **[C]** la Ley 21.459 (contenido de los arts. 1° a 8°), la Ley 18.216, la figura culposa del art. 27 de la Ley 19.913 (ubicación exacta) y las disposiciones transitorias de la Ley 21.595.

**Dos errores de la v3.7 corregidos** (entrada `A-014`): el lavado de activos integra la cuarta categoría (art. 4), no la tercera; y el catálogo de sustitutivas propias del art. 20 es remisión condicional, reclusión parcial en domicilio y reclusión parcial en establecimiento especial — no incluye la libertad vigilada intensiva. Se precisó además el carácter categórico de la exclusión del art. 12 y el doble plano del art. 17 (muy calificadas alteran el grado) y del art. 18 (simples operan dentro del grado).

**Limpieza menor**: suprimida del listado de módulos la línea de `ejemplo-estafa-empresarial.md`, prometido y nunca construido.

### Defectos que subsisten

1. Curación automatizada pendiente: `curar_norma.py` no se ha ejecutado sobre las Leyes 21.595, 20.393, 19.913, 21.459 y 18.216 (la verificación de esta versión es documental, no automatizada); modificaciones posteriores a marzo de 2024 no quedan descartadas.
2. Cinco módulos `no_propagado` sin texto en esta instalación.
3. `marco-legal.md` no comprende los artículos 292 y siguientes del Código Penal (Ley 21.577); su fecha de revalidación es enero de 2027.
4. No consta el texto de `C-001` a `C-011` ni de las tres entradas pendientes de las versiones 3.1 a 3.4.

## v3.7 — 10 de julio de 2026

**Subsanación del defecto N° 1 de la v3.6.** Se construyeron e indexaron los cuatro módulos ausentes: `references/metodologia-detallada.md`, `references/prueba-digital.md`, `references/calculo-penas.md` y `references/leyes-especiales.md`. Remedio elegido por el titular (cierre de `A-011`): construcción, no supresión de filas.

**Estado de verificación normativa.** Las citas del Código Penal y del Código Procesal Penal contenidas en los módulos nuevos son verificables contra `marco-legal.md` (curado, idNorma 1984 y 176595). Las citas de las Leyes 21.595, 20.393, 19.913, 21.459 y 18.216 se consignan en estado **[C] — por corroborar** y así lo declaran los propios módulos en su sección 0. **Tarea abierta**: curación de dichas leyes mediante `scripts/curar_norma.py` contra el XML oficial de LeyChile (dominio no accesible desde el entorno de construcción de esta versión).

**Tabla de triage (sección 5).** Suprimidos los cuatro marcadores **NO INSTALADO**; las filas remiten a los módulos ya instalados.

### Defectos que subsisten de la v3.6

1. ~~Módulos `metodologia-detallada.md`, `prueba-digital.md`, `calculo-penas.md` y `leyes-especiales.md` inexistentes.~~ **Subsanado en esta versión**, con la reserva de curación normativa antes indicada.
2. Cinco módulos figuran `no_propagado`: `decision-estrategica.md`, `razonamiento-probatorio.md`, `contraindicaciones.md`, `fiscalizacion-algoritmica.md`, `errata-acta-auditoria.md`. Su texto no consta en esta instalación.
3. `marco-legal.md` no comprende los artículos 292 y siguientes del Código Penal (asociación delictiva y criminal, Ley 21.577). Requiere nueva pasada de `curar_norma.py`.
4. No consta el texto de las entradas `C-001` a `C-011` de `contraindicaciones.md` ni de las tres entradas pendientes desde las versiones 3.1 a 3.4.

**El impedimento de publicación de una versión 2.0.0 fijado en la v3.6 queda levantado en cuanto a su causa (defecto N° 1); la numeración mayor queda no obstante diferida hasta la curación normativa de los módulos nuevos y la resolución de los defectos 2 a 4.**

## v3.6 — 9 de julio de 2026

**Cláusula de Integridad y Propagación (sección 0 del `SKILL.md`).** Pasos 0 a 3 y reglas R-1 a R-5. Ninguna sesión presume instalado lo construido en otra.

**Corrección del Protocolo de Cierre y Aprendizaje (sección 15.3, numeral 3).** Se distingue la corrección de manifiesto —que se aplica de inmediato y se informa— del cambio de criterio, que requiere aprobación expresa. La fórmula anterior, «nada se incorpora sin su aprobación», mantuvo congeladas ocho lecciones legítimas.

**Formato de `references/aprendizajes.md`.** Se incorporan los campos `ID` (identificador estable `A-0NN`, jamás reasignado) y `Estado` (`propuesto` | `aprobado` | `rechazado` | `derogado`), y el campo `Naturaleza`. Se proscribe la numeración ordinal en catálogos acumulativos.

**Entradas `A-001` a `A-013`.** Doce entradas nuevas, aprobadas por el titular. `A-011` queda aprobada en cuanto a la constatación, con el remedio pendiente de decisión.

**`index-maestro.json` y `verificar-integridad.sh`.** Mecanismo de integridad inexistente hasta esta versión. El índice declara veintiún archivos: doce instalados, cinco `no_propagado` y cuatro `ausente`.

**Tabla de triage (sección 5).** Cuatro filas marcadas **NO INSTALADO**. Medida interina; el remedio —construir o suprimir— permanece pendiente.

### Defectos constatados y no subsanados en esta versión

1. `references/metodologia-detallada.md`, `prueba-digital.md`, `calculo-penas.md` y `leyes-especiales.md` no existen. La descripción de la skill promete competencia sobre las Leyes 21.595, 20.393, 19.913 y 21.459, cuyo texto no posee.
2. Cinco módulos figuran `no_propagado`: `decision-estrategica.md`, `razonamiento-probatorio.md`, `contraindicaciones.md`, `fiscalizacion-algoritmica.md`, `errata-acta-auditoria.md`.
3. `marco-legal.md` no comprende los artículos 292 y siguientes del Código Penal.
4. No consta el texto de las entradas `C-001` a `C-011` de `contraindicaciones.md` ni de las tres entradas pendientes desde las versiones 3.1 a 3.4.

**Ninguna versión 2.0.0 ni superior se publica mientras subsista el defecto N° 1.**
