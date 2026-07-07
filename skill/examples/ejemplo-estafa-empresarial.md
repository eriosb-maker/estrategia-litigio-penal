# Ejemplo trabajado — Estafa empresarial (esquema Ponzi) con lavado de activos

> **NATURALEZA DE ESTE DOCUMENTO**: caso **enteramente ficticio**, construido con
> fines exclusivamente pedagógicos para demostrar el recorrido íntegro de las
> quince fases de la skill `analisis-penal-chile`, la carga condicional de sus
> módulos de referencia y la ejecución de sus motores deterministas
> (`scripts/prescripcion.py` y `scripts/estrategia_litigio.py`). Ninguna
> persona, empresa, RUC/RIT, tribunal o fiscal mencionado corresponde a un caso
> real; toda coincidencia es involuntaria. Las citas normativas sí son reales y
> están tomadas del texto verificado de `references/marco-legal.md` y
> `references/leyes-especiales.md`; se advierte expresamente cuando una cita
> excede el perímetro curado.
>
> Este documento se elabora conforme al artículo 6 del SKILL.md (estructura de
> entrega) y ejercita, en el orden del artículo 4, las quince fases: 1
> (reconocimiento), 2 (cronología), 3 (participantes), 4-5 (contradicciones), 6
> (ACH), 7 (financiero forense), 8 (prueba digital), 9 (elementos del tipo), 10
> (cálculo de penas), 11 (diligencias), 12 (teoría del caso dual + motor de
> estrategia), 13 (riesgos procesales), 14 (borrador de querella, extracto) y
> 15 (cierre y aprendizaje).

---

## PORTADA

- **RUC / RIT**: 2500987654-3 (ficticio) / RIT 1122-2026 (ficticio)
- **Tribunal**: 7° Juzgado de Garantía de Santiago (ficticio, para el ejercicio)
- **Delitos investigados**: estafa (art. 467 N° 1 CP), administración desleal
  (art. 470 N° 11 CP) y lavado de activos (art. 27 letra a) Ley N° 19.913)
- **Imputados**: Rodrigo Andrés Salinas Ibarra (ficticio) — gerente general y
  controlador de Inversiones Altamira SpA (ficticia); Valentina Paz Rojas
  Concha (ficticia) — subgerente de administración
- **Persona jurídica potencialmente responsable**: Inversiones Altamira SpA
  (ficticia), RUT 76.543.210-K (ficticio)
- **Tercero cuya situación se examina sin imputación formal**: Marco Antonio
  Ibáñez Paredes (ficticio) — contador externo
- **Víctimas**: 14 inversionistas particulares, identificados en este ejemplo
  como Víctima 1 a Víctima 14 (se omiten datos identificatorios reales,
  inexistentes por tratarse de un caso ficticio)
- **Fecha del informe**: 2026-07-07
- **Perspectiva del análisis**: dual (fiscal/querellante y defensa), conforme
  a la sección 9 del SKILL.md, con foco operativo en la defensa de Rodrigo
  Salinas Ibarra para efectos de la fase 12

## ÍNDICE

I. Resumen ejecutivo · II. Hechos investigados · III. Participantes · IV.
Análisis comparativo de versiones · V. Calificación jurídica · VI. Análisis
probatorio (ACH) · VII. Análisis financiero forense · VIII. Análisis de
prueba digital · IX. Cálculo de penas y marco punitivo · X. Diligencias
propuestas · XI. Teoría del caso (perspectiva dual) · XII. Análisis de
riesgos procesales · XIII. Conclusiones y recomendaciones · Anexo: extracto
de querella · Anexo: Protocolo de Cierre y Aprendizaje

---

## I. Resumen ejecutivo

Entre el 1 de septiembre de 2023 y el 15 de marzo de 2025, Rodrigo Andrés
Salinas Ibarra, en su calidad de gerente general y controlador de Inversiones
Altamira SpA, captó fondos de catorce inversionistas particulares por un
total de $1.100.000.000, ofreciendo un vehículo de inversión en instrumentos
de renta fija con rentabilidad garantizada del 2% mensual. Del examen de la
documentación financiera tenida a la vista se desprende que solo
$180.000.000 fueron efectivamente destinados a instrumentos de inversión
real, mientras que $620.000.000 se emplearon para pagar «rentabilidades» a
inversionistas antiguos con el dinero de los nuevos —patrón indiciario de
esquema Ponzi—, $210.000.000 fueron transferidos a cuentas personales del
imputado y $90.000.000 fueron convertidos a criptoactivos (USDT) en un
exchange extranjero entre enero y marzo de 2025. El perjuicio patrimonial
agregado, no restituido a la fecha de este informe, asciende a $850.000.000.

En tal contexto, los hechos son subsumibles, en un primer examen, en los
tipos de estafa (art. 467 N° 1 CP) y administración desleal (art. 470 N° 11
CP), ambos verificados en `references/marco-legal.md`; la conversión de
fondos a criptoactivos y su desvío hacia cuentas personales configuran,
además, un antecedente indiciario de lavado de activos conforme al art. 27
letra a) de la Ley N° 19.913 —verificado en `references/leyes-especiales.md`—,
norma que expresamente incluye entre sus delitos base «los artículos 467
número 1 del inciso primero e inciso final, 468 y 470, numerales 1°, 8° y
11» del Código Penal. Cabe advertir, como hallazgo central de la calificación
jurídica (capítulo V), que estos tipos **no integran el catálogo de los
artículos 1 a 4 de la Ley N° 21.595**, de modo que —salvo que se sostenga y
acredite una imputación autónoma por captación no autorizada de fondos del
público (arts. 59 a 61 de la Ley N° 18.045, no curados en esta skill)— el
caso se rige por el estatuto **común** de determinación de penas del Código
Penal, y no por el sistema especial de delitos económicos. Subsiste, en
cambio, una vía verificada para la responsabilidad penal de Inversiones
Altamira SpA por la vía del lavado, que se desarrolla en el capítulo V.3.

