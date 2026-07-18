# Cálculo de penas y marco punitivo

> **Estado del módulo**: OPERATIVO. El componente de derecho común (Código
> Penal) —arts. 11–13, 19–24 ter y 50–78 bis CP— consta **verificado** en
> `references/marco-legal.md` (curatoría del 2026-07-06, XML oficial LeyChile,
> idNorma 1984). El sistema especial de la Ley 21.595 consta **verificado** en
> `references/leyes-especiales.md` (curatoría del 2026-07-07, idNorma 1195119,
> arts. 1–47 y 60–68). La Ley 18.216 —solo supletoria en delitos económicos
> conforme al art. 19 de la Ley 21.595— consta **verificada** (cotejo del
> 2026-07-11 contra el XML oficial, idNorma 29636: umbrales por artículo,
> expulsión post-Ley 21.325 y catálogo de exclusiones del art. 1° en su
> versión 2025-02-12; sección VII). Incorporada en la reconciliación v4.3
> desde el linaje local v3.11.

Carga este archivo cuando el análisis requiera estimar pena concreta, evaluar
circunstancias modificatorias, pronunciarse sobre concursos o dimensionar el
marco punitivo de una imputación. El producto de este módulo es siempre un
**rango estimativo** con identificación de los factores que lo mueven; jamás
una aserción de pena exacta, que corresponde a la discrecionalidad judicial
reglada.

---

## I. Regla de anclaje normativo

1. Todo artículo del Código Penal citado en este módulo se coteja contra su
   texto verificado en `references/marco-legal.md`, sección 2.2 (arts. 50–78) y
   concordantes. No se transcribe aquí el texto legal: se remite.
2. La **tabla demostrativa del art. 56 CP** (duración de los grados de las penas
   divisibles) consta en el XML oficial como **imagen embebida** (no como texto),
   lo que explicaba su ausencia del extracto. El **cotejo único fue practicado el
   2026-07-17** mediante extracción del binario oficial (`Art56CP.jpeg`, SHA-256
   registrado) y verificación visual: la tabla de la sección III **coincide
   íntegramente** con la fuente. La transcripción completa de las cinco filas
   oficiales consta en `marco-legal.md`, sección 2.2, art. 56, nota de curatoría.
3. El sistema **especial** de determinación de penas para delitos económicos
   (Ley 21.595) se aplica con preferencia al régimen común cuando el hecho es
   posterior al 17-08-2023 y califica como delito económico. Su mecánica se
   describe en la sección VI sobre el texto verificado de
   `references/leyes-especiales.md`.

---

## II. Algoritmo general de determinación (régimen común)

La determinación se ejecuta en seis pasos secuenciales. En cada paso, consigna
la norma aplicada y el efecto sobre el marco.

**Paso 1 — Pena señalada por la ley (pena en abstracto).** Identifica la pena
asignada al delito consumado para el autor (art. 50 CP). Si la pena consta de
dos o más grados, cada grado es una pena distinta (arts. 57 y 58 CP).

**Paso 2 — Iter criminis y participación.** Aplica las rebajas de los
arts. 51 a 54 CP sobre las escalas graduales del art. 59 CP, conforme a las
reglas del art. 61 CP:

| Grado de desarrollo / participación | Autor | Cómplice | Encubridor |
|---|---|---|---|
| Consumado | pena de la ley (art. 50) | −1 grado (art. 51) | −2 grados (art. 52) |
| Frustrado | −1 grado (art. 51) | −2 grados (art. 52) | −3 grados (art. 53) |
| Tentativa | −2 grados (art. 52) | −3 grados (art. 53) | −4 grados (art. 54) |

Excepciones: figuras especialmente penadas por la ley (art. 55 CP) y los
encubridores del art. 17 N° 3 circunstancia 1ª y N° 4 (art. 52 incisos 2° y 3°
CP). Si falta grado inferior en la escala, se impone la multa (arts. 61 regla
5ª y 77 inc. 3° CP); si falta grado superior, presidio perpetuo —o perpetuo
calificado en la escala N° 1— (art. 77 inc. 2° CP).

