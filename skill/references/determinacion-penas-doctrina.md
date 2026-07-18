# Determinación de penas — Criterios de aplicación judicial (doctrina institucional curada)

> **Estado del módulo**: OPERATIVO — CAPA DOCTRINAL. Este módulo **no** contiene
> norma verificada. Su fuente única es la *Guía aplicada para la determinación
> de penas*, Academia Judicial de Chile, © 2026, 137 pp., autores Javier
> Wilenmann von Bernath, Francisco Maldonado Fuentes y Sebastián Valenzuela
> Agüero, validada por comité de jueces de garantía y orales en lo penal.
> PDF fuente: `Guia-aplicada-para-la-determinacion-de-penas.pdf`,
> SHA-256 `04a388ce92b4280920d7a66785868eccc4d507f7718ffcbd0d68dc7ce6fe6c81`.
> Curatoría del 2026-07-17 sobre extracción de texto íntegra del PDF.

## 0. Regla de jerarquía y uso

1. **Prelación normativa.** En caso de discrepancia entre este módulo y el texto
   verificado de `marco-legal.md`, `leyes-especiales.md` o `tributario.md`,
   prevalece siempre el texto verificado. Este módulo aporta *criterios de
   aplicación judicial* sobre normas ya verificadas; jamás sustituye la norma.
2. **Marcas pendientes levantadas (2026-07-17).** Las dos marcas que esta regla
   reservaba fueron subsanadas por curatoría determinística: el **art. 351 CPP**
   fue descargado y verificado vía `curar_norma.py --descargar` (XML oficial,
   SHA-256 registrado) e insertado en `marco-legal.md`, sección 3.7; la **tabla
   demostrativa del art. 56 CP** fue cotejada contra la imagen oficial embebida
   en el XML de LeyChile (cotejo conforme; transcripción verificada en
   `marco-legal.md`, sección 2.2). En consecuencia, la sección 2.5 de este
   módulo queda **habilitada para cita textual** del art. 351 CPP, con remisión
   al texto verificado.
3. **Jurisprudencia citada.** Toda sentencia individualizada en este módulo
   proviene de la guía (fuente documentada, no memoria del modelo), por lo que
   es citable *como referencia de la guía*. Su uso directo en escritos
   judiciales exige verificación previa contra la fuente primaria (texto del
   fallo), conforme al protocolo de `jurisprudencia-curada.md`. Estado por
   defecto de cada entrada: **candidata / pendiente de verificación primaria**.
4. **Cuándo cargar.** Carga este módulo junto con `calculo-penas.md` cuando el
   cálculo enfrente alguno de los problemas de aplicación de la sección 2, o
   cuando se requiera anticipar cómo razonará el tribunal (la guía consolida la
   práctica que la Academia Judicial difunde a los propios jueces, lo que le
   confiere valor predictivo estratégico).

## 1. Marco general consolidado por la guía

La guía descompone la determinación en la misma secuencia del algoritmo de
`calculo-penas.md`, sección II: (i) pena en abstracto del título de condena;
(ii) ajuste por ejecución imperfecta y participación (arts. 50–61 CP);
(iii) circunstancias modificatorias, con compensación racional previa y luego
atribución de efectos (arts. 65–68 ter CP); (iv) individualización (art. 69 CP);
(v) sustitutivas. Consigna expresamente que la **práctica judicial estándar**
fija la pena en el punto mínimo del marco resultante, y que todo apartamiento
hacia arriba exige fundamentación reforzada (p. 6 y caso RIT 85-2024). Esta
constatación es estratégica: el punto mínimo es la línea base esperable y la
carga argumentativa recae sobre quien pretende moverla.

## 2. Problemas de aplicación documentados

### 2.1. Individualización agravada vs. concurso ideal (RIT 85-2024, 3° TOP de Santiago)

Homicidio simple frustrado con secuelas graves: el tribunal individualizó en 4
años dentro de presidio menor en su grado máximo, expresando el disvalor de las
lesiones como «mayor extensión del mal» (art. 69 CP), en lugar de construir un
concurso ideal homicidio frustrado / lesiones consumadas. La guía valida ambas
vías y advierte que, siendo el marco resultante un grado simple, la regla del
art. 75 CP no produce efecto agravatorio, por lo que la vía del art. 69 permite
expresar el disvalor que el concurso ideal no captura. **Uso defensivo**: cuando
la acusación individualice sobre el mínimo invocando resultados lesivos,
verificar si esos resultados ya integran el injusto del tipo (prohibición de
doble valoración) y exigir la fundamentación reforzada que la propia práctica
estándar impone.