La evidencia digital y financiera converge de modo significativo: la
correspondencia electrónica y de mensajería instantánea contradice
directamente la versión exculpatoria del imputado principal, y las cartolas
bancarias documentan con precisión el patrón de desvío. El presente informe
desarrolla la cronología, la matriz de actores, el cotejo de versiones, el
Análisis de Hipótesis Competitivas, el análisis financiero y digital, la
calificación jurídica, el cálculo de penas —incluida la prescripción
computada con el motor determinista `scripts/prescripcion.py`—, las
diligencias pendientes, la teoría del caso dual —con el motor
`scripts/estrategia_litigio.py`— y los riesgos procesales.

## II. Hechos investigados (cronología)

*(Extracto de la plantilla `assets/templates/cronologia-hechos.md`; se
consignan los hitos de mayor relevancia probatoria. A = acreditado, I =
indiciario, H = hipótesis.)*

| N° | Fecha | Hecho | Fuente | Tipo | Certeza |
|---|---|---|---|---|---|
| 1 | 2023-09-01 | Constitución del vehículo de captación; primeros contratos de mandato de inversión suscritos con Víctimas 1 a 4 | Contratos, escritura social | documento | A |
| 2 | 2023-10 a 2024-06 | Incorporación sucesiva de las Víctimas 5 a 14; captación acumulada de $640.000.000 | Contratos, cartolas de ingreso | documento/financiera | A |
| 3 | 2023-11-05 | Primera transferencia desde la cuenta corriente de la SpA a la cuenta personal de Rodrigo Salinas, por $35.000.000 | Cartola bancaria SpA | financiera | A |
| 4 | 2024-02 a 2024-12 | Pagos mensuales de «rentabilidad» del 2% a inversionistas antiguos, financiados con capital de inversionistas nuevos (patrón Ponzi) | Cartolas bancarias, conciliación de flujos | financiera | I (patrón), A (transferencias individuales) |
| 5 | 2024-08-14 | Correo de Valentina Rojas a las Víctimas 1 a 14 adjuntando «Estado de Cartera — julio 2024.xlsx», que informa una rentabilidad acumulada del 14% | Correo electrónico con adjunto | digital | A (envío), I (veracidad del contenido) |
| 6 | 2024-08-13 | Metadata del archivo adjunto: fecha de creación 2024-08-13 19:47, fecha de última modificación por «Valentina Rojas» | Metadata del documento (propiedades OOXML) | digital | A |
| 7 | 2024-08-12 21:03 | Mensaje de WhatsApp de Valentina Rojas a Rodrigo Salinas: «¿pongo la cifra de 8% como el mes pasado?» | Respaldo de mensajería (a obtener; ver diligencias) | digital | I — pendiente de incorporación formal mediante diligencia (capítulo X) |
| 8 | 2024-08-12 21:11 | Respuesta de Rodrigo Salinas: «sí, así no preguntan» | Ídem | digital | I — pendiente de incorporación formal |
| 9 | 2025-01-10 a 2025-03-15 | Cuatro transferencias desde la cuenta de la SpA hacia un exchange de criptoactivos, por un total de $90.000.000, convertidas a USDT | Cartola bancaria SpA, registro del exchange (a oficiar) | financiera/digital | A (transferencias), I (destino final de los criptoactivos) |
| 10 | 2025-03-15 | Última transferencia relevante acreditada; cese de la actividad de captación | Cartola bancaria SpA | financiera | A |
| 11 | 2025-11-20 | Denuncia colectiva de las Víctimas 1, 3, 7 y 9 ante la Fiscalía Centro Norte (ficticia) | Denuncia | documento | A |
| 12 | 2026-02-10 | Formalización de la investigación en contra de Rodrigo Salinas Ibarra por estafa y administración desleal (hito del ejercicio; suspende la prescripción conforme al art. 96 CP en relación con el art. 233 letra a) CPP, ambos verificados) | Registro de audiencia | documento | A |

**Vacíos temporales relevantes**: no consta en los antecedentes examinados el
detalle mes a mes de los pagos de «rentabilidad» entre marzo y julio de 2024
(fila 4 agrupa el período); tampoco consta la cadena de custodia formal del
respaldo de WhatsApp (filas 7-8), que a la fecha de este informe permanece
como antecedente indiciario mientras no se practique la diligencia de
incautación y peritaje respectiva.

## III. Participantes

