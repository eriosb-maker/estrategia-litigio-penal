# Tributario — Código Tributario, Ley de Renta y Ley de IVA

> **Estado del módulo**: OPERATIVO — extractos verificados insertados el
> 2026-07-07 mediante `scripts/curar_norma.py` desde los XML oficiales de
> LeyChile, descargados directamente por el asistente con el resolver
> automático de idNorma (`--resolver`) y el modo de descarga con hash
> (`--descargar`), por instrucción expresa del abogado, conforme a la regla
> metodológica aprobada. Los artículos comprendidos en el perímetro de la
> sección 2 pueden citarse como texto verificado a la fecha indicada; todo
> artículo NO comprendido conserva la marca **«cita pendiente de
> verificación»**. Revalidación semestral obligatoria: vence el
> **2027-01-07**.

Carga este archivo cuando el caso involucre delitos tributarios (art. 97 CT),
facturación falsa o uso indebido de crédito fiscal IVA, incremento
patrimonial no justificado u otras discrepancias entre lo declarado al SII y
los flujos reales. Se integra directamente con `references/forense-financiero.md`
(capa tributaria del análisis financiero) y con `references/calculo-penas.md`
(determinación de la pena de los delitos del art. 97 CT).

---

## 1. Registro de curatoría

| Norma | idNorma | Versión de la norma | Perímetro extraído | Artículos | Observaciones |
|---|---|---|---|---|---|
| Código Tributario (DL 830) | 6374 | 2025-07-11 | 8 ter; 97-114; 161-167; 200-202 | 35 | Estructura «Doble Articulado» con disambiguador «(DEL ART. 1)» en el `NombreParte` de cada artículo interno; el motor lo depura desde esta curatoría. Sin advertencias de completitud. |
| Ley sobre Impuesto a las Ventas y Servicios (DL 825) | 6369 | 2025-10-25 | 2, 3, 8, 23-28 | 11 | Estructura simple (sin Doble Articulado). Sin advertencias de completitud. |
| Ley sobre Impuesto a la Renta (DL 824) | 6368 | 2026-03-27 | 2, 17, 21, 31, 33, 70 | 6 | Estructura «Doble Articulado», igual tratamiento que el Código Tributario. Sin advertencias de completitud. |

**Hashes SHA-256 de los XML de origen** (`curatoria/xml/` del repositorio):

- Código Tributario: `5951bfb4304e44e0c0804b52d95a7280a3f5af8f589307cb85f555d37a2ba8b8`
- Ley de Renta (DL 824): `db2988fd71ea8087a43365757fc4b3e78fd578851d46ad5680ec84d1d57807cf`
- Ley de IVA (DL 825): `44ae173b7ba30db4e99e3529e5d039228c9e1a02f8b50c09738f3a3a108d6629`

**Nota metodológica sobre el idNorma de los decretos leyes**: a diferencia de
las normas tipo «Ley N°», el servicio de LeyChile no resuelve el idNorma de
un decreto ley a partir de su número mediante el parámetro `idLey` (ensayado
y descartado en esta sesión: devuelve error). Los tres idNorma de esta tabla
se confirmaron mediante descarga real y cotejo del atributo `normaId` del
XML contra el número de decreto ley esperado, y quedan incorporados al
registro local de `scripts/curar_norma.py` (`REGISTRO_IDNORMA`) para
curatorías futuras.

---

## 2. Notas operativas mínimas (ancladas al texto verificado)

### 2.1 Código Tributario — catálogo de infracciones y delitos (art. 97)

El art. 97 CT (verificado) enumera, en veintiséis numerales, las
infracciones a las disposiciones tributarias y su sanción. No todas
constituyen delito: varias son meras infracciones administrativas
sancionadas solo con multa. Las hipótesis que la práctica identifica como
«delitos tributarios» —por llevar aparejada pena corporal— se concentran,
entre otros, en los numerales relativos a declaraciones maliciosamente
incompletas o falsas, uso de facturas, notas de débito, notas de crédito o
guías de despacho falsas o no fidedignas con la finalidad de aumentar el
crédito fiscal o disminuir impuestos, y la simulación de operaciones
tributarias. La calificación exacta de cada numeral —su texto y su pena
específica— debe verificarse directamente en el extracto insertado en la
sección 3, dado que la enumeración es extensa y las penas varían
sustancialmente entre numerales.

Los arts. 100 a 100 sexies (verificados) sancionan hipótesis conexas,
incluida la responsabilidad de contadores y otros profesionales que
faciliten o participen en la comisión de infracciones tributarias de sus
clientes. Los arts. 101 a 105 regulan infracciones de funcionarios y
disposiciones comunes. Los arts. 106 a 110 regulan la aplicación general de
las sanciones, incluido el error excusable (art. 110). Los arts. 111 y 111
bis (verificados) contienen las circunstancias atenuantes y agravantes
propias del sistema sancionatorio tributario —relevantes para el cálculo de
penas del capítulo IX de un informe, en concurrencia o sustitución de las
reglas generales del Código Penal, según el tipo concreto—. El art. 112
regula la reincidencia.

### 2.2 Procedimiento penal tributario — querella exclusiva del Director del SII (arts. 161-167)

El art. 162 CT (verificado) establece que las investigaciones de hechos
constitutivos de delitos tributarios sancionados con pena privativa de
libertad **solo pueden iniciarse por denuncia o querella del Servicio de
Impuestos Internos** (o, en su caso, del Consejo de Defensa del Estado a
requerimiento del Director). Se trata de un **requisito de procesabilidad**
de primer orden: su ausencia constituye un antecedente central para evaluar
la viabilidad de la persecución penal en cualquier caso de delito
tributario, y su verificación debe ser el primer paso del análisis de riesgos
procesales (fase 13 de la metodología). El mismo artículo faculta al
Director para optar, discrecionalmente, entre perseguir penalmente o remitir
el caso al procedimiento administrativo de aplicación de multas cuando la
infracción admite ambas vías, y regula el tratamiento de los acuerdos
reparatorios del art. 241 CPP (verificado en `marco-legal.md`) en esta
materia, exigiendo que no contemplen una suma inferior al mínimo de la pena
pecuniaria. El art. 163 (verificado) regula la responsabilidad del
representante legal ante la infracción; el art. 164 (verificado), la
posibilidad de que el Director conmute la pena corporal por multa, bajo los
supuestos que allí se especifican.

### 2.3 Prescripción tributaria (arts. 200-202)

Los arts. 200 a 202 CT (verificados) regulan la prescripción de las acciones
del Servicio para liquidar, revisar y girar impuestos, con plazos generales
y ampliados según la conducta del contribuyente (declaración maliciosamente
falsa, no declaración). **Se trata de una prescripción de naturaleza
administrativo-tributaria, distinta de la prescripción de la acción penal
del delito tributario**, que se rige por las reglas generales de los arts.
93 a 105 CP (verificadas en `marco-legal.md`) y se computa con
`scripts/prescripcion.py`. No confundir ambos plazos en el análisis: la
prescripción de la facultad de liquidar/girar no extingue por sí sola la
acción penal, ni a la inversa.

### 2.4 Ley de IVA — crédito fiscal y facturas falsas (arts. 23-28)

Los arts. 23 a 28 DL 825 (verificados) regulan el crédito fiscal —el
mecanismo mediante el cual el contribuyente descuenta el IVA soportado en
sus compras del IVA que debe enterar en arcas fiscales—. Es precisamente
este mecanismo el que las maniobras de facturación falsa buscan explotar,
inflando artificialmente el crédito fiscal mediante facturas que no
respaldan una operación real o que no son fidedignas. El art. 8 (verificado)
define el hecho gravado; los arts. 2 y 3 (verificados), las definiciones
generales y la calidad de contribuyente. El encuadre penal de esta maniobra
se sitúa en el Código Tributario (art. 97, sección 2.1), no en el DL 825,
que es la norma sustantiva que explica el mecanismo abusado, no el tipo
penal aplicable.

### 2.5 Ley de Renta — incremento patrimonial no justificado y gastos (arts. 21, 31, 33, 70)

El art. 70 DL 824 (verificado) contiene la regla de justificación de
inversiones, gastos y desembolsos: cuando el contribuyente no logra
justificar el origen de los fondos con que financió una inversión, gasto o
desembolso, esos fondos se presumen renta afecta a impuesto. Es la
herramienta sustantiva de uso más frecuente para evidenciar, en sede
tributaria, un patrimonio no declarado —función que en el análisis forense
financiero de `references/forense-financiero.md` se articula con las
diferencias entre lo declarado (F22/F29) y los flujos observados—. El art. 21
(verificado) regula el tratamiento de los retiros y gastos rechazados de las
empresas, relevante cuando un controlador desvía fondos sociales bajo la
apariencia de gastos del giro; el art. 31 (verificado) define los requisitos
de los gastos necesarios para producir la renta —el estándar frente al cual
se contrastan los gastos simulados—; el art. 33 (verificado) regula los
agregados y deducciones para determinar la renta líquida imponible; el
art. 2 (verificado) contiene las definiciones generales de renta devengada y
percibida, relevantes para fijar el momento de la obligación tributaria
eludida o evadida.

---

## 3. Extractos verificados

## CODIGO TRIBUTARIO (CT)

> **Fuente oficial**: Biblioteca del Congreso Nacional — LeyChile, servicio XML `obtxml opt=7`, idNorma 6374 (Decreto Ley 830), publicada el 1974-12-31.
> **Versión de la norma**: 2025-07-11 · **Estado**: no derogado.
> **Fecha de verificación de esta curatoría**: 2026-07-07. Todo uso posterior debe cotejar la vigencia en LeyChile.

### CT — Art. 8 TER
*Artículo 1 › Doble Articulado › TITULO PRELIMINAR › Párrafo 4.º Derechos de los Contribuyentes* — `idParte 9104346 · versión del artículo: 2020-02-24`

```
    Artículo 8° ter.- Los contribuyentes tendrán derecho
a que se les autoricen los documentos tributarios que sean
necesarios para el desarrollo de su giro o actividad.
    En el caso de los contribuyentes que por primera vez
deben emitir dichos documentos, la autorización procederá
previa entrega de una declaración jurada simple sobre la
existencia de su domicilio y la efectividad de las
instalaciones que, de acuerdo a la naturaleza de las
actividades o giro declarado por el contribuyente, permitan
el desarrollo de los mismos, efectuada en la forma y por los
medios que disponga el Servicio. Lo anterior es sin
perjuicio del ejercicio de las facultades de fiscalización
del Servicio.
    Las autorizaciones otorgadas conforme a este artículo
podrán ser diferidas, revocadas o restringidas, por la
Dirección Regional, mediante resolución fundada a
contribuyentes que se encuentren en algunas de las
situaciones a que se refieren las letras b), c) y d) del
artículo 59 bis, y sólo mientras subsistan las razones que
fundamentan tales medidas, y a contribuyentes respecto a los
cuales se haya dispuesto un cambio total de sujeto de
acuerdo a lo dispuesto en el artículo 3° del decreto ley
N°825, de 1974.
    La presentación maliciosa de la declaración jurada
simple a que se refiere el inciso segundo, conteniendo datos
o antecedentes falsos, configurará la infracción prevista
en el inciso primero del número 23 del artículo 97 y se
sancionará con la pena allí asignada, la que se podrá
aumentar hasta un grado atendida la gravedad de la conducta
desplegada, y multa de hasta 10 unidades tributarias
anuales.
```

### CT — Art. 97
*Artículo 1 › Doble Articulado › LIBRO SEGUNDO DE LOS APREMIOS Y DE LAS INFRACCIONES Y SANCIONES › TITULO II De las infracciones y sanciones. › Párrafo 1º. De los contribuyentes y otros obligados* — `idParte 8573433 · versión del artículo: 2024-10-24`

```
    Artículo 97.- Las siguientes infracciones a las
disposiciones tributarias serán sancionadas en la forma que
a continuación se indica:

    1°.- El retardo u omisión en la presentación de
declaraciones, informes o solicitudes de inscripciones en
roles o registros obligatorios, que no constituyan la base
inmediata para la determinación o liquidación de un
impuesto, con multa de una unidad tributaria mensual a una
unidad tributaria anual. En caso de retardo u omisión en la
presentación de informes referidos a operaciones realizadas
o antecedentes relacionados con terceras personas, se
aplicarán las multas contempladas en el inciso anterior.
Sin embargo, si requerido posteriormente bajo apercibimiento
por el Servicio, el contribuyente no da cumplimiento a estas
obligaciones legales en el plazo de 30 días, se le
aplicará además, una multa que será de hasta 0,2 Unidades
Tributarias Mensuales por cada mes o fracción de mes de
atraso y por cada persona que se haya omitido, o respecto de
la cual se haya retardado la presentación respectiva. Con
todo, la multa máxima que corresponda aplicar no podrá
exceder a 30 Unidades Tributarias Anuales, ya sea que el
infractor se trate de un contribuyente o de un Organismo de
la Administración del Estado.
    2°.- El retardo u omisión en la presentación de
declaraciones o informes, que constituyan la base inmediata
para la determinación o liquidación de un impuesto, con
multa de diez por ciento de los impuestos que resulten de la
liquidación, siempre que dicho retardo u omisión no sea
superior a 5 meses. Pasado este plazo, la multa indicada se
aumentará en un dos por ciento por cada mes o fracción de
mes de retardo, no pudiendo exceder el total de ella del
treinta por ciento de los impuestos adeudados.
    Esta multa no se impondrá en aquellas situaciones en
que proceda también la aplicación de la multa por atraso
en el pago, establecida en el N° 11 de este artículo y la
declaración no haya podido efectuarse por tratarse de un
caso en que no se acepta la declaración sin el pago.
    El retardo u omisión en la presentación de
declaraciones que no impliquen la obligación de efectuar un
pago inmediato, por estar cubierto el impuesto a juicio del
contribuyente, pero que puedan constituir la base para
determinar o liquidar un impuesto, con multa de una unidad
tributaria mensual a una unidad tributaria anual.
    3°.- La declaración incompleta o errónea, la omisión
de balances o documentos anexos a la declaración o la
presentación incompleta de éstos que puedan inducir a la
liquidación de un impuesto inferior al que corresponda, a
menos que el contribuyente pruebe haber empleado la debida
diligencia, con multa del cinco por ciento al veinte por
ciento de las diferencias de impuesto que resultaren.
    4°.- Las declaraciones maliciosamente incompletas o
falsas que puedan inducir a la liquidación de un impuesto
inferior al que corresponda o la omisión maliciosa en los
libros de contabilidad de los asientos relativos a las
mercaderías adquiridas, enajenadas o permutadas o a las
demás operaciones gravadas, la adulteración de balances o
inventarios o la presentación de éstos dolosamente
falseados, el uso de boletas, notas de débito, notas de
crédito o facturas ya utilizadas en operaciones anteriores,
o el empleo de otros procedimientos dolosos encaminados a
ocultar o desfigurar el verdadero monto de las operaciones
realizadas o a burlar el impuesto, con multa del cien por
ciento al trescientos por ciento del valor del tributo
defraudado y con presidio menor en su grado máximo.
    Los contribuyentes afectos al Impuesto a las Ventas y
Servicios u otros impuestos sujetos a retención o recargo,
que realicen maliciosamente cualquiera maniobra tendiente a
aumentar el verdadero monto de los créditos o imputaciones
que tengan derecho a hacer valer, en relación con las
cantidades que deban pagar, serán sancionados con la pena
de presidio menor en su grado máximo a presidio mayor en su
grado mínimo y con multa del cien por ciento al trescientos
por ciento de lo defraudado.
    El que, mediante cualquier maniobra fraudulenta,
obtuviere devoluciones de impuesto que no le correspondan,
será sancionado con la pena de presidio menor en su grado
máximo a presidio mayor en su grado medio y con multa del
cien por ciento al cuatrocientos por ciento de lo
defraudado.
    Si, como medio para cometer los delitos previstos en los
incisos anteriores, se hubiere hecho uso malicioso de
facturas u otros documentos falsos, fraudulentos o
adulterados, se aplicará la pena mayor asignada al delito
más grave.
    El que confeccione, venda o facilite, a cualquier
título, guías de despacho, facturas, notas de débito,
notas de crédit o boletas falsas, con o sin timbre del
Servicio, será sancionado con la pena de presidio menor en
su grado medio y multa de hasta 40 unidades tributarias
anuales.
     El que incurra en alguna de las conductas señaladas en
el párrafo anterior para cometer o posibilitar la comisión
de delitos de este número, será sancionado con la pena de
presidio menor en su grado máximo y multa de hasta 100
unidades tributarias anuales.
    5°.- La omisión maliciosa de declaraciones exigidas
por las leyes tributarias para la determinación o
liquidación de un impuesto, en que incurran el
contribuyente o su representante, y los gerentes y
administradores de personas jurídicas o los socios que
tengan el uso de la razón social, con multa del cincuenta
por ciento al trescientos por ciento del impuesto que se
trata de eludir y con presidio menor en sus grados medio a
máximo.
    6°.- La no exhibición de libros de contabilidad o de
libros auxiliares y otros documentos exigidos por el
Director o el Director Regional de acuerdo con las
disposiciones legales, la oposición al examen de los mismos
o a la inspección de establecimientos de comercio,
agrícolas, industriales o minerales, o el acto de entrabar
en cualquier forma la fiscalización ejercida en conformidad
a la ley, con multa de una unidad tributaria mensual a una
unidad tributaria anual. Sin embargo, respecto de
contribuyentes cuyos ingresos por ventas y servicios y otras
actividades del giro hayan superado las 50.000 unidades de
fomento durante el año comercial inmediatamente anterior,
que no exhiban o aporten antecedentes específicamente
requeridos en un procedimiento de fiscalización iniciado
conforme al artículo 59, les será aplicable la multa
establecida en el párrafo siguiente con las mismas
limitaciones.
    El que incumpla o entrabe la obligación de implementar
y utilizar sistemas tecnológicos de información conforme
al artículo 60 ter, con una multa de hasta 60 unidades
tributarias anuales, con un límite equivalente al 15% del
capital efectivo determinado al término del año comercial
anterior a aquel en que se cometió la infracción. En caso
que el contribuyente no esté obligado a determinarlo o no
sea posible hacerlo, la multa a aplicar será de 1 a 5
unidades tributarias anuales.
    Los contribuyentes autorizados a sustituir sus libros de
contabilidad por hojas sueltas llevadas en forma
computacional y aquellos autorizados a llevar sus
inventarios, balances, libros o registros contables o
auxiliares y todo otro documento de carácter tributario
mediante aplicaciones informáticas, medios electrónicos u
otros sistemas tecnológicos, que entraben, impidan o
interfieran de cualquier forma la fiscalización ejercida
conforme a la ley, con una multa de hasta 30 unidades
tributarias anuales, con un límite equivalente al 10% del
capital efectivo determinado al término del año comercial
anterior a aquel en que se cometió la infracción. En caso
que el contribuyente no esté obligado a determinarlo o no
sea posible hacerlo, la multa a aplicar será de 1 unidad
tributaria anual.
    7°.- El hecho de no llevar la contabilidad o los libros
auxiliares exigidos por el Director o el Director Regional
de acuerdo con las disposiciones legales, o de mantenerlos
atrasados, o de llevarlos en forma distinta a la ordenada o
autorizada por la ley, y siempre que no se dé cumplimiento
a las obligaciones respectivas dentro del plazo que señale
el Servicio, que no podrá ser inferior a diez días, con
multa de una unidad tributaria mensual a una unidad
tributaria anual.
    8°.- El comercio ejercido a sabiendas sobre
mercaderías, valores o especies de cualquiera naturaleza
sin que se hayan cumplido las exigencias legales relativas a
la declaración y pago de los impuestos que graven su
producción o comercio, con multa del cincuenta por ciento
al cuatrocientos por ciento de los impuestos eludidos y con
presidio o relegación menores en cualquiera de sus grados.
La reincidencia será sancionada con pena de presidio o
relegación menores en su grado máximo.
     Para la determinación de la pena aplicable el tribunal
tendrá especialmente en cuenta el valor de las especies
comerciadas o elaboradas.
    9°.- El ejercicio clandestino en cualquier de sus
formas del comercio o de la industria con multa de una
unidad tributaria anual a diez unidades tributarias anuales
y presidio o relegación menores en cualquiera de sus grados
y, además, con el comiso de los productos en instalaciones
de fabricación y envases respectivos. La reincidencia será
sancionada con pena de presidio o relegación menores en sus
grados medio a máximo.
     Para la determinación de la pena aplicable el tribunal
tendrá especialmente en cuenta el valor de las especies
comerciadas o elaboradas.
    10°.- El no otorgamiento o el no envío de la
información electrónica al Servicio de guías de despacho
de facturas, notas de débito, notas de crédito o boletas
en los casos y en la forma exigidos por las leyes, el uso de
boletas no autorizadas o de facturas, notas de débito,
notas de crédito o guías de despacho sin el timbre
correspondiente, el fraccionamiento del monto de las ventas
o el de otras operaciones para eludir el otorgamiento de
boletas, con multa del cincuenta por ciento al quinientos
por ciento del monto de la operación, con un mínimo de 2
unidades tributarias mensuales y un máximo de 40 unidades
tributarias anuales.
     En el caso de las infracciones señaladas en el
párrafo primero, éstas además deberán ser sancionadas
con clausura de hasta veinte días de la oficina, estudio,
establecimiento, sucursal, medio de transporte, maquinaria o
similar en que se haya cometido la infracción, el sitio en
internet o del sitio dentro de la plataforma virtual o
digital a través de la cual el contribuyente realiza el
ejercicio de la actividad comercial. Asimismo, no se
autorizará ni se permitirá la emisión al contribuyente de
documentos tributarios. En caso de reiteración de
infracciones, de acuerdo al párrafo tercero, el Director
podrá solicitar la suspensión del dominio web o suspender
el acceso al proveedor de pago o similar por el periodo que
dure la clausura.
    La reiteración de las infracciones señaladas en este
número se sancionará además con presidio o relegación
menor en su grado máximo. Para estos efectos se entenderá
que hay reiteración cuando se cometan dos o más
infracciones entre las cuales no medie un período superior
a tres años.
    Para los efectos de aplicar la clausura, el Servicio
podrá requerir el auxilio de la fuerza pública, la que
será concedida sin ningún trámite previo por el Cuerpo de
Carabineros, pudiendo procederse con allanamiento y
descerrajamiento si fuere necesario. En todo caso, se
pondrán sellos oficiales y carteles en los establecimientos
clausurados.
    Cada sucursal se entenderá como establecimiento
distinto para los efectos de este número.
    En los casos de clausura, el infractor deberá pagar a
sus dependientes las correspondientes remuneraciones
mientras dure aquélla. No tendrán este derecho los
dependientes que hubieren hecho incurrir al contribuyente en
la sanción.
    11°.- El retardo en enterar en Tesorería impuestos
sujetos a retención o recargo, con multa de un diez por
ciento de los impuestos adeudados. La multa indicada se
aumentará en un dos por ciento por cada mes o fracción de
mes de retardo, no pudiendo exceder el total de ella del
treinta por ciento de los impuestos adeudados.
    En los casos en que la omisión de la declaración en
todo o en parte de los impuestos que se encuentren retenidos
o recargados haya sido detectada por el Servicio en procesos
de fiscalización, la multa prevista en este número y su
límite máximo, serán de veinte y sesenta por ciento,
respectivamente.
    12°.- La reapertura de un establecimiento comercial o
industrial o de la sección que corresponda, el uso de
medios de transporte, maquinarias o similares, el uso de la
plataforma virtual o digital mediante la cual realiza su
actividad, o la emisión de documentos tributarios en papel
o electrónicos, con violación de una clausura impuesta por
el Servicio, con multa del veinte por ciento de una unidad
tributaria anual a dos unidades tributarias anuales y con
presidio o relegación menor en su grado medio.
    13°.- La destrucción o alteración de los sellos o
cerraduras puestos por el Servicio, o la realización de
cualquiera otra operación destinada a desvirtuar la
oposición de sello o cerraduras, con multa de media unidad
tributaria anual a cuatro unidades tributarias anuales y con
presidio menor en su grado medio.
    Salvo prueba en contrario, en los casos del inciso
precedente se presume la responsabilidad del contribuyente
y, tratándose de personas jurídicas, de su representante
legal.
    14°.- La sustracción, ocultación o enajenación de
especies que queden retenidas en poder del presunto
infractor, en caso de que se hayan adoptado medidas
conservativas, con multa de media unidad tributaria anual a
cuatro unidades tributarias anuales y con presidio menor en
su grado medio.
    La misma sanción se aplicará al que impidiere en forma
ilegítima el cumplimiento de la sentencia que ordene el
comiso.
    15°.- El incumplimiento de cualquiera de las
obligaciones establecidas en los artículos 34° y 60°
inciso penúltimo, con una multa del veinte por ciento al
cien por ciento de una unidad tributaria anual.
    16°.- La pérdida o inutilización no fortuita de los
libros de contabilidad o documentos que sirvan para
acreditar las anotaciones contables o que estén
relacionados con las actividades afectas a cualquier
impuesto, se sancionará de la siguiente manera:

    a) Con multa de una unidad tributaria mensual a veinte
unidades tributarias anuales, la que, en todo caso, no
podrá exceder de 15% del capital propio; o
    b) Si los contribuyentes no deben determinar capital
propio, resulta imposible su determinación o aquél es
negativo, con multa de media unidad tributaria mensual hasta
diez unidades tributarias anuales.

    Se presumirá no fortuita, salvo prueba en contrario, la
pérdida o inutilización de los libros de contabilidad o
documentos mencionados en el inciso primero, cuando se dé
aviso de este hecho o se lo detecte con posterioridad a una
notificación o cualquier otro requerimiento del Servicio
que diga relación con dichos libros y documentación.
Además, en estos casos, la pérdida o inutilización no
fortuita se sancionará de la forma que sigue:

    a) Con multa de una unidad tributaria mensual a treinta
unidades tributarias anuales, la que, en todo caso, no
podrá exceder de 25% del capital propio; o
    b) Si los contribuyentes no deben determinar capital
propio, no es posible determinarlo o resulta negativo, la
multa se aplicará con un mínimo de una unidad tributaria
mensual a un máximo de veinte unidades tributarias anuales.

    La pérdida o inutilización de los libros de
contabilidad o documentos mencionados en el inciso primero
materializada como procedimiento doloso encaminado a ocultar
o desfigurar el verdadero monto de las operaciones
realizadas o a burlar el impuesto, será sancionada conforme
a lo dispuesto en el inciso primero del N° 4° del
artículo 97 del Código Tributario.
    En todos los casos de pérdida o inutilización, los
contribuyentes deberán:

    a) Dar aviso al Servicio dentro de los 10 días
siguientes, y
    b) Reconstituir la contabilidad dentro del plazo y
conforme a las normas que fije el Servicio, plazo que no
podrá ser inferior a treinta días.

    El incumplimiento de lo previsto en el inciso anterior,
será sancionado con multa de hasta diez unidades
tributarias mensuales.
    Para los efectos previstos en los incisos primero y
segundo de este número, se entenderá por capital propio el
definido en el artículo 41, Nº 1°, de la Ley sobre
Impuesto a la Renta, vigente al inicio del año comercial en
que ocurra la pérdida o inutilización.
    En todo caso, la pérdida o inutilización de los libros
de contabilidad suspenderá la prescripción establecida en
los incisos primero y segundo del artículo 200, hasta la
fecha en que los libros legalmente reconstituidos queden a
disposición del Servicio.
    17°.- La movilización o traslado de bienes corporales
muebles realizado en vehículos destinados al transporte de
carga sin la correspondiente guía de despacho o factura,
otorgadas en la forma exigida por las leyes, será
sancionado con una multa del 10% al 200% de una unidad
tributaria anual. Si la movilización o traslado a que se
refiere el presente párrafo se realizare a sabiendas o
debiendo saber que no se han cumplido las exigencias legales
relativas a la declaración y pago de impuestos que graven
la producción o comercio, o que los bienes movilizados o
trasladados son falsos o de comercialización prohibida, la
multa será del 20% al 300% de una unidad tributaria anual.
    Sorprendida la infracción, el vehículo no podrá
continuar hacia el lugar de destino mientras no se exhiba la
guía de despacho o factura correspondiente a la carga
movilizada, pudiendo, en todo caso, regresar a su lugar de
origen. Esta sanción se hará efectiva con la sola
notificación del acta de denuncio y en su contra no
procederá recurso alguno. En caso de que la infracción se
cometa a propósito de la movilización o traslado de los
bienes indicados en la oración final del párrafo anterior,
se procederá a la incautación de los bienes.
    Para llevar a efecto la medida de que trata el inciso
anterior, el funcionario encargado de la diligencia podrá
recurrir al auxilio de la fuerza pública, la que le será
concedida por el Jefe de Carabineros más inmediato, y en el
menor plazo posible, sin más trámite, pudiendo procederse
con allanamiento y descerrajamiento si fuere necesario.
    18°.- Los que compren y vendan fajas de control de
impuestos o entradas a espectáculos públicos en forma
ilícita, serán sancionados con multa de uno a diez
unidades tributarias anuales y con presidio menor en su
grado medio.
    La sanción pecuniaria establecida en el inciso
precedente podrá hacerse efectiva indistintamente en contra
del que compre, venda o mantenga fajas de control y entradas
a espectáculos públicos en forma ilícita.
    19°.- El incumplimiento de la obligación de exigir el
otorgamiento de la factura o boleta, en su caso, y de
retirarla del local o establecimiento del emisor, será
sancionado con multa de hasta una unidad tributaria mensual
en el caso de las boletas, y de hasta veinte unidades
tributarias mensuales en el caso de facturas, previos los
trámites del procedimiento contemplado en el artículo 165
de este Código, y sin perjuicio de que al sorprenderse la
infracción, el funcionario del Servicio pueda solicitar el
auxilio de la fuerza pública para obtener la debida
identificación del infractor, dejándose constancia en la
unidad policial respectiva.
    20°.- La deducción como gasto o uso del crédito
fiscal que efectúen, en forma reiterada, los contribuyentes
del impuesto de Primera Categoría de la Ley de la Renta,
que no sean sociedades anónimas abiertas, de desembolsos
que sean rechazados o que no den derecho a dicho crédito,
de acuerdo a la Ley de la Renta o al decreto ley Nº 825, de
1974, por el hecho de ceder en beneficio personal y gratuito
del propietario o socio de la empresa, su cónyuge o hijos,
o de una tercera persona que no tenga relación laboral o de
servicios con la empresa que justifique el desembolso o el
uso del crédito fiscal, con multa de hasta el 200% de todos
los impuestos que deberían haberse enterado en arcas
fiscales, de no mediar la deducción indebida. La misma
multa se aplicará cuando el contribuyente haya deducido los
gastos o hecho uso del crédito fiscal respecto de los
vehículos y aquellos incurridos en supermercados y
comercios similares, a que se refiere el artículo 31 de la
ley sobre Impuesto a la Renta, sin cumplir con los
requisitos que dicha disposición establece.
    21º.- La no comparecencia injustificada ante el
Servicio, a un segundo requerimiento notificado al
contribuyente conforme a lo dispuesto en el artículo 11,
con una multa de una unidad tributaria mensual a una unidad
tributaria anual, la que se aplicará en relación al
perjuicio fiscal comprometido y procederá transcurridos 20
días desde el plazo de comparecencia indicado en la segunda
notificación. El Servicio deberá certificar la
concurrencia del contribuyente al requerimiento notificado.
    22.- El que autorice folios de facturas, boletas, guías
de despacho, notas de crédito, notas de débito u otros
documentos tributarios electrónicos a sabiendas que serán
utilizados para defraudar al Fisco, será sancionado con
pena de presidio menor en su grado máximo y multa de hasta
10 unidades tributarias anuales.
    23º.- El que maliciosamente proporcionare datos o
antecedentes falsos en la declaración inicial de
actividades o en sus modificaciones o en las declaraciones
exigidas con el objeto de obtener autorización de
documentación tributaria, será sancionado con la pena de
presidio menor en su grado máximo y con multa de hasta ocho
unidades tributarias anuales.
    El que concertado facilitare los medios para que en las
referidas presentaciones se incluyan maliciosamente datos o
antecedentes falsos, será sancionado con la pena de
presidio menor en su grado mínimo y con multa de una unidad
tributaria mensual a una unidad tributaria anual.
    24°.- Los contribuyentes de los impuestos establecidos
en la Ley sobre Impuesto a la Renta, que dolosamente reciban
contraprestaciones de las instituciones a las cuales
efectúen donaciones, en los términos establecidos en los
incisos primero y segundo del artículo 11 de la ley N°
19.885, sea en beneficio propio o en beneficio personal de
sus socios, directores o empleados, o del cónyuge o de los
parientes consanguíneos hasta el segundo grado, de
cualquiera de los nombrados, o simulen una donación, en
ambos casos, de aquellas que otorgan algún tipo de
beneficio tributario que implique en definitiva un menor
pago de algunos de los impuestos referidos, serán
sancionados con la pena de presidio menor en sus grados
mínimo a medio.
    Para los efectos de lo dispuesto en el inciso
precedente, se entenderá que existe una contraprestación
cuando en el lapso que media entre los seis meses anteriores
a la fecha de materializarse la donación y los veinticuatro
meses siguientes a esa data, el donatario entregue o se
obligue a entregar una suma de dinero o especies o preste o
se obligue a prestar servicios, cualquiera de ellos
avaluados en una suma superior al 10% del monto donado o
superior a 15 Unidades Tributarias Mensuales en el año a
cualquiera de los nombrados en dicho inciso.
    El donatario que dolosamente destine o utilice
donaciones de aquellas que las leyes permiten rebajar de la
base imponible afecta a los impuestos de la Ley sobre
Impuesto a la Renta o que otorgan crédito en contra de
dichos impuestos, a fines distintos de los que corresponden
a la entidad donataria de acuerdo a sus estatutos, será
sancionado con la pena de presidio menor en sus grados medio
a máximo.
    25.- El que actúe como usuario de las Zonas Francas
establecidas por ley, sin tener la habilitación
correspondiente, o teniéndola, la haya utilizado con la
finalidad de defraudar al Fisco, será sancionado con una
multa de hasta ocho Unidades Tributarias Anuales y con
presidio menor en sus grados medio a máximo.
    Se sancionará con las penas establecidas en el inciso
anterior a quien efectúe transacciones con una persona que
actúe como usuario de Zona Franca, sabiendo que éste no
cuenta con la habilitación correspondiente o teniéndola,
la utiliza con la finalidad de defraudar al Fisco.
    26.- La venta o abastecimiento clandestinos de gas
natural comprimido o gas licuado de petróleo para consumo
vehicular, entendiéndose por tal aquellas realizadas por
personas que no cuenten con las autorizaciones establecidas
en el inciso cuarto del artículo 2º de la ley Nº 18.502,
será penado con presidio menor en su grado mínimo a medio
y una multa de hasta cuarenta unidades tributarias anuales.
     27. El que habiendo tomado conocimiento del inicio de
un procedimiento administrativo o judicial tendiente a la
determinación o liquidación del impuesto o el cobro
judicial de obligaciones tributarias, ejecute actos o
contratos que disminuyan su activo o aumenten su pasivo sin
otra justificación económica o jurídica que la de
perjudicar a la administración tributaria o frustrar total
o parcialmente el cumplimiento de sus obligaciones
tributarias, será castigado con la pena de presidio menor
en su grado máximo.
```