**Paso 3 — Circunstancias modificatorias.** Califica las atenuantes (art. 11
CP), agravantes (art. 12 CP) y la mixta de parentesco (art. 13 CP), todas
verificadas en `marco-legal.md`. Filtra primero: (a) las agravantes que son
elemento del tipo o inherentes al delito no agravan (art. 63 CP); (b) las
circunstancias personales solo afectan a aquellos en quienes concurren, y las
materiales solo a quienes las conocieron (art. 64 CP: comunicabilidad).

**Paso 4 — Efecto de las circunstancias según la estructura de la pena.**
Aplica la regla que corresponda a la estructura del marco:

| Estructura de la pena señalada | Sin modificatorias | 1 atenuante / 0 agravante | 1 agravante / 0 atenuante | 2+ atenuantes / 0 agravante | 2+ agravantes / 0 atenuante | Mixtas |
|---|---|---|---|---|---|---|
| Una indivisible (art. 65) | se aplica tal cual | se aplica tal cual | se aplica tal cual (no agrava) | facultativo: −1 o −2 grados | se aplica tal cual | — |
| Dos indivisibles (art. 66) | cualquiera de sus grados | grado mínimo | grado máximo | facultativo: −1 o −2 grados bajo el mínimo | grado máximo | compensación racional |
| Un grado de divisible (art. 67) | toda su extensión | mínimum | máximum | facultativo: −1 o −2 grados | facultativo: +1 grado | compensación racional |
| Dos o más grados (art. 68) | toda su extensión | excluye grado máximo | excluye grado mínimo | facultativo: −1, −2 o −3 grados bajo el mínimo | facultativo: +1 grado sobre el máximo | compensación racional |

Reglas complementarias verificadas: **art. 68 bis** (una sola atenuante muy
calificada: facultad de rebajar un grado); **art. 68 ter** (reincidencia de los
numerales 14°, 15° y 16° del art. 12: exclusión del mínimo/mínimum, aumento de
grado a partir de la segunda condena con esa agravante, contrapeso de las
atenuantes 1ª y 9ª del art. 11 y salvedad de la cooperación eficaz);
**art. 72** (intervención de menores: exclusión del mínimo o aumento de grado);
**art. 73** (eximente incompleta con la mayoría de los requisitos: rebaja
obligatoria de 1 a 3 grados); **art. 103** (media prescripción: el hecho se
considera revestido de dos o más atenuantes muy calificadas y ninguna
agravante, con remisión a los arts. 65 a 68).

**Paso 5 — Individualización dentro del grado (art. 69 CP).** Fija la cuantía
según número y entidad de las circunstancias y la mayor o menor extensión del
mal, con la consideración especial de víctimas menores de 18 años, adultos
mayores (Ley 19.828) o personas con discapacidad (Ley 20.422), incorporada al
texto verificado del art. 69.

**Paso 6 — Multa, penas copulativas y accesorias.** La multa se regula por el
caudal o facultades del culpable, con posibilidad fundada de bajar del mínimo
legal y pago en parcialidades hasta un año (art. 70 CP); es la pena
inmediatamente inferior a la última en todas las escalas (art. 60 CP). Las
penas copulativas de distintas escalas se imponen todas (art. 61 regla 4ª);
las accesorias se declaran expresamente (arts. 22 y 76 CP). Recuerda que el
comiso de ganancias **no es pena** (art. 20 CP) y procede con toda sentencia
condenatoria (art. 24 bis CP), incluso respecto de terceros en las hipótesis
del art. 24 ter CP, y que las sanciones administrativas por el mismo hecho se
abonan conforme al art. 78 bis CP.

---

