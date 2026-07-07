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