| Nombre (ficticio) | Rol procesal | Rol material | Declaración | Vínculos |
|---|---|---|---|---|
| Rodrigo Andrés Salinas Ibarra | Imputado | Gerente general y controlador de la SpA; ordenó las transferencias a cuentas personales y al exchange | Prestó declaración voluntaria el 2026-01-15 (ver capítulo IV) | Empleador de Valentina Rojas; contratante de Marco Ibáñez |
| Valentina Paz Rojas Concha | Imputada | Subgerente de administración; redactó y envió los estados de cartera a los inversionistas | Prestó declaración voluntaria el 2026-01-20 (ver capítulo IV) | Subordinada de Rodrigo Salinas |
| Marco Antonio Ibáñez Paredes | Tercero, situación no formalizada | Contador externo; certificó los estados financieros anuales de la SpA sin verificación independiente de los saldos del exchange | No consta declaración a la fecha | Prestador de servicios externo, sin vínculo societario acreditado |
| Víctimas 1 a 14 | Víctimas / potenciales querellantes | Inversionistas que suscribieron contratos de mandato de inversión | Denuncia colectiva (fila 11 de la cronología) | Sin vínculo entre sí más allá de la relación contractual con la SpA |
| Inversiones Altamira SpA | Persona jurídica, responsabilidad penal en examen | Vehículo societario de la captación | No aplica | Controlada por Rodrigo Salinas Ibarra |

## IV. Análisis comparativo de versiones

*(Extracto de `assets/templates/matriz-contradicciones.md`.)*

| Tema controvertido | Rodrigo Salinas (decl. 2026-01-15) | Valentina Rojas (decl. 2026-01-20) | Evidencia objetiva | Calificación | Relevancia |
|---|---|---|---|---|---|
| Causa de la pérdida de los fondos | «Las pérdidas se debieron a la volatilidad del mercado de renta fija» | No se pronuncia sobre la causa; declara desconocerla | Cartolas: solo $180.000.000 de $1.100.000.000 captados fueron destinados a instrumentos de inversión reales | **XO** (contradicción con evidencia objetiva) | Alta — desvirtúa la eximente de caso fortuito y sostiene el elemento subjetivo del engaño |
| Conocimiento de Valentina Rojas sobre el destino real de los fondos | No se refiere específicamente a este punto | «Yo solo seguía las instrucciones del gerente; desconocía el destino final de los fondos» | Mensaje de WhatsApp (fila 7-8 de la cronología, pendiente de incorporación formal): «¿pongo la cifra de 8% como el mes pasado?» / «sí, así no preguntan» | **XO** (contradicción con evidencia digital, sujeta a la diligencia de incorporación) | Alta — de confirmarse la cadena de custodia, acredita conocimiento y participación dolosa de Valentina Rojas, no mera negligencia |
| Autorización de las transferencias a cuentas personales | «Esas transferencias correspondían a honorarios de gerencia devengados y no pagados» | No se pronuncia | No consta contrato de honorarios ni acuerdo de directorio que respalde la cifra ($210.000.000); no consta en los antecedentes examinados documento habilitante | **XO** | Alta — de no acreditarse el título habilitante, sostiene la administración desleal (art. 470 N° 11 CP) |

## V. Calificación jurídica

### V.1. Estafa — art. 467 N° 1 CP *(verificado)*

Conforme al texto verificado de `references/marco-legal.md`, el art. 467 CP
sanciona a quien, mediante engaño, provoca error en otro y lo hace incurrir
en una disposición patrimonial en su perjuicio o de un tercero, graduando la
pena según el monto del perjuicio. Adoptando, para efectos de este ejercicio,
un valor referencial de la UTM de $65.000 —**cifra no verificada contra el
Servicio de Impuestos Internos; en un caso real debe cotejarse el valor
vigente a la fecha de cada hecho, conforme lo exige el propio art. 467
respecto del momento de comisión**—, el perjuicio acreditado de $850.000.000
equivale aproximadamente a 13.077 UTM, cifra que cae en el tramo del art. 467
N° 1 («si el perjuicio excede de cuatrocientas unidades tributarias
mensuales y no pasa de cuarenta mil»): **presidio menor en su grado máximo y
multa de veintiuna a trescientas unidades tributarias mensuales**.

En cuanto al elemento subjetivo, la contradicción XO de la fila 1 del
capítulo IV —la explicación de «volatilidad del mercado» frente a una
asignación de fondos donde solo el 16% del capital captado se destinó
efectivamente a instrumentos de inversión— constituye un antecedente
indiciario de dolo directo, sin perjuicio de que su acreditación plena
requiere la pericia contable de la diligencia N° 1 del capítulo X.

### V.2. Administración desleal — art. 470 N° 11 CP *(verificado)*

El mismo cuerpo verificado sanciona con las penas del art. 467 a quien,
teniendo a su cargo la salvaguardia o gestión del patrimonio de otro, le
irroga perjuicio ejerciendo abusivamente facultades de disposición o
ejecutando acciones manifiestamente contrarias al interés del titular. Las
transferencias de $210.000.000 a cuentas personales de Rodrigo Salinas, sin
título habilitante acreditado (fila 3 del capítulo IV), configuran un
antecedente indiciario de este tipo, concurrente con la estafa sobre el mismo
sustrato patrimonial. **Riesgo jurídico a resolver**: la relación concursal
entre ambos tipos —dado que ambos recaen sobre el mismo patrimonio y podrían
responder al principio de especialidad o consunción antes que a un concurso
real— no consta zanjada por doctrina o jurisprudencia verificada en los
antecedentes de esta skill; se declara «cita pendiente de verificación» y se
recomienda investigación dogmática específica antes de la acusación.

### V.3. Inaplicabilidad, en principio, del sistema especial de la Ley N° 21.595