### CT — Art. 98
*Artículo 1 › Doble Articulado › LIBRO SEGUNDO DE LOS APREMIOS Y DE LAS INFRACCIONES Y SANCIONES › TITULO II De las infracciones y sanciones. › Párrafo 1º. De los contribuyentes y otros obligados* — `idParte 8573436 · versión del artículo: 2020-02-24`

```
    Artículo 98.- De las sanciones pecuniarias responden el
contribuyente y las demás personas legalmente obligadas.
Tratándose de personas jurídicas, serán solidariamente
responsables el gerente general, administrador o quienes
cumplan las tareas de éstos, y los socios a quienes
corresponda dicho cumplimiento, pero sólo en el caso que
hayan incurrido personalmente en las infracciones. Se
entenderá que incurren personalmente en las infracciones
quienes hayan tomado parte en la ejecución del hecho, sea
de una manera inmediata y directa, sea impidiendo o
procurando impedir que se evite, o quienes, concertados para
su ejecución, facilitan los medios con que se lleva a
efecto el hecho o lo presencian sin tomar parte inmediata en
él.
```

### CT — Art. 99
*Artículo 1 › Doble Articulado › LIBRO SEGUNDO DE LOS APREMIOS Y DE LAS INFRACCIONES Y SANCIONES › TITULO II De las infracciones y sanciones. › Párrafo 1º. De los contribuyentes y otros obligados* — `idParte 8573437 · versión del artículo: 2020-02-24`

```
    Artículo 99.- Las sanciones corporales y los apremios,
en su caso, se aplicarán a quien debió cumplir la
obligación y, tratándose de personas jurídicas, a los
gerentes, administradores o a quienes hagan las veces de
éstos y a los socios a quienes corresponda dicho
cumplimiento, pero sólo en el caso que hayan personalmente
incurrido en las infracciones. Se entenderá que incurren
personalmente en las infracciones quienes hayan tomado parte
en la ejecución del hecho, sea de una manera inmediata y
directa, sea impidiendo o procurando impedir que se evite, o
quienes, concertados para su ejecución, facilitan los
medios con que se lleva a efecto el hecho o lo presencian
sin tomar parte inmediata en él.
```

### CT — Art. 100
*Artículo 1 › Doble Articulado › LIBRO SEGUNDO DE LOS APREMIOS Y DE LAS INFRACCIONES Y SANCIONES › TITULO II De las infracciones y sanciones. › Párrafo 1º. De los contribuyentes y otros obligados* — `idParte 8573438 · versión del artículo: 1980-07-02`

```
    Artículo 100.- El contador que al confeccionar o firmar
cualquier declaración o balance o que como encargado de la
contabilidad de un contribuyente incurriere en falsedad o
actos dolosos, será sancionado con multa de una a diez
unidades tributarias anuales y podrá ser castigado con
presidio menor en sus grados medio a máximo, según la
gravedad de la infracción, a menos que le correspondiere
una pena mayor como copartícipe del delito del
contribuyente, en cuyo caso se aplicará esta última.
Además, se oficiará al Colegio de Contadores para los
efectos de las sanciones que procedan.
    Salvo prueba en contrario, no se considerará dolosa o
maliciosa la intervención del contador, si existe en los
libros de contabilidad, o al término de cada ejercicio, la
declaración firmada del contribuyente, dejando constancia
de que los asientos corresponden a datos que éste ha
proporcionado como fidedignos.
```

### CT — Art. 100 BIS
*Artículo 1 › Doble Articulado › LIBRO SEGUNDO DE LOS APREMIOS Y DE LAS INFRACCIONES Y SANCIONES › TITULO II De las infracciones y sanciones. › Párrafo 1º. De los contribuyentes y otros obligados* — `idParte 9510279 · versión del artículo: 2025-07-11`

```
    Artículo 100 bis.- La persona natural o jurídica,
respecto de quien se acredite haber diseñado o planificado
los actos, contratos o negocios respecto de los que se
hubiera declarado la existencia de abuso o simulación,
según lo dispuesto en los artículos 4 ter, 4 quáter, y 4
quinquies, será sancionada con las multas que se indican a
continuación.
    La persona que haya diseñado o planificado los actos,
contratos o negocios distinta del contribuyente, será
sancionada con multa de 100 unidades tributarias anuales,
salvo que: (a) exista reiteración respecto del mismo
diseño o planificación, en cuyo caso la multa será de 250
unidades tributarias anuales; o (b) se acredite que los
honorarios pactados sean superiores a 100 unidades
tributarias anuales, caso en el cual la multa podrá
extenderse hasta el total de los honorarios pactados con un
tope de 250 unidades tributarias anuales. En caso de que el
tercero fuese una persona jurídica, serán solidariamente
responsables las personas naturales o jurídicas que hayan
ejercido el cargo de directores, representantes o
administradores del asesor, si han infringido sus deberes de
dirección y supervisión respecto de éste, en
consideración a los estándares establecidos en la Ley N°
20.393 que Establece la Responsabilidad Penal de las
Personas Jurídicas.
    En aquellos casos en que no exista un tercero que haya
diseñado o planificado los actos, negocios o contratos
respecto de los cuales se hubiere declarado la existencia de
abuso o simulación, según lo dispuesto en los artículos 4
ter, 4 quáter, y 4 quinquies, o cuando existiendo el
tercero el contribuyente no lo haya identificado dentro del
proceso de fiscalización, será el contribuyente el
sancionado con una multa equivalente al 100% de las
diferencias de impuesto determinadas con un tope de 250
unidades tributarias anuales. En caso de existir, serán
solidariamente responsables de la multa la o las personas
naturales o jurídicas que hayan ejercido el cargo de
directores, representantes y/o administradores de los
mencionados contribuyentes al momento de cometerse el
conjunto o series de hechos, actos o negocios jurídicos, si
hubieren infringido sus deberes de dirección y supervisión
respecto del contribuyente sancionado, en consideración a
los estándares establecidos en la ley N° 20.393 que
Establece la Responsabilidad Penal de las Personas
Jurídicas.
    No aplicará la multa dispuesta en el inciso anterior
respecto de contribuyentes que determinen sus rentas
conforme a lo dispuesto en la letra D del artículo 14 de la
ley de la Renta.
    La multa a que se refiere el presente artículo deberá
solicitarse conforme el procedimiento establecido en el
artículo 160 bis, y deberá interponerse conjuntamente con
el requerimiento de declaración de existencia de abuso o
simulación, ante el mismo tribunal. Una vez declarada la
elusión, el tribunal deberá pronunciarse en la sentencia
sobre la procedencia de la multa y su monto. La multa solo
será exigible una vez que la sentencia que declaró la
existencia de abuso o simulación y la determinación de la
responsabilidad respectiva se encuentre firme. El giro donde
conste la multa no será susceptible de reclamo alguno, a
menos que el monto de ella no se conforme con lo fijado en
la sentencia que le sirve de antecedente.
    La acción de cobro de la Tesorería respecto de las
sanciones pecuniarias impuestas al contribuyente o, en su
caso, a sus directores, representantes y/o administradores,
prescribirá a los tres años, contados desde la
certificación de encontrarse firme la sentencia que
declaró la existencia de abuso o simulación y la
determinación de la responsabilidad respectiva.
```

### CT — Art. 100 TER
*Artículo 1 › Doble Articulado › LIBRO SEGUNDO DE LOS APREMIOS Y DE LAS INFRACCIONES Y SANCIONES › TITULO II De las infracciones y sanciones. › Párrafo 1º. De los contribuyentes y otros obligados* — `idParte 10522077 · versión del artículo: 2024-10-24`

```
     Artículo 100 ter.- Constituye una circunstancia
calificada para que el Director decida perseguir únicamente
la aplicación de una sanción pecuniaria según señala el
inciso tercero del artículo 162 del Código Tributario, la
cooperación eficaz que un contribuyente realice dentro del
procedimiento de recopilación de antecedentes a que se
refiere el N° 10 del artículo 161 y siempre que conduzca
al esclarecimiento de delitos tributarios y permita la
identificación de los demás responsables. Se entenderá
por cooperación eficaz el suministro de datos o
informaciones sustanciales, precisos, verídicos y
comprobables, desconocidos por el Servicio, sin los cuales
no se hubiese podido alcanzar los fines señalados.
    El Servicio, mediante resolución, establecerá los
parámetros objetivos para determinar el carácter
sustancial, preciso, veraz, comprobable y desconocido de los
antecedentes aportados.
    En el evento que la mencionada cooperación eficaz se
verifique durante la investigación a cargo del Ministerio
Público una vez presentada la denuncia o querella en los
términos del inciso primero del artículo 162, se podrá
reducir la pena hasta en dos grados, siempre que la
colaboración también se efectúe con el Ministerio
Público. La reducción de pena se determinará con
posterioridad a la individualización de la sanción penal
según las circunstancias atenuantes o agravantes comunes
que concurran; o de su compensación, de acuerdo con las
reglas generales.
    Lo dispuesto en el presente artículo no será aplicable
cuando la colaboración se refiera a delitos cometidos
únicamente por el contribuyente.
```

### CT — Art. 100 QUÁTER
*Artículo 1 › Doble Articulado › LIBRO SEGUNDO DE LOS APREMIOS Y DE LAS INFRACCIONES Y SANCIONES › TITULO II De las infracciones y sanciones. › Párrafo 1º. De los contribuyentes y otros obligados* — `idParte 10522078 · versión del artículo: 2024-10-24`

```
     Artículo 100 quáter.- Tendrán la calidad de
denunciantes anónimos las personas naturales que de manera
voluntaria y en la forma que establezca el Servicio mediante
resolución colaboren con investigaciones de hechos
constitutivos de delitos tributarios aportando antecedentes
sustanciales, precisos, veraces, comprobables y desconocidos
para el Servicio, para la detección, constatación o
acreditación de éstos, o de la participación del o de los
responsables de dichos delitos. No tendrán la calidad de
denunciantes anónimos quienes hayan incurrido en la
conducta sancionada o ejerzan un cargo de administración o
dirección respecto de la entidad denunciada cuando
corresponda o los abogados que hubiesen prestado asesoría,
durante los tres años anteriores a efectuar la denuncia.
Del mismo modo, no podrán acogerse al procedimiento
señalado en este artículo las personas naturales
querelladas, con una investigación formalizada en su
contra, acusadas o que se encuentren cumpliendo condena, por
delitos tributarios. Lo mismo regirá cuando respecto de
cualquiera de los sujetos mencionados se haya ejercido la
facultad de perseguir la multa de acuerdo al procedimiento
previsto en el artículo 100 bis o en el artículo 161, ni
quienes hayan recibido la información de las personas
inhabilitadas en los términos de este inciso.
    La calidad de denunciante anónimo se adquiere a partir
de la dictación de la resolución fundada que emita el
Servicio en la que se indique el cumplimiento de los
requisitos del inciso anterior, la que deberá ser
notificada al denunciante mediante correo electrónico. La
resolución del Servicio a que se refiere este inciso, así
como la identidad del denunciante anónimo, tendrán el
carácter de secreto, salvo que el mismo denunciante
renuncie a dicho anonimato. Las Policías, a requerimiento
del Servicio, deberán adoptar todas las medidas de
protección para el denunciante que sean pertinentes según
las necesidades de cada caso.
    Quien solicite que se le otorgue la calidad de
denunciante anónimo aportando antecedentes falsos o
fraudulentos, será sancionado con las penas de presidio
menor en su grado medio a máximo y multa de 15 unidades
tributarias mensuales, sin perjuicio de las acciones que el
denunciado pueda interponer para resarcir los perjuicios
causados. En caso de que el sancionado tenga la calidad de
denunciante anónimo según lo dispuesto en el inciso
anterior, de forma adicional perderá dicha calidad.
    La resolución señalada en el inciso segundo y la
identidad del denunciante anónimo, así como aquellos
antecedentes que puedan servir para su identificación,
tendrán el carácter de reservados conforme las reglas
establecidas en los artículos 35 y 206, y no podrán ser
divulgados en forma alguna. Únicamente podrán ser
utilizados para cumplir con los objetivos de investigación
que le son propios, salvo que el mismo denunciante renuncie
a dicho anonimato. Toda persona que haya tomado conocimiento
de la identidad de un denunciante anónimo o de quien haya
solicitado tal calidad de conformidad al inciso anterior
tendrá el deber de guardar secreto respecto de cualquier
antecedente que permita identificar a dicho denunciante, y
le será aplicable la facultad de abstenerse de declarar
únicamente sobre dichos antecedentes, en los términos
previstos en el artículo 303 del Código Procesal Penal y
en el artículo 360 del Código de Procedimiento Civil. La
infracción de la reserva de la información obtenida
mediante las disposiciones de este artículo se sancionará
con multa de 10 a 30 unidades tributarias mensuales. En caso
de que el infractor desempeñe funciones en el Servicio o en
otro organismo público, dicha infracción será sancionada,
además, con la pena de reclusión menor en cualquiera de
sus grados. Asimismo, dará lugar a responsabilidad
administrativa y se sancionará con destitución del cargo.
    De igual forma, la identidad de aquellas personas que
soliciten la calidad de denunciante anónimo y entreguen
antecedentes relativos a hechos constitutivos de delitos
tributarios y aduaneros tendrá el carácter de secreta, aun
cuando tales antecedentes no sean suficientes para dictar la
resolución referida en el inciso segundo, a menos que
proceda lo dispuesto en el inciso tercero.
    El denunciante anónimo que colabore con el Servicio de
conformidad a lo dispuesto en este artículo no será penal
ni administrativamente responsable por efectuar dicha
colaboración. Asimismo, tampoco será civilmente
responsable por los perjuicios que se produzcan por el solo
hecho de realizar la referida colaboración, salvo que
proceda la excepción establecida en el inciso tercero.
    Perderá la calidad de denunciante anónimo aquel que,
habiéndose otorgado la resolución señalada en el inciso
segundo, renuncie al anonimato o haga publicidad de la
denuncia.
```

### CT — Art. 100 QUINQUIES
*Artículo 1 › Doble Articulado › LIBRO SEGUNDO DE LOS APREMIOS Y DE LAS INFRACCIONES Y SANCIONES › TITULO II De las infracciones y sanciones. › Párrafo 1º. De los contribuyentes y otros obligados* — `idParte 10522079 · versión del artículo: 2024-10-24`

```
     Artículo 100 quinquies.- En aquellos casos que
producto de la información proporcionada se imponga
judicialmente al imputado o infractor la obligación de
pagar un monto de dinero por concepto de multa no inferior
al mínimo que establece el delito, ya sea en el proceso
penal o en un procedimiento bajo el artículo 161, con
ocasión de haberse ejercido la opción del inciso tercero
del artículo 162, el denunciante anónimo tendrá derecho a
recibir el 10% de la multa que se aplique como consecuencia
de la investigación y procedimiento en los cuales
colaboró. Para la procedencia de la retribución
establecida en el presente artículo el impuesto defraudado
deberá ser superior a 100 unidades tributarias anuales.
    Cuando distintos denunciantes anónimos hayan colaborado
en las mismas conductas sancionadas, el premio señalado en
el inciso anterior se distribuirá en la forma que determine
el Servicio mediante resolución.
    No tendrán derecho a la retribución establecida en el
presente artículo aquellos denunciantes que hubieran
renunciado al anonimato o que hubieran efectuado publicidad
de la denuncia regulada en el artículo anterior.
    Una vez enterada la multa por el infractor en la
Tesorería General de la República corresponderá a esta
institución entregar a cada denunciante anónimo el monto
correspondiente, según indique el Servicio mediante
resolución fundada. La Tesorería General de la República
deberá comunicar el pago tan pronto ello haya ocurrido, y
deberá tomar las medidas necesarias para cumplir con las
obligaciones establecidas en el inciso cuarto del artículo
anterior.
    El monto percibido por el denunciante anónimo en virtud
del presente artículo no constituirá renta y las
operaciones necesarias para efectuar el pago correspondiente
gozarán de secreto bancario.
```

### CT — Art. 100 SEXIES
*Artículo 1 › Doble Articulado › LIBRO SEGUNDO DE LOS APREMIOS Y DE LAS INFRACCIONES Y SANCIONES › TITULO II De las infracciones y sanciones. › Párrafo 1º. De los contribuyentes y otros obligados* — `idParte 10522080 · versión del artículo: 2024-10-24`

```
     Artículo 100 sexies.- Los contribuyentes que tomen
conocimiento de la existencia de diferencias de impuestos
que podrían fundarse en hechos constitutivos de delitos
tributarios, podrán efectuar una autodenuncia ante la
Dirección Nacional, siempre que cumplan los siguientes
requisitos:

    1. Acompañar una propuesta de las declaraciones de
impuesto que corresponda rectificar, las que podrán incluir
exclusivamente los tres años tributarios anteriores a aquel
en que se realiza la solicitud.
    2. No encontrarse, al momento de presentar la solicitud,
bajo un procedimiento de fiscalización por los mismos
impuestos contenidos en su autodenuncia.
    3. No haber sido condenado por delitos tributarios,
incluyendo las sentencias bajo el procedimiento del número
10 del artículo 161.
    4. No haberse aceptado con anterioridad la aplicación
del presente artículo.

    Aprobada por el Comité Ejecutivo la autodenuncia del
contribuyente, se determinarán las diferencias de impuestos
y dictarán los giros que correspondan. En estos casos el
contribuyente no será objeto de denuncia o querella en los
términos del artículo 162 ni del procedimiento del número
10 del artículo 161.
    En ningún caso las diferencias de impuesto determinadas
conforme a este artículo podrán ser objeto de condonación
respecto de los intereses y multas que correspondan. Sí
podrá accederse a un convenio de pago ante el Servicio de
Tesorerías.
    Los giros emitidos por aplicación del presente
artículo no serán objeto de recursos administrativos ni de
la reclamación contenida en el artículo 124.
    Lo dispuesto en el presente artículo no obsta a la
posibilidad de rectificar declaraciones en la medida que no
se funden en hechos constitutivos de delitos tributarios.
```

### CT — Art. 101
*Artículo 1 › Doble Articulado › LIBRO SEGUNDO DE LOS APREMIOS Y DE LAS INFRACCIONES Y SANCIONES › TITULO II De las infracciones y sanciones. › Párrafo 2º. De las infracciones cometidas por los funcionarios y ministros de fe y de las sanciones* — `idParte 8573439 · versión del artículo: 2024-10-24`

