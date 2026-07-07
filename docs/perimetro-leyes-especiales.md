# Perímetro propuesto — Curatoría de leyes especiales para `references/leyes-especiales.md`

> **CONSTANCIA DE EJECUCIÓN (2026-07-07)**: la curatoría se ejecutó en esta
> fecha con descarga directa desde el servicio oficial, por instrucción del
> abogado. idNorma confirmados: 21.595 → 1195119; 20.393 → 1008668; 19.913 →
> 219119; 21.459 → 1177743; 20.000 → 235507. Perímetros definitivos según el
> registro de curatoría de `skill/references/leyes-especiales.md` (177
> artículos, sin advertencias de completitud). Este documento se conserva como
> propuesta original; las diferencias de numeración quedaron resueltas contra
> el inventario real de cada XML.

> **Naturaleza de este documento**: propuesta de alcance para la próxima sesión de
> curatoría, elaborada para que la sesión parta con el perímetro ya definido. La
> numeración de artículos que sigue es **indicativa y debe confirmarse contra el XML
> oficial** una vez descargado: varias de estas leyes han sido renumeradas o
> modificadas (en particular la Ley 20.393 tras la Ley 21.595), de modo que ningún
> número de artículo de este documento puede citarse en escritos antes de la
> verificación. Los idNorma indicados como «a confirmar» se validan en la propia
> página de LeyChile al momento de la descarga.
>
> **Procedimiento** (idéntico al validado para CP y CPP, conforme a la regla
> metodológica pendiente de aprobación): (1) el abogado descarga el XML consolidado
> desde `https://www.leychile.cl/Consulta/obtxml?opt=7&idNorma=<ID>`; (2) se valida
> el idNorma con `curar_norma.py --listar`; (3) se extrae el perímetro aprobado;
> (4) control de calidad: derogados marcados, artículos no hallados advertidos,
> fechas de versión revisadas artículo por artículo (regla «2222-02-02»); (5) el
> extracto se inserta sin edición manual en `references/leyes-especiales.md`.

---

## 1. Ley 21.595 — Delitos económicos (D.O. 17-08-2023)

**idNorma**: a confirmar en LeyChile.

**Núcleo propuesto para extracción íntegra**:
- Artículos iniciales de calificación: definición de delito económico y las
  cuatro categorías del catálogo (arts. 1 a 4, con sus remisiones).
- Sistema especial de determinación de la pena: atenuantes y agravantes
  especiales, reglas de concurrencia y de sustitución (bloque central de la ley,
  numeración a confirmar).
- Pena de multa a través del sistema de días-multa: unidades, tramos y criterios
  de determinación.
- Inhabilitaciones especiales para condenados por delitos económicos.
- Régimen del comiso de ganancias en su remisión al CP (los arts. 24 bis y
  24 ter CP ya constan verificados en `marco-legal.md`) y comiso sin condena.

**Queda fuera del perímetro** (marca «cita pendiente de verificación»): las
disposiciones modificatorias de otros cuerpos legales (la ley modifica CP, CPP,
Ley 20.393 y numerosas leyes sectoriales), salvo las ya capturadas en las
curatorías respectivas.

**Punto de control**: la ley aplica a hechos posteriores al 17-08-2023 según su
régimen transitorio; verificar las reglas de entrada en vigencia diferida en el
propio XML (posible marca «2222-02-02»).

---

## 2. Ley 20.393 — Responsabilidad penal de las personas jurídicas (D.O. 02-12-2009, texto post-Ley 21.595)

**idNorma**: a confirmar en LeyChile.

**Núcleo propuesto para extracción íntegra**:
- Ámbito: catálogo de delitos y personas jurídicas alcanzadas (arts. 1 a 2,
  numeración a confirmar).
- Presupuestos de la responsabilidad: hecho de la persona relacionada, deber de
  dirección y supervisión, y efecto del modelo de prevención de delitos
  (arts. 3 y siguientes).
- Modelo de prevención de delitos: elementos mínimos.
- Responsabilidad autónoma de la persona jurídica.
- Catálogo de penas (disolución, inhabilitación para contratar con el Estado,
  pérdida de beneficios fiscales, multa, supervisión), reglas de determinación
  y circunstancias modificatorias.
- Reglas procesales esenciales de la investigación y juzgamiento de la persona
  jurídica.

