# Entradas de `aprendizajes.md` — APROBADAS E INCORPORADAS

> **Estado**: las tres entradas siguientes fueron formuladas conforme al Protocolo de
> Cierre y Aprendizaje (SKILL.md, sección 15.3) y **aprobadas por el abogado el
> 2026-07-07** («apruebo las tres»). Quedaron incorporadas ese mismo día a la sección
> «Aprendizajes activos» de `references/aprendizajes.md` de la skill instalada, con
> incremento de versión a **3.6** y constancia en el registro de cambios. Este archivo
> se conserva como acta de la aprobación.

---

### [2026-07-06] — Fuente-verificada — Servicio XML oficial de LeyChile (`obtxml opt=7`)
- **Contexto**: sesión de curatoría normativa que pobló `references/marco-legal.md` (248 artículos CP/CPP) desde los XML oficiales de la Biblioteca del Congreso Nacional.
- **Lección**: el servicio `https://www.leychile.cl/Consulta/obtxml?opt=7&idNorma=<ID>` (opcionalmente `&notaPIE=1`) entrega el texto consolidado y vigente de la norma en esquema `EsquemaIntercambioNorma-v1-0`, con metadatos de versión por artículo (idParte y fecha de versión). Identificadores verificados: Código Penal → idNorma **1984**; Código Procesal Penal (Ley 19.696) → idNorma **176595**; Código Tributario (DL 830) → idNorma **6374**.
- **Regla operativa**: toda cita normativa de la skill se verifica contra XML descargado desde ese servicio, identificando la norma por su idNorma verificado. Queda prohibido el uso de mirrors privados, agregadores o versiones sin fecha.
- **Vigencia**: permanente.

### [2026-07-06] — Metodología — Curatoría normativa exclusivamente vía `curar_norma.py` sobre XML descargado por el abogado
- **Contexto**: misma sesión de curatoría. Se constató que la transcripción manual o reconstruida de memoria introduce riesgo de texto desactualizado o inexacto, incompatible con el estándar del estudio.
- **Lección**: la única cadena admisible para poblar módulos normativos es: (1) el abogado descarga personalmente el XML desde LeyChile; (2) el XML se procesa con `scripts/curar_norma.py`, que valida idNorma, extrae el perímetro, marca derogados, excluye transitorios y advierte artículos no hallados; (3) el extracto se inserta íntegro, sin edición manual del texto legal.
- **Regla operativa**: ninguna curatoría normativa se ejecuta por transcripción manual ni desde la memoria del modelo. Si no hay XML aportado por el abogado, el artículo conserva la marca «cita pendiente de verificación».
- **Vigencia**: permanente.

### [2026-07-06] — Fuente-verificada — La marca «2222-02-02» en el XML de LeyChile denota vigencia diferida, no error de fuente
- **Contexto**: al procesar el XML del Código Penal (idNorma 1984) se observó que el atributo de versión de la norma reporta la fecha «2222-02-02», coexistiendo con artículos cuya fecha de versión individual es real (la más reciente del perímetro: 17-09-2025).
- **Lección**: LeyChile utiliza la fecha centinela «2222-02-02» para señalar que el cuerpo normativo contiene al menos una disposición con **vigencia diferida** (aún no vigente); no constituye error del servicio ni invalida la descarga.
- **Regla operativa**: cuando el XML reporte versión de norma «2222-02-02», la curatoría debe (a) dejar constancia de la marca en el encabezado del extracto, y (b) verificar la fecha de versión **artículo por artículo**, identificando cuáles disposiciones del perímetro tienen vigencia diferida antes de citarlas como derecho vigente.
- **Vigencia**: permanente.

---

# Segunda tanda — Entradas de la sesión de curatoría de leyes especiales (2026-07-07), PENDIENTES DE APROBACIÓN

### [2026-07-07] — Metodología — Enmienda: descarga del XML ejecutable por el asistente desde el servicio oficial, por instrucción del abogado
- **Contexto**: sesión de curatoría de las cinco leyes especiales. El abogado instruyó expresamente que el asistente descargara los XML («puedes bajar tú mismo estas leyes»), lo que enmienda la regla aprobada el 2026-07-07 que exigía descarga personal del abogado.
- **Lección**: la finalidad de la regla es la autenticidad de la fuente, no la identidad del descargador. La descarga directa por el asistente preserva la cadena de custodia si se ejecuta contra el servicio oficial `obtxml opt=7`, con idNorma resuelto desde el enlace canónico de LeyChile, validación de idNorma por `curar_norma.py` y hash SHA-256 registrado en el módulo.
- **Regla operativa**: la descarga del XML puede ejecutarla el asistente, dentro de la sesión de trabajo y previa instrucción del abogado, únicamente desde `https://www.leychile.cl/Consulta/obtxml?opt=7&idNorma=<ID>`, dejando registro de: URL, idNorma canónico, fecha de descarga y SHA-256. Sigue prohibida toda fuente distinta del servicio oficial y toda transcripción de memoria.
- **Vigencia**: permanente (sujeta a aprobación).

### [2026-07-07] — Fuente-verificada — La Ley 20.393 usa estructura «Doble Articulado» en el XML de LeyChile
- **Contexto**: el inventario inicial de la Ley 20.393 (idNorma 1008668) arrojó solo tres artículos (PRIMERO/SEGUNDO/TERCERO): su estatuto completo (arts. 1 a 29, con variantes bis a quinquies) está anidado dentro del Artículo PRIMERO bajo un nodo `tipoParte="Doble Articulado"`.
- **Lección**: las leyes promulgatorias con articulado aprobado «como texto» requieren que el motor de curatoría descienda al interior de los artículos; de lo contrario la extracción queda vacía sin advertencia.
- **Regla operativa**: `curar_norma.py` (versión del repositorio `estrategia-litigio-penal`, con prueba de regresión) recorre también el articulado anidado; ante toda norma nueva, cotejar el total inventariado contra la estructura visible en LeyChile antes de extraer.
- **Vigencia**: permanente (sujeta a aprobación).

### [2026-07-07] — Fuente-verificada — Numeración ordinal («Art. 1°») en leyes recientes
- **Contexto**: la extracción de la Ley 21.459 (idNorma 1177743) omitió los arts. 1° a 9° porque su `NombreParte` incluye el indicador ordinal («1°», «8º»), que el parser no reconocía como número.
- **Lección**: LeyChile registra la numeración ordinal de forma heterogénea (con ° u º); la comparación numérica debe normalizar esos indicadores.
- **Regla operativa**: `curar_norma.py` normaliza los indicadores ordinales (°, º, ª) antes de comparar; en toda curatoría, verificar que el número de artículos extraídos coincida con el perímetro y tratar la «Advertencia de completitud» como bloqueo hasta esclarecer su causa.
- **Vigencia**: permanente (sujeta a aprobación).