## III. Duración de los grados *(cotejo conforme, 2026-07-17, contra la TABLA DEMOSTRATIVA oficial del art. 56 CP —imagen embebida en el XML de LeyChile, SHA-256 registrado en `marco-legal.md`, sección 2.2—)*

| Pena | Duración |
|---|---|
| Presidio/reclusión mayor grado máximo | 15 años y 1 día a 20 años |
| Presidio/reclusión mayor grado medio | 10 años y 1 día a 15 años |
| Presidio/reclusión mayor grado mínimo | 5 años y 1 día a 10 años |
| Presidio/reclusión menor grado máximo | 3 años y 1 día a 5 años |
| Presidio/reclusión menor grado medio | 541 días a 3 años |
| Presidio/reclusión menor grado mínimo | 61 a 540 días |
| Prisión (faltas) | 1 a 60 días, en tres grados |

La clasificación crimen / simple delito / falta se determina por la pena
asignada en la escala general del art. 21 CP (art. 3 CP), y arrastra
consecuencias directas sobre prescripción (sección V) y sobre el iter criminis
punible.

---

## IV. Concursos

- **Concurso real** (art. 74 CP): se imponen todas las penas; cumplimiento
  simultáneo si es posible y, si no, sucesivo comenzando por la más grave.
- **Concurso ideal y medial** (art. 75 CP): se impone solo «la pena mayor
  asignada al delito más grave».
- **Reiteración de delitos de la misma especie** (art. 351 CPP, **verificado el
  2026-07-17**, `marco-legal.md` sección 3.7, versión del artículo 2000-10-12):
  (i) si las diversas infracciones pueden estimarse como un solo delito, se
  impone la pena correspondiente a ellas así estimadas, aumentada en uno o dos
  grados; (ii) en su defecto, la pena del delito que, aisladamente considerado
  y con las circunstancias del caso, tenga asignada pena mayor, aumentada en
  uno o dos grados según el número de delitos; (iii) **cláusula de
  favorabilidad**: procede el art. 74 CP si de él resulta pena menor, cotejo
  que debe consignarse expresamente en el cálculo; (iv) son de una misma
  especie los delitos que afectan al **mismo bien jurídico** (inciso final).
  La regla es ahora **base de cálculo habilitada**, no mera alternativa a
  cotejar.
- En delitos económicos, el sistema de la Ley 21.595 contiene reglas propias de
  concurrencia *(pendiente de verificación, sección VI)*.

---

## V. Prescripción como límite del marco punitivo

Los plazos, el cómputo, la interrupción, la suspensión y la media prescripción
(arts. 93 a 105 CP) constan verificados en `marco-legal.md`, sección 2.3, y su
cálculo se ejecuta con el **motor determinístico** `scripts/prescripcion.py`
(también publicado como `src/prescripcion.py` en el repositorio
`estrategia-litigio-penal`, con su suite pytest). Reglas de uso:

1. El motor entrega fechas y estados (vigente / suspendida / prescrita /
   imprescriptible) y la fecha de la **media prescripción** (art. 103 CP), que
   habilita la rebaja de la sección II, paso 4.
2. La formalización suspende la prescripción (art. 233 letra a CPP, verificado,
   en relación con el art. 96 CP); la decisión de no perseverar la deja
   continuar «como si nunca se hubiere interrumpido» (art. 248 letra c CPP,
   verificado).
3. La salida del motor es insumo auxiliar: el cómputo definitivo (feriados,
   momento consumativo en delitos permanentes o de resultado separado, delitos
   especiales de corto tiempo) queda sujeto al criterio del abogado.

---

## VI. Sistema especial de la Ley 21.595 — delitos económicos *(verificado en `leyes-especiales.md`)*

Para hechos que califiquen como delito económico, el algoritmo común de la
sección II se **reemplaza** en lo pertinente por las reglas siguientes, todas
citables sobre el texto verificado (curatoría 2026-07-07, idNorma 1195119):

