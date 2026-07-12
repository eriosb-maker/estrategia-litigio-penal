# Capa de evaluación y CI — `estrategia-litigio-penal`

**Fecha de construcción**: 2026-07-12. **Origen**: línea V del plan de mejoras trazado en la sesión de reconciliación de linajes (v4.3), ejecutada a solicitud expresa del titular.

## 1. Objeto

Detectar de forma automática, en cada `push` y `pull_request`, tres clases de regresión que hasta esta fecha dependían de auditoría manual:

1. **Regresión de comportamiento** en los motores deterministas (`prescripcion.py`, `estrategia_litigio.py`, `curar_norma.py`).
2. **Desincronización binaria** entre la ruta canónica de un motor y su copia empaquetada dentro de `skill/` — el defecto exacto que en la reconciliación de v4.3 produjo 22 fallos silenciosos porque el paquete instalado operaba con un motor obsoleto.
3. **Vencimiento inadvertido** de los plazos de revalidación semestral declarados en los módulos normativos curados.

## 2. Componentes

### 2.1 Casos dorados (`tests/test_casos_dorados.py`)

Ocho pruebas de regresión sobre hechos íntegramente ficticios, con fundamento normativo declarado caso a caso y valor esperado fijado por ejecución de control:

| Caso | Motor | Regla verificada que ejercita |
|---|---|---|
| A | `prescripcion.py` | Art. 94 N° 3 CP — plazo simple de cinco años, sin incidencias |
| B | `prescripcion.py` | Art. 96 CP / art. 233 a) y 248 c) CPP — suspensión por formalización y su cese retroactivo |
| C | `prescripcion.py` | Art. 100 CP — ausencia del territorio, un día de plazo por cada dos de ausencia |
| D | `prescripcion.py` | Arts. 96 y 99 CP — interrupción por nuevo delito, reinicio del cómputo |
| E | `estrategia_litigio.py` | Arts. 237, 241 y 406 CPP — viabilidad prima facie de salidas y punto de equilibrio juicio/abreviado |

Regla de mantenimiento declarada en el propio archivo: todo cambio del valor esperado de un caso dorado es, por definición, un cambio de criterio (SKILL.md 15.3.b) y exige aprobación expresa del titular antes de modificarse.

### 2.2 Sincronía de motores (`scripts/verificar_sincronia_motores.py`)

Compara por hash SHA-256 cada motor canónico (`scripts/curar_norma.py`, `src/prescripcion.py`) contra su copia empaquetada en `skill/scripts/`. Cualquier divergencia binaria detiene el pipeline. Implementa de forma automática el aprendizaje A-022 (prohibición de copias duales de motores deterministas), hasta ahora solo exigible por disciplina manual del operador.

**Hallazgo de esta sesión**: al construir el control se constató que ambos motores empaquetados en el repositorio (`skill/scripts/curar_norma.py` y, tras el reformateo de estilo aplicado en esta misma sesión, `skill/scripts/prescripcion.py`) divergían de su ruta canónica. Se trata de una corrección de manifiesto (SKILL.md 3.a): se sincronizaron ambos ejemplares por copia directa desde la ruta canónica.

### 2.3 Vigilancia de revalidación (`scripts/vigilar_revalidacion.py`)

Escanea `marco-legal.md`, `leyes-especiales.md`, `tributario.md` y `curatoria/encabezado-leyes-especiales.md` en busca de la marca «vence el AAAA-MM-DD» y compara contra la fecha de ejecución. Con umbral por defecto de 60 días, alerta (⚠️) el vencimiento próximo y señala (⛔) el ya vencido. En la ejecución programada mensual (`schedule`, primer día de cada mes), el paso adicional del workflow abre o actualiza un issue de GitHub cuando corresponde, evitando que el vencimiento del 2027-01-06/07 —hoy a 178-179 días— pase inadvertido como advirtió el titular.

### 2.4 Workflow (`​.github/workflows/ci-cd.yml`)

Reescrito íntegramente. El defecto más relevante del workflow anterior —los pasos de lint y de pruebas terminaban en `|| true`, de modo que el pipeline **nunca podía fallar** independientemente del resultado— queda corregido: ambos pasos ahora propagan su código de salida. Se agregan los jobs `sincronia-motores`, `integridad-skill` (ejecuta `verificar-integridad.sh` cuando el linaje del repositorio lo contenga; hoy emite advertencia por su ausencia, conforme al estado documentado en el `CHANGELOG`) y `vigilancia-revalidacion`.

**Corrección de manifiesto adicional**: al activar el lint estricto, `black --check` reveló que `src/main.py` y `src/prescripcion.py` no conformaban al formateador declarado en `requirements.txt`, y `flake8` señaló tres importaciones no usadas en `src/main.py` (`re`, `functools.lru_cache`, `collections.OrderedDict`). Se aplicó `black` y se retiraron las importaciones. Ninguna corrección altera comportamiento; ambas son mecánicas y verificables por herramienta.

## 3. Resolución de la observación sobre `src/main.py`

`src/main.py` (clase `EstrategiaLitigioPenal`, versión declarada «v1.3 Optimizado») fue identificado como prototipo temprano, anterior y no equivalente al motor real y verificado `skill/scripts/estrategia_litigio.py`: su `análisis_integral()` no calculaba exposición esperada, punto de equilibrio ni viabilidad de salidas, sino que devolvía una estructura de eco sin cómputo jurídico. Por instrucción expresa del titular (2026-07-12), el archivo fue **eliminado**, junto con sus tres puntos de dependencia:

- `Dockerfile`: el `CMD` invocaba `python -m src.main` y el `HEALTHCHECK` suponía un servidor HTTP en el puerto 8000 que el código jamás implementó —el contenedor, tal como estaba escrito, nunca pudo pasar su propio healthcheck—. Se sustituyó por un contenedor de utilidad cuyo comando por defecto ejecuta la suite de pruebas, sin pretensión de servicio HTTP inexistente.
- `README.md`: se actualizaron el «Quick Start» y la lista de módulos.
- Ausencia de referencias internas: `src/__init__.py` no importaba `main`; ningún test dependía de él.

## 4. Estado de propagación

Todo lo anterior existe en el árbol de trabajo local (`/home/claude/repo-check`, clon de `eriosb-maker/estrategia-litigio-penal`, rama `main`, commit base `c371af0`). **No se ha ejecutado `git push` alguno.** Conforme a la regla de acción del entorno, la publicación de contenido en un repositorio remoto requiere autorización expresa y por turno; los archivos quedan a su disposición para revisión antes de decidir el commit.

Cabe recordar, además, que este repositorio permanece en el linaje v4.2, anterior a la reconciliación v4.3/v4.5: `skill/` carece todavía de la Cláusula de Integridad, de `references/audiencia-preparacion.md` y de los demás módulos incorporados en el paquete instalado. La capa de CI aquí construida opera correctamente sobre el estado actual del repositorio, pero su cobertura será plena solo cuando el paquete reconciliado se incorpore como fuente única, conforme al defecto N° 6 ya registrado en el `CHANGELOG` de v4.3.