```
    Artículo 101.- Serán sancionados con suspensión de su
empleo hasta por cinco meses y el 50% de su remuneración,
los funcionarios del Servicio que cometan alguna de las
siguientes infracciones:

    1°.- Atender profesionalmente a los contribuyentes en
cuanto diga relación con la aplicación de las leyes
tributarias, excepto la atención profesional que puedan
prestar a sociedades de beneficencia, instituciones privadas
de carácter benéfico y, en general, fundaciones o
corporaciones que no persigan fines de lucro.
    2°.- Permitir o facilitar a un contribuyente el
incumplimiento de las leyes tributarias.
    3°.- Ofrecer su intervención en cualquier sentido para
reducir la carga tributaria de un contribuyente o para
liberarle, disminuirle o evitar que se le aplique una
sanción.
    4°.- Obstaculizar injustificadamente la tramitación o
resolución de un asunto o cometer abusos comprobados en el
ejercicio de su cargo.
    5°.- Infringir la obligación de guardar el secreto de
las declaraciones en los términos señalados en este
Código.

    En los casos de los números 2° y 3°, si se comprobare
que el funcionario infractor hubiere solicitado o recibido
una remuneración o recompensa, será sancionado con la
destitución de su cargo y multa del cien por ciento del
beneficio solicitado o aceptado como remuneración o
recompensa, sin perjuicio de las penas contenidas en el
Código Penal. En este caso, el plazo señalado en la letra
e) del artículo 12 del Estatuto Administrativo será de
diez años.
    Igual sanción podrá aplicarse en las infracciones
señaladas en los números 1°, 4° y 5°, atendida la
gravedad de la falta.
    La reincidencia en cualquiera de las infracciones
señaladas en los números 1°, 4° y 5°, será sancionada
con la destitución de su cargo del funcionario infractor.
```

### CT — Art. 102
*Artículo 1 › Doble Articulado › LIBRO SEGUNDO DE LOS APREMIOS Y DE LAS INFRACCIONES Y SANCIONES › TITULO II De las infracciones y sanciones. › Párrafo 2º. De las infracciones cometidas por los funcionarios y ministros de fe y de las sanciones* — `idParte 8573441 · versión del artículo: 1981-02-12`

```
    Artículo 102.- Todo funcionario, sea fiscal o municipal
o de instituciones o empresas públicas, incluyendo las que
tengan carácter fiscal, semifiscal, municipal o de
administración autónoma, que falte a las obligaciones que
le impone este Código, o las leyes tributarias, será
sancionado con multa del cinco por ciento de una unidad
tributaria anual a cuatro unidades tributarias anuales. La
reincidencia en un período de dos años será castigada con
multa de media unidad tributaria anual a cuatro unidades
tributarias anuales, sin perjuicio de las demás sanciones
que puedan aplicarse de acuerdo con el estatuto que rija sus
funciones.
```

### CT — Art. 103
*Artículo 1 › Doble Articulado › LIBRO SEGUNDO DE LOS APREMIOS Y DE LAS INFRACCIONES Y SANCIONES › TITULO II De las infracciones y sanciones. › Párrafo 2º. De las infracciones cometidas por los funcionarios y ministros de fe y de las sanciones* — `idParte 8573442 · versión del artículo: 1974-12-31`

```
    Artículo 103.- Los notarios, Conservadores, archiveros
y otros ministros de fe que infrinjan las obligaciones que
les imponen las diversas leyes tributarias, serán
sancionados en la forma prevista en dichas leyes.
```

### CT — Art. 104
*Artículo 1 › Doble Articulado › LIBRO SEGUNDO DE LOS APREMIOS Y DE LAS INFRACCIONES Y SANCIONES › TITULO II De las infracciones y sanciones. › Párrafo 2º. De las infracciones cometidas por los funcionarios y ministros de fe y de las sanciones* — `idParte 8573443 · versión del artículo: 1974-12-31`

```
    Artículo 104.- Las mismas sanciones previstas en los
artículos 102° y 103°, se impondrán a las personas en
ellos mencionadas que infrinjan las obligaciones relativas a
exigir la exhibición y dejar constancia de la cédula del
rol único tributario o en su defecto del certificado
provisorio, en aquellos casos previstos en este Código, en
el Reglamento del Rol Unico Tributario o en otras
disposiciones tributarias.
```

### CT — Art. 105
*Artículo 1 › Doble Articulado › LIBRO SEGUNDO DE LOS APREMIOS Y DE LAS INFRACCIONES Y SANCIONES › TITULO II De las infracciones y sanciones. › Párrafo 3º. Disposiciones comunes* — `idParte 8573444 · versión del artículo: 2013-02-01`

```
    Artículo 105.- Las sanciones pecuniarias serán
aplicadas administrativamente por el Servicio o por el
Tribunal Tributario y Aduanero, de acuerdo con el
procedimiento que corresponda del Libro Tercero, excepto en
aquellos casos en que de conformidad al presente Código
sean de la competencia de la justicia ordinaria civil.
    La aplicación de las sanciones pecuniarias por la
justicia ordinaria se regulará en relación a los tributos
cuya evasión resulte acreditada en el respectivo juicio.
    Sin perjuicio de lo dispuesto en el artículo 162°, si
la infracción estuviere afecta a sanción corporal o a
sanción pecuniaria y corporal, la aplicación de ellas
corresponderá a los tribunales con competencia en lo penal.
    El ejercicio de la acción penal es independiente de la
acción de determinación y cobro de impuestos.
```

### CT — Art. 106
*Artículo 1 › Doble Articulado › LIBRO SEGUNDO DE LOS APREMIOS Y DE LAS INFRACCIONES Y SANCIONES › TITULO II De las infracciones y sanciones. › Párrafo 3º. Disposiciones comunes* — `idParte 8573446 · versión del artículo: 2001-06-19`

```
    Artículo 106.- Las sanciones pecuniarias podrán ser
remitidas, rebajadas o suspendidas, a juicio exclusivo del
Director Regional si el contribuyente probare que ha
procedido con antecedentes que hagan excusable la acción u
omisión en que hubiere incurrido o si el implicado se ha
denunciado y confesado la infracción y sus circunstancias.
    Sin perjuicio de lo anterior, el Director Regional
podrá anular las denuncias notificadas por infracciones que
no constituyan amenazas para el interés fiscal u omitir los
giros de las multas que se apliquen en estos casos, de
acuerdo a normas o criterios de general aplicación que fije
el Director.
```

### CT — Art. 107
*Artículo 1 › Doble Articulado › LIBRO SEGUNDO DE LOS APREMIOS Y DE LAS INFRACCIONES Y SANCIONES › TITULO II De las infracciones y sanciones. › Párrafo 3º. Disposiciones comunes* — `idParte 8573447 · versión del artículo: 2009-01-27`

```
    Artículo 107.- Las sanciones que el Servicio o el
Tribunal Tributario y Aduanero impongan se aplicarán dentro
de los márgenes que corresponda, tomando en consideración:

    1° La calidad de reincidente en infracción de la misma
especie.
    2° La calidad de reincidente en otras infracciones
semejantes.
    3° El grado de cultura del infractor.
    4° El conocimiento que hubiere o pudiere haber tenido
de la obligación legal infringida.
    5° El perjuicio fiscal que pudiere derivarse de la
infracción.
    6° La cooperación que el infractor prestare para
esclarecer su situación.
    7° El grado de negligencia o el dolo que hubiere
mediado en el acto u omisión.
    8° Otros antecedentes análogos a los anteriores o que
parezcan justo tomar en consideración atendida la
naturaleza de la infracción y sus circunstancias.
```

### CT — Art. 108
*Artículo 1 › Doble Articulado › LIBRO SEGUNDO DE LOS APREMIOS Y DE LAS INFRACCIONES Y SANCIONES › TITULO II De las infracciones y sanciones. › Párrafo 3º. Disposiciones comunes* — `idParte 8573448 · versión del artículo: 1974-12-31`

```
    Artículo 108.- Las infracciones a las obligaciones
tributarias no producirán nulidad de los actos o contratos
en que ellas incidan, sin perjuicio de la responsabilidad
que corresponda, de conformidad a la ley, a los
contribuyentes, ministros de fe o funcionarios por el pago
de los impuestos, intereses y sanciones que procedan.
```

### CT — Art. 109
*Artículo 1 › Doble Articulado › LIBRO SEGUNDO DE LOS APREMIOS Y DE LAS INFRACCIONES Y SANCIONES › TITULO II De las infracciones y sanciones. › Párrafo 3º. Disposiciones comunes* — `idParte 8573449 · versión del artículo: 1974-12-31`

```
    Artículo 109.- Toda infracción de las normas
tributarias que no tenga señalada una sanción específica,
será sancionada con multa no inferior a un uno por ciento
ni superior a un cien por ciento de una unidad tributaria
anual, o hasta del triple del impuesto eludido si la
contravención tiene como consecuencia la evasión del
impuesto.
    Las multas establecidas en el presente Código no
estarán afectas a ninguno de los recargos actualmente
establecidos en disposiciones legales y aquellas que deban
calcularse sobre los impuestos adeudados, se determinarán
sobre los impuestos reajustados según la norma establecida
en el artículo 53.
```

### CT — Art. 110
*Artículo 1 › Doble Articulado › LIBRO SEGUNDO DE LOS APREMIOS Y DE LAS INFRACCIONES Y SANCIONES › TITULO II De las infracciones y sanciones. › Párrafo 3º. Disposiciones comunes* — `idParte 8573450 · versión del artículo: 1974-12-31`

```
    Artículo 110.- En los procesos criminales generados por
infracción de las disposiciones tributarias, podrá
constituir la causal de exención de responsabilidad penal
contemplada en el N° 12° del artículo 10° del Código
Penal o, en su defecto, la causal atenuante a que se refiere
el número 1° del artículo 11° de ese cuerpo de leyes, la
circunstancia de que el infractor de escasos recursos
pecuniarios, por su insuficiente ilustración o por alguna
otra causa justificada, haga presumir que ha tenido un
conocimiento imperfecto del alcance de las normas
infringidas. El tribunal apreciará en conciencia los hechos
constitutivos de la causal eximente o atenuante.
```

### CT — Art. 111
*Artículo 1 › Doble Articulado › LIBRO SEGUNDO DE LOS APREMIOS Y DE LAS INFRACCIONES Y SANCIONES › TITULO II De las infracciones y sanciones. › Párrafo 3º. Disposiciones comunes* — `idParte 8573451 · versión del artículo: 1980-07-02`

```
    Artículo 111.- En los procesos criminales generados por
infracción a las normas tributarias, la circunstancia de
que el hecho punible no haya acarreado perjuicio al interés
fiscal, como también el haberse pagado el impuesto debido,
sus intereses y sanciones pecuniarias, serán causales
atenuantes de responsabilidad penal.
    Constituirá circunstancia agravante de responsabilidad
penal que el delincuente haya utilizado, para la comisión
del hecho punible, asesoría tributaria, documentación
falsa, fraudulenta o adulterada, o se haya concertado con
otros para realizarlo.
    Igualmente constituirá circunstancia agravante de
responsabilidad penal que el delincuente teniendo la calidad
de productor, no haya emitido facturas, facilitando de este
modo la evasión tributaria de otros contribuyentes.
```

### CT — Art. 111 BIS
*Artículo 1 › Doble Articulado › LIBRO SEGUNDO DE LOS APREMIOS Y DE LAS INFRACCIONES Y SANCIONES › TITULO II De las infracciones y sanciones. › Párrafo 3º. Disposiciones comunes* — `idParte 10104241 · versión del artículo: 2020-02-24`

```
    Artículo 111 bis.- En los procesos criminales generados
por infracción de las disposiciones tributarias, la
imposición del monto de la multa inferior al señalado en
este Código, conforme al artículo 70 del Código Penal,
sólo procederá comprobándose un efectivo o considerable
resarcimiento al perjuicio fiscal causado, entendiéndose
para estos efectos el pago de, al menos, el 50% del monto
del impuesto adeudado, debidamente reajustado a la fecha del
pago. Lo establecido en este artículo aplicará también
para aceptar la procedencia de acuerdos reparatorios.
```

### CT — Art. 112
*Artículo 1 › Doble Articulado › LIBRO SEGUNDO DE LOS APREMIOS Y DE LAS INFRACCIONES Y SANCIONES › TITULO II De las infracciones y sanciones. › Párrafo 3º. Disposiciones comunes* — `idParte 8573452 · versión del artículo: 2002-05-31`

```
    Artículo 112.- En los casos de reiteración de
infracciones a las leyes tributarias sancionadas con pena
corporal, se aplicará la pena correspondiente a las
diversas infracciones, estimadas como un solo delito,
aumentándola, en su caso, conforme a lo dispuesto en el
artículo 351 del Código Procesal Penal.
    Sin perjuicio de lo dispuesto en el N° 10 del artículo
97 en los demás casos de infracciones a las leyes
tributarias, sancionadas con pena corporal, se entenderá
que existe reiteración cuando se incurra en cualquiera de
ellas en más de un ejercicio comercial anual.
```

### CT — Art. 113
*Artículo 1 › Doble Articulado › LIBRO SEGUNDO DE LOS APREMIOS Y DE LAS INFRACCIONES Y SANCIONES › TITULO II De las infracciones y sanciones. › Párrafo 3º. Disposiciones comunes* — `idParte 8573453 · versión del artículo: 2009-01-27`

**[DEROGADO]** — El texto se omite deliberadamente; verificar la norma derogatoria en LeyChile.

### CT — Art. 114
*Artículo 1 › Doble Articulado › LIBRO SEGUNDO DE LOS APREMIOS Y DE LAS INFRACCIONES Y SANCIONES › TITULO II De las infracciones y sanciones. › Párrafo 3º. Disposiciones comunes* — `idParte 8573454 · versión del artículo: 2017-10-20`

```
    Artículo 114.- Las acciones penales corporales y las
penas respectivas prescribirán de acuerdo con las normas
señaladas en el Código Penal.
     En los mismos plazos relativos a los crímenes o
simples delitos prescribirá la acción para perseguir la
aplicación de la pena de multa, cuando se ejerza la opción
a que se refiere el inciso tercero del artículo 162 de este
Código.
```

### CT — Art. 161
*Artículo 1 › Doble Articulado › LIBRO TERCERO DE LA COMPETENCIA PARA CONOCER DE LOS ASUNTOS CONTENCIOSOS TRIBUTARIOS, DE LOS PROCEDIMIENTOS Y DE LA PRESCRIPCIÓN › TITULO IV Del Procedimiento para la Aplicación de Sanciones › Párrafo 1º. Procedimiento general* — `idParte 8573509 · versión del artículo: 2024-10-24`

```
    Artículo 161.- Las sanciones por infracción a las
disposiciones tributarias, que no consistan en penas
privativas de libertad, serán aplicadas por el Tribunal
Tributario y Aduanero, previo el cumplimiento de los
trámites que a continuación se indican:

    1° En conocimiento de haberse cometido una infracción
o reunidos los antecedentes que hagan verosímil su
comisión, se levantará un acta por el funcionario
competente del Servicio, quien la notificará al denunciado
personalmente o por cédula.
     El acta señalada en el inciso anterior deberá ser
presentada ante el Tribunal Tributario y Aduanero
correspondiente al domicilio del denunciado, junto con la
documentación y antecedentes que le sirven de sustento y un
correo electrónico del denunciado. El Tribunal la tendrá
por recibida mediante una resolución que será notificada
al denunciado por correo electrónico y, en subsidio, a
través de su publicación en el sitio web del respectivo
tribunal. Para efectos de la notificación por correo
electrónico al denunciado el tribunal deberá considerar la
dirección electrónica que haya informado el Servicio, sin
perjuicio que de existir otra dirección informada por el
propio denunciado al tribunal deberá estarse a esta
última.
    2° El denunciado podrá formular sus descargos dentro
del plazo de diez días hábiles, contados desde la
notificación de la resolución referida en el numeral
precedente. Dicha presentación deberá cumplir con los
requisitos que establece el artículo 125.
    En las causas de cuantía igual o superior a treinta y
dos unidades tributarias mensuales, se requerirá patrocinio
y representación en los términos de los artículos 1º y
2º de la ley Nº 18.120.
    3° Pendiente el procedimiento, se podrán tomar las
medidas conservativas necesarias para evitar que
desaparezcan los antecedentes que prueben la infracción o
que se consumen los hechos que la constituyen, así como
aquellas señaladas en el artículo 137, en forma que no se
impida el desenvolvimiento de las actividades del
contribuyente.
    Contra la resolución que ordene las medidas anteriores
y sin que ello obste a su cumplimiento, podrá ocurrirse
ante el Tribunal que la dictó, dentro del término de cinco
días, contado desde la notificación de la resolución
respectiva, quien resolverá con citación del Jefe del
Servicio del lugar donde se haya cometido la infracción. El
fallo que se dicte sólo será apelable en lo devolutivo. El
plazo para apelar será de 15 días, contado desde la
notificación de la sentencia
     4° Presentados los descargos se conferirá traslado al
Servicio por el término de diez días. Vencido el plazo que
dispone el denunciado para formular descargos o, en su caso,
vencido el plazo de que dispone el Servicio para evacuar su
traslado respecto de los descargos formulados, haya
contestado o no, el Tribunal Tributario y Aduanero, de
oficio o a petición de parte, deberá recibir la causa a
prueba si hubiere controversia sobre algún hecho
substancial y pertinente. La resolución que se dicte al
efecto señalará los puntos sobre los cuales deberá recaer
la prueba. En su contra sólo procederán los recursos de
reposición y de apelación, dentro del plazo de cinco
días, contado desde la notificación. De interponerse
apelación, deberá hacerse siempre en subsidio de la
reposición y procederá en el solo efecto devolutivo. El
recurso de apelación se tramitará en cuenta y en forma
preferente. El término probatorio será de veinte días y
dentro de él se deberá rendir toda la prueba. El Servicio
y el contribuyente deberán acreditar sus respectivas
pretensiones dentro del procedimiento.
    Vencido el término probatorio y dentro de los diez
días siguientes las partes podrán hacer por escrito las
observaciones que el examen de la prueba les sugiera. Si no
fuera necesario cumplir nuevas diligencias, o cumplidas las
que se hubieren ordenado, el Juez Tributario y Aduanero que
esté conociendo del asunto citará a las partes a oír
sentencia.
    El Tribunal Tributario y Aduanero tendrá el plazo de
sesenta días para dictar sentencia, contado desde que el
tribunal dicte la resolución a que se refiere el inciso
anterior.
    5° Contra la sentencia que se dicte sólo procederán
los recursos a que se refiere el artículo 140.
    En contra de la sentencia de segunda instancia,
procederán los recursos de casación, en conformidad a los
artículos 144 y 145.
    6° Suprimido.
    7° No regirá el procedimiento de este Párrafo
respecto de los intereses o de las sanciones pecuniarias
aplicados por el Servicio y relacionados con hechos que
inciden en una liquidación o reliquidación de impuestos ya
notificada al contribuyente. En tales casos, deberá
reclamarse de dichos intereses y sanciones conjuntamente con
el impuesto, y de conformidad a lo dispuesto en el Título
II de este Libro.
    8° El procedimiento establecido en este Párrafo no
será tampoco aplicable al cobro que la Tesorería haga de
intereses devengados en razón de la mora o atraso en el
pago.
    9° En lo establecido por este artículo y en cuanto la
naturaleza de la tramitación lo permita, se aplicarán las
demás normas contenidas en el Título II de este Libro.
    10. No se aplicará el procedimiento de este Párrafo
tratándose de infracciones que este Código sanciona con
multa y pena privativa de libertad. En estos casos
corresponderá al Servicio recopilar los antecedentes que
habrán de servir de fundamento a la decisión del Director
a que se refiere el artículo 162, inciso tercero.

    Con el objeto de llevar a cabo la recopilación a que se
refiere el inciso precedente, el Director podrá ordenar la
aposición de sello y la incautación de los libros de
contabilidad y demás documentos relacionados con el giro
del negocio del presunto infractor.
    Las medidas mencionadas en el inciso anterior podrán
ordenarse para ser cumplidas en el lugar en que se
encuentren o puedan encontrarse los respectivos libros de
contabilidad y documentos, aunque aquél no corresponda al
domicilio del presunto infractor.
    Para llevar a efecto las medidas de que tratan los
incisos anteriores, el funcionario encargado de la
diligencia podrá recurrir al auxilio de la fuerza pública,
la que será concedida por el Jefe de Carabineros más
inmediato sin más trámite que la exhibición de la
resolución que ordena dicha medida, pudiendo procederse con
allanamiento y descerrajamiento si fuere necesario.
    Contra la resolución que ordene dichas medidas y sin
que ello obste a su cumplimiento, podrá ocurrirse ante el
Juez Tributario y Aduanero competente, en el plazo de diez
días contado desde la notificación de la resolución
respectiva, quien resolverá con citación del Jefe del
Servicio del lugar donde se haya cometido la infracción. El
fallo que se dicte sólo será apelable en lo devolutivo. El
plazo para apelar será de 15 días, contado desde la
notificación de la sentencia.
```

### CT — Art. 162
*Artículo 1 › Doble Articulado › LIBRO TERCERO DE LA COMPETENCIA PARA CONOCER DE LOS ASUNTOS CONTENCIOSOS TRIBUTARIOS, DE LOS PROCEDIMIENTOS Y DE LA PRESCRIPCIÓN › TITULO IV Del Procedimiento para la Aplicación de Sanciones › Párrafo 1º. Procedimiento general* — `idParte 8573512 · versión del artículo: 2009-01-27`

```
    Artículo 162.- Las investigaciones de hechos
constitutivos de delitos tributarios sancionados con pena
privativa de libertad sólo podrán ser iniciadas por
denuncia o querella del Servicio. Con todo, la querella
podrá también ser presentada por el Consejo de Defensa del
Estado, a requerimiento del Director.
    En las investigaciones penales y en los procesos que se
incoen, la representación y defensa del Fisco
corresponderá sólo al Director, por sí o por medio de
mandatario, cuando la denuncia o querella fuere presentada
por el Servicio, o sólo al Consejo de Defensa del Estado,
en su caso. El denunciante o querellante ejercerá los
derechos de la víctima, de conformidad al Código Procesal
Penal. En todo caso, los acuerdos reparatorios que celebre,
conforme al artículo 241 del Código Procesal Penal, no
podrán contemplar el pago de una cantidad de dinero
inferior al mínimo de la pena pecuniaria, sin perjuicio del
pago del impuesto adeudado y los reajustes e intereses
penales que procedan de acuerdo al artículo 53 de este
Código.
    Si la infracción pudiere ser sancionada con multa y
pena privativa de libertad, el Director podrá,
discrecionalmente, interponer la respectiva denuncia o
querella o enviar los antecedentes al Director Regional para
que persiga la aplicación de la multa que correspondiere a
través del procedimiento administrativo previsto en el
artículo anterior.
    La circunstancia de haberse iniciado el procedimiento
por denuncia administrativa señalado en el artículo
anterior, no será impedimento para que, en los casos de
infracciones sancionadas con multa y pena corporal, se
interponga querella o denuncia. En tal caso, el Juez
Tributario y Aduanero se declarará incompetente para seguir
conociendo el asunto en cuanto se haga constar en el proceso
respectivo el hecho de haberse acogido a tramitación la
querella o efectuado la denuncia.
    La interposición de la acción penal o denuncia
administrativa no impedirá al Servicio proseguir los
trámites inherentes a la determinación de los impuestos
adeudados; igualmente no inhibirá al Juez Tributario y
Aduanero para conocer o continuar conociendo y fallar la
reclamación correspondiente.
    El Ministerio Público informará al Servicio, a la
brevedad posible, los antecedentes de que tomare
conocimiento con ocasión de las investigaciones de delitos
comunes y que pudieren relacionarse con los delitos a que se
refiere el inciso primero.
    Si no se hubieren proporcionado los antecedentes sobre
alguno de esos delitos, el Servicio los solicitará al
fiscal que tuviere a su cargo el caso, con la sola finalidad
de decidir si presentará denuncia o interpondrá querella,
o si requerirá que lo haga al Consejo de Defensa del
Estado. De rechazarse la solicitud, el Servicio podrá
ocurrir ante el respectivo juez de garantía, quien
decidirá la cuestión mediante resolución fundada.
```

### CT — Art. 163
*Artículo 1 › Doble Articulado › LIBRO TERCERO DE LA COMPETENCIA PARA CONOCER DE LOS ASUNTOS CONTENCIOSOS TRIBUTARIOS, DE LOS PROCEDIMIENTOS Y DE LA PRESCRIPCIÓN › TITULO IV Del Procedimiento para la Aplicación de Sanciones › Párrafo 1º. Procedimiento general* — `idParte 8573513 · versión del artículo: 2002-05-31`

```
    Artículo 163.- Cuando el Director del Servicio debiere
prestar declaración testimonial en un proceso penal por
delito tributario, se aplicará lo dispuesto en los
artículos 300 y 301 del Código Procesal Penal.
    Si, en los procedimientos penales que se sigan por los
mismos delitos, procediere la prisión preventiva, para
determinar en su caso la suficiencia de la caución
económica que la reemplazará, el tribunal tomará
especialmente en consideración el hecho de que el perjuicio
fiscal se derive de impuestos sujetos a retención o recargo
o de devoluciones de tributos; el monto actualizado,
conforme al artículo 53 de este Código, de lo evadido o
indebidamente obtenido, y la capacidad económica que
tuviere el imputado.
```

### CT — Art. 164
*Artículo 1 › Doble Articulado › LIBRO TERCERO DE LA COMPETENCIA PARA CONOCER DE LOS ASUNTOS CONTENCIOSOS TRIBUTARIOS, DE LOS PROCEDIMIENTOS Y DE LA PRESCRIPCIÓN › TITULO IV Del Procedimiento para la Aplicación de Sanciones › Párrafo 1º. Procedimiento general* — `idParte 8573514 · versión del artículo: 1974-12-31`

```
    Artículo 164.- Las personas que tengan conocimiento de
la comisión de infracciones a las normas tributarias,
podrán efectuar la denuncia correspondiente ante la
Dirección o Director Regional Competente.
    El denunciante no será considerado como parte ni
tendrá derecho alguno en razón de su denuncia, la que se
tramitará con arreglo al procedimiento general establecido
en este Párrafo o al que corresponda, de conformidad a este
Libro.
```

### CT — Art. 165
*Artículo 1 › Doble Articulado › LIBRO TERCERO DE LA COMPETENCIA PARA CONOCER DE LOS ASUNTOS CONTENCIOSOS TRIBUTARIOS, DE LOS PROCEDIMIENTOS Y DE LA PRESCRIPCIÓN › TITULO IV Del Procedimiento para la Aplicación de Sanciones › Párrafo 2º. Procedimientos especiales para la aplicación de ciertas multas* — `idParte 8573515 · versión del artículo: 2020-02-24`

