# Esquemas argumentales — Reconstrucción y ataque de la cadena inferencial

> Módulo de referencia condicional. Cárgalo cuando debas reconstruir la estructura del argumento de cargo (o del propio), localizar las máximas de la experiencia que operan implícitas en la acusación o en la sentencia, preparar alegato de clausura, o fundar un recurso de nulidad por defecto de fundamentación. Se carga junto a `references/razonamiento-probatorio.md` cuando el argumento atacado incorpore cifras o agregue indicios.

## 0. Estado del módulo, procedencia y advertencia de estatuto

Este módulo adapta el esquema analítico del argumento propuesto por Stephen Toulmin —datos, afirmación, garantía, respaldo, modalizador y refutación— como **instrumento interno de control del razonamiento probatorio**. El esquema no es categoría del derecho chileno ni fuente de obligación alguna: es una herramienta de disección cuyo rendimiento es crítico, no constructivo. Su utilidad consiste en obligar a explicitar el enunciado general que un argumento mantiene tácito, y en señalar el punto donde ese enunciado debe acreditarse o se desploma.

**Procedencia bibliográfica**: las obras de Toulmin y sus fechas de edición **no han sido verificadas** contra catálogo bibliográfico en esta curatoría, y ninguna cita textual suya se tiene por auténtica. Mientras subsista esta marca, el módulo no atribuye frases entrecomilladas al autor ni consigna años de publicación. `[PENDIENTE-BIBLIOGRÁFICO]`

**Advertencia sobre representaciones corrientes del esquema.** Las versiones divulgativas suelen disponer los seis elementos como una cadena lineal —dato → afirmación → respaldo → modalizador → refutación—. La disposición es incorrecta y destruye el único elemento con rendimiento forense: el **respaldo sostiene a la garantía**, no a la afirmación; el modalizador y la refutación penden de la afirmación. Quien trabaje con la figura lineal perderá exactamente aquello que este módulo persigue.

**Regla de traducción** (concordante con `razonamiento-probatorio.md`): el esquema se emplea hacia adentro y se traduce hacia afuera. Ningún escrito, informe o alegato exhibe el diagrama, su vocabulario ni la cita del autor. Véase la contraindicación **C-016**.

## 1. Anclaje normativo

El esquema no tendría rendimiento alguno si no existiese una norma que obligue al tribunal a exhibir su razonamiento. Esa norma existe y consta curada en `references/marco-legal.md`:

- **Art. 297 CPP** (sección 3.6). Inciso primero: la libertad de apreciación no autoriza a contradecir «los principios de la lógica, las máximas de la experiencia y los conocimientos científicamente afianzados». Inciso tercero: la fundamentación «deberá permitir la **reproducción del razonamiento** utilizado para alcanzar las conclusiones a que llegare la sentencia».
- **Art. 342, letras c) y d), CPP** (sección 3.10). La letra c) exige la exposición «clara, lógica y completa» de los hechos que se dieren por probados y de la valoración de los medios de prueba «de acuerdo con lo dispuesto en el artículo 297»; la letra d), las razones legales o doctrinales de la calificación.
- **Art. 374, letras e) y f), CPP** (sección 3.8). Motivo absoluto de nulidad por omisión de los requisitos del art. 342 letras c), d) o e), y por infracción del art. 341.
- **Art. 341 CPP** (sección 3.10). Congruencia entre acusación y sentencia: la condena no puede exceder el contenido de la acusación.
- **Art. 340 CPP** (sección 3.6). Estándar de convicción, que opera como modalizador del sistema y no admite reducción numérica (véase `razonamiento-probatorio.md`, 2.4).

De la conjunción del art. 297 inciso tercero con el art. 342 letra c) se desprende la premisa operativa de este módulo: **si el razonamiento debe poder reproducirse, debe poder reconstruirse; y si puede reconstruirse, puede exhibirse su eslabón faltante**. El esquema argumental es el procedimiento de esa reconstrucción.

## 2. Los seis elementos y su traducción al proceso penal chileno

| Elemento | Qué es | Su correlato en la causa | Dónde se ataca |
|---|---|---|---|
| **Dato** | El antecedente del que se parte | Medio de prueba rendido o antecedente de la carpeta | Licitud, autenticidad, cadena de custodia, suficiencia |
| **Afirmación** | La conclusión que se pretende justificar | Proposición fáctica de la acusación | Congruencia con la acusación (art. 341); exceso respecto del dato |
| **Garantía** | El enunciado general que autoriza el paso del dato a la afirmación | **Máxima de la experiencia** (art. 297 inc. 1°) | Su carácter implícito; su falsedad; su alcance excesivo |
| **Respaldo** | Lo que sostiene la garantía | Pericia, estudio, regularidad acreditada, conocimiento científicamente afianzado | **Su ausencia**: la máxima invocada sin respaldo alguno |
| **Modalizador** | La fuerza atribuida a la conclusión | Estándar del art. 340 CPP | Afirmación categórica sostenida en inferencia graduada |
| **Refutación** | Condiciones en que la afirmación no valdría | Hipótesis alternativa (ACH, fase 6) | Su omisión: el fallo que no se hace cargo de la prueba desestimada (art. 297 inc. 2°) |