Del examen del catálogo verificado en `references/leyes-especiales.md` se
desprende que ni el art. 467 ni el art. 470 N° 11 CP figuran entre las
disposiciones enumeradas en los artículos 1, 2, 3 o 4 de la Ley N° 21.595. En
consecuencia, **no corresponde aplicar a estos dos tipos el sistema especial
de determinación de penas** (arts. 12 a 18 de esa ley), sino el régimen común
de los arts. 50 a 78 bis CP, conforme se desarrolla en el capítulo IX. Cabe
advertir que el art. 1 N° 1 de la Ley N° 21.595 sí incluye «los artículos 59,
60, 61 y 62 de la ley N° 18.045, de Mercado de Valores», disposiciones que
sancionan la captación u oferta pública de valores sin la autorización de la
Comisión para el Mercado Financiero —hipótesis fácticamente plausible en un
esquema como el descrito—; sin embargo, **la Ley N° 18.045 no se encuentra
curada en esta skill**, por lo que esta vía de calificación se deja
expresamente como «cita pendiente de verificación» y como diligencia de
curatoría recomendada (capítulo X, diligencia N° 6). De confirmarse esa
calificación en una sesión de curatoría futura, el caso completo pasaría al
régimen especial de la Ley N° 21.595, con las consecuencias que ello importa
sobre el cálculo de penas del capítulo IX.

### V.4. Lavado de activos — art. 27 letra a) Ley N° 19.913 *(verificado)*

El texto verificado de esa disposición sanciona, con **presidio mayor en sus
grados mínimo a medio y multa de doscientas a mil unidades tributarias
mensuales**, a quien oculte o disimule el origen ilícito de bienes
provenientes, entre otros, de hechos constitutivos de los delitos de los
«artículos 467 número 1 del inciso primero e inciso final, 468 y 470,
numerales 1°, 8° y 11» del Código Penal —ambos tipos base de este caso—. La
conversión de $90.000.000 a criptoactivos (fila 9 de la cronología), en
tramos sucesivos hacia un exchange extranjero, constituye un antecedente
indiciario de ocultamiento del origen ilícito de esos fondos, sujeto a
corroboración mediante la diligencia de oficio al exchange (capítulo X).

**Hallazgo relevante para la responsabilidad de la persona jurídica**: el
art. 1 N° 1 de la Ley N° 20.393 —verificado en `references/leyes-especiales.md`—
extiende la responsabilidad penal de las personas jurídicas a «los delitos a
que se refieren los artículos 1, 2, 3 y 4 de la Ley de Delitos Económicos,
**sean o no considerados como delitos económicos por esa ley**». El art. 4 de
la Ley N° 21.595 (cuarta categoría, verificado) menciona expresamente, como
uno de sus dos artículos base, «el artículo 27 de la ley N° 19.913». De la
concatenación de ambos textos verificados se desprende una **inferencia
razonable, sin jurisprudencia consolidada verificada en los antecedentes de
esta skill**: la sola mención del art. 27 en el art. 4 de la Ley N° 21.595
bastaría para incluir el delito de lavado en el catálogo del art. 1 N° 1 de
la Ley N° 20.393, con independencia de que —como se concluyó en el capítulo
V.1— el hecho base (estafa) no satisfaga las condiciones de las categorías 1
a 3 del art. 4 y, por tanto, el lavado mismo no llegue a calificar como
«delito económico» para los efectos de la propia Ley N° 21.595. Se trata de
una tesis jurídica novedosa que el abogado responsable debe validar
autónomamente antes de sostenerla en juicio; de confirmarse, habilitaría
perseguir la responsabilidad autónoma de Inversiones Altamira SpA por el
delito de lavado, conforme al modelo de prevención de delitos exigido por el
art. 3 de la Ley N° 20.393 (verificado).

## VI. Análisis probatorio — Análisis de Hipótesis Competitivas (ACH)

*(Extracto de `assets/templates/ach-hipotesis-competitivas.md`.)*

**H1 — Esquema Ponzi doloso**: Rodrigo Salinas diseñó y ejecutó, con la
participación consciente de Valentina Rojas, un esquema de captación
fraudulenta en el que los «rendimientos» pagados a inversionistas antiguos
provenían del capital de inversionistas nuevos, mientras desviaba fondos a su
patrimonio personal y a criptoactivos para dificultar su rastreo.

**H2 — Negligencia grave sin dolo de estafa**: Rodrigo Salinas gestionó de
forma temeraria e incompetente los fondos captados, sin intención inicial de
defraudar, y solo ante las pérdidas comenzó a usar capital nuevo para cubrir
compromisos anteriores, incurriendo en una espiral que no controló.

**H3 — Buena fe de Valentina Rojas y Marco Ibáñez**: ambos fueron engañados
por Rodrigo Salinas del mismo modo que los inversionistas, limitándose a
ejecutar instrucciones y a certificar cifras que se les presentaron como
reales, sin conocimiento efectivo de la maniobra.

| N° | Evidencia | Certeza | H1 | H2 | H3 |
|---|---|---|---|---|---|
| 1 | Solo 16% del capital captado se invirtió realmente (fila 4 cronología) | A | ++ | + | 0 |
| 2 | $210.000.000 a cuentas personales sin título habilitante (fila 3) | A | ++ | − | 0 |
| 3 | $90.000.000 convertidos a criptoactivos en tramos sucesivos (fila 9) | A | ++ | −− | 0 |
| 4 | Mensaje de WhatsApp «así no preguntan» (filas 7-8, pendiente de incorporación formal) | I | ++ | −− | −− (respecto de Valentina) |
| 5 | Metadata del estado de cartera con cifras no verificadas (filas 5-6) | A | + | 0 | 0 |
| 6 | Ausencia de declaración de Marco Ibáñez a la fecha | — | 0 | 0 | 0 (neutro hasta obtenerla) |