```
    Artículo 165.- Las denuncias por las infracciones
sancionadas en los números 1°, 2°, 3º, 6°, 7°, 10°,
11°, 15, 16, 17, 19, 20 y 21 del artículo 97, en la
primera parte del inciso cuarto del artículo 62 ter y en el
artículo 109, se someterán al procedimiento que a
continuación se señala:

    1° Las multas establecidas en los números 1 inciso
primero, 2 y 11 del artículo 97 serán determinadas por el
Servicio, o por los propios contribuyentes, y aplicadas sin
otro trámite que el de ser giradas por el servicio o
solucionadas por el contribuyente al momento de presentar la
declaración o de efectuar el pago.
    2° En los casos a que se refieren los números 1º,
inciso segundo, 3º, 6°, 7°, 10°, 15, 16, 17, 19, 20 y 21
del artículo 97, la primera parte del inciso cuarto del
artículo 62 ter y artículo 109, las infracciones serán
notificadas personalmente o por cédula por los funcionarios
del Servicio, y las multas respectivas serán giradas
inmediatamente de vencido el plazo a que se refiere el
número 4 siguiente, en caso de que el contribuyente no haga
uso del recurso establecido en dicho número. Si se presenta
este recurso, se suspenderá el giro de la multa hasta que
se resuelva sobre los descargos del contribuyente.
    3° Notificada la infracción o giro, según sea el
caso, los contribuyentes acogidos al artículo 14 letra D)
N° 8 de la ley sobre impuesto a la renta podrán, por una
única vez, solicitar la sustitución de la multa respectiva
por la participación obligatoria del contribuyente o su
representante a programas de capacitación en materias
tributarias impartidos por el Servicio de manera presencial
o a distancia.
    Sólo podrá solicitarse lo dispuesto en este número
respecto de las multas contempladas en el artículo 97
números 1°, inciso primero, 2°, 3°, 15, 19 y 21.
    La solicitud de sustitución deberá presentarse dentro
del plazo de reclamo a que se refiere el número 4°
siguiente, individualizando a las personas que participarán
en los programas de capacitación.
    Autorizada por el Servicio la sustitución de la multa
de conformidad a lo dispuesto precedentemente, si no se
diere cumplimiento a la obligación de asistencia y
aprobación de los programas de capacitación a que se
refiere este número, o si, habiéndose dado cumplimiento,
se incurre nuevamente, dentro del plazo de tres años
contado desde la solicitud de sustitución, en las mismas
conductas que motivaron la infracción, se aplicará la
multa originalmente sustituida, incrementada en hasta un
25%. Los plazos establecidos en los artículos 200 y 201, se
suspenderán durante el periodo a que se refiere este
artículo.
    4° Notificado el giro de las multas a que se refiere el
N° 1, o las infracciones de que trata el N° 2, el
contribuyente podrá reclamar por escrito, dentro del plazo
de quince días, contado desde la notificación del giro o
de la infracción, en su caso, ante el Tribunal Tributario y
Aduanero de su jurisdicción.
    5º. Formulado el reclamo, se conferirá traslado al
Servicio por el término de diez días. Vencido el plazo,
haya o no contestado el Servicio, el Juez Tributario y
Aduanero podrá recibir la causa a prueba si estima que
existen hechos substanciales y pertinentes controvertidos,
abriendo un término probatorio de ocho días. En la misma
resolución determinará la oportunidad en que la prueba
testimonial deba rendirse. Dentro de los dos primeros días
del término probatorio las partes deberán acompañar una
nómina de los testigos de que piensan valerse, con
expresión de su nombre y apellido, domicilio y profesión u
oficio. No podrán declarar más de cuatro testigos por cada
parte. En todo caso, el tribunal podrá citar a declarar a
personas que no figuren en las listas de testigos o decretar
otras diligencias probatorias que estime pertinentes.
    Las resoluciones dictadas en primera instancia se
notificarán a las partes de conformidad con lo dispuesto en
el artículo 131 bis.
    6º. El Juez Tributario y Aduanero resolverá el reclamo
dentro del trigésimo día desde que los autos queden en
estado de sentencia y, en contra de ésta, sólo procederá
el recurso de apelación para ante la Corte de Apelaciones
respectiva, el que se concederá en ambos efectos. Dicho
recurso deberá entablarse dentro de décimoquinto día,
contado desde la notificación de dicha resolución. Si el
recurso fuere desechado por la unanimidad de los miembros
del tribunal de segunda instancia, éste ordenará que el
recurrente pague, a beneficio fiscal, una cantidad adicional
equivalente al diez por ciento de la multa reajustada, y se
condenará en las costas del recurso al recurrente, de
acuerdo a las reglas generales.
    La Corte de Apelaciones verá la causa en forma
preferente, en cuenta y sin esperar la comparecencia de las
partes, salvo que estime conveniente el conocimiento de ella
previa vista y en conformidad a las normas prescritas para
los incidentes.
    En contra de la sentencia de segunda instancia no
procederán los recursos de casación en la forma y en el
fondo.
    7° Se aplicarán las normas contenidas en el Título II
de este Libro, al procedimiento establecido en este
artículo, en cuanto la naturaleza de la tramitación lo
permita. No se aplicará en este procedimiento lo dispuesto
en el inciso segundo del artículo 129.
    8° La iniciación del procedimiento y la aplicación de
sanciones pecuniarias no constituirán impedimento para el
ejercicio de la acción penal que corresponda.
    9° Suprimido.
    10º La interposición de reclamo en contra de la
liquidación de los impuestos originados en los hechos
infraccionales sancionados en el Nº 20 del artículo 97º,
suspenderá la resolución de la reclamación que se hubiere
deducido en contra de la notificación de la citada
infracción, hasta que la sentencia definitiva que falle el
reclamo en contra de la liquidación quede ejecutoriada.
```

### CT — Art. 166
*Artículo 1 › Doble Articulado › LIBRO TERCERO DE LA COMPETENCIA PARA CONOCER DE LOS ASUNTOS CONTENCIOSOS TRIBUTARIOS, DE LOS PROCEDIMIENTOS Y DE LA PRESCRIPCIÓN › TITULO IV Del Procedimiento para la Aplicación de Sanciones › Párrafo 3º. De las denuncias por infracciones a los impuestos a las asignaciones por causa de muerte y a las donaciones* — `idParte 8573517 · versión del artículo: 2003-10-10`

```
    Artículo 166.- Derogado.
```

### CT — Art. 167
*Artículo 1 › Doble Articulado › LIBRO TERCERO DE LA COMPETENCIA PARA CONOCER DE LOS ASUNTOS CONTENCIOSOS TRIBUTARIOS, DE LOS PROCEDIMIENTOS Y DE LA PRESCRIPCIÓN › TITULO IV Del Procedimiento para la Aplicación de Sanciones › Párrafo 3º. De las denuncias por infracciones a los impuestos a las asignaciones por causa de muerte y a las donaciones* — `idParte 8573519 · versión del artículo: 2003-10-10`

```
    Artículo 167.- Derogado.
```

### CT — Art. 200
*Artículo 1 › Doble Articulado › LIBRO TERCERO DE LA COMPETENCIA PARA CONOCER DE LOS ASUNTOS CONTENCIOSOS TRIBUTARIOS, DE LOS PROCEDIMIENTOS Y DE LA PRESCRIPCIÓN › TITULO VI De la Prescripción* — `idParte 8573553 · versión del artículo: 2017-10-20`

```
    Artículo 200.- El Servicio podrá liquidar un impuesto,
revisar cualquiera deficiencia en su liquidación y girar
los impuestos a que hubiere lugar, dentro del término de
tres años contado desde la expiración del plazo legal en
que debió efectuarse el pago.
    El plazo señalado en el inciso anterior será de seis
años para la revisión de impuestos sujetos a declaración,
cuando ésta no se hubiere presentado o la presentada fuere
maliciosamente falsa. Para estos efectos, constituyen
impuestos sujetos a declaración aquellos que deban ser
pagados previa declaración del contribuyente o del
responsable del impuesto.
    En los plazos señalados en los incisos anteriores y
computados en la misma forma prescribirá la acción del
Servicio para perseguir las sanciones pecuniarias que
accedan a los impuestos adeudados.
    Los plazos anteriores se entenderán aumentados por el
término de tres meses desde que se cite al contribuyente,
de conformidad al artículo 63 o a otras disposiciones que
establezcan el trámite de la citación para determinar o
reliquidar un impuesto, respecto de los impuestos derivados
de las operaciones que se indiquen determinadamente en la
citación. Si se prorroga el plazo conferido al
contribuyente en la citación respectiva, se entenderán
igualmente aumentados, en los mismos términos, los plazos
señalados en este artículo. Si se requiere al
contribuyente en los términos del inciso tercero del
artículo 63, los plazos señalados se aumentarán en un
mes.
    Las acciones para perseguir las sanciones de carácter
pecuniario y otras que no accedan al pago de un impuesto
prescribirán en tres años contados desde la fecha en que
se cometió la infracción.
```

### CT — Art. 201
*Artículo 1 › Doble Articulado › LIBRO TERCERO DE LA COMPETENCIA PARA CONOCER DE LOS ASUNTOS CONTENCIOSOS TRIBUTARIOS, DE LOS PROCEDIMIENTOS Y DE LA PRESCRIPCIÓN › TITULO VI De la Prescripción* — `idParte 8573555 · versión del artículo: 1974-12-31`

```
    Artículo 201.- En los mismos plazos señalados en el
artículo 200, y computados en la misma forma, prescribirá
la acción del Fisco para perseguir el pago de los
impuestos, intereses, sanciones y demás recargos.
    Estos plazos de prescripción se interrumpirán:

    1°.- Desde que intervenga reconocimiento u obligación
escrita.
    2°.- Desde que intervenga notificación administrativa
de un giro o liquidación.
    3°.- Desde que intervenga requerimiento judicial.

    En el caso del número 1°, a la prescripción del
presente artículo sucederá la de largo tiempo del
artículo 2.515 del Código Civil. En el caso del número
2°, empezará a correr un nuevo término que será de tres
años, el cual sólo se interrumpirá por el reconocimiento
u obligación escrita o por el requerimiento judicial.
    Decretada la suspensión del cobro judicial a que se
refiere el artículo 147, no procederá el abandono de la
instancia en el juicio ejecutivo correspondiente mientras
subsista aquélla.
    Los plazos establecidos en el presente artículo y en el
que antecede se suspenderán durante el período en que el
Servicio esté impedido, de acuerdo a lo dispuesto en el
inciso 2° del artículo 24, de girar la totalidad o parte
de los impuestos comprendidos en una liquidación cuyas
partidas o elementos hayan sido objeto de una reclamación
tributaria.
```

### CT — Art. 202
*Artículo 1 › Doble Articulado › LIBRO TERCERO DE LA COMPETENCIA PARA CONOCER DE LOS ASUNTOS CONTENCIOSOS TRIBUTARIOS, DE LOS PROCEDIMIENTOS Y DE LA PRESCRIPCIÓN › TITULO VI De la Prescripción* — `idParte 8573556 · versión del artículo: 2003-10-10`

```
    Artículo 202.- Derogado.
```


## LEY SOBRE IMPUESTO A LAS VENTAS Y SERVICIOS (DL 825 (IVA))

> **Fuente oficial**: Biblioteca del Congreso Nacional — LeyChile, servicio XML `obtxml opt=7`, idNorma 6369 (Decreto Ley 825), publicada el 1974-12-31.
> **Versión de la norma**: 2025-10-25 · **Estado**: no derogado.
> **Fecha de verificación de esta curatoría**: 2026-07-07. Todo uso posterior debe cotejar la vigencia en LeyChile.

### DL 825 (IVA) — Art. 2
*TITULO I NORMAS GENERALES › PARRAFO 2º Definiciones* — `idParte 8675259 · versión del artículo: 2022-02-04`

```
    Artículo 2°- Para los efectos de esta ley, salvo que
la naturaleza del texto implique otro significado, se
entenderá:
    1°) Por "venta", toda convención independiente de la
designación que le den las partes, que sirva para
transferir a título oneroso el dominio de bienes corporales
muebles, bienes corporales inmuebles construidos, de una
cuota de dominio sobre dichos bienes o de derechos reales
constituidos sobre ellos, como, asimismo, todo acto o
contrato que conduzca al mismo fin o que la presente ley
equipare a venta. Los terrenos no se encontrarán afectos al
impuesto establecido en esta ley.
    2°) Por "servicio", la acción o prestación que una
persona realiza para otra y por la cual percibe un interés,
prima, comisión o cualquiera otra forma de remuneración.
    Tratándose de un servicio que comprenda conjuntamente
prestaciones tanto afectas como no afectas o exentas del
impuesto establecido en esta ley, sólo se gravarán
aquellas que, por su naturaleza, se encuentren afectas. En
consecuencia, cada prestación será gravada, o no, de forma
separada y atendiendo a su naturaleza propia, para lo cual
se deberá determinar el valor de cada una
independientemente. No obstante, si un servicio comprende un
conjunto de prestaciones tanto afectas, como no afectas o
exentas, que no puedan individualizarse unas de otras, se
afectará con el impuesto de esta ley la totalidad de dicho
servicio. Para efectos de la determinación de los valores
respectivos el Servicio de Impuestos Internos podrá aplicar
lo establecido en el artículo 64 del Código Tributario.
    3°) Por "vendedor" cualquier persona natural o
jurídica, incluyendo las comunidades y las sociedades de
hecho, que se dedique en forma habitual a la venta de bienes
corporales muebles e inmuebles, sean ellos de su propia
producción o adquiridos de terceros. Corresponderá al
Servicio de Impuestos Internos calificar la habitualidad.
Con todo, no se considerará habitual la enajenación de
inmuebles que se efectúe como consecuencia de la ejecución
de garantías hipotecarias así como la enajenación
posterior de inmuebles adjudicados o recibidos en pago de
deudas y siempre que exista una obligación legal de vender
dichos inmuebles dentro de un plazo determinado; y los
demás casos de ventas forzadas en pública subasta
autorizadas por resolución judicial.
    Se considera también "vendedor" al productor,
fabricante o vendedor habitual de bienes corporales
inmuebles que venda materias primas o insumos que, por
cualquier causa, no utilice en sus procesos productivos.
    4°) Por "prestador de servicios" cualquier persona
natural o jurídica, incluyendo las comunidades y las
sociedades de hecho, que preste servicios en forma habitual
o esporádica.
    5°) Por "periodo tributario", un mes calendario, salvo
que esta ley o la Dirección Nacional de Impuestos Internos
señale otro diferente.
```

### DL 825 (IVA) — Art. 3
*TITULO I NORMAS GENERALES › Párrafo 3º De los contribuyentes.* — `idParte 8675261 · versión del artículo: 2024-10-24`

```
    Artículo 3°- Son contribuyentes, para los efectos de
esta ley, las personas naturales o jurídicas, incluyendo
las comunidades y las sociedades de hecho, que realicen
ventas, que presten servicios o efectúen cualquier otra
operación gravada con los impuestos establecidos en ella.
    En el caso de las comunidades y sociedades de hecho, los
comuneros y socios serán solidariamente responsables de
todas las obligaciones de esta ley que afecten a la
respectiva comunidad o sociedad de hecho.
    No obstante lo dispuesto en el inciso primero, el
tributo afectará al adquirente, beneficiario del servicio o
persona que deba soportar el recargo o inclusión, en los
casos que lo determine esta ley o las normas generales que
imparta la Dirección Nacional del Servicio de Impuestos
Internos, a su juicio exclusivo, para lo cual podrá
considerar, entre otras circunstancias, el volumen de ventas
y servicios o ingresos registrados, por los vendedores y
prestadores de servicios y,o los adquirentes y beneficiarios
o personas que deban soportar el recargo o inclusión. En
virtud de esta facultad, la Dirección referida podrá
disponer el cambio de sujeto del tributo también sólo por
una parte de la tasa del impuesto, como asimismo autorizar a
los vendedores o prestadores de servicios, que por la
aplicación de lo dispuesto en este inciso no puedan
recuperar oportunamente sus créditos fiscales, a imputar el
respectivo impuesto soportado o pagado a cualquier otro
impuesto fiscal incluso de retención o de recargo que deban
pagar por el mismo período tributario, a darle el carácter
de pago provisional mensual de la ley de la renta, o a que
les sea devuelto por el Servicio de Tesorerías en el plazo
de treinta días de presentada la solicitud, la cual deberá
formularse dentro del mes siguiente al de la retención del
tributo efectuado por el adquirente o beneficiario del
servicio; pero en todos los casos hasta el monto del débito
fiscal correspondiente.

    Igualmente, la Dirección podrá determinar que las
obligaciones que afecten a los contribuyentes a que se
refieren los incisos primero y segundo correspondan a un
vendedor o prestador del servicio, o al mandatario, también
respecto del impuesto que debe recargar el adquirente o
beneficiario, por las ventas o servicios que estos últimos
a su vez efectúen o presten a terceros cuando se trate de
contribuyentes de difícil fiscalización.
    En los casos a que se refiere el inciso anterior, la
Dirección podrá, para los efectos de la aplicación del
Impuesto al Valor Agregado, determinar la base imponible
correspondiente a la transferencia o prestación de servicio
que efectúe el adquirente o beneficiario, cuando se trate
de especies no sujetas al régimen de fijación de precios.
    Asimismo, la Dirección a su juicio exclusivo, podrá
imponer a los vendedores o prestadores de servicios exentos,
la obligación de retener, declarar y pagar el tributo que
corresponda a los adquirentes afectos o a determinadas
personas que importen desde los recintos de Zonas Francas.
    La Dirección podrá disponer, mediante una o más
resoluciones fundadas, que los emisores de tarjetas de pago
con provisión de fondos, débito, crédito u otros sistemas
de pago análogos recarguen, retengan, declaren y/o paguen
el total o una parte de los impuestos contemplados en esta
ley, respecto de todo o parte de las operaciones realizadas
por personas naturales o jurídicas u otro tipo de entidades
sin personalidad jurídica domiciliadas o residentes en el
extranjero que no se hayan sujetado al régimen de
tributación simplificada establecido en el párrafo 7° bis
y que se solucionen por su intermedio.
```

### DL 825 (IVA) — Art. 8
*TITULO II IMPUESTO AL VALOR AGREGADO › PARRAFO 1º Del hecho gravado* — `idParte 8675268 · versión del artículo: 2024-10-24`

```
    Artículo 8°- El impuesto de este Título afecta a las
ventas y servicios. Para estos efectos serán consideradas
también como ventas y servicios según corresponda:

    a) Las importaciones, sea que tengan o no el carácter
de habituales.
    Asimismo se considerará venta la primera enajenación
de los vehículos automóviles importados al amparo de las
partidas del Capítulo 0 del Arancel Aduanero, en cuya
virtud gozan de exención total o parcial de derechos e
impuestos con respecto a los que les afectarían en el
régimen general.
    Los Notarios no podrán autorizar ningún documento ni
las firmas puestas en él, tratándose de un contrato afecto
al impuesto que grava la operación establecida en el inciso
anterior, sin que se les acredite previamente el pago del
mismo, debiendo dejar constancia de este hecho en el
instrumento respectivo. A su vez, el Servicio de Registro
Civil e Identificación no inscribirá en su Registro de
Vehículos Motorizados ninguna transferencia de los
vehículos señalados, si no constare, en el Título
respectivo el hecho de haberse pagado el impuesto;
    b) Los aportes a sociedades y otras transferencias de
dominio de bienes corporales muebles e inmuebles, efectuados
por vendedores, que se produzcan con ocasión de la
constitución, ampliación o modificación de sociedades, en
la forma que lo determine, la Dirección Nacional de
Impuestos Internos;
    c) Las adjudicaciones de bienes corporales muebles e
inmuebles de su giro, realizadas en liquidaciones de
sociedades civiles y comerciales. Igual norma se aplicará
respecto de las sociedades de hecho y comunidades, salvo las
comunidades hereditarias y provenientes de la disolución de
la sociedad conyugal;
    d) Los retiros de bienes corporales muebles e inmuebles
efectuados por un vendedor o por el dueño, socios,
directores o empleados de la empresa, para su uso o consumo
personal o de su familia, ya sean de su propia producción o
comprados para la reventa, o para la prestación de
servicios, cualquiera que sea la naturaleza jurídica de la
empresa. Para estos efectos, se considerarán retirados para
su uso o consumo propio todos los bienes que faltaren en los
inventarios del vendedor o prestador de servicios y cuya
salida de la empresa no pudiere justificarse con
documentación fehaciente, salvo los casos de fuerza mayor,
calificada por el Servicio de Impuestos Internos, u otros
que determine el Reglamento.
    Igualmente serán considerados como ventas los retiros
de bienes corporales muebles e inmuebles destinados a rifas
y sorteos, aún a título gratuito, y sean o no de su giro,
efectuados con fines promocionales o de propaganda por los
vendedores afectos a este impuesto.
    Lo establecido en el inciso anterior será aplicable,
del mismo modo, a toda entrega o distribución gratuita de
bienes corporales muebles e inmuebles que los vendedores
efectúen con iguales fines.
    No se considerarán comprendidas en esta letra, las
entregas gratuitas a que se refiere el N° 3 del artículo
31 de la Ley sobre Impuesto a la Renta que cumplan con los
requisitos que para cada caso establece la citada
disposición. El contribuyente respectivo no perderá el
derecho al uso del crédito fiscal por el impuesto que se le
haya recargado en la adquisición de los bienes respectivos
ni se aplicarán las normas de proporcionalidad para el uso
del crédito fiscal que establece esta ley.
    Los impuestos que se recarguen en razón de los retiros
a que se refiere esta letra, no darán derecho al crédito
establecido en el artículo 23°.
    e) Los contratos de instalación o confección de
especialidades y los contratos generales de construcción;
    f) La venta de establecimientos de comercio y, en
general, la de cualquier otra universalidad que comprenda
bienes corporales muebles e inmuebles de su giro o que
formen parte del activo inmovilizado del contribuyente,
estos últimos, siempre que cumplan los requisitos
señalados en la letra m) del presente artículo. Este
tributo no se aplicará a la cesión del derecho de
herencia;
    g) El arrendamiento, subarrendamiento, usufructo o
cualquiera otra forma de cesión del uso o goce temporal de
bienes corporales muebles, inmuebles amoblados, inmuebles
con instalaciones o maquinarias que permitan el ejercicio de
alguna actividad comercial o industrial y de todo tipo de
establecimientos de comercio.
    Para calificar que se trata de un inmueble amoblado o un
inmueble con instalaciones o maquinarias que permitan el
ejercicio de alguna actividad comercial o industrial se
deberá tener presente que los bienes muebles o las
instalaciones y maquinarias sean suficientes para su uso
para habitación u oficina, o para el ejercicio de la
actividad industrial o comercial, respectivamente. Para
estos efectos, el Servicio, mediante resolución,
determinará los criterios generales y situaciones que
configurarán este hecho gravado;
    h) El arrendamiento, subarrendamiento o cualquier otra
forma de cesión del uso o goce temporal de marcas, patentes
de invención, procedimientos o fórmulas industriales y
otras prestaciones similares;
    i) El estacionamiento de automóviles y otros vehículos
en playas de estacionamiento u otros lugares destinados a
dicho fin;
    j) Las primas de seguros de las cooperativas de
servicios de seguros, sin perjuicio de las exenciones
contenidas en el artículo 12;
    k) SUPRIMIDA
    l) Los contratos de arriendo con opción de compra que
recaigan sobre bienes corporales inmuebles realizados por un
vendedor;
    m) La venta de bienes corporales muebles e inmuebles que
formen parte del activo inmovilizado de la empresa, siempre
que, por estar sujeto a las normas de este título, el
contribuyente haya tenido derecho a crédito fiscal por su
adquisición, importación, fabricación o construcción.
    No obstante lo dispuesto en el párrafo precedente, no
se considerará, para los efectos del presente artículo, la
venta de bienes corporales muebles que formen parte del
activo inmovilizado de la empresa, efectuada después de
transcurrido un plazo de treinta y seis meses contado desde
su adquisición, importación, fabricación o término de
construcción, según proceda, siempre que dicha venta haya
sido efectuada por o a un contribuyente acogido a lo
dispuesto en el artículo 14 letra D) de la ley sobre
Impuesto a la Renta, a la fecha de dicha venta.
     Previa citación al contribuyente, según lo dispuesto
en el artículo 63 del Código Tributario, el Servicio
podrá liquidar y girar el impuesto sobre la venta de bienes
corporales muebles e inmuebles que formen parte del activo
inmovilizado a que se refiere el párrafo primero de esta
letra, que realice la empresa que se crea o subsista con
ocasión de una reorganización empresarial, cuando dicha
reorganización haya tenido por objeto principal evitar el
pago del impuesto. Para tales efectos, se deberán
considerar las circunstancias particulares de la operación
y sus efectos tributarios, tales como la temporalidad entre
las operaciones, el hecho de que la empresa que se crea o
subsista se encuentre sujeta a las normas de este título,
si los bienes están o no destinados al giro o actividades
afectas al impuesto de este Título, entre otras.
    n) Los siguientes servicios remunerados realizados por
prestadores domiciliados o residentes en el extranjero:

     1. La intermediación de servicios prestados en Chile,
cualquiera sea su naturaleza, o de ventas realizadas en
Chile o en el extranjero siempre que estas últimas den
origen a una importación;
     2. El suministro o la entrega de contenido de
entretenimiento digital, tal como videos, música, juegos u
otros análogos, a través de descarga, streaming u otra
tecnología, incluyendo para estos efectos, textos,
revistas, diarios y libros;
     3. La puesta a disposición de software,
almacenamiento, plataformas o infraestructura informática;
y
     4. La publicidad, con independencia del soporte o medio
a través del cual sea entregada, materializada o ejecutada.
```

### DL 825 (IVA) — Art. 23
*TITULO II IMPUESTO AL VALOR AGREGADO › PARRAFO 6º Del Crédito Fiscal* — `idParte 8675394 · versión del artículo: 2022-07-26`