La columna decisiva es la tercera. La acusación casi nunca enuncia su garantía: la supone compartida. El trabajo consiste en escribirla por ella, en la forma general que necesariamente tiene, y en exhibir entonces lo que esa forma general cuesta.

## 3. Protocolo de reconstrucción

Se aplica por **proposición fáctica controvertida**, no por delito ni por imputado. Usa la plantilla `assets/templates/ficha-toulmin.md`.

1. **Aislar la afirmación.** Transcribe la proposición fáctica tal como la formula la acusación —o el considerando, si se trabaja sobre sentencia—, sin resumirla ni mejorarla. Reformularla en términos propios es el error inicial más frecuente: se refuta entonces una tesis que nadie sostuvo.
2. **Inventariar los datos.** Identifica qué antecedentes concretos se invocan para esa proposición y solo para ella. Un mismo medio de prueba puede sostener varias afirmaciones con garantías distintas; se trata por separado en cada ficha.
3. **Enunciar la garantía implícita.** Formula el enunciado general que haría válido el paso, en la forma «siempre que ocurre X, ocurre Y» o «quien hace X, normalmente sabe o quiere Z». Si no logras formularlo, el salto probablemente no existe como inferencia sino como afirmación desnuda: consígnalo, porque es un hallazgo y no un fracaso del método.
4. **Interrogar el respaldo.** Pregunta qué sostiene esa generalización: ¿una pericia?, ¿una regularidad estadística acreditada?, ¿un conocimiento científicamente afianzado?, ¿o únicamente la plausibilidad intuitiva de quien la enuncia? La respuesta más frecuente es la última, y es el punto de ataque.
5. **Medir el modalizador.** Compara la fuerza real que la garantía respaldada permite atribuir a la conclusión con la fuerza que la acusación le atribuye. La brecha entre ambas es materia de alegato.
6. **Construir la refutación.** Enuncia las condiciones bajo las cuales los mismos datos son compatibles con la inocencia o con una calificación distinta. Esta columna es insumo directo de la hipótesis alternativa de la fase 6 y de la teoría del caso dual de la fase 12.
7. **Aplicar el método al propio argumento.** La ficha se construye primero sobre la tesis propia y después sobre la ajena. Una tesis propia cuya garantía no soporta el paso 4 no se lleva a audiencia: se corrige o se abandona.

## 4. Catálogo de garantías habituales en delitos económicos

Las siguientes generalizaciones operan tácitamente en la mayoría de las acusaciones por delitos económicos. Ninguna es falsa por definición; todas exigen respaldo que rara vez se rinde. Se consignan con el respaldo que las habilitaría y con el modo de ataque correspondiente.

**G-1. «Quien firma un documento conoce su contenido.»**
Respaldo exigible: acreditación del proceso concreto de suscripción —volumen documental, delegación de firma, existencia de firma electrónica compartida, práctica interna de visación previa—. Ataque: el carácter rutinario o delegado de la suscripción destruye la generalización sin necesidad de negar la firma.

**G-2. «Quien ocupa el cargo conoce las operaciones relevantes de la sociedad.»**
Respaldo exigible: estructura efectiva de reporte, actas que acrediten que la operación se presentó al órgano, flujo real de información. Ataque: la inferencia de conocimiento desde el cargo es, en rigor, una imputación por posición, vecina de la responsabilidad objetiva. Articula con `leyes-especiales.md` cuando se invoque el modelo de prevención de la Ley 20.393.

**G-3. «El incremento patrimonial no justificado proviene de la actividad investigada.»**
Respaldo exigible: descarte documentado de fuentes lícitas alternativas y determinación del período de imputación. Ataque: la garantía invierte materialmente la carga de la prueba. Articula con `tributario.md` (art. 70 LIR) y con `forense-financiero.md`, donde la distinción elusión/evasión/lavado es previa a toda inferencia de origen ilícito.