**Punto de control**: la Ley 21.595 sustituyó extensamente esta ley (catálogo
amplio de delitos económicos, pena de supervisión, días-multa). El texto
consolidado post-reforma es el único citable; toda referencia doctrinaria
anterior a 2023 debe cotejarse contra la numeración vigente.

---

## 3. Ley 19.913 — UAF y lavado de activos (D.O. 18-12-2003)

**idNorma**: a confirmar en LeyChile.

**Núcleo propuesto para extracción íntegra**:
- Art. 27: tipo de lavado de activos (incluido autolavado y lavado culposo),
  catálogo de delitos base y penalidad.
- Art. 28: asociación para el lavado (verificar vigencia tras la Ley 21.577
  sobre asociaciones delictivas y criminales).
- Reglas de comiso e investigación patrimonial asociadas al Título respectivo,
  incluido el comiso sin condena en su remisión al CPP.
- Deberes de información: sujetos obligados y reporte de operaciones
  sospechosas (arts. 2 y 3), en cuanto insumo del análisis forense financiero.
- Secreto y levantamiento de secreto bancario en el marco de la investigación
  de lavado.

**Queda fuera del perímetro**: la orgánica administrativa interna de la UAF
(planta, personal, presupuesto).

---

## 4. Ley 21.459 — Delitos informáticos (D.O. 20-06-2022)

**idNorma**: a confirmar en LeyChile.

**Núcleo propuesto para extracción íntegra**:
- Tipos penales (Título I completo): ataque a la integridad de un sistema
  informático; acceso ilícito; interceptación ilícita; ataque a la integridad
  de los datos informáticos; falsificación informática; receptación de datos
  informáticos; fraude informático; abuso de los dispositivos (arts. 1 a 8,
  numeración a confirmar).
- Circunstancias modificatorias especiales, incluida la cooperación eficaz.
- Disposiciones procesales: técnicas especiales de investigación y la
  **preservación provisoria de datos informáticos**, insumo directo de
  `references/prueba-digital.md`.
- Modificaciones pertinentes al CPP en materia de registros y comiso de datos,
  si constan en el texto consolidado de otra norma, se capturan en la curatoría
  del cuerpo respectivo.

**Punto de control**: esta ley implementa el Convenio de Budapest; su catálogo
integra además el listado de delitos base de la Ley 20.393. Anclar
`prueba-digital.md` a los artículos verificados una vez curados.

---

## 5. Ley 20.000 — Tráfico ilícito de estupefacientes (D.O. 16-02-2005)

**idNorma**: a confirmar en LeyChile.

**Núcleo propuesto para extracción íntegra**:
- Tipos nucleares: elaboración y producción (art. 1); tráfico (art. 3);
  microtráfico (art. 4); desvío de precursores (art. 2); suministro indebido
  y prescripción abusiva (arts. 6 a 8, a confirmar).
- Formas especiales: cultivo (arts. 8 a 10, a confirmar), facilitación de
  bienes o inmuebles.
- Circunstancias modificatorias especiales (arts. 19 a 22, a confirmar),
  incluida la **cooperación eficaz** (art. 22) y las agravantes especiales.
- Reglas de determinación de pena propias y comiso.
- Técnicas especiales de investigación (entregas vigiladas, agentes
  encubiertos e informantes) en cuanto afectan la licitud de la prueba.
- Falta de consumo (art. 50) solo como referencia de deslinde con el
  microtráfico.

**Punto de control**: verificar la coordinación con la Ley 21.577 en materia de
asociación criminal (derogación o sustitución de la antigua asociación ilícita
del art. 16) y las reformas posteriores sobre penas y precursores.

---

## Cierre

Aprobado este perímetro (con los ajustes que el abogado disponga), la sesión de
curatoría requiere únicamente: los cinco XML descargados por el abogado, la
ejecución de `curar_norma.py` por ley, el control de calidad artículo por
artículo y la inserción de los extractos en `references/leyes-especiales.md`,
cuyo texto metodológico (sistema de determinación Ley 21.595, matriz RPPJ,
tipologías de lavado) se redactará sobre los artículos ya verificados. Con ello,
las marcas «pendiente de verificación» de `calculo-penas.md` y
`prueba-digital.md` se sustituyen por citas verificadas.