```
    Artículo 23°- Los contribuyentes afectos al pago del
tributo de este Título tendrán derecho a un crédito
fiscal contra el débito fiscal determinado por el mismo
período tributario, el que se establecerá en conformidad a
las normas siguientes:
    1°.- Dicho crédito será equivalente al impuesto de
este Título recargado en las facturas que acrediten sus
adquisiciones o la utilización de servicios, o, en el caso
de las importaciones, el pagado por la importación de las
especies al territorio nacional respecto del mismo período.
Por consiguiente, dará derecho a crédito el impuesto
soportado o pagado en las operaciones que recaigan sobre
especies corporales muebles o servicios destinados a formar
parte de su Activo Realizable o Activo Fijo, y aquellas
relacionadas con gastos de tipo general, que digan relación
con el giro o actividad del contribuyente. Igualmente dará
derecho a crédito el impuesto de este Título recargado en
las facturas emitidas con ocasión de un contrato de venta o
un contrato de arriendo con opción de compra de un bien
corporal inmueble y de los contratos referidos en la letra
e) del artículo 8°.
    2°.- No procede el derecho al crédito fiscal por la
importación o adquisición de bienes o la utilización de
servicios que se afecten a hechos no gravados por esta ley o
a operaciones exentas o que no guarden relación directa con
la actividad del vendedor.
    3°.- En el caso de importación o adquisición de
bienes o de utilización de servicios que se afecten o
destinen a operaciones gravadas y operaciones exentas o a
hechos no gravados por esta ley, el crédito se calculará
en forma proporcional, de acuerdo con las normas que
establezca el Reglamento.
    4°.- No darán derecho a crédito las importaciones,
arrendamiento con o sin opción de compra y adquisiciones de
automóviles, station wagons y similares y de los
combustibles, lubricantes, repuestos
y reparaciones para su mantención, ni las de productos o
sus componentes que gocen en cualquier forma de subsidios al
consumidor de acuerdo a la facultad del artículo 48, salvo
que el giro o actividad habitual del contribuyente sea la
venta o el arrendamiento de dichos bienes, según
corresponda, salvo en aquellos casos en que se ejerza la
facultad del inciso primero del artículo 31 de la Ley sobre
Impuesto a la Renta. Tampoco darán derecho a crédito los
gastos incurridos en supermercados y comercios similares que
no cumplan con los requisitos que establece el inciso
primero del artículo 31 de la Ley sobre Impuesto a la
Renta.

    5°.- No darán derecho a crédito los impuestos
recargados o retenidos en facturas no fidedignas o falsas o
que no cumplan con los requisitos legales o reglamentarios y
en aquéllas que hayan sido otorgadas por personas que
resulten no ser contribuyentes de este impuesto.
    Lo establecido en el inciso anterior no se aplicará
cuando el pago de la factura se haga dando cumplimiento a
los siguientes requisitos:
    a) Con un cheque nominativo, vale vista nominativo o
transferencia electrónica de dinero a nombre del emisor de
la factura, girados contra la cuenta corriente bancaria del
respectivo comprador o beneficiario del servicio.
    b) Haber anotado por el librador al extender el cheque o
por el banco al extender el vale vista, en el reverso del
mismo, el número del rol único tributario del emisor de la
factura y el número de ésta. En el caso de transferencias
electrónicas de dinero, esta misma información, incluyendo
el monto de la operación, se deberá haber registrado en
los respaldos de la transacción electrónica del banco.
    El contribuyente deberá aportar los antecedentes que
acrediten las circunstancias de las letras a) y b)
precedentes, dentro del plazo de un mes contado desde la
fecha de notificación del requerimiento realizado por el
Servicio de Impuestos Internos. En caso que no dé
cumplimiento a lo requerido, previa certificación del
Director Regional respectivo, se presumirá que la factura
es falsa o no fidedigna, no dando derecho a la utilización
del crédito fiscal mientras no se acredite que dicha
factura es fidedigna.
    Con todo, si con posterioridad al pago de una factura
ésta fuese objetada por el Servicio de Impuestos Internos,
el comprador o beneficiario del servicio perderá el derecho
al crédito fiscal que ella hubiere originado, a menos que
acredite a satisfacción de dicho Servicio, lo siguiente:
    a) La emisión y pago del cheque, vale vista o
transferencia electrónica, mediante el documento original o
fotocopia de los primeros o certificación del banco, según
corresponda, con las especificaciones que determine el
Director del Servicio de Impuestos Internos.
    b) Tener registrada la respectiva cuenta corriente
bancaria en la contabilidad, si está obligado a llevarla,
donde se asentarán los pagos efectuados con cheque, vale
vista o transferencia electrónica de dinero.
    c) Que la factura cumple con las obligaciones formales
establecidas por las leyes y reglamentos.
    d) La efectividad material de la operación y de su
monto, por los medios de prueba instrumental o pericial que
la ley establece, cuando el Servicio de Impuestos Internos
así lo solicite.
    No obstante lo dispuesto en los incisos segundo, tercero
y cuarto, no se perderá el derecho a crédito fiscal, si se
acredita que el impuesto ha sido recargado y enterado
efectivamente en arcas fiscales por el vendedor.
    Lo dispuesto en los incisos segundo, tercero y cuarto no
se aplicará en el caso que el comprador o beneficiario del
servicio haya tenido conocimiento o participación en la
falsedad de la factura.
    6°.- Cuando los contribuyentes que se dediquen a la
venta habitual de bienes corporales inmuebles o las empresas
constructoras, no puedan determinar la procedencia del
crédito fiscal conforme a los números 1 al 3 de este
artículo, en el período tributario en que adquirieron o
construyeron los bienes, deberán aplicar las siguientes
reglas:

     a) El impuesto soportado será considerado
provisionalmente como crédito fiscal del período
correspondiente; y
     b) El crédito fiscal provisional deberá ser ajustado
en cada periodo en que se realicen operaciones no gravadas o
exentas, adicionando, debidamente reajustado, al débito
fiscal de dicho período, el monto equivalente al impuesto
soportado en la adquisición o construcción de la o las
unidades que se transfieren en dichas operaciones.
    7º.- El impuesto recargado en facturas emitidas en
medios distintos del papel, de conformidad al artículo 54,
dará derecho a crédito fiscal para el comprador o
beneficiario en el período en que hagan el acuse de recibo
o se entiendan recibidas las mercaderías entregadas o el
servicio prestado, conforme a lo establecido en el inciso
primero del artículo 9º de la ley Nº 19.983, que regula
la transferencia y otorga mérito ejecutivo a la copia de la
factura. Esta limitación no regirá en el caso de
prestaciones de servicios,  ni de actos o contratos afectos
en los que, por aplicación de lo dispuesto en el artículo
55, la factura deba emitirse antes de concluirse la
prestación de los servicios o de la entrega de los bienes
respectivos.
```

### DL 825 (IVA) — Art. 24
*TITULO II IMPUESTO AL VALOR AGREGADO › PARRAFO 6º Del Crédito Fiscal* — `idParte 8675379 · versión del artículo: 2020-02-24`

```
    Artículo 24°- Del crédito calculado con arreglo a las
normas del artículo anterior, deberán deducirse los
impuestos correspondientes a las cantidades recibidas en el
mismo período por concepto de bonificaciones, descuentos y
devoluciones, que los vendedores y prestadores de servicios
hubieren a su vez rebajado al efectuar las deducciones
permitidas en el artículo 21°.
    Por otra parte, deberá sumarse al crédito fiscal el
impuesto que conste en las notas de débito recibidas y
registradas durante el mes, por aumentos del impuesto ya
facturado.
    No obstante lo dispuesto en los incisos precedentes y en
el artículo anterior, los contribuyentes podrán efectuar
los ajustes señalados o deducir el crédito fiscal del
débito fiscal o recuperar este crédito en el caso de los
exportadores, dentro de los dos períodos tributarios
siguientes a aquel que se indica en dichas normas, sólo
cuando las respectivas notas de crédito y débito, las
facturas o comprobantes de ingreso del impuesto tratándose
de importaciones, según corresponda, se reciban o se
registren con retraso, por cualquier hecho no imputable al
contribuyente.
```

### DL 825 (IVA) — Art. 25
*TITULO II IMPUESTO AL VALOR AGREGADO › PARRAFO 6º Del Crédito Fiscal* — `idParte 8675444 · versión del artículo: 1976-12-03`

```
    Artículo 25°- Para hacer uso del crédito fiscal, el
contribuyente deberá acreditar que el impuesto le ha sido
recargado en las respectivas facturas, o pagado según los
comprobantes de ingreso del impuesto tratándose de
importaciones, y que estos documentos han sido registrados
en los libros especiales que señala el artículo 59°. En
el caso de impuestos acreditados con factura, éstos sólo
podrán deducirse si se hubieren recargado separadamente en
ellas.
```

### DL 825 (IVA) — Art. 26
*TITULO II IMPUESTO AL VALOR AGREGADO › PARRAFO 6º Del Crédito Fiscal* — `idParte 8675445 · versión del artículo: 1976-12-03`

```
    Artículo 26°- Si de la aplicación de las normas
contempladas en los artículos precedentes resultare un
remanente de crédito en favor del contribuyente, respecto
de un período tributario, dicho remanente no utilizado se
acumulará a los créditos que tengan su origen en el
período tributario inmediatamente siguiente. Igual regla se
aplicará en los períodos sucesivos, si a raíz de estas
acumulaciones subsistiere un remanente a favor del
contribuyente.
```

### DL 825 (IVA) — Art. 27
*TITULO II IMPUESTO AL VALOR AGREGADO › PARRAFO 6º Del Crédito Fiscal* — `idParte 8675446 · versión del artículo: 1976-12-03`

```
    Artículo 27°- Para los efectos de imputar los
remanentes de crédito fiscal a los débitos que se generen
por las operaciones realizadas en los períodos tributarios
inmediatamente siguientes, los contribuyentes podrán
reajustar dichos remanentes, convirtiéndolos en unidades
tributarias mensuales según su monto vigente a la fecha en
que debió pagarse el tributo, y posteriormente
reconvirtiendo el número de unidades tributarias así
obtenido, al valor en pesos de ellas a la fecha en que se
impute efectivamente dicho remanente.
    Las diferencias de crédito fiscal que provengan de la
no utilización oportuna por el contribuyente del mecanismo
de reajuste antes señalado no podrán invocarse como
crédito fiscal en períodos posteriores.
    El Presidente de la República estará facultado para
hacer extensiva la reajustabilidad anteriormente señalada,
a las sumas que los contribuyentes hayan cancelado en exceso
en un período tributario, en razón de cambio en las
modalidades de declaración y pago del impuesto de esta ley.
```

### DL 825 (IVA) — Art. 27 BIS
*TITULO II IMPUESTO AL VALOR AGREGADO › PARRAFO 6º Del Crédito Fiscal* — `idParte 8675393 · versión del artículo: 2020-02-24`

```
    Artículo 27 bis.- Los contribuyentes gravados con el
impuesto del Título II de esta ley y los exportadores que
tengan remanentes de crédito fiscal, determinados de
acuerdo con las normas del artículo 23, durante dos
períodos tributarios consecutivos como mínimo originados
en la adquisición de bienes corporales muebles o inmuebles
destinados a formar parte de su activo fijo o de servicios
que deban integrar el valor de costo de éste, podrán
imputar ese remanente acumulado en dichos períodos,
debidamente reajustado de conformidad con lo dispuesto en el
artículo 27, a cualquier clase de impuesto fiscal, incluso
de retención, y a los derechos, tasas y demás gravámenes
que se perciban por intermedio de las Aduanas u optar porque
dicho remanente les sea reembolsado por la Tesorería
General de la República.  En el caso que en los dos o más
períodos tributarios señalados se originen créditos
fiscales en adquisiciones distintas a las anteriores o en
utilizaciones de servicios de los no señalados
precedentemente, el monto de la la imputación o de la
devolución se determinará aplicando al total del remanente
acumulado, el porcentaje que represente el Impuesto al Valor
Agregado soportado por adquisiciones de bienes corporales
muebles o inmuebles destinados al Activo Fijo o de servicios
que se integran al costo de éste, en relación al total del
crédito fiscal de los dos o más períodos tributarios.
Tratándose de bienes corporales inmuebles, se entenderán
como destinados a formar parte de su activo fijo, desde el
momento en que la obra o cada una de sus etapas es recibida
conforme por quien la encargó. En caso que el contribuyente
haya obtenido devoluciones durante el desarrollo de la obra,
deberá, al término de la misma, presentar, a requerimiento
del Servicio, el certificado de recepción definitiva, y
acreditar su incorporación efectiva al activo inmovilizado.
    Los contribuyentes señalados en el inciso anterior,
restituirán las sumas recibidas mediante los pagos
efectivos que realicen en Tesorería por concepto del
Impuesto al Valor Agregado, generado en la operaciones
normales que efectúen a contar del mes siguiente del
período al cual esas sumas corresponden. En el caso de que
en cualquiera de los períodos tributarios siguientes
existan operaciones exentas o no gravadas, deberán
adicionalmente restituir las sumas equivalentes a las
cantidades que resulten de aplicar la tasa de impuesto
establecida en el artículo 14°, que se determine de
multiplicar las operaciones totales del mes por la
proporción de operaciones gravadas usada para determinar el
crédito fiscal en el mes de adquisición del activo fijo
que originó la devolución y restar de dicho resultado las
operaciones afectas del mes. A los contribuyentes que no
hayan realizado ventas o prestaciones de servicios en dicho
período de dos o más meses, se les determinará en el
primer mes en que tengan operaciones si han importado o
adquirido bienes corporales muebles o inmuebles o recibido
servicios afectado a operaciones gravadas, no gravadas o
exentas aplicándose la proporcionalidad que establece el
reglamento, debiendo devolver el exceso, correspondiente a
las operaciones exentas o no gravadas, debidamente
reajustado en conformidad al artículo 27°, adicionándolo
al débito fiscal en la primera declaración del Impuesto al
Valor Agregado. De igual forma, deberá devolverse el
remanente de crédito obtenido por el contribuyente, o la
parte que proceda, cuando se haya efectuado una imputación
u obtenido una devolución superior a la que corresponda de
acuerdo a la ley o a su reglamento, y en el caso de término
de giro de la empresa. Las devoluciones a que se tengan
derecho por las exportaciones, se regirán por lo dispuesto
en el artículo 36°.
     Para hacer efectiva la imputación a que se refieren
los incisos anteriores, los contribuyentes deberán
solicitar al Servicio de Tesorerías que se les emita un
Certificado de Pago por una suma de hasta el monto de los
créditos acumulados, expresados en unidades tributarias.
Dicho certificado, que se extenderá en la forma y
condiciones que establezca el Reglamento, será nominativo,
intransferible a terceras personas y a la vista, y podrá
fraccionarse en su valor para los efectos de realizar las
diversas imputaciones que autoriza la presente disposición.
    Para obtener la devolución del remanente de crédito
fiscal, los contribuyentes que opten por este procedimiento,
deberán presentar una solicitud ante el Servicio de
Impuestos Internos, a fin de que éste verifique y
certifique, en forma previa a la devolución por la
Tesorería General de la República, la correcta
constitución de este crédito. El Servicio de Impuestos
Internos deberá pronunciarse dentro del plazo de 20 días
contado desde la fecha en que reciba los antecedentes
correspondientes. Si no lo hiciere al término de dicho
plazo, la solicitud del contribuyente se entenderá aprobada
y el Servicio de Tesorerías deberá proceder a la
devolución del remanente de crédito fiscal que
corresponda, dentro del plazo de cinco días hábiles
contado desde la fecha en que se le presente la copia de la
referida solicitud debidamente timbrada por el Servicio de
Impuestos Internos. No será aplicable el procedimiento
establecido en el artículo 80 y siguientes para el
procedimiento de devolución que establece este artículo.
    La infracción consistente en utilizar cualquier
procedimiento doloso encaminado a efectuar imputaciones y
obtener devoluciones improcedentes o superiores a las que
realmente corresponda, se sancionará en conformidad con lo
dispuesto en los incisos segundo y tercero del N° 4 del
artículo 97 del Código Tributario, según se trate de
imputaciones o devoluciones.
    La no devolución a arcas fiscales de las sumas
imputadas o devueltas en exceso según lo prescrito en el
inciso cuarto de este artículo, y que no constituya fraude,
se sancionará como no pago oportuno de impuestos sujetos a
retención o recargo, aplicándose los intereses, reajustes
y sanciones desde la fecha en que se emitió el Certificado
de Pago que dio origen al derecho a la imputación, o desde
la fecha de la devolución en su caso.
    Para los efectos de lo dispuesto en este artículo se
entenderá que forman parte del activo fijo, los bienes
corporales muebles importados en virtud de un contrato de
arrendamiento con o sin opción de compra, respecto del
impuesto pagado en la importación, siempre que dichos
bienes, por su naturaleza y características, correspondan a
los que normalmente se clasifican en el citado activo.
```

### DL 825 (IVA) — Art. 27 TER
*TITULO II IMPUESTO AL VALOR AGREGADO › PARRAFO 6º Del Crédito Fiscal* — `idParte 9399186 · versión del artículo: 2020-02-24`

```
     Artículo 27 ter.- Los contribuyentes gravados con los
impuestos de los Títulos II y III de esta ley, que tengan
la calidad de acreedores en un Procedimiento Concursal de
Reorganización regido por la Ley de Reorganización y
Liquidación de Activos de Empresas y Personas, que hayan
sido recargados en facturas pendientes de pago emitidas a
deudores de un Acuerdo de Reorganización, podrán imputar
el monto de dichos tributos a cualquier clase de impuestos
fiscales, incluso de retención, y a los derechos, tasas y
demás gravámenes que se perciban por intermedio de las
Aduanas u optar porque éstos les sean reembolsados por la
Tesorería General de la República. En el caso de que se
hayan efectuado abonos a dichas deudas, la imputación o
devolución, en su caso, sólo podrán hacerse valer sobre
la parte no cubierta por los abonos, si la hubiera.
     Los contribuyentes señalados en este artículo
restituirán los impuestos correspondientes a contar del mes
siguiente del período en que venza el plazo para que el
deudor efectúe el pago de las sumas acordadas en el
respectivo Acuerdo de Reorganización. De igual forma,
deberán devolverse dichos tributos cuando se haya efectuado
una imputación u obtenido una devolución superior a la que
corresponda y en el caso de término de giro de la empresa.
No procederá, sin embargo, dicha restitución en caso que
se declare el término o incumplimiento del Acuerdo de
Reorganización, mediante resolución firme y ejecutoriada,
dándose inicio a un Procedimiento Concursal de
Liquidación, siempre que el respectivo contribuyente
comunique dicha circunstancia al Servicio de Impuestos
Internos, en la forma y plazo que éste determine, mediante
resolución.
     Para hacer efectiva la imputación a que se refieren
los incisos anteriores, los contribuyentes deberán
solicitar al Servicio de Tesorerías que se les emita un
Certificado de Pago por una suma de hasta el monto de los
créditos acumulados, expresados en unidades tributarias
mensuales. Dicho certificado, que se extenderá en la forma
y condiciones que fije el Servicio de Tesorerías, mediante
resolución, será nominativo, intransferible a terceros y a
la vista, y podrá fraccionarse en su valor para los efectos
de realizar las diversas imputaciones que autoriza la
presente disposición.
     Para obtener la devolución de los impuestos recargados
en las facturas pendientes de pago, los contribuyentes que
opten por este procedimiento deberán presentar una
solicitud ante el Servicio de Impuestos Internos, conforme a
los artículos 80 y siguientes a fin de que éste verifique
y certifique, en forma previa a la devolución por la
Tesorería General de la República, que los respectivos
tributos hayan sido declarados y enterados en arcas fiscales
oportunamente, y que éstos se encuentran al día en el pago
de sus obligaciones tributarias.
     Para hacer uso del beneficio establecido en el presente
artículo, el Acuerdo de Reorganización debe haber sido
aprobado mediante resolución firme y ejecutoriada. La
Superintendencia de Insolvencia y Reemprendimiento remitirá
al Servicio de Impuestos Internos copia de los Acuerdos de
Reorganización que se hallen en dicho estado, en la forma y
plazo que dicha Superintendencia fije, mediante resolución.
     Los contribuyentes que sean Personas Relacionadas con
el deudor de un Acuerdo de Reorganización no podrán
impetrar el derecho que establece el presente artículo.
     La infracción consistente en utilizar cualquier
procedimiento doloso encaminado a efectuar imputaciones y
obtener devoluciones improcedentes o superiores a las que
realmente corresponda, se sancionará en conformidad con lo
dispuesto en los párrafos segundo y tercero del número 4
del artículo 97 del Código Tributario, según se trate de
imputaciones o devoluciones.
     La no devolución a arcas fiscales de las sumas
imputadas o devueltas en exceso según lo previsto en el
inciso segundo de este artículo, y que no constituya
fraude, se sancionará como no pago oportuno de impuestos
sujetos a retención o recargo, aplicándose los intereses,
reajustes y sanciones desde la fecha en que se emitió el
Certificado de Pago que dio origen al derecho a la
imputación, o desde la fecha de la devolución, en su caso.
```

### DL 825 (IVA) — Art. 28
*TITULO II IMPUESTO AL VALOR AGREGADO › PARRAFO 6º Del Crédito Fiscal* — `idParte 8675498 · versión del artículo: 1987-07-23`

```
    Artículo 28°- En los casos de término de giro, el
saldo de crédito que hubiere quedado en favor del
contribuyente podrá ser imputado por éste al impuesto del
presente Título que se causare con motivo de la venta o
liquidación del establecimiento o de los bienes corporales
muebles o inmuebles que lo componen. Si aún quedare un
remanente a su favor, sólo podrá imputarlo al pago del
impuesto a la renta de primera categoría que adeudare por
el último ejercicio.
    Serán aplicables a los saldos o remanentes a que se
refiere este artículo, las normas de reajustabilidad que
establece el artículo anterior, en lo que fueren
pertinentes.
```


## APRUEBA TEXTO QUE INDICA DE LA LEY SOBRE IMPUESTO A LA RENTA (DL 824 (Renta))

> **Fuente oficial**: Biblioteca del Congreso Nacional — LeyChile, servicio XML `obtxml opt=7`, idNorma 6368 (Decreto Ley 824), publicada el 1974-12-31.
> **Versión de la norma**: 2026-03-27 · **Estado**: no derogado.
> **Fecha de verificación de esta curatoría**: 2026-07-07. Todo uso posterior debe cotejar la vigencia en LeyChile.

### DL 824 (Renta) — Art. 2
*Artículo 1 › Doble Articulado › TITULO I Normas Generales › PARRAFO 2 Definiciones* — `idParte 8656024 · versión del artículo: 2020-02-24`

```
    ARTICULO 2°.- Para los efectos de la presente ley se
aplicarán, en lo que no sean contrarias a ella, las
definiciones establecidas en el Código Tributario y,
además, salvo que la naturaleza del texto implique otro
significado, se entenderá:
    1.- Por "renta", los ingresos que constituyan utilidades
o beneficios que rinda una cosa o actividad y todos los
beneficios, utilidades e incrementos de patrimonio que se
perciban o devenguen, cualquiera que sea su naturaleza,
origen o denominación.
    2.- Por "renta devengada", aquélla sobre la cual se
tiene un título o derecho, independientemente de su actual
exigibilidad y que constituye un crédito para su titular.
    3.- Por "renta percibida", aquélla que ha ingresado
materialmente al patrimonio de una persona. Debe, asimismo,
entenderse que una renta devengada se percibe desde que la
obligación se cumple por algún modo de extinguir distinto
al pago.
    4.- Por "renta mínima presunta", la cantidad que no es
susceptible de deducción alguna por parte del
contribuyente.
    5.- Por "capital efectivo", el total del activo con
exclusión de aquellos valores que no representen
inversiones efectivas, tales como valores intangibles,
nominales, transitorios y de orden.
    En el caso de contribuyentes no sometidos a las normas
del artículo 41°, la valorización de los bienes que
conforman su capital efectivo se hará por su valor real
vigente a la fecha en que se determine dicho capital. Los
bienes físicos del activo inmovilizado se valorizarán
según su valor de adquisición debidamente reajustado de
acuerdo a la variación experimentada por el índice de
precios al consumidor en el período comprendido entre el
último día del mes que anteceda al de su adquisición y el
último día del mes que anteceda a aquél en que se
determine el capital efectivo, menos las depreciaciones
anuales que autorice la Dirección. Los bienes físicos del
activo realizable se valorizarán según su valor de costo
de reposición en la plaza respectiva a la fecha en que se
determine el citado capital, aplicándose las normas
contempladas en el N° 3 del artículo 41.
    6.- Por "sociedades de personas", las sociedades de
cualquier clase o denominación, excluyéndose únicamente a
las anónimas.
    Para todos los efectos de esta ley, las sociedades por
acciones reguladas en el Párrafo 8° del Título VII del
Código de Comercio, se considerarán anónimas.
    7.- Por "año calendario", el período de doce meses que
termina el 31 de Diciembre.
    8.- Por "año comercial", el período de doce meses que
termina el 31 de Diciembre o el 30 de Junio y, en los casos
de término de giro, del primer ejercicio del contribuyente
o de aquél en que opere por primera vez la autorización de
cambio de fecha del balance, el período que abarque el
ejercicio respectivo según las normas de los incisos
séptimo y octavo del artículo 16 del Código Tributario.
    9.- Por "año tributario", el año en que deben pagarse
los impuestos o la primera cuota de ellos.
    10.- "Por capital propio tributario", el conjunto de
bienes, derechos y obligaciones, a valores tributarios, que
posee una empresa. Dicho capital propio se determinará
restando al total de activos que representan una inversión
efectiva de la empresa, el pasivo exigible, ambos a valores
tributarios. Para la determinación del capital propio
tributario deberán considerarse los activos y pasivos
valorados conforme a lo señalado en el artículo 41, cuando
corresponda aplicar dicha norma.
    Tratándose de una empresa individual, formarán parte
del capital propio tributario los activos y pasivos del
empresario individual que hayan estado incorporados al giro
de la empresa, debiendo excluirse los activos y pasivos que
no originen rentas gravadas en la primera categoría o que
no correspondan al giro, actividades o negocios de la
empresa.
    11.- Por "impuestos finales", los impuestos global
complementario y adicional establecidos en esta ley.
    12.- Por "establecimiento permanente", un lugar que sea
utilizado para la realización permanente o habitual de todo
o parte del negocio, giro o actividad de una persona o
entidad sin domicilio ni residencia en Chile, ya sea
utilizado o no en forma exclusiva para este fin, tales como,
oficinas, agencias, instalaciones, proyectos de
construcción y sucursales.
    También se considerará que existe un establecimiento
permanente cuando una persona o entidad sin domicilio ni
residencia en Chile realice actividades en el país
representado por un mandatario y en el ejercicio de tales
actividades dicho mandatario habitualmente concluya
contratos propios del giro ordinario del mandante,
desempeñe un rol principal que lleve a su conclusión o
negocie elementos esenciales de éstos sin que sean
modificados por la persona o entidad sin domicilio ni
residencia en Chile. En consecuencia, no constituirá
establecimiento permanente de una persona o entidad sin
domicilio ni residencia en Chile un mandatario no
dependiente ni económica ni jurídicamente del mandante,
que desempeñe actividades en el ejercicio de su giro
ordinario.
    No se considerará que existe un establecimiento
permanente si la persona o entidad sin domicilio ni
residencia en Chile realiza exclusivamente actividades
auxiliares del negocio o giro, o actividades preparatorias
para la puesta en marcha del mismo en el país.
```

### DL 824 (Renta) — Art. 17
*Artículo 1 › Doble Articulado › TITULO I Normas Generales › Párrafo 4º Disposiciones varias* — `idParte 8656042 · versión del artículo: 2022-02-04`