1. **Calificación** (arts. 1 a 7): verificar la pertenencia del hecho a las
   categorías del catálogo y, en las hipótesis de los arts. 2, 3 y 4 N° 2 y 3,
   el conocimiento exigido por el art. 8 N° 2.
2. **Régimen especial excluyente** (art. 12): no se aplican los arts. 65 a 69
   CP ni las modificatorias de los arts. 11 a 13 CP. En su lugar:
   - **Atenuantes** (art. 13): culpabilidad disminuida y perjuicio limitado
     (más de 40 y hasta 400 UTM).
   - **Atenuantes muy calificadas** (art. 14): culpabilidad muy disminuida y
     cuantía de bagatela (hasta 40 UTM; hipótesis del art. 111 inc. 1° del
     Código Tributario en delitos tributarios — art. 111 CT verificado en
     `references/tributario.md`).
   - **Agravantes** (art. 15): culpabilidad elevada (posición intermedia,
     abuso de autoridad, sanción previa por delito económico, hipótesis del
     art. 111 incs. 2° y 3° CT, verificado) y perjuicio o beneficio relevante
     (sobre 400 y hasta 40.000 UTM).
   - **Agravantes muy calificadas** (art. 16): culpabilidad muy elevada
     (posición jerárquica superior, presión sobre subordinados) y perjuicio
     muy elevado (sobre 40.000 UTM, bienes de primera necesidad, grupos
     vulnerables, hipótesis de los arts. 251 quinquies N° 2 y 260 ter CP).
   - **Efectos sobre el marco** (art. 17): las simples operan en la
     individualización; las muy calificadas mueven mínimum/máximum o excluyen
     grados, y en concurrencia plural rebajan o aumentan en un grado, con
     compensación por número entre muy calificadas.
   - **Individualización** (art. 18): dentro del grado, según atenuantes y
     agravantes simples, intensidad de la culpabilidad y extensión del mal.
3. **Multa obligatoria en días-multa** (arts. 10 y 27 a 29): número de
   días-multa correlativo a la extensión de la pena privativa y valor del
   día-multa según capacidad económica; no es sustituible.
4. **Inhabilitaciones y prohibiciones** (arts. 30 a 39): consecuencias
   adicionales no sustituibles.
5. **Comiso de ganancias** (arts. 40 a 47, en relación con los arts. 20,
   24 bis y 24 ter CP verificados) y comiso sin condena.
6. **Sustitución restrictiva** (arts. 19 a 26): solo remisión condicional y
   reclusión parcial (domiciliaria o en establecimiento especial); la Ley
   18.216 es únicamente supletoria (art. 19) *(texto de la 18.216 pendiente
   de verificación)*.
7. **Non bis in idem administrativo** (art. 11, en relación con el art. 78
   bis CP verificado).

Concurrencia habitual: si interviene una persona jurídica, análisis paralelo
bajo la Ley 20.393 *(verificada, texto post-21.595, en `leyes-especiales.md`)*;
si hay flujos de origen ilícito, encuadre bajo el art. 27 de la Ley 19.913
*(verificado)* con el módulo `references/forense-financiero.md`.

---

## VII. Penas sustitutivas — Ley 18.216 **[V — cotejo del 2026-07-11, idNorma 29636]**