**Evaluación**: H1 es la hipótesis con menor evidencia refutatoria; H2 queda
refutada con fuerza por los ítems 2, 3 y 4 (la desviación sistemática hacia
patrimonio personal y criptoactivos es incompatible con la mera negligencia
de gestión). Respecto de Valentina Rojas, H3 depende íntegramente de la
incorporación formal del respaldo de WhatsApp (ítem 4): mientras no se
practique esa diligencia, su situación debe tratarse como indiciaria y no
acreditada. Respecto de Marco Ibáñez, no consta en los antecedentes
examinados evidencia que permita evaluar su hipótesis; se declara
expresamente pendiente hasta obtener su declaración (diligencia N° 5).

**Control de sesgos**: se advierte riesgo de sesgo de confirmación al
construir H1 como hipótesis principal desde el reconocimiento inicial (fase
1); se mitigó exigiendo, para cada ítem de evidencia, su calificación
epistémica expresa y manteniendo H3 como hipótesis viva respecto de Valentina
Rojas hasta la corroboración formal del ítem 4.

**Preguntas críticas sin responder**: (i) ¿existe respaldo formal e íntegro
de la conversación de WhatsApp de las filas 7-8, con cadena de custodia
verificable?; (ii) ¿qué declaró o declarará Marco Ibáñez sobre su
verificación de los saldos del exchange?; (iii) ¿existe documentación
societaria (acta de directorio, contrato de honorarios) que respalde los
$210.000.000 transferidos a Rodrigo Salinas?

## VII. Análisis financiero forense

*(Carga condicional de `references/forense-financiero.md`, fase 7, por
existir flujo de fondos y componente de criptoactivos.)*

| Flujo | Monto | Destino | Calificación |
|---|---|---|---|
| Captación total de inversionistas | $1.100.000.000 | Cuenta corriente de la SpA | Acreditado |
| Inversión real en instrumentos de renta fija | $180.000.000 | Terceros institucionales (a individualizar) | Acreditado en cuanto al monto; pendiente la verificación de la naturaleza de los instrumentos |
| Pago de «rentabilidades» a inversionistas antiguos | $620.000.000 | Cuentas de las Víctimas 1 a 14 | Acreditado; patrón Ponzi indiciario |
| Transferencias a cuentas personales de Rodrigo Salinas | $210.000.000 | Cuenta personal | Acreditado; sin título habilitante acreditado |
| Conversión a criptoactivos (USDT) | $90.000.000 | Exchange extranjero (a oficiar) | Acreditado en el origen; destino final pendiente de verificación |

La matriz de coherencia entre lo declarado y lo observado no pudo
completarse íntegramente por no constar en los antecedentes examinados los
formularios F29 de la SpA para el período 2023-2025; se propone como
diligencia N° 4 del capítulo X. El patrón de flujo —capital nuevo empleado
para pagar rendimientos comprometidos con capital antiguo— es indiciario de
esquema Ponzi y constituye, conforme al capítulo VI, el elemento de mayor
peso refutatorio contra la hipótesis H2 (mera negligencia).

## VIII. Análisis de prueba digital

*(Carga condicional de `references/prueba-digital.md`, fase 8, por existir
evidencia digital.)*

- **Correo electrónico y adjunto** (filas 5-6 de la cronología): la metadata
  del archivo «Estado de Cartera — julio 2024.xlsx» —fecha de creación
  2024-08-13 19:47, un día antes de su envío— es consistente con su
  confección para el envío y no revela, por sí sola, manipulación retroactiva
  de fechas anteriores; su valor probatorio principal reside en el cotejo de
  las cifras informadas (14% de rentabilidad acumulada) con los flujos reales
  del capítulo VII, que las contradice.
- **Mensajería instantánea** (filas 7-8): constituye, a la fecha de este
  informe, evidencia **no incorporada formalmente**: no consta cadena de
  custodia, hash de integridad ni acta de incautación del dispositivo de
  origen. Su valor probatorio actual es indiciario y queda condicionado a la
  diligencia N° 2 del capítulo X (peritaje del dispositivo de Valentina
  Rojas, con verificación de IMEI y respaldo contemporáneo).
- **Registros del exchange de criptoactivos**: no constan en los antecedentes
  examinados; su obtención requiere oficio internacional (diligencia N° 3).

## IX. Cálculo de penas y marco punitivo

*(Carga condicional de `references/calculo-penas.md`, fase 10, aplicando su
algoritmo de seis pasos sobre el régimen común, conforme a la conclusión del
capítulo V.3.)*

**Paso 1 — Pena en abstracto**: estafa del art. 467 N° 1 CP: presidio menor
en su grado máximo (un solo grado, 3 años 1 día a 5 años) y multa de 21 a 300
UTM. Administración desleal del art. 470 N° 11 CP: remite a la misma pena.

**Paso 2 — Iter criminis y participación**: Rodrigo Salinas, autor de delito
consumado (art. 50 CP): sin rebaja. Valentina Rojas: su participación exacta
(autora, cómplice) depende de la corroboración del ítem 4 del ACH; de
acreditarse su conocimiento y colaboración activa en el envío de cifras
falsas, sería coautora (art. 15 CP, verificado) del delito de estafa; de no
acreditarse, su situación podría no alcanzar responsabilidad penal.