```
    ARTICULO 17°.- No constituye renta:

    1°.- La indemnización de cualquier daño emergente y
del daño moral, siempre que la indemnización por este
último haya sido establecida por sentencia ejecutoriada.
Tratándose de bienes susceptibles de depreciación, la
indemnización percibida hasta concurrencia del valor
inicial del bien reajustado de acuerdo con el porcentaje de
variación experimentada por el índice de precios al
consumidor entre el último día del mes que antecede al de
la adquisición del bien y el último día del mes anterior
a aquél en que haya ocurrido el siniestro que da origen a
la indemnización.
    Lo dispuesto en este número no regirá respecto de la
indemnización del daño emergente en el caso de bienes
incorporados al giro de un negocio, empresa o actividad,
cuyas rentas efectivas deban tributar con el impuesto de la
Primera Categoría, sin perjuicio de la deducción como
gasto de dicho daño emergente.
    2°.- Las indemnizaciones por accidentes del trabajo,
sea que consistan en sumas fijas, rentas o pensiones.
    3°.- Las sumas percibidas por el beneficiario o
asegurado en cumplimiento de contratos de seguros de vida,
seguros de desgravamen, seguros dotales o seguros de rentas
vitalicias durante la vigencia del contrato, al vencimiento
del plazo estipulado en él o al tiempo de su transferencia
o liquidación. Sin embargo, la exención contenida en este
número no comprende las rentas provenientes de contratos de
seguros de renta vitalicia convenidos con los fondos
capitalizados en Administradoras de Fondos de Pensiones, en
conformidad a lo dispuesto en el Decreto Ley N° 3.500, de
1980.
    Lo dispuesto en este número se aplicará también a
aquellas cantidades que se perciban en cumplimiento de un
seguro dotal por el mero hecho de cumplirse el plazo
estipulado, siempre que dicho plazo sea superior a cinco
años, pero sólo por aquella parte que no exceda anualmente
de diecisiete unidades tributarias mensuales, según el
valor de dicha unidad al 31 de diciembre del año en que se
perciba el ingreso, considerando cada año que medie desde
la celebración del contrato y el año en que se perciba el
ingreso y el conjunto de los seguros dotales contratados por
el perceptor. Para determinar la renta correspondiente se
deducirá del monto percibido, acrecentado por todas las
sumas percibidas con cargo al conjunto de seguros dotales
contratados por el contribuyente debidamente reajustadas
según la variación del índice de precios al consumidor
ocurrida entre el primero del mes anterior a la percepción
y el primero del mes anterior al término del año
respectivo, aquella parte de los ingresos percibidos
anteriormente que se afectaron con los impuestos de esta ley
y el total de la prima pagada a la fecha de percepción del
ingreso, reajustados en la forma señalada. Si de la
operación anterior resultare un saldo positivo, la
compañía de seguros que efectúe el pago deberá retener
un 15% de dicho saldo, retención que se sujetará, en lo
que corresponda, a lo dispuesto en el Párrafo 2º del
Título V de esta ley. Con todo, se considerará renta toda
cantidad percibida con cargo a un seguro dotal, cuando no
hubiere fallecido el asegurado, o se hubiere invalidado
totalmente, si el monto pagado por concepto de prima hubiere
sido rebajado de la base imponible del impuesto establecido
en el artículo 43º.
    4°.- Las sumas percibidas por los beneficiarios de
pensiones o rentas vitalicias derivadas de contratos que,
sin cumplir con los requisitos establecidos en el Párrafo
2° del título XXXIII del Libro IV del Código Civil, hayan
sido o sean convenidos con sociedades anónimas chilenas,
cuyo objeto social sea el de constituir pensiones o rentas
vitalicias, siempre que el monto mensual de las pensiones o
rentas mencionadas no sea, en conjunto, respecto del
beneficiario, superior a un cuarto de una unidad tributaria.
    5°.- El valor de los aportes recibidos por sociedades y
sus reajustes, sólo respecto de éstas.
    Tampoco constituirá renta el mayor valor o sobreprecio
y sus reajustes obtenidos por sociedades anónimas en la
colocación de acciones de su propia emisión, los que se
considerarán capital respecto de la sociedad. Asimismo, no
constituirán renta las sumas o bienes que tengan el
carácter de aportes entregados por el asociado al gestor de
una cuenta en participación, sólo respecto de la
asociación, y siempre que fueren acreditados
fehacientemente.
    6°.- La distribución de utilidades o de fondos
acumulados que las sociedades anónimas hagan a sus
accionistas en forma de acciones total o parcialmente
liberadas o mediante el aumento del valor nominal de las
acciones, todo ello representativo de una capitalización
equivalente, como así también, la parte de los dividendos
que provengan de los ingresos a que se refiere este
artículo, sin perjuicio de lo dispuesto en el artículo 29
respecto de los números 25 y 28 del presente artículo.
    Las acciones totalmente liberadas a que refiere el
párrafo anterior, no tendrán valor de adquisición en su
futura enajenación y el mayor valor obtenido en la misma no
se beneficiará con la tributación contemplada en el
artículo 107. Tratándose de acciones parcialmente
liberadas o de acciones que aumentaron su valor nominal, no
formará parte del valor de adquisición de las mismas
aquella parte liberada o aquella en que aumentó su valor
nominal, respectivamente, no siendo procedente en dicha
parte la tributación contemplada en el artículo 107
respecto del mayor valor obtenido en su enajenación.
    7°.- Las devoluciones de capital, hasta el valor de
aporte o de adquisición de su participación, y sus
reajustes, siempre que no correspondan a utilidades
capitalizadas que deban pagar los impuestos de esta ley. Las
sumas retiradas, remesadas o distribuidas por estos
conceptos se imputarán y afectarán con los impuestos de
primera categoría, global complementario o adicional,
según corresponda, en la forma dispuesta por el artículo
14.
    8°.- Las cantidades que se señalan a continuación,
obtenidas por personas naturales, siempre que no se originen
en la enajenación de bienes asignados a su empresa
individual, con las excepciones y en los casos y condiciones
que se indican en los párrafos siguientes:

    a) Enajenación o cesión de acciones de sociedades
anónimas, en comandita por acciones o de derechos sociales
en sociedades de personas.

    i) No constituirá renta aquella parte que se obtenga
hasta la concurrencia del costo tributario del bien
respectivo, esto es, aquel conformado por su valor de aporte
o adquisición, incrementado o disminuido, según el caso,
por los aumentos o disminuciones de capital posteriores
efectuados por el enajenante, debidamente reajustados de
acuerdo al porcentaje de variación experimentado por el
índice de precios al consumidor entre el mes anterior al de
adquisición, aporte, aumento o disminución de capital, y
el mes anterior al de la enajenación.
    ii) Para determinar el mayor valor que resulte de la
enajenación, se deducirá del precio o valor asignado a
dicha enajenación, el costo tributario del bien respectivo.
    iii) Del mayor valor así determinado deberán deducirse
las pérdidas provenientes de la enajenación de los bienes
señalados en esta letra, obtenidas en el mismo ejercicio.
Para estos efectos, dichas pérdidas se reajustarán de
acuerdo con el porcentaje de variación del índice de
precios al consumidor en el período comprendido entre el
mes anterior al de la enajenación que produjo esas
pérdidas y el mes anterior al del cierre del ejercicio. En
todo caso, para que proceda esta deducción, dichas
pérdidas deberán acreditarse fehacientemente ante el
Servicio.
    iv) El mayor valor que se determine conforme a los
literales anteriores, se afectará con impuestos finales en
base percibida.
    v) Sin perjuicio de lo anterior, el impuesto global
complementario podrá declararse y pagarse sobre la base de
renta devengada, en cuyo caso podrán aplicarse las
siguientes reglas:

    El mayor valor referido se entenderá devengado durante
el período de años comerciales en que las acciones o
derechos sociales que se enajenan han estado en poder del
enajenante, hasta un máximo de diez años, en caso de ser
superior a éste, y aun cuando en dichos años el enajenante
no hubiere obtenido rentas afectas al señalado impuesto o
las obtenidas hubieren quedado exentas del mismo. Para tal
efecto, las fracciones de años se considerarán como un
año completo.
    La cantidad correspondiente a cada año se obtendrá de
dividir el total del mayor valor obtenido, reajustado en la
forma indicada en el párrafo siguiente, por el número de
años de tenencia de las acciones o derechos sociales, con
un máximo de diez.
    Para los efectos de realizar la declaración anual,
respecto del citado mayor valor serán aplicables las normas
sobre reajustabilidad del número 4º del artículo 33, y no
se aplicará en ningún período la exención establecida en
el artículo 57.
    Las cantidades reajustadas correspondientes a cada año
se convertirán a unidades tributarias mensuales, según el
valor de esta unidad en el mes de diciembre del año en que
haya tenido lugar la enajenación, y se ubicarán en los
años en que se devengaron, con el objeto de liquidar el
impuesto global complementario de acuerdo con las normas
vigentes y según el valor de la citada unidad en el mes de
diciembre de los años respectivos.
    Las diferencias de impuestos o reintegros de
devoluciones que se determinen por aplicación de las reglas
anteriores, según corresponda, se expresarán en unidades
tributarias mensuales del año respectivo y se solucionarán
en el equivalente de dichas unidades en el mes de diciembre
del año en que haya tenido lugar la enajenación.
    El impuesto que resulte de la reliquidación establecida
precedentemente se deberá declarar y pagar en el año
tributario que corresponda al año calendario o comercial en
que haya tenido lugar la enajenación.
    La reliquidación del impuesto global complementario
conforme con los párrafos anteriores en ningún caso
implicará modificar las declaraciones de impuesto a la
renta correspondientes a los años comerciales que se
tomaron en consideración para efectos del cálculo de dicho
impuesto.

    vi) Cuando el conjunto de los resultados determinados en
la enajenación de los bienes a que se refieren las letras
a), c) y d) de este número, no exceda del equivalente a 10
unidades tributarias anuales, según su valor al cierre del
ejercicio en que haya tenido lugar la enajenación, se
considerarán para los efectos de esta ley como un ingreso
no constitutivo de renta. En caso que excedan dicha suma,
los respectivos mayores valores se afectarán con la
tributación que corresponda.

    b) Enajenación de bienes raíces situados en Chile, o
de derechos o cuotas respecto de tales bienes raíces
poseídos en comunidad.

    i) Se aplicarán, en lo que fuesen pertinentes, las
reglas señaladas en los literales ii) y iii), de la letra
a) anterior. No obstante, para efectos de esta letra b), el
costo tributario también estará conformado por el valor de
adquisición del bien respectivo y los desembolsos
incurridos en mejoras que hayan aumentado su valor,
reajustados de acuerdo a la variación del índice de
precios al consumidor entre el mes anterior al de la
adquisición o mejora, según corresponda, y el mes anterior
a la enajenación. Las referidas mejoras deberán haber sido
efectuadas por el enajenante o un tercero, siempre que hayan
pasado a formar parte de la propiedad del enajenante, y
declaradas en la oportunidad que corresponda ante el
Servicio, en la forma que establezca mediante resolución,
para ser incorporadas en la determinación del avalúo
fiscal de la respectiva propiedad para los fines del
impuesto territorial, con anterioridad a la enajenación.
    ii) No constituirá renta, asimismo, aquella parte del
mayor valor que no exceda, independiente del número de
enajenaciones realizadas o del número de bienes raíces de
propiedad del contribuyente, la suma total equivalente a
8.000 unidades de fomento. Para el cómputo del valor de
ésta, se utilizará el valor de la unidad de fomento que
corresponda al último día del ejercicio en que tuvo lugar
la enajenación respectiva. El Servicio mantendrá a
disposición de los contribuyentes los antecedentes de que
disponga sobre las enajenaciones que realicen para efectos
de computar el límite señalado.
    iii) En caso que el mayor valor referido exceda en todo
o en parte el límite del ingreso no constitutivo de renta
anterior, se gravará dicho exceso con el impuesto global
complementario o adicional, según corresponda, o bien,
tratándose de personas naturales con domicilio o residencia
en Chile, con un impuesto único y sustitutivo de 10%, a
elección del enajenante, en ambos casos sobre la base de
renta percibida.
    iv) Lo establecido en los números ii) y iii)
precedentes aplicará siempre que entre la fecha de
adquisición y enajenación del bien raíz transcurra un
plazo que exceda de un año. No obstante, dicho plazo será
de cuatro años en caso de una enajenación de un bien raíz
producto de una subdivisión de terrenos, urbanos o rurales,
o derivado de la construcción de edificios por pisos o
departamentos, incluyendo en este caso las bodegas y los
estacionamientos, el que se contará desde la adquisición o
la construcción, según corresponda.
    v) Sin perjuicio de lo anterior, el impuesto global
complementario que corresponda conforme a los números
precedentes podrá declararse y pagarse sobre la base de la
renta devengada, en cuyo caso podrán aplicarse las reglas
dispuestas en el literal v), de la letra a) anterior.
    vi) En la enajenación de los bienes referidos,
adquiridos por sucesión por causa de muerte, el enajenante
podrá deducir, en la proporción que le corresponda, como
crédito en contra del impuesto respectivo, el impuesto
sobre las asignaciones por causa de muerte de la ley número
16.271 pagado sobre dichos bienes. El monto del crédito
corresponderá a la suma equivalente que resulte de aplicar
al valor del impuesto efectivamente pagado por el
asignatario, la proporción que se determine entre el valor
del bien raíz respectivo que se haya considerado para el
cálculo del impuesto y el valor líquido del total de las
asignaciones que le hubieren correspondido al enajenante de
acuerdo a la ley. El monto del crédito a que tenga derecho
el enajenante, se determinará al término del ejercicio en
que se efectúe la enajenación, y para ello el valor del
impuesto sobre las asignaciones por causa de muerte, el
valor del bien y de las asignaciones líquidas que le
hubieren correspondido al enajenante, se reajustarán de
acuerdo a la variación del índice de precios al consumidor
entre el mes anterior a la fecha de pago del referido
impuesto y el mes anterior al término del ejercicio en que
se efectúa la enajenación.

    c) Enajenación de pertenencias mineras y derechos de
aguas. Para determinar el mayor valor obtenido en la
enajenación de dichos bienes y el ingreso no constitutivo
de renta, se aplicarán, en lo que fuesen pertinentes, las
reglas establecidas en los literales i), ii), iii) y vi) de
la letra a) anterior. En el evento que proceda gravar el
mayor valor determinado, este se afectará con los impuestos
global complementario o adicional, según corresponda, sobre
la base de la renta percibida.

    d) Enajenación de bonos y demás títulos de deuda.
Para determinar el mayor valor obtenido en la enajenación
de dichos bienes y el ingreso no constitutivo de renta, se
aplicarán, en lo que fuesen pertinentes, las reglas
establecidas en los literales i), ii), iii) y vi) de la
letra a) anterior. Sin embargo, en este caso, el valor de
adquisición deberá disminuirse con las amortizaciones de
capital recibidas por el enajenante, reajustadas de acuerdo
al porcentaje de variación del índice de precios al
consumidor entre el mes anterior a la amortización y el mes
anterior a la enajenación. En el evento que proceda gravar
el mayor valor determinado, este se afectará con los
impuestos global complementario o adicional, según
corresponda, sobre la base de renta percibida.

    e) Enajenación del derecho de propiedad intelectual o
industrial. No constituye renta el mayor valor obtenido en
su enajenación, siempre que el enajenante sea el respectivo
inventor o autor.

    f) No constituye renta la adjudicación de bienes en la
partición de una comunidad hereditaria y a favor de uno o
más herederos del causante, de uno o más herederos de
éstos, o de los cesionarios de ellos, ya sea que se trate
de personas naturales o no. El valor de adquisición para
fines tributarios de los bienes que se le adjudiquen
corresponderá al valor que se haya considerado para los
fines del impuesto a las herencias en relación al bien de
que se trate, reajustado de acuerdo a la variación del
índice de precios al consumidor entre el mes anterior al de
la apertura de la sucesión y el mes anterior al de la
adjudicación.

    g) No constituye renta la adjudicación de bienes que se
efectúe en favor del propietario, comunero, socio o
accionista, se trate de una persona natural o no, con
ocasión de la liquidación o disolución de una empresa o
sociedad, en tanto, la suma de los valores tributarios del
total de los bienes que se le adjudiquen, no exceda del
capital que haya aportado a la empresa, determinado en
conformidad al número 7º.- de este artículo, más las
rentas o cantidades que le correspondan en la misma y que se
hayan considerado para efectos de la aplicación en el
artículo 38 bis, al término de giro. El valor de
adquisición de los bienes que se le adjudiquen
corresponderá a aquel que haya registrado la empresa o
sociedad de acuerdo a las normas de la presente ley al
término de giro, conforme a lo establecido en el referido
artículo 38 bis.

    h) No constituye renta la adjudicación de bienes en
liquidación de sociedad conyugal a favor de cualquiera de
los cónyuges, de comunidad de bienes a favor de cualquiera
de los convivientes civiles, o de uno o más de los
herederos o cesionarios de éstos o aquellos y ya sea que se
trate de personas naturales o no. El valor de adquisición
para fines tributarios de los bienes que se le adjudiquen
corresponderá al valor de adjudicación. Las reglas
precedentes se aplicarán a la adjudicación de bienes con
ocasión de la liquidación de la comunidad pactada por los
convivientes civiles.

    i) No constituye renta el mayor valor proveniente de la
enajenación de vehículos destinados al transporte de
pasajeros o exclusivamente al transporte de carga ajena, que
sean de propiedad de personas naturales que a la fecha de
enajenación posean sólo uno de dichos vehículos, aun
cuando lo hubiere asignado a su empresa individual que
tributa sobre renta presunta.

    j) No se considerará enajenación, para los efectos de
esta ley, las cesiones de instrumentos financieros que se
efectúen con ocasión de un contrato de retrocompra
celebrado con un banco, corredora de bolsa o agente de
valores. La diferencia que en estos casos se determine entre
el valor de la compraventa al contado y el valor de la
compraventa a plazo, celebradas ambas operaciones en forma
conjunta y simultánea, será considerada para el vendedor
al contado como un gasto por intereses de aquellos indicados
en el número 1°.-, del inciso cuarto del artículo 31, y
para el comprador al contado, como un ingreso percibido o
devengado, según corresponda, el que tributará conforme a
las normas generales de esta ley. Las reglas referidas en
este párrafo se aplicarán ya sea que el comprador al
contado sea una persona natural o no, y aun cuando actúe en
su calidad de empresario individual.

    k) No se considerará enajenación, para los efectos de
esta ley, ya sea que las partes sean personas naturales o
no, y aun cuando se trate de bienes asignados a su empresa
individual, la cesión y la restitución de acciones de
sociedades anónimas abiertas con presencia bursátil, que
se efectúen con ocasión de un préstamo o arriendo de
acciones, en una operación bursátil de venta corta,
siempre que las acciones que se den en préstamo o en
arriendo se hubieren adquirido en una bolsa de valores del
país o en un proceso de oferta pública de acciones regido
por el título XXV de la ley número 18.045, con motivo de
la constitución de la sociedad o de un aumento de capital
posterior, o de la colocación de acciones de primera
emisión.
    Para determinar los impuestos que graven los ingresos
que perciba o devengue el cedente por las operaciones
señaladas en el inciso anterior, se aplicarán las normas
generales de esta ley. En el caso del cesionario, los
ingresos que obtuviese producto de la enajenación de las
acciones cedidas se entenderán percibidos o devengados, en
el ejercicio en que se deban restituir las acciones al
cedente, cuyo costo se reconocerá conforme a lo establecido
en el artículo 30.
    Lo dispuesto en los dos párrafos anteriores se
aplicará también al préstamo de bonos en operaciones
bursátiles de venta corta. En todo caso, el prestatario
deberá adquirir los bonos que deba restituir en alguno de
los mercados formales a que se refiere el artículo 48 del
decreto ley Nº 3.500, de 1980.

    l) Tratamiento tributario de los planes de compensación
laboral que consistan en la entrega de opciones para
adquirir acciones, bonos u otros títulos emitidos en Chile
o en el exterior.

    i) Planes de compensación laboral pactados en contratos
individuales de trabajo o en contratos o convenios
colectivos de trabajo.
    No constituye renta para los directores, consejeros y
trabajadores, la entrega que efectúa la empresa, o sus
relacionados, en los términos del número 17 del artículo
8° del Código Tributario, de una opción para adquirir
acciones, bonos u otros títulos emitidos en Chile o en el
exterior, así como tampoco el ejercicio de la misma. Sin
embargo, el mayor valor obtenido en la enajenación de la
respectiva opción tributará conforme a lo dispuesto en el
número iv) de la letra a) anterior, el que será
equivalente a la diferencia entre el precio o valor de
enajenación y el valor pagado con ocasión de la entrega de
la opción, de existir.
    El mayor valor obtenido en la enajenación de las
acciones, bonos u otros títulos emitidos en Chile o en el
exterior adquiridos una vez ejercida la opción tributará
conforme a las reglas generales. Para estos efectos, se
entenderá por mayor valor la diferencia entre el precio o
valor de enajenación y el monto que se determine de la suma
de los valores pagados con ocasión de la entrega o
adquisición y ejercicio de la opción, de existir. No
obstante, en caso que aplique al mayor valor lo dispuesto en
el artículo 107, se afectará con impuestos finales la
diferencia entre el valor de adquisición determinado de
acuerdo a lo indicado en el número iii) siguiente, y la
cantidad que corresponda a la suma de los valores pagados
con ocasión de la entrega y ejercicio de la opción, si
fuera aplicable.
    ii) Planes de compensación laboral que no fueron
pactados en contratos individuales de trabajo o en convenios
o contratos colectivos de trabajo.
    No constituye renta para los directores, consejeros y
trabajadores, la entrega que efectúa la empresa, o sus
relacionados, en los términos del número 17 del artículo
8° del Código Tributario, de una opción para adquirir
acciones, bonos u otros títulos emitidos en Chile o en el
exterior.
    Constituye mayor remuneración para las referidas
personas el ejercicio de la respectiva opción,
remuneración que se gravará con el impuesto único de
segunda categoría, o con impuestos finales, según
corresponda, y que será equivalente a la diferencia entre
el valor de adquisición de las acciones, bonos u otros
títulos emitidos en Chile o en el exterior, de acuerdo a lo
indicado en el literal iii) siguiente, y el monto que se
determine de la suma de los valores pagados con ocasión de
la entrega y ejercicio de la opción, de existir.
    Asimismo, el mayor valor obtenido en la enajenación de
la respectiva opción tributará conforme a lo dispuesto en
el número iv) de la letra a) anterior, y será equivalente
a la diferencia entre el precio o valor de enajenación y el
valor pagado con ocasión de la entrega de la opción, de
existir.
    El mayor valor obtenido en la enajenación de las
acciones, bonos u otros títulos emitidos en Chile o en el
exterior adquiridos una vez ejercida la opción, tributará
conforme a las reglas generales. Para estos efectos, se
entenderá por mayor valor la diferencia entre el precio o
valor de enajenación y el valor de adquisición de dichas
acciones, bonos o títulos, a que se refiere el literal iii)
siguiente.
    iii) Para efectos de lo dispuesto en los literales i) y
ii) precedentes, se deberán tener presente las siguientes
reglas, según corresponda:
    Los valores pagados con ocasión de la entrega y
ejercicio de una opción se reajustarán de acuerdo al
porcentaje de variación experimentado por el índice de
precios al consumidor entre el mes anterior al de su pago y
el mes anterior al de la enajenación de la opción o de las
de acciones, bonos u otros títulos emitidos en Chile o en
el exterior, según corresponda.
    Se considerará como valor de adquisición de las
acciones, adquiridas mediante el ejercicio de una opción,
el valor de libros o el valor de mercado, a que se refieren
los artículos 130 a 132 del Decreto Supremo número 702, de
2011, del Ministerio de Hacienda, que aprueba el nuevo
reglamento de sociedades anónimas, según se trate de
acciones de sociedades anónimas cerradas o abiertas. En el
caso de acciones emitidas en el exterior, se utilizarán los
mismos parámetros de valoración, atendiendo a las
características de las acciones de que se trate.
    Tratándose de bonos u otros títulos emitidos en Chile
o en el exterior, adquiridos mediante el ejercicio de una
opción, se considerará como valor de adquisición el valor
de mercado, tomando en cuenta, entre otros elementos, su
valor nominal, la tasa de cupón, el plazo para su rescate o
la calificación del instrumento.
    Los valores de adquisición referidos en los dos
párrafos precedentes se reajustarán de acuerdo al
porcentaje de variación experimentado por el índice de
precios al consumidor entre el mes anterior al de la
adquisición de las acciones, bonos o demás títulos y el
mes anterior al de la enajenación de los mismos.

    m) Enajenaciones de toda clase de bienes no contemplados
en las letras precedentes. Se aplicarán, en lo que fuesen
pertinentes, las reglas señaladas en los literales i), ii),
iii) y iv) de la letra a) anterior. En estos casos, el costo
tributario estará conformado por el valor de adquisición
de los respectivos bienes, debidamente reajustado de acuerdo
al porcentaje de variación experimentado por el índice de
precios al consumidor entre el mes anterior a la
adquisición y el mes anterior al de la enajenación.

    No obstante lo dispuesto en las letras precedentes, si
la enajenación de dichos bienes se efectúa por el
propietario a una sociedad de personas o anónima cerrada en
que participe directa o indirectamente; o, al cónyuge,
conviviente civil o parientes ascendientes o descendientes
hasta el segundo grado de consanguinidad; o, a un
relacionado en los términos del número 17 del artículo
8° del Código Tributario; o, a los directores, gerentes,
administradores, ejecutivos principales o liquidadores, así
como a toda entidad controlada directamente o indirectamente
por estos últimos, el mayor valor obtenido se gravará con
impuestos finales en base devengada. Lo establecido en este
inciso no aplicará a la entrega y ejercicio de opciones a
que se refiere la letra l) anterior.

    Por su parte, en los mismos casos señalados en el
inciso anterior, no se aplicará lo dispuesto en los
literales v) y vi) de la letra a) anterior, esto es, la
renta no podrá considerarse devengada en más de un
ejercicio y no tendrá lugar el ingreso no constitutivo de
renta de 10 unidades tributarias anuales.

    El Servicio podrá aplicar lo dispuesto en el artículo
64 del Código Tributario, cuando el valor de la
enajenación de un bien raíz o de otros bienes o valores
que se transfieran sea notoriamente superior al valor
comercial de los inmuebles de características y ubicación
similares en la localidad respectiva, o de los corrientes en
plaza, considerando las circunstancias en que se realiza la
operación. La diferencia entre el valor de la enajenación
y el que se determine en virtud de esta disposición estará
sujeta a la tributación establecida en el literal ii) del
inciso primero del artículo 21. La tasación, liquidación
y giro que se efectúen con motivo de la aplicación del
citado artículo 64 del Código Tributario podrán
reclamarse en la forma y plazos que esta disposición
señala y de acuerdo con los procedimientos que indica.

    Para los efectos de este número, se entenderá por
fecha de adquisición o enajenación la del respectivo
contrato, instrumento u operación, sin perjuicio que,
tratándose de las operaciones de la letra b) anterior, se
considerará la fecha de la inscripción respectiva.

    9°.- La adquisición de bienes de acuerdo con los
párrafos 2° y 4° del Título V del Libro II del Código
Civil, o por prescripción, sucesión por causa de muerte o
donación.
    10°.- Los beneficios que obtiene el deudor de una renta
vitalicia por el mero hecho de cumplirse la condición que
le pone término o disminuye su obligación de pago, como
también el incremento del patrimonio derivado del
cumplimiento de una condición o de un plazo suspensivo de
un derecho, en el caso de fideicomiso y del usufructo.
    11°.- Las cuotas que eroguen los asociados.
    12°.- El mayor valor que se obtenga en la enajenación
ocasional de bienes muebles de uso personal del
contribuyente o de todos o algunos de los objetos que forman
parte del mobiliario de su casa habitación.
    13°.- La asignación familiar, los beneficios
previsionales y la indemnización por desahucio y la de
retiro hasta un máximo de un mes de remuneración por cada
año de servicio o fracción superior a seis meses.
Tratándose de dependientes del sector privado, se
considerará remuneración mensual el promedio de lo ganado
en los últimos 24 meses, excluyendo gratificaciones,
participaciones, bonos y otras remuneraciones
extraordinarias y reajustando previamente cada remuneración
de acuerdo a la variación que haya experimentado el Indice
de Precios al Consumidor entre el último día del mes
anterior al del devengamiento de la remuneración y el
último día del mes anterior al del término del contrato.
    14°.- La alimentación, movilización o alojamiento
proporcionado al empleado u obrero sólo en el interés del
empleador o patrón, o la cantidad que se pague en dinero
por esta misma causa, siempre que sea razonable a juicio del
Director Regional.
    15°.- Las asignaciones de traslación y viáticos, a
juicio del Director Regional.
    16°.- Las sumas percibidas por concepto de gastos de
representación siempre que dichos gastos estén
establecidos por ley.
    17°.- Las pensiones o jubilaciones de fuente
extranjera.
    18°.- Las cantidades percibidas o los gastos pagados
con motivo de becas de estudio.
    19°.- Las pensiones alimenticias que se deben por ley a
determinadas personas, únicamente respecto de éstas.
    20°.- La constitución de la propiedad intelectual,
como también la constitución de los derechos que se
originen de acuerdo a los Títulos III, IV, V y VI del
Código Minería y su artículo 72, sin perjuicio de los
beneficios que se obtengan de dichos bienes.
    21°.- El hecho de obtener de la autoridad
correspondiente una merced, una concesión o un permiso
fiscal o municipal.
    22°.- Las remisiones, por ley, de deudas, intereses u
otras sanciones.
    23°.- Los premios otorgados por el Estado o las
Municipalidades, por la Universidad de Chile, por la
Universidad Técnica del Estado, por una Universidad
reconocida por el Estado, por una corporación o fundación
de derechos público o privado, o por alguna otra persona o
personas designadas por ley, siempre que se trate de
galardones establecidos de un modo permanente en beneficio
de estudios, investigaciones y creaciones de ciencias o de
arte, y que la persona agraciada no tenga la calidad de
empleado u obrero de la entidad que lo otorga; como
asimismo, los premios del Sistema de Pronósticos y Apuestas
creados por el Decreto Ley N° 1.298, de 1975.
    24°.- Los premios de rifas de beneficencia autorizadas
previamente por decreto supremo.
    25°.- Los reajustes y amortizaciones de bonos, pagarés
y otros títulos de créditos emitidos por cuenta o con
garantía del Estado y los emitidos por cuenta de
instituciones, empresas y organismos autónomos del Estado y
las Municipalidades; los reajustes y las amortizaciones de
los bonos o letras hipotecarias emitidas por instituciones
de crédito hipotecario; los reajustes de depósitos de
ahorro en el Banco del Estado de Chile, en la Corporación
de la Vivienda y en las Asociaciones de Ahorro y Préstamos;
los reajustes de los certificados de ahorro reajustables del
Banco Central de Chile, de los bonos y pagarés reajustables
de la Caja Central de Ahorros y Préstamos y de las
hipotecas del sistema nacional de ahorros y préstamos, y
los reajustes de los depósitos y cuotas de ahorros en
cooperativas y demás instituciones regidas por el Decreto
R.R.A. N° 20, de 5 de abril de 1963, todo ello sin
perjuicio de lo dispuesto en el artículo 29.
    También se comprenderán los reajustes que en las
operaciones de crédito de dinero de cualquier naturaleza, o
instrumentos financieros, tales como bonos, debentures,
pagarés, letras o valores hipotecarios estipulen las partes
contratantes, se fije por el emisor o deban, según la ley,
ser presumidos o considerados como tales, pero sólo hasta
las sumas o cantidades determinadas de acuerdo con lo
dispuesto en el artículo 41 bis, todo ello sin perjuicio de
lo señalado en el artículo 29.
    26°.- Los montepíos a que se refiere la ley número
5.311.
    27°.- Las gratificaciones de zona establecidas o
pagadas en virtud de una ley.
    28°.- El monto de los reajustes que, de conformidad a
las disposiciones del párrafo 3o del Título V de esta ley,
proceda respecto de los pagos provisionales efectuados por
los contribuyentes, sin perjuicio de lo dispuesto en el
artículo 29°.
    29°.- Los ingresos que no se consideren rentas o que se
reputen capital según texto expreso de una ley.
    30° La parte de los gananciales que uno de los
cónyuges, sus herederos o cesionarios, perciba del otro
cónyuge, sus herederos o cesionarios, como consecuencia del
término del régimen patrimonial de participación en los
gananciales.
    31.- Las compensaciones económicas convenidas por los
cónyuges o los convivientes civiles en escritura pública,
acta de avenimiento o transacción y aquellas decretadas por
sentencia judicial.
```