Filtros de procedencia prima facie:
- **Remisión condicional (art. 4)**: pena no superior a tres años; sin condenas anteriores por crimen o simple delito (no se computan las cumplidas diez o cinco años antes, respectivamente); pronóstico favorable; e innecesariedad de intervención o ejecución efectiva. Vedada para los ilícitos de los arts. 15 letra b) y 15 bis letra b), en que procede reclusión parcial o libertad vigilada.
- **Reclusión parcial (art. 8)**: pena no superior a tres años; límites de condenas previas (ninguna, o privativas que en total no excedan de dos años, con la misma regla de descuento temporal); regla especial de improcedencia por reclusiones parciales anteriores, reforzada en delitos contra la propiedad de los Párrafos 1 a 4 bis del Título IX y 456 bis A CP.
- **Libertad vigilada (art. 15)**: pena superior a dos y no superior a tres años, o los supuestos especiales de la letra b) (art. 4 Ley 20.000 y manejo en estado de ebriedad del art. 196 Ley de Tránsito, con pena superior a 540 días y hasta tres años); sin condenas anteriores y con pronóstico de eficacia de la intervención. **Intensiva (art. 15 bis)**: pena superior a tres y no superior a cinco años, o los delitos VIF y sexuales de su letra b) con pena superior a 540 días y hasta cinco años.
- **Expulsión (art. 34)**: pena igual o inferior a cinco años; procede respecto del extranjero **sin residencia legal** y, tras la Ley 21.325, también del residente legal salvo arraigo calificado por el juez con informe del Servicio Nacional de Migraciones; excluida en Ley 20.000, contrabando calificado y trata/tráfico de migrantes; prohibición de regreso por diez años con revocación en caso de retorno.
- **Prestación de servicios en beneficio de la comunidad (art. 11)**: pena igual o inferior a trescientos días, voluntad del condenado, y solo cuando los antecedentes penales hagan improcedentes las demás sustitutivas; procede por una sola vez.

Advertencias: (a) el catálogo de exclusiones del art. 1° (versión 2025-02-12) es extenso y de expansión continua —comprende hoy, entre otros, el art. 293 CP (asociación criminal), figuras sexuales y de homicidio calificado, y la exclusión general de los crímenes y simples delitos de la Ley 17.798, con sustitutivas restringidas para sus simples delitos—; se verifica caso a caso contra la versión vigente a la fecha de la sentencia; (b) el abono de la privación de libertad sufrida durante el proceso se computa siempre; (c) la pena mixta y las reglas de quebrantamiento integran el escenario de riesgo, no la nota al pie.

En delitos económicos, el régimen sustitutivo especial de la Ley 21.595
prevalece *(verificado: arts. 19 a 26, sección VI)*; la Ley 18.216 es solo
supletoria (art. 19 Ley 21.595). Consigna siempre en el informe si la pena
probable queda dentro o fuera del umbral de sustitución: esa frontera suele
decidir la estrategia (juicio, abreviado o salida alternativa; ejecuta
`scripts/estrategia_litigio.py` cuando la decisión lo amerite).

---

## VIII. Esquema de presentación del cálculo

1. **Pena en abstracto**: tipo penal, norma, estructura del marco.
2. **Iter criminis y participación**: rebajas aplicadas y escala utilizada.
3. **Circunstancias modificatorias**: acreditadas, alegables y controvertidas,
   con su filtro de los arts. 63 y 64 CP.
4. **Marco resultante**: regla aplicada (arts. 65–68 ter) y rango en grados.
5. **Individualización estimada**: cuantía probable dentro del grado (art. 69).
6. **Multa, accesorias y comiso**: incluido el comiso de ganancias (24 bis/ter).
7. **Sistema especial**: si aplica Ley 21.595, cálculo paralelo *(pendiente de
   verificación)* y comparación de resultados.
8. **Sustitución**: procedencia prima facie de penas sustitutivas.
9. **Prescripción**: salida del motor `prescripcion.py` y media prescripción.
10. **Conclusión**: rango probable, escenarios (mejor/peor caso defensivo y
    acusador) y factores que mueven el resultado.

---

## IX. Cierre

El cálculo de penas es estimativo y está sujeto a la discrecionalidad judicial
dentro del marco reglado. Su función es estratégica: dimensionar la exposición
punitiva real para decidir entre juicio oral, procedimiento abreviado o salidas
alternativas, y calibrar la negociación. Toda cifra que este módulo produzca
debe poder reconducirse a un artículo verificado de `marco-legal.md` o portar
la marca «pendiente de verificación»; la frontera entre ambas categorías es,
también aquí, condición de validez del análisis.
