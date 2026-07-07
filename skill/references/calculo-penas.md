# Cálculo de penas y marco punitivo

> **Estado del módulo**: OPERATIVO en su componente de derecho común (Código
> Penal), cuyo sustento normativo —arts. 11–13, 19–24 ter y 50–78 bis CP— consta
> **verificado** en `references/marco-legal.md` (curatoría del 2026-07-06, XML
> oficial LeyChile, idNorma 1984). El componente de leyes especiales (sistema de
> la Ley 21.595 y penas sustitutivas de la Ley 18.216) permanece **pendiente de
> verificación** hasta la curatoría de sus XML; toda cita de esos cuerpos lleva
> la marca correspondiente y no puede fundar conclusiones en escritos.

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
   divisibles) no fue capturada por el extracto XML (el servicio la omite como
   elemento tabular). Las duraciones consignadas en la sección III provienen del
   conocimiento consolidado de la escala y deben cotejarse **una única vez**
   contra la edición oficial en la próxima sesión de curatoría; hasta entonces
   conservan la marca *(tabla pendiente de cotejo)*.
3. El sistema **especial** de determinación de penas para delitos económicos
   (Ley 21.595) se aplica con preferencia al régimen común cuando el hecho es
   posterior al 17-08-2023 y califica como delito económico. Su mecánica se
   describe en la sección VI con marca «pendiente de verificación» integral.

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

## III. Duración de los grados *(tabla pendiente de cotejo contra el art. 56 CP)*

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
- **Reiteración de delitos de la misma especie**: la regla de acumulación
  jurídica del art. 351 CPP queda fuera del perímetro verificado del CPP
  *(cita pendiente de verificación)*; hasta su curatoría, se enuncia como
  alternativa a cotejar y no como base de cálculo.
- En delitos económicos, el sistema de la Ley 21.595 contiene reglas propias de
  concurrencia *(pendiente de verificación, sección VI)*.

---

## V. Prescripción como límite del marco punitivo

Los plazos, el cómputo, la interrupción, la suspensión y la media prescripción
(arts. 93 a 105 CP) constan verificados en `marco-legal.md`, sección 2.3, y su
cálculo se ejecuta con el **motor determinístico** `src/prescripcion.py` del
repositorio `estrategia-litigio-penal` (pruebas pytest incluidas). Reglas de
uso:

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

## VI. Sistema especial de la Ley 21.595 — delitos económicos *(íntegramente pendiente de verificación)*

> **Advertencia**: esta sección describe la arquitectura del sistema para
> efectos de planificación del análisis. Ningún artículo de la Ley 21.595 ha
> sido curado aún; la numeración y el detalle se incorporarán desde el XML
> oficial conforme al perímetro propuesto en `skill/perimetro-leyes-especiales.md`.
> Hasta entonces, **no citar en escritos**.

Para hechos posteriores al 17-08-2023 que califiquen como delito económico
(catálogo en cuatro categorías), el análisis debe:

1. Verificar la calificación del hecho en el catálogo y la calidad exigida en
   el sujeto, según la categoría.
2. Sustituir las modificatorias comunes por las **atenuantes y agravantes
   especiales** de la ley (entre otras, cooperación eficaz y posición o rol en
   la organización), con sus reglas propias de concurrencia y efecto en grados.
3. Determinar la **multa en días-multa**, en función de la capacidad económica
   del condenado y la gravedad del hecho.
4. Evaluar las **inhabilitaciones especiales** y la **pena de supervisión**
   cuando proceda.
5. Aplicar el régimen de **comiso de ganancias** ya verificado en el CP
   (arts. 20, 24 bis y 24 ter) y el comiso sin condena.
6. Considerar el régimen especial de sustitución de penas privativas, más
   restrictivo que el de la Ley 18.216 común.

Concurrencia habitual: si interviene una persona jurídica, análisis paralelo
bajo la Ley 20.393 *(pendiente de verificación)*; si hay flujos de dinero de
origen ilícito, encuadre bajo la Ley 19.913 *(pendiente de verificación)* con
el módulo `references/forense-financiero.md`.

---

## VII. Penas sustitutivas — Ley 18.216 *(pendiente de verificación)*

Verifica la procedencia conforme al siguiente cuadro de trabajo, cuyos
umbrales deben cotejarse contra el texto vigente de la Ley 18.216 antes de
afirmarse en escritos:

- **Remisión condicional**: pena que no exceda de 3 años y ausencia de condenas
  anteriores por crimen o simple delito.
- **Reclusión parcial**: pena que no exceda de 3 años.
- **Libertad vigilada**: pena superior a 2 y no superior a 3 años.
- **Libertad vigilada intensiva**: pena superior a 3 y no superior a 5 años, o
  hipótesis especiales.
- **Expulsión**: extranjeros, según residencia y quántum.
- **Prestación de servicios en beneficio de la comunidad**: penas cortas.

En delitos económicos, el régimen sustitutivo especial de la Ley 21.595
prevalece *(pendiente de verificación)*. Consigna siempre en el informe si la
pena probable queda dentro o fuera del umbral de sustitución: esa frontera
suele decidir la estrategia (juicio, abreviado o salida alternativa; ejecuta
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