### DL 824 (Renta) — Art. 21
*Artículo 1 › Doble Articulado › TITULO II Del impuesto cedular por categorías › PRIMERA CATEGORIA De las rentas del capital y de las empresas comerciales, industriales, mineras y otras › Párrafo 1º De los contribuyentes y de la tasa del impuesto* — `idParte 8656049 · versión del artículo: 2020-02-24`

```
     ARTICULO 21°.- Las sociedades anónimas, los
contribuyentes del número 1 del artículo 58, los
empresarios individuales, comunidades y sociedades de
personas que declaren sus rentas efectivas de acuerdo a un
balance general según contabilidad completa, deberán
declarar y pagar conforme a los artículos 65, número 1, y
69 de esta ley, un impuesto único de 40%, que no tendrá el
carácter de impuesto de categoría, el que se aplicará
sobre:

     i. Las partidas del número 1 del artículo 33, que
correspondan a retiros de especies o a cantidades
representativas de desembolsos de dinero que no deban
imputarse al valor o costo de los bienes del activo y que
beneficien directa o indirectamente a los relacionados a la
empresa o sus propietarios, según dispone el inciso final
de este artículo, o bien, en aquellos casos en que el
contribuyente no logre acreditar la naturaleza y efectividad
del desembolso. La tributación señalada se aplicará,
salvo que estas partidas resulten gravadas conforme a lo
dispuesto en el literal i) del inciso tercero de este
artículo;

     ii. Las cantidades que se determinen por aplicación de
lo dispuesto en los artículos 17, número 8, inciso cuarto;
35 inciso tercero, 36, inciso segundo; 38, 41 E, 70 y 71 de
esta ley, y aquellas que se determinen por aplicación de lo
dispuesto en los incisos tercero al sexto del artículo 64,
y en el artículo 65 del Código Tributario, según
corresponda, y

     No se afectarán con este impuesto, ni con aquel
señalado en el inciso tercero siguiente: (i) los gastos
anticipados que deban ser aceptados en ejercicios
posteriores; (ii) el impuesto de Primera Categoría; el
impuesto único de este artículo, el impuesto establecido
en el número 2, del artículo 38 bis y el impuesto
territorial, todos ellos pagados; (iii) los intereses,
reajustes y multas pagados al Fisco, municipalidades y a
organismos o instituciones públicas creadas por ley; (iv)
las partidas a que se refiere el número 12° del artículo
31 y las patentes mineras, en ambos casos en la parte que no
puedan ser deducidas como gasto, y (v) los gastos efectuados
por Corporaciones y Fundaciones chilenas, salvo que se
aplique, según su naturaleza, los supuestos del numeral
iii) del inciso tercero.

     Los contribuyentes de los impuestos global
complementario o adicional, que sean propietarios,
comuneros, socios o accionistas de empresas, comunidades o
sociedades que determinen su renta efectiva de acuerdo a un
balance general según contabilidad completa, deberán
declarar y pagar los impuestos referidos, según
corresponda, sobre las cantidades que se señalan a
continuación en los literales i) al iv), impuestos cuyo
importe se incrementará en un monto equivalente al 10% de
las citadas cantidades. Esta tributación se aplicará en
reemplazo de la establecida en el inciso primero:

     i) Las partidas del número 1 del artículo 33, que
corresponden a retiros de especies o a cantidades
representativas de desembolsos de dinero que no deban
imputarse al valor o costo de los bienes del activo, cuando
hayan beneficiado al propietario, socio, comunero o
accionista. En estos casos, el Servicio podrá,
fundadamente, determinar el beneficio que tales sujetos han
experimentado. Cuando dichas cantidades beneficien a dos o
más accionistas, comuneros o socios y no sea posible
determinar el monto del beneficio que corresponde a cada uno
de ellos, se afectarán con la tributación establecida en
este inciso, en proporción a su participación en el
capital o en las utilidades de la empresa o sociedad
respectiva.

     El Servicio de Impuestos Internos podrá revisar la
efectividad de los montos declarados como utilidades afectas
a impuestos finales no retiradas, remesadas o distribuidas
de la empresa, y los activos que la representan, para
efectos de determinar la procedencia de lo señalado en este
número (i) siempre que el Servicio determine en forma
fundada que constituyen un retiro, remesa o distribución
encubierta, que haya debido resultar imputada a cantidades
afectas a dichos impuestos cuando así corresponda de
acuerdo a lo dispuesto en el artículo 14. Para estos
efectos el Servicio considerará, entre otros elementos, las
utilidades de balance acumuladas en la empresa a la fecha de
la revisión, los activos de la misma y la relación entre
dichos antecedentes y el monto que se pretende como retiro,
remesa o distribución encubierta. Asimismo, deberá
considerar el origen de los activos, junto a otras
circunstancias relevantes, lo que deberá ser expresado por
el Servicio, fundadamente, al determinar que se trata de un
retiro, remesa o distribución encubierto de cantidades
afectas a la tributación de este inciso.

     ii) Los préstamos que la empresa, establecimiento
permanente, la comunidad o sociedad respectiva, con
excepción de las sociedades anónimas abiertas, efectúe a
sus propietarios, comuneros, socios o accionistas
contribuyentes de los impuestos global complementario o
adicional, en la medida que el Servicio determine de manera
fundada que constituyen un retiro, remesa o distribución,
encubierta, que resulte imputada a cantidades afectas a
dichos impuestos cuando así corresponda de acuerdo a lo
señalado en el artículo 14. La tributación de este inciso
se aplicará sobre el total de la cantidad prestada,
reajustada según el porcentaje de variación del Índice de
Precios al Consumidor entre el mes anterior al del
otorgamiento del préstamo y el mes que antecede al término
del ejercicio, deduciéndose debidamente reajustadas todas
aquellas cantidades que el propietario, socio o accionista
beneficiario haya restituido a la empresa o sociedad a
título de pago del capital del préstamo y sus reajustes
durante el ejercicio respectivo. Para estos efectos el
Servicio considerará, entre otros elementos, las utilidades
de balance acumuladas en la empresa a la fecha del préstamo
y la relación entre éstas y el monto prestado; el destino
y destinatario final de tales recursos; el plazo de pago del
préstamo, sus prórrogas o renovaciones, tasa de interés u
otras cláusulas relevantes de la operación, circunstancias
y elementos que deberán ser expresados por el Servicio,
fundadamente, al determinar que el préstamo es un retiro,
remesa o distribución encubierto de cantidades afectas a la
tributación de este inciso.

     Las sumas que establece este numeral se deducirán en
la empresa, comunidad o sociedad acreedora, de las
cantidades a que se refieren el número 4.-, de la letra A),
del artículo 14 y el número 2.- de la letra B), de dicho
artículo, en la misma forma que los retiros, remesas o
distribuciones.

     iii) El beneficio que represente el uso o goce, a
cualquier título, o sin título alguno, que no sea
necesario para producir la renta, de los bienes del activo
de la empresa o sociedad respectiva. Para estos efectos, se
presumirá de derecho que el valor mínimo del beneficio
será del 10% del valor del bien determinado para fines
tributarios al término del ejercicio; del 20% del mismo
valor en el caso de automóviles, station wagons y
vehículos similares; y del 11% del avalúo fiscal
tratándose de bienes raíces, o en cualquiera de los casos
señalados, el monto equivalente a la depreciación anual
mientras sea aplicable, cuando represente una cantidad
mayor, cualquiera que sea el período en que se hayan
utilizado los bienes en el ejercicio o en la proporción que
justifique fehacientemente el contribuyente.

     Del valor mínimo del beneficio calculado conforme a
las reglas anteriores podrán rebajarse las sumas
efectivamente pagadas que correspondan al período por el
uso o goce del bien, aplicándose a la diferencia la
tributación establecida en este inciso tercero.

     En el caso de contribuyentes que realicen actividades
en zonas rurales, no se aplicará la tributación
establecida en el inciso tercero al beneficio que represente
el uso o goce de los activos de la empresa ubicados en tales
sitios. Tampoco se aplicará dicha tributación al beneficio
que represente el uso o goce de los bienes de la empresa
destinados al esparcimiento de su personal, o el uso de
otros bienes por éste, si estuviera disponible y pudiera
ser utilizada por todos los trabajadores de la empresa, bajo
criterios de universalidad y sin exclusiones. En caso que
dicho uso fuere exclusivo para ciertos trabajadores o para
directores de la empresa, se aplicará el impuesto
establecido en el inciso primero de este artículo, que
será de cargo de la empresa, comunidad o sociedad
propietaria y el beneficio por dicho uso se calculará
conforme a las reglas precedentes.

     Cuando el uso o goce de un mismo bien se haya concedido
simultáneamente a más de un socio, comunero o accionista y
no sea posible determinar la proporción del beneficio que
corresponde a cada uno de ellos, éste se determinará
distribuyéndose conforme a las reglas que establece el
artículo 14, letra A), para la atribución de rentas. En
caso que el uso o goce se haya conferido por un período
inferior al año comercial respectivo, circunstancia que
deberá ser acreditada por el beneficiario, ello deberá ser
considerado para efectos del cálculo de los impuestos.

     Las sumas que establece este numeral no se deducirán
en la empresa, comunidad o sociedad respectiva, de las
cantidades a que se refieren el número 4.- de la letra A)
del artículo 14, y el número 2.- de la letra B) del mismo
artículo.

     iv) En el caso que cualquier bien de la empresa,
comunidad o sociedad sea entregado en garantía de
obligaciones, directas o indirectas, del propietario,
comunero, socio o accionista, y ésta fuera ejecutada por el
pago total o parcial de tales obligaciones, se aplicará la
tributación de este párrafo al propietario, comunero,
socio o accionista cuyas deudas fueron garantizadas de esta
forma. En este caso, la tributación referida se calculará
sobre la garantía ejecutada, según su valor corriente en
plaza, conforme a lo dispuesto en el artículo 64 del
Código Tributario.

     Las sumas que establece este numeral, hasta el valor
tributario del activo que resulta ejecutado, se deducirán
en la empresa, comunidad o sociedad respectiva, de las
cantidades a que se refieren el número 4.- de la letra A)
del artículo 14, y el número 2.- de la letra B), de dicho
artículo, en la misma forma que los retiros, remesas o
distribuciones.

     Para la aplicación de la tributación establecida en
el inciso tercero, se entenderá que las partidas señaladas
en el literal i) benefician, que el préstamo se ha
efectuado, que el beneficio señalado en el literal iii) se
ha conferido o que se han garantizado obligaciones al
propietario, comunero, socio o accionista, según sea el
caso, cuando dichas cantidades tengan como beneficiario de
las partidas señaladas en el literal i), deudor del
préstamo, beneficiario por el uso o goce señalado en el
literal iii), o sujeto cuyas deudas se han garantizado, a
sus respectivos cónyuges, convivientes civiles, hijos no
emancipados legalmente, o bien a cualquier persona
relacionada con aquellos conforme a las normas de relación
del número 17 del artículo 8° del Código Tributario o, a
los directores, gerentes, administradores, ejecutivos
principales o liquidadores, así como a toda entidad
controlada directamente o indirectamente por ellos, y,
además, se determine que el beneficiario final, en el caso
de los préstamos y garantías es el propietario, socio,
comunero o accionista respectivo.
```

### DL 824 (Renta) — Art. 31
*Artículo 1 › Doble Articulado › TITULO II Del impuesto cedular por categorías › PRIMERA CATEGORIA De las rentas del capital y de las empresas comerciales, industriales, mineras y otras › Párrafo 3º De la base imponible* — `idParte 8656061 · versión del artículo: 2020-02-24`

