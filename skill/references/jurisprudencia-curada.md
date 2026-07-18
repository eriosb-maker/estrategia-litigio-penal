# Jurisprudencia curada — Registro y protocolo de verificación

> **Naturaleza del módulo**. Este archivo es el **contenedor único** de jurisprudencia verificada de la skill, análogo en disciplina a `marco-legal.md` respecto de la normativa. A diferencia de la ley —cuyo texto oficial consta en XML estructurado de LeyChile y admite curatoría automatizada—, no existe fuente oficial estructurada de jurisprudencia chilena accesible desde este entorno. En consecuencia, **el texto de todo considerando lo aporta el titular** desde la fuente que tenga a la vista (Oficina Judicial Virtual del Poder Judicial, copia de la sentencia en la carpeta investigativa o del tribunal, base comercial identificada), y este módulo se limita a fijarlo, identificarlo, sellarlo con hash y someterlo a reglas de estado.
>
> **Instrucción de uso**. Cárgalo cada vez que un análisis requiera citar, invocar o ponderar jurisprudencia. Ninguna cita jurisprudencial puede fundar una conclusión del informe si no consta aquí en estado **[V]**; toda otra referencia jurisprudencial se consigna expresamente como «pendiente de verificación» y no puede sostener por sí sola la tesis del documento.
>
> **Instrucción de actualización**. Las fichas se ingresan mediante `scripts/curar_jurisprudencia.py` (comandos `--plantilla`, `--validar`, `--agregar`, `--verificar`, `--listar`), que asigna el identificador, computa el hash del texto y verifica las reglas de estado. Se admite el ingreso manual solo si respeta íntegramente el formato y se ejecuta luego `--verificar`.

---

## 1. Regla rectora — prohibición de jurisprudencia de memoria

**Ninguna sentencia, rol, fecha, considerando o doctrina jurisprudencial proveniente de la memoria del modelo puede ingresar a este registro, ni citarse en informe alguno como si estuviera verificada.** La memoria del modelo es fuente conocida de citas inexistentes o deformadas (roles inventados, considerandos atribuidos a fallos que no los contienen, doctrinas jurisprudenciales sin respaldo). La regla es absoluta e inderogable, en línea con la prohibición N° 2 de la sección 13 del `SKILL.md`.

Lo que el modelo sí puede hacer, y debe declarar como tal:

- **Sugerir líneas de búsqueda**: «convendría verificar si existe jurisprudencia de la Corte Suprema sobre la calificación del inciso primero del art. 97 N° 4 CT como simple delito o crimen», sin atribuir esa doctrina a fallo alguno.
- **Analizar el texto de una sentencia aportada por el titular**, extraer su ratio, delimitar su alcance y proponer la ficha correspondiente, cuyo ingreso en estado [V] queda condicionado a las reglas de la sección 3.

## 2. Formato estandarizado de la ficha

```
### J-0NN — [Materia] — Tribunal, Rol N° XXXX-AAAA, de DD-MM-AAAA
- **Estado**: [V] | [PV] | [NU] | [S]
- **Tribunal y sala**: (v. gr., Corte Suprema, Segunda Sala)
- **Tipo de recurso o procedimiento**: (nulidad, apelación, amparo, juicio oral, etc.)
- **Rol**: identificador del ingreso ante el tribunal que dictó el fallo
- **RUC/RIT de origen** (si consta y su mención está autorizada por el titular):
- **Fecha de la sentencia**: AAAA-MM-DD
- **Redactor** (si consta):
- **Considerando(s) invocado(s)**: N° ...
- **Tesis que sostiene**: enunciado abstracto de la regla jurisprudencial, en una o dos frases, sin sobreextender el fallo.
- **Alcance y límites**: qué NO resuelve la sentencia; contexto fáctico que condiciona su aplicabilidad.
- **Materia**: categoría del índice temático (sección 5).
- **Fuente del texto**: origen material del texto transcrito (Oficina Judicial Virtual, copia en carpeta RUC autorizado, base identificada). Obligatoria para [V].
- **Fecha de verificación**: AAAA-MM-DD. Obligatoria para [V].
- **SHA-256 del texto**: hash del texto normalizado del considerando. Obligatorio para [V]; lo computa el script.
- **Texto del considerando**:

> «...transcripción fiel aportada por el titular...»
```

**Identificador estable.** El campo `ID` se asigna en orden de ingreso, de la forma `J-0NN`, y **jamás se reasigna** (regla A-013). Las fichas que pasen a estado [NU] o [S] conservan su identificador; el número queda quemado.