### 2.2. Media prescripción del art. 103 CP y concurrencia con atenuantes simples (RIT 5081-2014, 3° JG de Santiago)

Problema nuclear para toda tesis de media prescripción. La guía identifica dos
alternativas interpretativas ante la ausencia de regla de efectos para
«atenuantes muy calificadas» en el CP:

- **Alternativa 1 — aplicación única del art. 103.** El efecto se operacionaliza
  como el de dos atenuantes simples (en marco de un grado: art. 67 inc. 4°,
  rebaja facultativa de uno o dos grados desde el mínimo). Las atenuantes
  simples concurrentes (11 N° 6 y N° 9) quedan absorbidas y solo operan en la
  individualización.
- **Alternativa 2 — efecto acumulativo.** Se aplica primero el art. 103 (rebaja
  de 1–2 grados) y luego, nuevamente, el efecto de las atenuantes simples
  (rebaja adicional de 1–2 grados), habilitando rebajas totales de 2 a 4 grados
  y, en el caso estudiado, incluso pena de prisión.

El tribunal del caso siguió la primera alternativa: acogió el art. 103, rebajó
dos grados «como límite legal» del art. 67 y negó la multa pedida por la
defensa, imponiendo 61 días sustituidos por remisión condicional. La guía deja
la cuestión abierta como genuinamente controvertida y remite a Parra (2019),
«Los efectos de la media prescripción penal», *Revista de Derecho* U. de
Concepción, Vol. 87, N° 246. **Nota táctica**: en el análisis del RUC
2410023084-0 la alternativa 2 debe plantearse como petición principal y la
alternativa 1 como piso subsidiario, consignando que la primera carece de
respaldo uniforme y anticipando la contratesis de absorción (Protocolo de
Contradicción Obligatoria de `argumentacion-forense`).

Dato procesal adicional del fallo: la formalización —no el despacho de la orden
de detención— es el hito que suspende la prescripción, criterio concordante con
la sección V de `calculo-penas.md` y con el motor `prescripcion.py`.

### 2.3. Compensación racional, derogación del art. 449 N° 2 CP y nuevo art. 68 ter (RIT 99-2023, TOP de Valparaíso; CS Rol 2885-2025)

La Ley 21.694 (promulgada 27-08-2024, publicada 04-09-2024) derogó el art. 449
N° 2 CP y trasladó el efecto de la reincidencia al actual art. 68 ter CP, que
permite «recorrer la pena en toda su extensión» cuando la reincidencia concurre
con la atenuante del art. 11 N° 9, entre otras. En adecuación de sentencia
(art. 18 CP), el TOP mantuvo la pena original de 3 años y 1 día pese al nuevo
marco ampliado; la Corte Suprema confirmó el rechazo del amparo (Rol
2885-2025), **con voto disidente del Ministro Llanos**, para quien, habiendo el
tribunal de instancia fijado originalmente el mínimo posible, la coherencia con
sus propios fundamentos exigía rebajar a 541 días. **Uso defensivo**: el voto
disidente suministra el argumento de congruencia interna —si la sentencia
original individualizó en el mínimo por ser el mínimo, la ampliación
sobreviniente del marco arrastra la pena al nuevo mínimo—; su carácter de
disidencia obliga a presentarlo como criterio minoritario, nunca como doctrina
asentada.

### 2.4. Subida del marco penal con pluralidad de agravantes (art. 68 inc. 4° CP)

La guía constata disparidad jurisprudencial entre dos mecánicas:

- **Subida «en bloque»**: desplazamiento íntegro del marco compuesto en un
  grado (en el caso del art. 366 bis: presidio mayor en sus grados mínimo a
  medio, con punto de práctica en 5 años y 1 día).
- **Subida desde el grado superior** (criterio que la guía adopta por
  fidelidad al tenor del art. 68 inc. 4°: «la inmediatamente superior en grado
  al máximo de los designados por la ley»): el marco queda en el grado único
  inmediatamente superior al techo (presidio mayor en su grado medio; punto de
  práctica en 10 años y 1 día).

La guía registra además que parte de los tribunales trata el «podrá» como
facultad para no subir, incluso invocando proporcionalidad, y que un sector
doctrinal califica ciertas soluciones intermedias como elusión de ley. **Uso
estratégico**: la brecha entre ambas mecánicas puede exceder los cinco años de
privación de libertad; en defensa, la facultatividad del «podrá» y la
proporcionalidad concreta son la primera línea; en el peor escenario acotado,
debe presupuestarse la subida desde el grado superior, que es la tesis que la
Academia difunde a los jueces.

### 2.5. Multiplicidad de delitos: algoritmo concursal y art. 351 CPP