**Paso 3 — Circunstancias modificatorias**: se identifica, como antecedente
indiciario a verificar mediante extracto de filiación, la posible atenuante
del art. 11 N° 6 CP (irreprochable conducta anterior) respecto de Rodrigo
Salinas. Como agravante, se plantea el art. 12 N° 7 CP (abuso de confianza),
dado que actuó prevalido de la confianza depositada por los inversionistas en
su calidad de gerente general; su procedencia debe evaluarse conforme al
filtro del art. 63 CP (inherencia al tipo), pues el abuso de confianza es
también elemento típico de la administración desleal, lo que podría excluir
su aplicación respecto de ese delito conforme a la regla verificada.

**Paso 4 — Efecto sobre el marco**: tratándose de un solo grado de pena
divisible (art. 467 N° 1 CP), rige el art. 67 CP verificado. De concurrir una
atenuante y una agravante, corresponde su compensación racional, recorriendo
el tribunal la extensión del grado (3 años 1 día a 5 años).

**Paso 5 — Individualización** (art. 69 CP, verificado): la extensión del
mal —$850.000.000 de perjuicio sobre 14 víctimas— constituye un factor que,
dentro del marco compensado, orienta la cuantía hacia el tramo medio-alto del
grado. Como estimación de trabajo para el capítulo XI, se adopta una pena
probable de referencia de **4 años**, sujeta a revisión conforme avance la
investigación.

**Paso 6 — Multa, concurso y comiso**: multa de 21 a 300 UTM (art. 467 N° 1
CP) conforme al caudal del condenado (art. 70 CP, verificado). La relación
concursal entre estafa, administración desleal y lavado —posible concurso
medial del art. 75 CP si el lavado se estimara medio necesario para consumar
o encubrir la estafa— es un **riesgo jurídico a resolver** (capítulo V.2); de
calificarse así, se aplicaría «solo la pena mayor asignada al delito más
grave» (art. 75 CP, verificado), esto es, la del lavado (presidio mayor
mínimo a medio: 5 años 1 día a 15 años), lo que elevaría sustancialmente la
exposición penal. El comiso de ganancias (arts. 20, 24 bis y 24 ter CP,
verificados) resulta aplicable respecto de los $210.000.000 y de los
$90.000.000 en criptoactivos, en tanto se acredite su origen delictivo.

**Prescripción de la acción penal** — computada con `scripts/prescripcion.py`
sobre el art. 467 N° 1 CP (simple delito, plazo de 5 años conforme al art. 94
CP verificado), tomando como fecha de inicio el último acto acreditado
(2025-03-15) y como fecha de consulta la de este informe (2026-07-07):

```
Prescripción de la acción penal — simple delito
Inicio del cómputo: 2025-03-15 (efectivo: 2025-03-15)
Estado al 2026-07-07: suspendida (art. 96 CP)
Media prescripción (art. 103 CP): 2027-09-15 (no alcanzada)
Nota: Suspensión desde el 2026-02-10 (formalización de la investigación),
art. 96 CP en relación con el art. 233 letra a) CPP: el término no corre
mientras subsista.
```

De no haberse formalizado, el motor computa la fecha de cumplimiento del
plazo en **2030-03-15**, lo que ilustra —a efectos exclusivamente
pedagógicos— el margen de holgura disponible en este caso hipotético. Ambos
resultados son insumo auxiliar: el cómputo definitivo, incluida la
calificación del hecho como eventualmente permanente o continuado —lo que
podría desplazar la fecha de inicio del cómputo—, es de resorte exclusivo del
abogado (art. 102 CP, verificado).

**Penas sustitutivas** (Ley N° 18.216): *cita pendiente de verificación*, por
no estar curada esa ley en esta skill; con una pena estimada de 4 años, el
umbral usual de remisión condicional (hasta 3 años) no se satisfaría, siendo
eventualmente aplicable un régimen de libertad vigilada, sujeto a
verificación del texto vigente.

## X. Diligencias propuestas

| Prioridad | Diligencia | Objetivo | Fundamento | Plazo sugerido | Riesgo de omisión |
|---|---|---|---|---|---|
| Alta | Incautación y peritaje del dispositivo móvil de Valentina Rojas, con hash de integridad y verificación de IMEI | Incorporar formalmente el respaldo de WhatsApp (ítem 4 del ACH) | Arts. 217 y 236 CPP *(cita pendiente de verificación; fuera del perímetro curado)* | 30 días | Pérdida de evidencia digital volátil; imposibilidad de acreditar el conocimiento de Valentina Rojas |
| Alta | Pericia contable sobre la totalidad de las cartolas bancarias de la SpA (2023-2025) | Consolidar la matriz de coherencia del capítulo VII y precisar el perjuicio exacto por víctima | Art. 9 CPP (autorización judicial de diligencias que afecten derechos), verificado | 60 días | Imprecisión del monto exacto del perjuicio para efectos del art. 467 CP |
| Alta | Oficio internacional al exchange de criptoactivos para identificar al titular final de la cuenta que recibió los USDT | Determinar el destino final de los $90.000.000 y sustentar el art. 27 Ley 19.913 | Cooperación internacional; art. 27 Ley N° 19.913, verificado | 90 días (sujeto a cooperación internacional) | Imposibilidad de acreditar el ocultamiento del origen ilícito |
| Media | Oficio al Servicio de Impuestos Internos por los formularios F29 de la SpA, período 2023-2025 | Completar la matriz de coherencia declarado/observado | `references/forense-financiero.md` | 45 días | Vacío probatorio en la capa tributaria del análisis financiero |
| Media | Citación a declarar de Marco Ibáñez Paredes | Esclarecer H3 respecto del contador externo | Arts. 190 y 191 CPP *(cita pendiente de verificación)* | 30 días | Persistencia de un vacío probatorio relevante para la ACH |
| Media | Curatoría de los arts. 59 a 61 de la Ley N° 18.045 | Evaluar la calificación autónoma por captación no autorizada de fondos del público y su efecto sobre el régimen de la Ley N° 21.595 | Protocolo de curatoría, `references/marco-legal.md` sección 1 | Próxima sesión de curatoría | Pérdida de una vía de calificación jurídica potencialmente más gravosa (o, según el caso, más favorable a la defensa por la vía de sus reglas especiales) |
| Baja | Solicitud de acta de directorio o contrato de honorarios de Rodrigo Salinas | Verificar el título habilitante alegado en su declaración (capítulo IV) | Documental | 20 días | Persistencia de la contradicción XO sin evidencia dirimente adicional |

