# Leyes especiales — Delitos económicos, RPPJ, lavado, delitos informáticos y drogas

> **Estado del módulo**: OPERATIVO — extractos verificados insertados el
> 2026-07-07 mediante `scripts/curar_norma.py` (versión con soporte de
> «Doble Articulado» y numeración ordinal) desde los XML oficiales de
> LeyChile (Biblioteca del Congreso Nacional), descargados directamente del
> servicio `obtxml opt=7` por instrucción expresa del abogado, con
> validación de idNorma y hash SHA-256 registrado. Todo artículo NO
> comprendido en los perímetros de este módulo conserva la marca **«cita
> pendiente de verificación»**. Revalidación semestral obligatoria: vence el
> **2027-01-07**.

---

## 1. Registro de curatoría

| Ley | idNorma | Versión de la norma | Perímetro extraído | Artículos | Observaciones |
|---|---|---|---|---|---|
| 21.595 (delitos económicos) | 1195119 | 2025-09-29 | 1–47 y 60–68 | 56 | Art. 64 [DEROGADO]. Se excluyen los arts. 48–59 (modificatorias de otros cuerpos) y transitorios. |
| 20.393 (RPPJ, texto post-21.595) | 1008668 | 2023-08-17 | 1–29 (articulado interno) | 37 | Estructura «Doble Articulado»: el estatuto está anidado en el Artículo PRIMERO. Incluye 11 bis, 17–17 quinquies, 18 bis, 19 bis y 20 bis. |
| 19.913 (UAF y lavado) | 219119 | 2026-05-30 | 1–7 y 19–41 | 32 | Se excluye la orgánica de personal (arts. 8–18) y transitorios. Art. 27 en versión 2023-11-23. |
| 21.459 (delitos informáticos) | 1177743 | **2222-02-02** | 1–21 | 21 | Arts. 9 y 16 [DEROGADOS]. **Vigencia diferida**: el art. 11 registra versión «2222-02-02» — verificar su entrada en vigencia antes de invocarlo. |
| 20.000 (drogas) | 235507 | 2026-05-23 | 1–25 y 50–54 | 31 | Art. 22 (cooperación eficaz) [DEROGADO] desde 2024-09-04: cotejar el régimen general vigente (art. 68 ter CP, verificado en `marco-legal.md`) antes de alegarla. |

**Hashes SHA-256 de los XML de origen** (archivos en `curatoria/xml/` del
repositorio `estrategia-litigio-penal`):

- Ley 21.595: `e82acdb67e0d0ca07331e57dfc67f59b8dc6c460b805fa88d448da2f2a2e43de`
- Ley 20.393: `2678edc90addfbc5b2d8aeab641daa055b98fecaf885c0c055f143803b96a0ed`
- Ley 19.913: `ec610ca927e8edc488fcfc4363568bcf42624be150e22e7e61281673ec224c5b`
- Ley 21.459: `58ebbbcb1f60c7e38b3c976973361b799d16ec1e7b9296ee605a5cb37d3ef3fb`
- Ley 20.000: `a3911fba97f6728deb4b12667b75a614d04929f01cc72de1668e84261f1bcc2d`

Ninguna extracción arrojó advertencia de completitud: los perímetros
solicitados constan íntegros en los XML procesados.

---

## 2. Notas operativas mínimas (ancladas al texto verificado)

1. **Ley 21.595 — sistema especial de determinación.** Para los responsables
   de delitos económicos (art. 8), la determinación de la pena de presidio o
   reclusión y su sustitución se rigen por esta ley, con las reglas generales
   solo en subsidio (art. 9). El art. 12 **excluye** los arts. 65 a 69 CP y
   las modificatorias de los arts. 11 a 13 CP, reemplazándolas por las
   atenuantes (art. 13), atenuantes muy calificadas (art. 14), agravantes
   (art. 15) y agravantes muy calificadas (art. 16), con umbrales en UTM
   (40 / 400 / 40.000); los efectos sobre el marco se rigen por el art. 17 y
   la individualización por el art. 18. Todo delito económico conlleva
   además multa en días-multa (arts. 10 y 27 a 29), inhabilitaciones
   (arts. 30 y siguientes) y el régimen de comiso de ganancias (arts. 40 a
   47). Las penas sustitutivas propias (arts. 19 a 26) se limitan a remisión
   condicional y reclusión parcial (domiciliaria o en establecimiento
   especial), con la Ley 18.216 solo supletoria (art. 19).
2. **Ley 20.393 — RPPJ.** El texto extraído corresponde íntegramente a la
   versión reformada por la Ley 21.595 (fecha de versión 2023-08-17 en su
   articulado sustantivo). La estructura del cuerpo comprende el ámbito y
   presupuestos de la responsabilidad, el modelo de prevención, el catálogo
   y determinación de penas (incluidos los arts. 17 a 17 quinquies) y las
   reglas procesales (Título III, arts. 21 a 29).
3. **Ley 19.913 — lavado.** El tipo del art. 27 consta en su versión
   2023-11-23 (posterior a la Ley 21.595). La asociación del art. 28
   conserva versión 2009-12-02: cotejar su coordinación con el régimen de
   asociaciones delictivas y criminales de la Ley 21.577 *(cuerpo no curado;
   cita pendiente de verificación)* antes de imputar por esa vía.
4. **Ley 21.459 — delitos informáticos.** Tipos en los arts. 1° a 8°
   (ataque a la integridad de sistemas, acceso ilícito, interceptación,
   ataque a la integridad de datos, falsificación, receptación de datos,
   fraude y abuso de dispositivos). El art. 9 (circunstancias) y el art. 16
   están derogados desde 2024; el art. 11 tiene **vigencia diferida**
   (marca «2222-02-02»): no citarlo como derecho vigente sin verificar su
   entrada en vigor en LeyChile.
5. **Ley 20.000 — drogas.** Núcleo típico en los arts. 1 a 12 (elaboración,
   precursores, tráfico, microtráfico del art. 4 con versión 2026-05-23,
   suministro, cultivo), agravantes especiales en los arts. 19 a 21, técnicas
   especiales de investigación en los arts. 23 a 25 y faltas (incluido el
   consumo, art. 50) en los arts. 50 a 54. La cooperación eficaz del art. 22
   está **derogada** desde 2024-09-04; el beneficio se rige por el régimen
   general *(art. 68 ter CP, verificado en `marco-legal.md`)*.

**Regla de uso**: en el análisis, cita siempre artículo e inciso sobre el
texto insertado en las secciones siguientes; si el artículo requerido no
integra el perímetro, decláralo «cita pendiente de verificación» y propone su
curatoría incremental.

---