Secuencia consolidada por la guía (Parte II): **(1)** depurar títulos (unidad de
acción y concurso aparente, por especialidad o consunción; la guía documenta
jurisprudencia dividida en el ejemplo arts. 196/209 vs. 194 LdT); **(2)**
verificar en orden: concurso ideal → concurso medial → delitos de la misma
especie → cláusula concursal especial; **(3)** aplicar la regla penológica que
corresponda (arts. 75 CP o 351 CPP), y solo en su defecto **(4)** la
acumulación material del art. 74 CP; luego continuar con modificatorias e
individualización sobre el marco unificado.

Criterios de aplicación del art. 351 CPP documentados:

1. **Misma especie** = protección del mismo bien jurídico (inciso final). En
   delitos pluriofensivos (robo con violencia), la homogeneidad se juzga por el
   **bien jurídico predominante**, criterio ampliamente mayoritario.
2. **Inciso segundo** (delitos que no pueden estimarse como uno solo): (i)
   determinar individualmente la pena de cada título, (ii) identificar la más
   grave, (iii) exasperar en uno o dos grados. La comparación se efectúa entre
   **marcos o grados, sin agotar la individualización** de cada delito; la guía
   critica expresamente la práctica de individualizar cada pena en concreto
   antes de comparar.
3. La elección entre art. 351 CPP y art. 74 CP se resuelve por el resultado más
   favorable al condenado, cotejo que debe consignarse en el cálculo.

**Nota de gobernanza (actualizada el 2026-07-17)**: el texto del art. 351 CPP
consta **verificado** en `marco-legal.md`, sección 3.7 (idParte 8646929,
versión del artículo 2000-10-12, XML oficial SHA-256 registrado). Esta sección
queda habilitada tanto para el razonamiento de aplicación como para la **cita
textual**, siempre con remisión al extracto verificado.

### 2.6. Delitos económicos — LDE (Ley 21.595), personas naturales

La guía confirma la mecánica de la sección VI de `calculo-penas.md` y agrega
criterios operativos:

1. **Calificación previa**: arts. 1 (siempre), 2 y 3 (contexto corporativo de
   mediana o gran empresa), lavado/receptación (delito base económico o
   contexto corporativo).
2. **Modificatorias bidimensionales**: el juez está *obligado* a graduar
   perjuicio (muy bajo / bajo / alto / muy alto, por umbrales UTM de los
   arts. 13–16 N° 2) y culpabilidad (N° 1 de los mismos artículos); hasta dos
   modificatorias por hecho. Las simples solo operan en la individualización
   (art. 18); las muy calificadas mueven el marco (art. 17).
3. **Sustitutivas — tabla de decisión rápida** (verificable contra arts. 19–26
   LDE en `leyes-especiales.md`):

   | Pena individualizada | Condición sobre muy calificadas | Sustitutiva |
   |---|---|---|
   | ≤ 3 años | al menos una atenuante MC no compensada | remisión condicional (art. 21) |
   | ≤ 3 años | sin agravante MC no compensada | reclusión parcial domiciliaria (art. 24) |
   | 3 años y 1 día a 5 años | sin agravante MC no compensada | reclusión parcial en establecimiento especial (art. 26) |
   | cualquiera | agravante MC no compensada | cumplimiento efectivo |
   | > 5 años | irrelevante | cumplimiento efectivo |

   No proceden libertad vigilada (en ninguna forma) ni servicios en beneficio
   de la comunidad.
4. **Multa obligatoria**: en todos los casos, por días-multa (arts. 26 y ss.
   LDE), imponiendo la de mayor cuantía cuando concurra con multa del tipo.
5. **Ejercicio Nova Austral** (arts. 136 LGPA y 470 N° 8 CP, perjuicio ≈ USD 50
   millones): la guía desarrolla el cálculo completo por interviniente
   (autor, inductor, encubridores) y la determinación de días-multa sobre
   capacidad económica real, incluyendo ingresos societarios del condenado
   (base imponible IGC más utilidades de sociedades de las que es único socio).
   Referencia metodológica para la matriz de capacidad económica del módulo
   `forense-financiero.md`.

### 2.7. Personas jurídicas — Ley 20.393

Tres operaciones consolidadas: **(1)** marco ajustado del tipo (abstracto →
ejecución imperfecta → modificatorias de los arts. 6 y 7 de la Ley 20.393 con
los efectos de los arts. 65 y ss. CP → ajuste concursal previo si procede) y
clasificación crimen / simple delito según los grados resultantes; **(2)**
selección de penas: multa y publicación del extracto son obligatorias; las
restantes (prohibiciones, supervisión) se seleccionan por mérito, evitando
efectos sociales o de mercado indeseados; **(3)** individualización de la
multa.