**G-4. «La proximidad temporal entre operaciones revela concierto.»**
Respaldo exigible: tasa base de coocurrencia en el giro respectivo; descarte de causa común lícita (ciclo de pagos, vencimiento tributario, estacionalidad). Ataque: es la forma patrimonial de la adición indebida de indicios condicionalmente dependientes (`razonamiento-probatorio.md`, 2.3).

**G-5. «La complejidad de la estructura societaria revela ánimo de ocultamiento.»**
Respaldo exigible: comparación con estructuras corrientes del sector; acreditación de que la complejidad carece de función tributaria, regulatoria o de financiamiento legítima. Ataque: la garantía convierte una decisión de organización empresarial en indicio de dolo sin término de comparación.

**G-6. «Quien se beneficia del delito participó en él.»**
Respaldo exigible: ninguno disponible en términos generales; el beneficio es compatible con la ignorancia. Ataque: la garantía confunde el provecho con la intervención y, aplicada a personas jurídicas, elude los criterios de atribución de la Ley 20.393.

**G-7. «Quien usa un dispositivo es su titular registrado.»**
Respaldo exigible: acreditación de uso exclusivo —custodia física, credenciales no compartidas, ausencia de acceso remoto—. Ataque: remite a `prueba-digital.md`; la atribución de autoría de un mensaje exige más que la titularidad de la cuenta o del equipo.

**G-8. «El silencio o la negativa a declarar sugiere ocultamiento.»**
Respaldo exigible: ninguno admisible. La garantía es **normativamente inadmisible**: contradice el derecho a guardar silencio del art. 93 CPP (sección 3.9) y la presunción de inocencia. Ataque: no se discute su plausibilidad, se denuncia su improcedencia.

El catálogo es abierto. Toda garantía nueva que se identifique en una causa y resulte de rendimiento general se propone como entrada G-NN, conforme al Protocolo de Cierre y Aprendizaje (sección 15.3 del SKILL.md), con identificadores estables y sin reasignación.

## 5. Rendimiento por etapa procesal

- **Investigación.** La ficha identifica qué diligencia falta: no la que confirmaría la afirmación, sino la que acreditaría o destruiría la garantía. Esta es su aplicación de mayor valor, porque orienta la fase 11 hacia el eslabón débil y no hacia el dato abundante.
- **Audiencia de preparación.** La garantía inadmisible —G-8 es el caso puro— y el dato ilícito se atacan por vías distintas: aquélla no es objeto de exclusión probatoria del art. 276 CPP, sino materia de alegato. Confundirlas desperdicia la oportunidad procesal. Véase `audiencia-preparacion.md`.
- **Juicio oral.** El contraexamen se ordena por garantías, no por testigos: cada pregunta persigue el respaldo de una generalización determinada. El alegato de clausura expone la cadena reconstruida y señala el eslabón sin respaldo, en lenguaje de máximas de la experiencia.
- **Recurso de nulidad.** Es aquí donde el módulo rinde su producto más directo. La sentencia que afirma un hecho sin exhibir la máxima que autoriza el paso desde el medio de prueba no permite «la reproducción del razonamiento» (art. 297 inc. 3°) y omite la exposición «clara, lógica y completa» exigida por el art. 342 letra c), con lo que se configura el motivo absoluto del art. 374 letra e). La ficha de reconstrucción es el borrador material del capítulo de nulidad: muestra, proposición por proposición, dónde el fallo calló.

## 6. Límites del esquema

Tres límites deben declararse antes de emplearlo, y se consignan por honestidad metodológica y no por cortesía:

1. **No es criterio de corrección.** El esquema muestra la estructura de un argumento; no dice cuál es verdadero. Una cadena impecablemente articulada puede ser falsa, y una conclusión correcta puede estar mal expuesta.
2. **No sustituye la dogmática.** La calificación jurídica —art. 342 letra d)— se decide con los criterios del tipo penal, no con el análisis de la inferencia. El esquema opera sobre la premisa fáctica, no sobre la norma.
3. **Su exhaustividad es onerosa.** Aplicado a toda proposición de una carpeta voluminosa produce decenas de fichas inútiles. Se reserva para las proposiciones fácticas que, de caer, arrastran la imputación: aquellas que la fase 6 identifique como diagnósticas entre hipótesis.

## 7. Cierre operativo

El esquema argumental no agrega poder de convicción: lo sustrae al adversario. Su producto típico no es una tesis nueva, sino la exhibición de que la tesis de cargo descansa en un enunciado general que nadie enunció y que nadie acreditó. Ese hallazgo se traduce siempre, antes de ingresar a un escrito, al lenguaje del art. 297 CPP y a las categorías epistémicas del repositorio (acreditado / indiciario / hipótesis), conforme a la contraindicación C-016.