## XI. Teoría del caso (perspectiva dual)

**Teoría acusadora (fiscal/querellante)**: Rodrigo Salinas Ibarra, con la
colaboración consciente de Valentina Rojas Concha, diseñó y ejecutó un
esquema de captación fraudulenta de inversionistas, sostenido mediante el
pago de rendimientos con capital de nuevos inversionistas, y desvió una
porción sustancial de los fondos hacia su patrimonio personal y hacia
criptoactivos para dificultar su persecución. La prueba financiera (capítulo
VII) y la digital (capítulo VIII), en su convergencia, acreditan tanto el
engaño (estafa) como el abuso de las facultades de administración
(administración desleal) y el ocultamiento del origen de los fondos
desviados (lavado).

**Teoría defensiva esperable**: Rodrigo Salinas podría sostener (i) que las
transferencias a su cuenta personal correspondían a honorarios de gerencia
legítimamente devengados —lo que exige a la defensa producir con urgencia el
respaldo documental que hoy no consta—; (ii) que la conversión a
criptoactivos obedeció a una estrategia de diversificación de la cartera de
inversión, y no a ocultamiento; (iii) que las pérdidas se debieron a
decisiones de inversión de buena fe, frustradas por la volatilidad del
mercado. La debilidad estructural de esta teoría reside en que solo el 16%
del capital captado se destinó efectivamente a instrumentos de inversión
(fila 4 del capítulo II), extremo difícil de conciliar con cualquiera de las
tres líneas defensivas.

**Motor de estrategia** (`scripts/estrategia_litigio.py`, ejecutado con
parámetros de trabajo propios de este ejercicio: probabilidad de condena
0,72; pena probable en juicio oral 6 años —incorporando el riesgo de concurso
medial con el lavado, capítulo IX—; pena solicitada por el Ministerio
Público 8 años; oferta hipotética de procedimiento abreviado 3 años; costo
estimado del juicio oral $45.000.000; costo de una salida negociada
$15.000.000):

```
"valor_esperado": {
  "exposicion_penal_esperada_juicio_anios": 4.32,
  "exposicion_privativa_esperada_juicio_anios": 3.672,
  "costo_economico_juicio": 45000000,
  "exposicion_abreviado_anios": 3.0,
  "diferencial_abreviado_vs_juicio_anios": -1.32,
  "prob_condena_de_equilibrio": 0.5
}
```

El modelo indica que, con la probabilidad de condena estimada (0,72),
superior al punto de equilibrio (0,50), la exposición esperada del juicio
oral (4,32 años) excede en 1,32 años a la del procedimiento abreviado
hipotético (3 años), lo que —en términos exclusivamente cuantitativos y
sujeto a la ponderación de factores no capturados por el modelo, como el
interés del imputado en sostener su inocencia— orienta hacia la exploración
de una salida negociada. El propio motor advierte, además, que el
procedimiento abreviado **no procede prima facie** con una pena solicitada de
8 años, por exceder el umbral del art. 406 CPP; ello sugiere, como punto de
negociación con el Ministerio Público, procurar que la acusación se
circunscriba a hipótesis cuya pena solicitada no supere ese umbral —cuestión
que a su vez depende de que se descarte, o se acote, el riesgo de concurso
medial identificado en el capítulo IX—. Esta salida es un **insumo auxiliar**,
sujeto a verificación normativa y a la decisión exclusiva del abogado y su
cliente, conforme lo advierte el propio motor en sus observaciones.

## XII. Análisis de riesgos procesales

- **Prescripción**: vigente y suspendida por la formalización, conforme al
  cálculo del capítulo IX; el margen de holgura era amplio (hasta 2030-03-15)
  de no haberse formalizado, lo que reduce este riesgo a la fecha del
  informe.
- **Nulidad por prueba ilícita**: el mayor riesgo se concentra en la
  mensajería instantánea (filas 7-8 del capítulo II), incorporada hoy sin
  cadena de custodia formal; de no subsanarse mediante la diligencia N° 1 del
  capítulo X, la defensa dispone de un flanco de impugnación serio.
- **Sobreseimiento o no perseverar**: bajo, dada la convergencia de evidencia
  financiera acreditada (capítulo VII), independiente de la suerte de la
  evidencia digital.
- **Salidas alternativas**: la suspensión condicional (art. 237 CPP,
  verificado) no procede prima facie con una pena probable de 4 a 6 años,
  conforme al resultado del motor de estrategia; el acuerdo reparatorio (art.
  241 CPP, verificado) exige bien jurídico disponible de carácter patrimonial
  y consentimiento de las 14 víctimas, lo que resulta operativamente complejo
  pero no jurídicamente descartado respecto de la estafa (no así, en
  principio, respecto del lavado).