Criterios de la multa documentados en el ejercicio Penta (soborno, arts. 250 y
248 bis CP; rebaja adicional del art. 407 CPP por abreviado, con debate sobre
su acumulabilidad con la colaboración):

- **Prelación del sistema especial**: conforme al art. 12 de la Ley 20.393, el
  sistema de días-multa cede ante mecanismos legales de cálculo especiales; en
  soborno, la guía estima preferente la **multa proporcional** (duplo al
  cuádruplo del beneficio), y solo subsidiariamente el sistema de días-multa
  (2–200 simples delitos; 200–400 crímenes).
- **Punto medio como default** (art. 16 Ley 20.393), corregido a la mitad o
  cuarto inferior por atenuantes, y refinado por graduación de perjuicio y
  reproche organizacional (modelo de prevención «de papel» en gran empresa =
  reproche muy elevado; colaboración y remediación pre-formalización lo
  degradan).
- **Conversión**: valor del día-multa = utilidad anual / 365 (en el ejercicio:
  125 días-multa sobre utilidad de MM$ 38.500 ≈ $13.185 millones).
- El fallo real impuso 10.000 UTM y prohibición de contratar por 3 años bajo la
  ley vigente a la fecha de los hechos; la guía contrasta ambos modelos como
  ejercicio de derecho intertemporal.

### 2.8. Responsabilidad penal adolescente (Ley 20.084) — mínimo esencial

Dos reglas de alto valor para eventuales recursos: (i) la determinación parte
de la pena inferior en un grado al mínimo legal, aplicando los arts. 50 a 78 CP
con exclusión del art. 69 y **sin aplicación del art. 351 CPP**; (ii) la
exasperación por reiteración opera *dentro del tramo* del art. 23 LRPA
—ampliando extensión o sustituyendo por sanción más gravosa del mismo tramo—,
estando **prohibido subir de tramo**, criterio afirmado tajantemente por la
Corte Suprema en nulidad: Roles 57.252-2021, 2442-2025 y 4757-2025
*(candidatas, pendientes de verificación primaria)*. Los criterios de
intensidad son los del art. 24 (número de delitos, nexos, valoración de
conjunto).

## 3. Lote de jurisprudencia candidata para `jurisprudencia-curada.md`

Todas las entradas provienen de la guía; estado: **pendiente de verificación
primaria** conforme al protocolo de la Línea IV. No citar en escritos sin
verificación contra el texto del fallo.

| Resolución | Materia | Aporte |
|---|---|---|
| RIT 85-2024, 3° TOP Santiago | homicidio frustrado; individualización agravada art. 69 | apartamiento fundado del punto mínimo |
| RIT 5081-2014, 3° JG Santiago | media prescripción art. 103 + atenuantes simples | alternativa de aplicación única; suspensión por formalización |
| RIT 99-2023, TOP Valparaíso y CS Rol 2885-2025 | art. 68 ter post-Ley 21.694; adecuación art. 18 CP | facultad de recorrer el marco; disidencia Llanos (congruencia con el mínimo) |
| RIT 65-2022, TOP Curicó | subida del marco art. 68 inc. 4° | «podrá» como facultad; proporcionalidad |
| RIT 100-2025, TOP Rancagua; RIT 733-2009, JG Lautaro; RIT 165-2009 y 5-2010, TOP Calama | concursos; art. 351 CPP | misma especie por bien jurídico predominante; exasperación sin individualización previa |
| RIT 4-2025, 7° TOP Santiago; RIT 271-2024, TOP Antofagasta | reiteración y unificación en RPA | mecánica del art. 25 en relación con el 23 LRPA |
| CS Roles 57.252-2021, 2442-2025, 4757-2025 | RPA, nulidad | prohibición de subir de tramo del art. 23 LRPA |

Doctrina citada por la guía: Parra, Francisco (2019), «Los efectos de la media
prescripción penal», *Revista de Derecho*, Universidad de Concepción, Vol. 87,
N° 246 *(referencia de la fuente; no verificada)*.

## 4. Cierre

Este módulo suministra la capa de práctica judicial que el algoritmo normativo
de `calculo-penas.md` no puede contener por diseño. Su función es doble:
anticipar el razonamiento probable del tribunal —la guía es el material con que
la Academia Judicial capacita a los propios jueces— y acotar el peor escenario
en cada punto controvertido, conforme a la regla de decisión de
`argumentacion-forense`. Toda afirmación aquí contenida se reconduce a la
fuente única identificada en el encabezado; toda cita normativa se coteja
contra los módulos verificados; y toda sentencia mantiene su marca de
verificación pendiente hasta su curatoría individual.