```
    ARTICULO 31°.- La renta líquida de las personas
referidas en el artículo anterior se determinará
deduciendo de la renta bruta todos los gastos necesarios
para producirla, entendiendo por tales aquellos que tengan
aptitud de generar renta, en el mismo o futuros ejercicios y
se encuentren asociados al interés, desarrollo o
mantención del giro del negocio, que no hayan sido
rebajados en virtud del artículo 30°, pagados o adeudados,
durante el ejercicio comercial correspondiente, siempre que
se acrediten o justifiquen en forma fehaciente ante el
Servicio. No se deducirán los gastos incurridos en la
adquisición, mantención o explotación de bienes no
destinados al giro del negocio o empresa, de los bienes de
los cuales se aplique la presunción de derecho a que se
refiere el literal iii) del inciso tercero del artículo 21
y la letra f), del número 1°, del artículo 33, como
tampoco en la adquisición y arrendamiento de automóviles,
station wagons y similares, cuando no sea éste el giro
habitual, y en combustible, lubricantes, reparaciones,
seguros y, en general, todos los gastos para su mantención
y funcionamiento. No obstante, procederá la deducción de
los gastos respecto de los vehículos señalados, cuando el
Director, mediante resolución fundada, lo establezca por
cumplirse los requisitos establecidos en la primera parte de
este inciso.
    Sin perjuicio de lo indicado en el inciso precedente,
los gastos incurridos en el extranjero se acreditarán con
los correspondientes documentos emitidos en el exterior de
conformidad a las disposiciones legales del país
respectivo, siempre que conste en ellos, a lo menos, la
individualización y domicilio del prestador del servicio o
del vendedor de los bienes adquiridos según corresponda, la
naturaleza u objeto de la operación y la fecha y monto de
la misma. El contribuyente deberá presentar una traducción
al castellano de tales documentos cuando así lo solicite el
Servicio de Impuestos Internos. Aun en el caso que no exista
el respectivo documento de respaldo, la Dirección Regional
podrá aceptar la deducción del gasto si a su juicio éste
es razonable y necesario para la operación del
contribuyente, atendiendo a factores tales como la relación
que exista entre las ventas, servicios, gastos o los
ingresos brutos y el desembolso de que se trate de igual o
similar naturaleza, de contribuyentes que desarrollen en
Chile la misma actividad o una semejante.
    Respecto de las cantidades a que se refiere el artículo
59, cuando se originen en actos o contratos celebrados con
partes directa o indirectamente relacionadas de la entidad
local respectiva en los términos del artículo 41 E, sólo
procederá su deducción como gasto en el año calendario o
comercial de su pago, abono en cuenta o puesta a
disposición. Para que proceda su deducción, se requiere
que se haya declarado y pagado el respectivo impuesto
adicional, salvo que tales cantidades se encuentren exentas
o no gravadas con el citado tributo, ya sea por ley o por
aplicación de un convenio para evitar la doble tributación
internacional. Adicionalmente, para que sea procedente su
deducción deberán cumplir con los requisitos que establece
este artículo, en cuanto sean aplicables. Lo dispuesto en
este inciso, no obsta a la aplicación de lo dispuesto en el
citado artículo 41 E.
    Procederá la deducción de los siguientes gastos
especiales, siempre que, además de los requisitos que para
cada caso se señalen, cumplan los requisitos generales de
los gastos a que se refiere el inciso primero, en la medida
que a estos últimos les sean aplicables estos requisitos
generales conforme a la naturaleza del gasto respectivo:
    1°.- Los intereses pagados o devengados sobre las
cantidades adeudadas, dentro del año a que se refiere el
impuesto.
         Con todo, los intereses y demás gastos financieros
que conforme a las disposiciones de este artículo cumplan
con los requisitos para ser deducidos como gastos, que
provengan de créditos destinados a la adquisición de
derechos sociales, acciones, bonos y, en general, cualquier
tipo de capital mobiliario, podrán ser deducidos como
tales.
    2°.- Los impuestos establecidos por leyes chilenas, en
cuanto se relacionen con el giro de la empresa y siempre que
no sean los de esta ley, con excepción del impuesto
territorial, a menos que en este último caso no proceda su
utilización como crédito y que no constituyan
contribuciones especiales de fomento o mejoramiento. No
procederá esta rebaja en los casos en que el impuesto haya
sido sustituido por una inversión en beneficio del
contribuyente.
    3°.- Las pérdidas sufridas por el negocio o empresa
durante el año comercial a que se refiere el impuesto,
comprendiendo las que provengan de delitos contra la
propiedad.
    Se incluye, también, la deducción del costo para fines
tributarios de aquellos alimentos destinados al consumo
humano, alimentos para mascotas, productos de higiene y aseo
personal, y productos de aseo y limpieza, libros, artículos
escolares, ropa, juguetes, materiales de construcción,
entre otros, que correspondan a bienes de uso o consumo,
cuyas características y condiciones se determinen mediante
resolución del Servicio. Para estos efectos, se exigirá
que se trate de bienes respecto de los cuales su
comercialización se ha vuelto inviable por razones de
plazo, desperfectos o fallas en su fabricación,
manipulación o transporte, por modificaciones sustantivas
en las líneas de comercialización que conlleven la
decisión de productores y vendedores de eliminar tales
bienes del mercado pero que, conservando sus condiciones
para el consumo o uso según corresponda, son entregados
gratuitamente a instituciones sin fines de lucro,
debidamente inscritas ante el Servicio, para su
distribución gratuita, consumo o utilización entre
personas naturales de escasos recursos beneficiarias de
tales instituciones, u otras instituciones sin fines de
lucro que las puedan utilizar en el cumplimiento de sus
fines, todas circunstancias que deberán ser acreditadas de
manera fehaciente ante el Servicio, en la forma que éste
determine mediante resolución.
    Del mismo modo, se procederá en la entrega gratuita de
especialidades farmacéuticas y otros productos
farmacéuticos que autorice el reglamento que emite el
Ministerio de Salud para el control de los productos
farmacéuticos de uso humano, bajo los requisitos y
condiciones que dicho reglamento determine, a los
establecimientos asistenciales públicos o privados, para
ser dispensados en la misma condición de gratuidad a los
pacientes.
    En conformidad con lo dispuesto en la ley número
20.920, que establece marco para la gestión de residuos, la
responsabilidad extendida del productor y fomento al
reciclaje, no se aceptará como gasto y se afectará con el
impuesto único establecido en el inciso primero del
artículo 21, la destrucción voluntaria de materias primas,
insumos o bienes procesados o terminados que puedan ser
entregados gratuitamente en los términos de los párrafos
anteriores.
    Podrán, asimismo, deducirse las pérdidas de ejercicios
anteriores, siempre que concurran los requisitos del inciso
primero, las cuales deberán imputarse al ejercicio
inmediatamente siguiente y así sucesivamente.
    Las rentas o cantidades que se perciban a título de
retiros o dividendos provenientes de otras empresas no se
imputarán a las pérdidas de la empresa receptora. Por su
parte, el monto del impuesto de primera categoría asociado
a los retiros o dividendos que se perciban de otras
empresas, se controlará en el registro SAC de la empresa
receptora, establecido en el artículo 14 letra A N° 2
letra d).
    Las pérdidas se determinarán aplicando a los
resultados del balance las normas relativas a la
determinación de la renta líquida imponible contenidas en
este párrafo y su monto se reajustará, cuando deba
imputarse a los años siguientes, de acuerdo con el
porcentaje de variación experimentada por el índice de
precios al consumidor en el período comprendido entre el
último día del mes anterior al del cierre del ejercicio
comercial en que se generaron las pérdidas y el último
día del mes anterior al del cierre del ejercicio en que
proceda su deducción.
    Con todo, las sociedades con pérdidas que en el
ejercicio hubieren sufrido cambio en la propiedad de los
derechos sociales, acciones o del derecho a participación
en sus utilidades, no podrán deducir las pérdidas
generadas antes del cambio de propiedad de los ingresos
percibidos o devengados con posterioridad a dicho cambio.
Ello siempre que, además, con motivo del cambio señalado o
en los doce meses anteriores o posteriores a él la sociedad
haya cambiado de giro o ampliado el original a uno distinto,
salvo que mantenga su giro principal, o bien al momento del
cambio indicado en primer término, no cuente con bienes de
capital u otros activos propios de su giro de una magnitud
que permita el desarrollo de su actividad o de un valor
proporcional al de adquisición de los derechos o acciones,
o pase a obtener solamente ingresos por participación, sea
como socio o accionista, en otras sociedades o por
reinversión de utilidades. Para este efecto, se entenderá
que se produce cambio de la propiedad en el ejercicio cuando
los nuevos socios o accionistas adquieran o terminen de
adquirir, directa o indirectamente, a través de sociedades
relacionadas, a lo menos el 50% de los derechos sociales,
acciones o participaciones. Lo dispuesto en este inciso no
se aplicará cuando el cambio de propiedad se efectúe entre
empresas relacionadas, en los términos que establece el
número 17 del artículo 8° del Código Tributario.
    4°.- Los créditos incobrables castigados durante el
año, siempre que hayan sido contabilizados oportunamente y
se hayan agotado prudencialmente los medios de cobro.
    Sin perjuicio de lo dispuesto en el párrafo anterior,
los contribuyentes podrán deducir de su renta líquida,
salvo que se trate de operaciones con relacionados, en los
términos del número 17.- del artículo 8° del Código
Tributario, los créditos que se encuentren impagos por más
de 365 días contados desde su vencimiento o el valor que
resulte de aplicar un porcentaje sobre el monto de los
créditos vencidos. El Servicio, mediante sucesivas
resoluciones, establecerá los rangos de porcentajes tomando
de referencia indicadores de incobrabilidad del sector o
mercado relevante en que opera el contribuyente. Las
recuperaciones totales o parciales de créditos se
considerarán de acuerdo a lo dispuesto en el artículo 29.
    Las provisiones y castigos de los créditos incluidos en
la cartera vencida de los bancos e instituciones
financieras, entendiéndose dentro de estas últimas a las
empresas operadoras y/o emisoras de tarjetas de crédito no
bancarias, de acuerdo a las instrucciones que impartan en
conjunto la Superintendencia de Bancos e Instituciones
Financieras y el Servicio de Impuestos Internos. Las
recuperaciones totales o parciales de créditos se
considerarán de acuerdo a lo dispuesto en el artículo 29.
    Las instrucciones de carácter general que se impartan
en virtud del inciso anterior, serán también aplicables a
las remisiones de créditos riesgosos que efectúen los
bancos y sociedades financieras a sus deudores, en la parte
en que se encuentren afectos a provisiones constituídas
conforme a la normativa sobre clasificación de la cartera
de créditos establecida por la Superintendencia de Bancos e
Instituciones financieras.
    Las normas generales que se dicten deberán contener, a
lo menos, las siguientes condiciones:
    a) Que se trate de créditos clasificados en las dos
últimas categorías de riesgo establecidas para la
clasificación de cartera, y
    b) Que el crédito de que se trata haya permanecido en
alguna de las categorías indicadas a lo menos por el
período de un año, desde que se haya pronunciado sobre
ella la Superintendencia.
    Lo dispuesto en este número se aplicará también a los
créditos que una institución financiera haya adquirido de
otra, siempre que se cumpla con las condiciones antedichas.
    Lo dispuesto en el párrafo segundo no se aplicará en
el caso de créditos entre empresas consideradas
relacionadas conforme al número 17 del artículo 8° del
Código Tributario, salvo que se trate de empresas o
sociedades de apoyo al giro. Se entenderá que constituyen
empresas o sociedades de apoyo al giro aquellas sociedades o
empresas cuyo objeto único sea prestar servicios destinados
a facilitar el cumplimiento o desarrollo del negocio de
empresas relacionadas, o que por su intermedio se pueda
realizar operaciones del giro de las mismas.
    5°.- Una cuota anual de depreciación por los bienes
físicos del activo inmovilizado a contar de su utilización
en la empresa, calculada sobre el valor neto de los bienes a
la fecha del balance respectivo, una vez efectuada la
revalorización obligatoria que dispone el artículo 41°.
    El porcentaje o cuota correspondiente al período de
depreciación dirá relación con los años de vida útil
que mediante normas generales fije la Dirección y operará
sobre el valor neto total del bien. No obstante, el
contribuyente podrá aplicar una depreciación acelerada,
entendiéndose por tal aquélla que resulte de fijar a los
bienes físicos del activo inmovilizado adquiridos nuevos o
internados, una vida útil equivalente a un tercio de la
fijada por la Dirección o Dirección Regional. No podrán
acogerse al régimen de depreciación acelerada los bienes
nuevos o internados cuyo plazo de vida útil total fijada
por la Dirección o Dirección Regional sea inferior a tres
años. Los contribuyentes podrán en cualquiera oportunidad
abandonar el régimen de depreciación acelerada, volviendo
así definitivamente al régimen normal de depreciaciones a
que se refiere este número. Al término del plazo de
depreciación del bien, éste deberá registrarse en la
contabilidad por un valor equivalente a un peso, valor que
no quedará sometido a las normas del artículo 41°, y que
deberá permanecer en los registros contables hasta la
eliminación total del bien motivada por la venta, castigo,
retiro u otra causa. Tratándose de bienes que se han hecho
inservibles para la empresa antes del término del plazo de
depreciación que se les haya asignado, podrá aumentarse al
doble la depreciación correspondiente.
    En todo caso, cuando se aplique el régimen de
depreciación acelerada, sólo se considerará para los
efectos de lo dispuesto en el artículo 14, la depreciación
normal que corresponde al total de los años de vida útil
del bien. La diferencia que resulte en el ejercicio
respectivo entre la depreciación acelerada y la
depreciación normal, sólo podrá deducirse como gasto para
los efectos de primera categoría.
    La Dirección Regional, en cada caso particular, a
petición del contribuyente o del Comité de Inversiones
Extranjeras, podrá modificar el régimen de depreciación
de los bienes cuando los antecedentes así lo hagan
aconsejable.
    Para los efectos de esta ley no se admitirán
depreciaciones por agotamiento de las sustancias naturales
contenidas en la propiedad minera, sin perjuicio de lo
dispuesto en el inciso primero del artículo 30.
    5º bis.- Para los efectos de lo dispuesto en el número
5° precedente, los contribuyentes que en los 3 ejercicios
anteriores a aquel en que comience la utilización del bien,
sea que se trate de bienes nuevos o usados, tengan un
promedio anual de ingresos del giro igual o inferior a
100.000 unidades de fomento, podrán depreciar los bienes
del activo inmovilizado considerando como vida útil del
respectivo bien el equivalente a un décimo de la vida útil
fijada por la Dirección o Dirección Regional, expresada en
años, despreciando los valores decimales que resulten. En
todo caso, la vida útil resultante no podrá ser inferior a
un año. Si la empresa tuviere una existencia inferior a 3
ejercicios, el promedio se calculará considerando los
ejercicios de existencia efectiva.
    Para efectos de determinar el promedio de ingresos
anuales del giro conforme a lo dispuesto en los párrafos
precedentes, los ingresos de cada mes se expresarán en
unidades de fomento según el valor de ésta en el último
día del mes respectivo.
    En lo demás, se aplicarán las reglas que establece el
número 5° anterior.
    6°.- Sueldos, salarios y otras remuneraciones, pagados
o adeudados por la prestación de servicios personales.
    Se aceptarán como gasto las asignaciones de
movilización, alimentación, viático, las cantidades por
concepto de gastos de representación, participaciones,
gratificaciones legales y contractuales e indemnizaciones,
como así también otros conceptos o emolumentos de similar
naturaleza, siempre que los mismos guarden relación directa
con la naturaleza de la actividad de los trabajadores en la
empresa. Tratándose de pagos voluntarios por estos
conceptos, se aceptarán como gasto cuando se paguen o
abonen en cuenta y se retengan o paguen los impuestos que
sean aplicables.
    Tratándose de personas que por cualquiera circunstancia
personal o por la importancia de su haber en la empresa,
cualquiera sea la condición jurídica de ésta, hayan
podido influir, a juicio de la Dirección Regional, en la
fijación de sus remuneraciones, éstas sólo se aceptarán
como gasto en la parte que, según el Servicio, sean
razonablemente proporcionadas a la importancia de la
empresa, a las rentas declaradas, a los servicios prestados
y a la rentabilidad del capital, sin perjuicio de los
impuestos que procedan respecto de quienes perciban tales
pagos.
    No obstante disposición legal en contrario, para fines
tributarios, se aceptará como gasto la remuneración
razonablemente proporcionada en los términos del párrafo
anterior, que se asigne al socio, accionista o empresario
individual que efectivamente trabaje en el negocio o
empresa. En todo caso, dichas remuneraciones se
considerarán rentas del artículo 42, número 1. Asimismo,
se aceptará como gasto las remuneraciones pagadas al
cónyuge o conviviente civil del propietario o a sus hijos,
en la medida que se trate de una remuneración
razonablemente proporcionada en los términos del párrafo
anterior y que efectivamente trabajen en el negocio o
empresa.
    Las remuneraciones por servicios prestados en el
extranjero se aceptarán también como gastos, siempre que
se acrediten fehacientemente y se encuentren, por su
naturaleza, vinculadas directa o indirectamente al
desarrollo del giro.
    En el caso de reorganizaciones de grupos empresariales,
sea que consistan en reorganizaciones societarias o de
funciones, incluyendo los procesos de toma de control o
traspasos dentro de grupos económicos, que contemplen el
traslado total o parcial de trabajadores dentro de un mismo
grupo empresarial, sin solución de continuidad laboral, en
que se reconozcan por el nuevo empleador los años de
servicio prestados a otras empresas del grupo, procederá la
deducción como gasto el pago de las indemnizaciones que
correspondan por años de servicio al término de la
relación laboral, proporcionalmente según el tiempo
trabajado en las empresas donde se hayan prestado
efectivamente los servicios.
    6º bis.- Las becas de estudio que se paguen a los hijos
de los trabajadores de la empresa, siempre que ellas sean
otorgadas con relación a las cargas de familia u otras
normas de carácter general y uniforme aplicables a todos
los trabajadores de la empresa. En todo caso, el monto de la
beca por cada hijo, no podrá ser superior en el ejercicio
hasta la cantidad equivalente a una y media unidad
tributaria anual, salvo que el beneficio corresponda a una
beca para estudiar en un establecimiento de educación
superior y se pacte en un contrato o convenio colectivo de
trabajo, caso en el cual este límite será de hasta un
monto equivalente a cinco y media unidades tributarias
anuales.
    7°.- Las donaciones efectuadas cuyo único fin sea la
realización de programas de instrucción básica o media
gratuitas, técnica, profesional o universitaria en el
país, ya sean privados o fiscales, ya sea que los programas
de instrucción sean realizados directamente por la
institución donataria o a través de otras entidades o
establecimientos docentes, académicos o educacionales,
sólo en cuanto no excedan del 2% de la renta líquida
imponible de la empresa o del 1,6°/°° del capital propio
de la empresa al término del correspondiente ejercicio.
Esta disposición no será aplicada a las empresas afectas a
la ley N° 16.624.
    Lo dispuesto en el inciso anterior se aplicará también
a las donaciones que se hagan a los Cuerpos de Bomberos de
la República, Fondo de Solidaridad Nacional, Fondo de
Abastecimiento y Equipamiento Comunitario, Servicio Nacional
de Menores y a los Comités Habitacionales Comunales.
    Las donaciones a que se refiere este número no
requerirán del trámite de la insinuación y estarán
exentas de toda clase de impuestos.
    8°.- Los reajustes y diferencias de cambio provenientes
de créditos o préstamos destinados al giro del negocio o
empresa, incluso los originados en la adquisición de bienes
del activo inmovilizado y realizable.
    9°.- Los gastos de organización y puesta en marcha,
los cuales podrán ser amortizados hasta en un lapso de seis
ejercicios comerciales consecutivos contados desde que se
generaron dichos gastos o desde el año en que la empresa
comience a generar ingresos de su actividad principal,
cuando este hecho sea posterior a la fecha en que se
originaron los gastos.
    En el caso de empresas cuyo único giro según la
escritura de constitución sea el de desarrollar determinada
actividad por un tiempo inferior a 6 años no renovable o
prorrogable, los gastos de organización y puesta en marcha
se podrán amortizar en el número de años que abarque la
existencia legal de la empresa.
    Cuando con motivo de la fusión de sociedades,
comprendiéndose dentro de este concepto la reunión del
total de los derechos o acciones de una sociedad en manos de
una misma persona, el valor de la inversión total realizada
en los derechos o acciones de la sociedad fusionada, resulte
mayor al valor total o proporcional, según corresponda, que
tenga el capital propio de la sociedad absorbida,
determinado de acuerdo al artículo 41 de esta ley, la
diferencia que se produzca deberá, en primer término,
distribuirse entre todos los activos no monetarios que se
reciben con motivo de la fusión cuyo valor tributario sea
inferior al corriente en plaza. La distribución se
efectuará  en la proporción que represente el valor
corriente en plaza de cada uno de dichos bienes sobre el
total de ellos, aumentándose el valor tributario de éstos
hasta concurrencia de su valor corriente en plaza o de los
que normalmente se cobren o cobrarían en convenciones de
similar naturaleza, considerando las circunstancias en que
se realiza la operación. De subsistir la diferencia o una
parte de ella, ésta se considerará como un activo
intangible, sólo para los efectos de que sea castigado o
amortizado a la disolución de la empresa o sociedad, o
bien, al término de giro de la misma. Con todo, este activo
intangible formará parte del capital propio de la empresa,
y se reajustará anualmente conforme a lo dispuesto en el
número 6 del artículo 41.
    El valor de adquisición de los derechos o acciones a
que se refiere el inciso anterior, para determinar la citada
diferencia, deberá reajustarse según el porcentaje de
variación del Índice de Precios al Consumidor entre el mes
anterior al de la adquisición de los mismos y el mes
anterior al del balance correspondiente al ejercicio
anterior a aquel en que se produce la fusión.
    Conforme a lo dispuesto en el artículo 64 del Código
Tributario, el Servicio podrá tasar fundadamente los
valores de los activos determinados por el contribuyente en
caso que resulten ser notoriamente superiores a los
corrientes en plaza o los que normalmente se cobren o
cobrarían en convenciones de similar naturaleza,
considerando las circunstancias en que se realiza la
operación. La diferencia determinada en virtud de la
referida tasación, se considerará como parte del activo
intangible, según lo señalado en este número.
    10°.- Los gastos incurridos en la promoción o
colocación en el mercado de artículos nuevos fabricados o
producidos por el contribuyente, pudiendo el contribuyente
prorratearlos hasta en tres ejercicios comerciales
consecutivos, contados desde que se generaron dichos gastos.
    11°.- Los gastos incurridos en la investigación
científica y tecnológica en interés de la empresa aún
cuando no sean necesarios para producir la renta bruta del
ejercicio, pudiendo ser deducidos en el mismo ejercicio en
que se pagaron o adeudaron o hasta en seis ejercicios
comerciales consecutivos.
    12º.- Los pagos que se efectúen al exterior por los
conceptos indicados en el inciso primero del artículo 59 de
esta ley, hasta por un máximo de 4% de los ingresos por
ventas o servicios, del giro, en el respectivo ejercicio.
    El límite establecido en el inciso anterior no se
aplicará cuando, en el ejercicio respectivo, entre el
contribuyente y el beneficiario del pago no exista o no haya
existido relación directa o indirecta en el capital,
control o administración de uno u otro. Para que sea
aplicable lo dispuesto en este inciso, dentro de los dos
meses siguientes al del término del ejercicio respectivo,
el contribuyente o su representante legal, deberá formular
una declaración jurada en la que señale que en dicho
ejercicio no ha existido la relación indicada. Esta
declaración deberá conservarse con los antecedentes de la
respectiva declaración anual de impuesto a la renta, para
ser presentada al Servicio cuando éste lo requiera. El que
maliciosamente suscriba una declaración jurada falsa será
sancionado en conformidad con el artículo 97, número 4,
del Código Tributario.
    Tampoco se aplicará el límite establecido en el inciso
primero de este número, si en el país de domicilio del
beneficiario de la renta ésta se grava con impuestos a la
renta con tasa igual o superior a 30%. El Servicio de
Impuestos Internos, de oficio o a petición de parte,
verificará los países que se encuentran en esta
situación.
    Para determinar si los montos pagados por los conceptos
indicados en el inciso primero de este número se encuentran
o no dentro del límite allí indicado, deberán sumarse en
primer lugar todos los pagos que resulten de lo dispuesto en
los incisos segundo y tercero. Los restantes pagos se
sumarán a continuación de aquéllos.
    13°.- Los gastos o desembolsos incurridos con motivo de
exigencias, medidas o condiciones medioambientales impuestas
para la ejecución de un proyecto o actividad, contenidas en
la resolución dictada por la autoridad competente que
apruebe dicho proyecto o actividad de acuerdo a la
legislación vigente sobre medio ambiente.
    También podrán deducirse: a) los gastos o desembolsos
en los que el titular incurra con ocasión de compromisos
ambientales incluidos en el estudio o en la declaración de
impacto ambiental, respecto de un proyecto o actividad que
cuente o deba contar, de acuerdo con la legislación vigente
sobre medio ambiente, con una resolución dictada por la
autoridad competente que apruebe dicho proyecto o actividad
y b) los gastos o desembolsos efectuados en favor de la
comunidad y que supongan un beneficio de carácter
permanente, tales como gastos asociados a la construcción
de obras o infraestructuras de uso comunitario, su
equipamiento o mejora, el financiamiento de proyectos
educativos o culturales específicos y otros aportes de
similar naturaleza. En ambos casos, los gastos o desembolsos
deben constar en un contrato o convenio suscrito con un
órgano de la administración del Estado. Dichos pagos o
desembolsos no deben efectuarse directa o indirectamente en
beneficio de empresas del mismo grupo empresarial en los
términos del número 14 del artículo 8° del Código
Tributario o de personas o entidades relacionadas en los
términos del número 17 de la misma norma. Si los pagos o
desembolsos exceden de la cantidad mayor entre la suma
equivalente al 2% de la renta líquida imponible del
ejercicio respectivo, del 1,6 por mil del capital propio
tributario de la empresa, según el valor de éste al
término del ejercicio respectivo, o del 5% de la inversión
total anual que se efectúe en la ejecución del proyecto,
dicho exceso no será aceptado como gasto.
    14°. Los desembolsos o descuentos, ordenados por
entidades fiscalizadoras, que efectivamente pague el
contribuyente en cumplimiento de una obligación legal de
compensar el daño patrimonial a sus clientes o usuarios,
cuando dicha obligación legal no exija probar la
negligencia del contribuyente.
    Las cantidades que obtenga el contribuyente tras repetir
en contra de los terceros responsables se agregará a la
renta líquida del ejercicio en que se perciban. En estos
casos, las sumas que pague el tercero responsable para
reembolsar los desembolsos o descuentos a que se refiere
este número, no serán aceptados como gasto deducible de la
renta líquida imponible del tercero responsable, pero no se
gravarán con el impuesto establecido en el artículo 21 de
esta ley. Asimismo, pendientes las acciones de repetición
en contra de los terceros responsables, los desembolsos o
descuentos efectuados en cumplimiento de la obligación
legal de compensar no constituirán un activo para efectos
tributarios ni tendrán el tratamiento contemplado en el
número 4 de este artículo. Si se determina la negligencia
del contribuyente por autoridad competente, los desembolsos
o descuentos pagados no serán aceptados como gasto
deducible de la renta líquida imponible, pero no se
gravarán con el impuesto establecido en el artículo 21 de
esta ley.
    Las mismas reglas anteriores se aplicarán en caso que
el contribuyente, sin mediar culpa infraccional de su parte,
reponga o restituya un producto, o bonifique o devuelva
cantidades pagadas, a sus clientes o usuarios en los
términos de los artículos 19, 20 y 21 de la ley número
19.496. En estos casos, se considerarán como un menor
ingreso del ejercicio en que se obtuvieron las cantidades
pagadas y se agregarán a la renta líquida imponible del
ejercicio en que efectúen la referida reposición,
restitución, bonificación o devolución, y hasta el valor
de reposición, tratándose de productos.
    También constituyen gasto los desembolsos acordados
entre partes no relacionadas que tengan como causa el
cumplimiento de una transacción, judicial o extrajudicial,
o el cumplimiento de una cláusula penal.
```

### DL 824 (Renta) — Art. 33
*Artículo 1 › Doble Articulado › TITULO II Del impuesto cedular por categorías › PRIMERA CATEGORIA De las rentas del capital y de las empresas comerciales, industriales, mineras y otras › Párrafo 3º De la base imponible* — `idParte 8656063 · versión del artículo: 2020-02-24`

```
    ARTICULO 33°.- Para la determinación de la renta
liquida imponible, se aplicarán las siguientes normas:
    1°.- Se agregarán a la renta líquida las partidas que
se indican a continuación y siempre que hayan disminuido la
renta líquida declarada:
    a) SUPRIMIDA
    b) SUPRIMIDA
    c) Los retiros particulares en dinero o especies
efectuados por el contribuyente;
    d) Las sumas pagadas por bienes del activo inmovilizado
o mejoras permanentes que aumenten el valor de dichos bienes
y los desembolsos que deban imputarse al costo de los bienes
citados;
    e) Los costos, gastos y desembolsos que sean imputables
a ingresos no reputados renta o rentas exentas, los que
deberán rebajarse de los beneficios que dichos ingresos o
rentas originan;
    En los casos de gastos y desembolsos imputables tanto a
rentas gravadas como ingresos no renta y/o rentas exentas de
los impuestos finales, se deberá agregar aquella parte
asociada a los ingresos no renta y rentas exentas. Para
determinar dicho valor el contribuyente deberá optar por
una de las siguientes alternativas, la cual deberá mantener
por al menos 3 años comerciales consecutivos:

    1) Aplicar al total de gastos de utilización común,
pagados o adeudados en el ejercicio, el porcentaje que
resulte de dividir el total de ingresos no constitutivos de
rentas y rentas exentas de los impuestos finales, sobre el
total de ingresos brutos del ejercicio, incluyendo dentro de
estos últimos los ingresos no renta y rentas exentas.
    2) Aplicar al total de gastos de utilización común,
pagados o adeudados en el ejercicio, el factor que resulte
de multiplicar el resultado individual de las operaciones
señaladas en las letras a) y b) siguientes:

    a) La proporción entre el monto de los activos que
generan rentas no gravadas y exentas de los impuestos
finales sobre el monto total de activos asociados a la
generación de tales rentas. Los valores aludidos se
determinarán al cierre del ejercicio considerando lo
dispuesto en el artículo 41, según proceda. Si dichos
activos no existieren al término del ejercicio, se
atenderá a su valor al inicio del ejercicio o en su
defecto, al valor de adquisición.
    b) La proporción entre los ingresos no constitutivos de
rentas y rentas exentas de los impuestos finales, sobre el
total de ingresos brutos, incluidos en estos últimos los
ingresos no renta y rentas exentas, al término del
ejercicio respectivo, relacionadas con los activos y gastos
de este inciso.
    Para las operaciones descritas en las letras a) y b)
anteriores deberá considerarse la permanencia en días de
dichos activos e ingresos brutos durante el ejercicio
respectivo, tomando como base 365 días o la cantidad que
corresponda al año comercial respectivo.

    3) Con todo, cuando las metodologías señaladas
anteriormente no reflejen adecuadamente la situación del
modelo de negocios del contribuyente, éste podrá proponer
al Servicio un método alternativo que podrá considerar
factores de proporcionalidad, fijos o móviles, en base al
valor presente de los flujos futuros de los respectivos
bienes o funciones, u otra metodología basada en técnicas
de general aceptación. Para este efecto, se aplicará el
procedimiento previsto en el artículo 26 bis del Código
Tributario, en la forma y con los requisitos que el Servicio
regulará mediante resolución.
    f) Los gastos o desembolsos provenientes de los
siguientes beneficios que se otorguen a las personas
señaladas en el inciso segundo del N° 6 del artículo 31°
o a accionistas de sociedades anónimas cerradas o a
accionistas de sociedades anónimas abiertas dueños del 10%
o más de las acciones, al empresario individual o socios de
sociedad de personas y a personas que en general tengan
interés en la sociedad o empresa: uso o goce que no sea
necesario para producir la renta, de bienes a título
gratuito o avaluados en un valor inferior al costo, casos en
los cuales se les aplicará como renta a los beneficiarios
no afectados por el artículo 21 la presunción de derecho
establecida en el literal iii) del inciso tercero de dicho
artículo, sin perjuicio de lo dispuesto en la oración
final de ese inciso, condonación total o parcial de deudas,
exceso de intereses pagados, arriendos pagados o percibidos
que se consideren desproporcionados, acciones suscritas a
precios especiales y todo otro beneficio similar, y sin
perjuicio de los impuestos que procedan respecto de sus
beneficiarios, y
    g) Las cantidades cuya deducción no autoriza el
artículo 31° o que se rebajen en exceso de los márgenes
permitidos por la ley o la Dirección Regional, en su caso.
    2°.- Se deducirán de la renta líquida las partidas
que se señalan a continuación, siempre que hayan aumentado
la renta líquida declarada:
    a) Los dividendos percibidos y las utilidades sociales
percibidas o devengadas por el contribuyente en tanto no
provengan de sociedades o empresas constituidas fuera del
país, aún cuando se hayan constituido con arreglo a las
leyes chilenas;
    b) Rentas exentas por esta ley o leyes especiales
chilenas. En el caso de intereses exentos, sólo podrán
deducirse los determinados de conformidad a las normas del
artículo 41 bis.
    c) Las cantidades a que se refieren los numerales i. del
inciso primero e i) del inciso tercero, del artículo 21.
    3°.- Los agregados a la renta líquida que procedan de
acuerdo con las letras a), b), c), f) y g), del N° 1° se
efectuarán reajustándolos previamente de acuerdo con el
porcentaje de variación que haya experimentado el Indice de
Precios al Consumidor en el período comprendido entre el
último día del mes anterior a la fecha de la erogación o
desembolso efectivo de la respectiva cantidad y el último
día del mes anterior a la fecha del balance.
    4°.- La renta líquida correspondiente a actividades
clasificadas en esta categoría, que no se determine en base
a los resultados de un balance general, deberá reajustarse
de acuerdo con el porcentaje de variación experimentada por
el índice de precios al consumidor en el período
comprendido entre el último día del mes anterior a aquél
en que se percibió o devengó y el último día del mes
anterior al del cierre del ejercicio respectivo. Tratándose
de rentas del artículo 20, N° 2, se considerará el
último día del mes anterior al de su percepción.
    No quedará sujeta a las normas sobre reajuste
contempladas en este número ni a las de los artículos 54°
inciso penúltimo, y 62°, inciso primero, la renta líquida
imponible que se establezca en base al sistema de
presunciones que contempla el artículo 34°. Tampoco
quedará sujeta a las normas sobre reajuste antes
señaladas, la renta líquida imponible que se determine por
inversiones en el extranjero e ingresos gravados en el
extranjero, la cual se regirá por lo dispuesto en el
artículo 41 A número 7 letra a) y 41 B inciso primero.
    5º.- Derogado.
```

### DL 824 (Renta) — Art. 70
*Artículo 1 › Doble Articulado › TITULO V De la administración del impuesto › Párrafo 1º De la declaración y pago anual* — `idParte 8656110 · versión del artículo: 2014-09-29`

```
    ARTICULO 70°.- Se presume que toda persona disfruta de
una renta a lo menos equivalente a sus gastos de vida y de
las personas que viven a sus expensas.
    Si el interesado no probare el origen de los fondos con
que ha efectuado sus gastos, desembolsos o inversiones, se
presumirá que corresponden a utilidades afectas al impuesto
de Primera Categoría según el N° 3° del artículo 20 o
clasificadas en la Segunda Categoría conforme al N° 2°
del artículo 42, atendiendo a la actividad principal del
contribuyente.
    Los contribuyentes que no estén obligados a llevar
contabilidad completa, podrán acreditar el origen de dichos
fondos por todos los medios de prueba que establece la ley.
    Cuando el contribuyente probare el origen de los fondos,
pero no acreditare haber cumplido con los impuestos que
hubiese correspondido aplicar sobre tales cantidades, los
plazos de prescripción establecidos en el artículo 200 del
Código Tributario se entenderán aumentados por el término
de seis meses contados desde la notificación de la
citación efectuada en conformidad con el artículo 63 del
Código Tributario, para perseguir el cumplimiento de las
obligaciones tributarias y de los intereses penales y multas
que se derivan de tal incumplimiento.
```

---

## 4. Cierre

Este módulo habilita, por primera vez en la skill, el análisis penal
tributario con texto verificado: el requisito de procesabilidad exclusiva
del art. 162 CT, el catálogo de infracciones del art. 97 CT, y las
herramientas sustantivas de la Ley de Renta y la Ley de IVA que explican los
patrones de fraude fiscal detectados por `references/forense-financiero.md`.
Los artículos fuera de este perímetro —en particular el detalle completo de
cada numeral del art. 97 más allá de su enumeración general, y las normas de
determinación de la renta líquida imponible no listadas en la sección 2.5—
conservan la marca «pendiente de verificación» y requieren ampliación del
perímetro en una curatoría futura si el caso concreto lo exige.