**Normalización para el hash.** El script normaliza el texto en Unicode NFC, recorta extremos y colapsa espacios internos antes de computar SHA-256, de modo que diferencias tipográficas irrelevantes no rompan la verificación, pero cualquier alteración de contenido sí lo haga.

## 3. Reglas de estado

| Estado | Denominación | Condiciones | Efecto en los informes |
|---|---|---|---|
| **[V]** | Verificada | Texto del considerando transcrito; fuente del texto identificada; fecha de verificación; hash computado y coincidente. Las cuatro condiciones son copulativas. | Puede fundar conclusiones, citándose con tribunal, rol, fecha y considerando. |
| **[PV]** | Pendiente de verificación | Individualización razonable (tribunal, rol o fecha aproximada) sin texto verificado. | Solo puede mencionarse con la advertencia expresa «cita pendiente de verificación»; no funda por sí sola conclusión alguna. |
| **[NU]** | No ubicable / rechazada | Búsqueda efectuada por el titular sin resultado, o texto obtenido que no contiene la doctrina atribuida. | Prohibida su cita como autoridad. Se conserva la ficha como antecedente negativo, para no repetir la búsqueda ni reintroducir la cita espuria. |
| **[S]** | Superada | Verificada en su momento, pero contradicha por jurisprudencia posterior de igual o superior jerarquía, ingresada también a este registro. | Solo se cita para dar cuenta de la evolución jurisprudencial, con mención expresa de la ficha que la supera. |

**Regla de degradación.** Ante duda sobre el cumplimiento de las condiciones de [V], la ficha se degrada a [PV]. La presunción opera siempre en el sentido de la degradación, jamás en el de la promoción (R-5).

**Regla de firmeza.** La ficha debe consignar, cuando el titular lo conozca, si la sentencia se encuentra firme o ejecutoriada, o si fue objeto de recursos. Una sentencia de instancia recurrida se pondera con esa reserva expresa.

## 4. Reglas de higiene del registro

1. **Sin datos sensibles innecesarios.** La individualización del fallo (tribunal, rol, fecha) es información pública del sistema judicial. No se transcriben del considerando datos personales de víctimas, testigos o terceros que no sean indispensables para la ratio; en su lugar se consigna «[identidad omitida]». El RUC/RIT de origen de causas del estudio solo se registra con autorización expresa del titular.
2. **Una ficha, un fallo.** Si de una misma sentencia interesan varios considerandos sobre materias distintas, se admiten fichas separadas, cada una con su hash, dejando constancia cruzada.
3. **Trazabilidad de ingreso.** Toda ficha consigna la fecha de ingreso al registro y, en lo posible, el caso o análisis que la motivó (sin datos de clientes).
4. **Crecimiento causa a causa.** El registro no aspira a la exhaustividad —inviable sin fuente oficial estructurada—, sino a la fiabilidad: crece con las sentencias que el titular efectivamente tiene a la vista en su práctica.
5. **Interacción con `aprendizajes.md`.** Cuando una ficha [V] cristalice un criterio de aplicación general para la skill, se captura además como entrada de categoría `Jurisprudencia` en `references/aprendizajes.md`, con remisión al identificador `J-0NN`. La ficha contiene el texto; el aprendizaje, la regla operativa.

## 5. Índice temático

*Se puebla a medida que ingresan fichas. Categorías iniciales, ampliables:*

- Prescripción de la acción penal (arts. 93–105 CP; art. 97 N° 4 CT)
- Exclusión de prueba e ilicitud (art. 276 CPP)
- Prueba digital: autenticación, cadena de custodia, licitud de la obtención
- Lavado de activos (Ley 19.913)
- Responsabilidad penal de personas jurídicas (Ley 20.393)
- Delitos económicos y sistema de determinación de penas (Ley 21.595)
- Delitos tributarios (art. 97 CT)
- Ciberdelincuencia (Ley 21.459)
- Debido proceso y nulidad (arts. 373–374 CPP)
- Medidas cautelares (arts. 139–155 CPP)

---

## 6. Registro de fichas

*Sin fichas ingresadas a la fecha de creación del módulo (2026-07-12). El primer identificador disponible es `J-001`. Los identificadores se asignan mediante `scripts/curar_jurisprudencia.py --agregar` y jamás se reasignan.*

<!-- INICIO-REGISTRO-FICHAS -->
<!-- FIN-REGISTRO-FICHAS -->

---

*Módulo creado el 2026-07-12 (línea IV del plan de mejoras; skill v4.6). Verificación de integridad: el archivo queda indexado en `index-maestro.json` y su consistencia interna se controla con `scripts/curar_jurisprudencia.py --verificar`.*