- **Insolvencia provocada**: dado que $90.000.000 ya fueron convertidos a
  criptoactivos y transferidos al extranjero, existe riesgo cierto de
  frustración de la eventual responsabilidad civil y del comiso; se
  recomienda evaluar medidas cautelares reales *(art. 157 CPP — cita
  pendiente de verificación)* con urgencia.
- **Responsabilidad penal de la persona jurídica**: el riesgo para
  Inversiones Altamira SpA depende de la tesis desarrollada en el capítulo
  V.4, novedosa y no consolidada jurisprudencialmente; se recomienda no
  descartarla sin un análisis dogmático adicional.

## XIII. Conclusiones y recomendaciones

Del examen de los antecedentes se desprende que los hechos configuran, con
un grado de acreditación alto, los tipos de estafa (art. 467 N° 1 CP) y
administración desleal (art. 470 N° 11 CP), con un antecedente indiciario
serio de lavado de activos (art. 27 letra a) Ley N° 19.913) respecto de la
conversión a criptoactivos. La calificación bajo el sistema especial de la
Ley N° 21.595 **no procede**, conforme al catálogo verificado, salvo que la
curatoría pendiente de la Ley N° 18.045 habilite una vía de calificación
autónoma. Subsiste una tesis verificada pero jurídicamente novedosa para
extender responsabilidad penal a la persona jurídica por la vía del lavado.
El análisis exhibe fortalezas probatorias claras en el plano financiero y
debilidades relevantes en el plano digital, hoy no incorporado con el rigor
de cadena de custodia exigible. La estrategia procesal recomendada,
conforme al motor cuantitativo, favorece explorar una salida negociada,
condicionada a acotar el riesgo de concurso medial con el lavado para
habilitar el procedimiento abreviado. Todas las conclusiones de este
ejercicio son revisables a la luz de las siete diligencias propuestas en el
capítulo X y quedan, en su integridad, sujetas al criterio del abogado
responsable.

**Trazabilidad**: archivos consultados —
`references/marco-legal.md` (arts. 467, 470 N° 11, 20, 24 bis, 24 ter, 50-78
bis, 93-105, 9, 96, 233, 237, 241, 406 CPP/CP), `references/leyes-especiales.md`
(arts. 1-4 Ley 21.595, art. 1 y 3 Ley 20.393, art. 27 Ley 19.913),
`references/calculo-penas.md`, `references/prueba-digital.md`,
`references/forense-financiero.md`, `references/estrategia-litigio.md`,
`assets/templates/cronologia-hechos.md`, `matriz-contradicciones.md`,
`ach-hipotesis-competitivas.md`; motores ejecutados —
`scripts/prescripcion.py`, `scripts/estrategia_litigio.py`.

---

## Anexo: extracto de querella (borrador, requiere revisión humana)

*(Conforme a `assets/templates/modelo-querella.md`, fase 14, a petición
hipotética del usuario en este ejercicio; se reproduce solo el capítulo de
los hechos, a título ilustrativo.)*

> **S. J. DE GARANTÍA DE [CIUDAD]**. [NOMBRE DEL QUERELLANTE], en
> representación de las Víctimas 1 a 14 (ficticias), viene en deducir
> querella criminal en contra de Rodrigo Andrés Salinas Ibarra y Valentina
> Paz Rojas Concha, y en contra de todos quienes resulten responsables, por
> los delitos de estafa (art. 467 N° 1 CP) y administración desleal (art. 470
> N° 11 CP), y en carácter subsidiario por lavado de activos (art. 27 letra
> a) Ley N° 19.913), fundada en los siguientes antecedentes:
>
> **I. LOS HECHOS**. Que, entre el 1 de septiembre de 2023 y el 15 de marzo de
> 2025, el querellado Salinas Ibarra, en su calidad de gerente general y
> controlador de Inversiones Altamira SpA, captó de mis representados la suma
> total de $1.100.000.000 [...] *(placeholder: continuar con la relación
> circunstanciada completa conforme a la cronología del capítulo II,
> completando únicamente con datos verificados del expediente real cuando
> este ejercicio se adapte a un caso concreto)*.

## Anexo: Protocolo de Cierre y Aprendizaje (demostración)

Conforme a la sección 15.3 del SKILL.md, se deja constancia de que este
ejercicio no derivó de una sesión de trabajo sobre un caso real ni de
correcciones del usuario sobre criterios jurídicos: es, en sí mismo, la
demostración pedagógica prevista en el catálogo de la skill (paso 6 del plan
de trabajo del repositorio `estrategia-litigio-penal`). En consecuencia, **no
se propone ninguna entrada nueva a `references/aprendizajes.md`** derivada de
este ejercicio; de usarse este documento como plantilla para un caso real, la
sesión correspondiente deberá ejecutar su propio Protocolo de Cierre y
Aprendizaje sobre las lecciones específicas que arroje.

Al término de una sesión sobre un caso real como el aquí ilustrado,
correspondería generar el archivo `estado-del-caso-2500987654-3.md` conforme
a la plantilla `assets/templates/estado-del-caso.md`, consignando como
plazo crítico la prescripción computada en el capítulo IX y como decisión
estratégica pendiente la aceptada por el cliente respecto de la salida
negociada del capítulo XI.
