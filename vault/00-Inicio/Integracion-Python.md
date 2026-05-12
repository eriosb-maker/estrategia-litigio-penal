---
tipo: doc
etiquetas: [doc, integracion, python]
---

# 🔗 Integración Python ↔ Obsidian

> Los **motores de análisis** (Bayes y Teoría de Juegos) viven en `src/`.
> Los **scripts CLI** que escriben al vault viven en `scripts/`.
> Obsidian es la **interfaz** que captura, organiza y visualiza.

---

## 🚀 Setup Inicial (una sola vez)

Desde la raíz del proyecto (no desde `vault/`):

```bash
./scripts/litigio.sh setup
```

Esto instala las dependencias de `requirements.txt` (pydantic, pytest, etc.).

---

## 🎯 Comandos Principales

Todos pasan por el wrapper `litigio.sh` para no recordar paths Python:

| Comando | Qué hace |
|---------|----------|
| `./scripts/litigio.sh nueva` | Crea nueva causa (genera 6 archivos en `01-Causas/RUC/`) |
| `./scripts/litigio.sh bayes <RUC>` | Análisis Bayesiano interactivo, guarda en `04-Analisis-Bayes.md` |
| `./scripts/litigio.sh juegos <RUC>` | Análisis Teoría de Juegos, guarda en `05-Estrategia-TJ.md` |
| `./scripts/litigio.sh completo <RUC>` | **Recomendado**: Bayes + TJ encadenados (TJ usa P(condena) del Bayes) |
| `./scripts/litigio.sh conexiones <RUC>` | Reporte de cross-referencias |
| `./scripts/litigio.sh buscar "término"` | Búsqueda en todo el vault |
| `./scripts/litigio.sh demo` | Ejecuta el caso de demostración |

---

## 🧠 Flujo Recomendado: Crear y Analizar una Causa

### 1. Crear la causa

**Opción A — Desde terminal (Python):**
```bash
./scripts/litigio.sh nueva
```
Te pregunta nombre, RUC, materia, rol, tribunal, etc. Crea la estructura completa con 6 archivos.

**Opción B — Desde Obsidian (Templater):**
1. Ve a `01-Causas/`.
2. Crea una nota nueva con cualquier nombre.
3. Templater dispara pop-ups y autorenombra.

> Las dos opciones son intercambiables. Python es más rápido para batch; Templater es más rápido si ya estás en Obsidian.

---

### 2. Llenar Hechos y Pruebas (en Obsidian)

Usa los atajos del Paso 5:
- `Ctrl+Shift+H` → agregar hecho
- Edición directa de `02-Pruebas.md` para inventario probatorio

---

### 3. Ejecutar el análisis completo

```bash
./scripts/litigio.sh completo 2024-001
```

Te pregunta:
- **Para Bayes**: cada evidencia con su P(E|culpable) y P(E|inocente)
- **Para TJ**: costos, valores, BATNAs de ambos lados

Y al final:
- ✅ Escribe `04-Analisis-Bayes.md` con la P(condena) posterior y análisis de sensibilidad
- ✅ Escribe `05-Estrategia-TJ.md` con equilibrio Nash, ZOPA y recomendación
- ✅ Usa la **P(condena) del Bayes** para alimentar la matriz de pagos del TJ (consistencia)

---

### 4. Revisar resultados en Obsidian

Vuelves al vault, recargas las notas (Obsidian las detecta automáticamente). El `00-Resumen.md` de la causa ya tiene enlaces a ambos análisis.

---

## 📊 Cómo Funciona el Análisis Bayesiano

Para cada evidencia ingresas:
- **P(E | culpable)**: probabilidad de observar esa evidencia *si el imputado es culpable*
- **P(E | inocente)**: lo mismo *si es inocente*

El sistema calcula el **likelihood ratio** (LR = P(E|C) / P(E|I)) y lo acumula:

```
Odds posterior = Odds prior × LR₁ × LR₂ × ... × LRₙ
P(Condena | Evidencias) = Odds / (1 + Odds)
```

Y entrega:
- Probabilidad posterior
- Escenarios (pesimista / base / optimista)
- Análisis de sensibilidad (qué evidencia es **crítica**: si la excluyes, ¿cuánto cambia el resultado?)
- Recomendación estratégica según el umbral del estándar de prueba

> **Umbral penal**: 90% (más allá de duda razonable)
> **Umbral civil**: 51% (preponderancia)

---

## 🎮 Cómo Funciona el Análisis de Teoría de Juegos

Modelas a los dos jugadores (tú y la contraparte) con:
- **P(ganar juicio)**: viene del Bayes o lo estimas
- **Valor ganar / perder / acuerdo**: en CLP equivalentes
- **Costo del juicio**: honorarios, tiempo, costo emocional

El sistema construye una **matriz 2×2** (Juicio vs. Negociar) y calcula:

- **BATNA** de cada parte (Best Alternative To Negotiated Agreement)
- **ZOPA** (Zona de Posible Acuerdo) — si existe, hay rango donde ambos prefieren acuerdo
- **Equilibrio de Nash** — qué estrategia es estable
- **Recomendación**: ir a juicio, negociar, o salida alternativa

---

## 🔧 Tips para Estimar Probabilidades

> Las probabilidades son **subjetivas pero disciplinadas**. La gracia del enfoque Bayesiano no es eliminar el juicio del abogado, sino hacerlo **explícito y revisable**.

### Para P(prior) — antes de ver evidencia
- Tasa de condena base del delito en el tribunal: ~70-85% típicamente en Chile
- Si es flagrancia: súbela
- Si es delito imposible de demostrar: bájala

### Para P(E | culpable) vs. P(E | inocente)
- Pregúntate: "Si el imputado realmente lo hizo, ¿qué tan probable es que apareciera esta evidencia?"
- "Y si NO lo hizo, ¿qué tan probable es que apareciera de todos modos?"
- La **diferencia** entre ambas (no el valor absoluto) es lo que mueve la aguja

### Ejemplos de LR típicos
| Evidencia | LR aproximado |
|-----------|---------------|
| ADN coincidente (alta calidad) | 1,000,000+ |
| Huella dactilar (12 puntos) | 1,000+ |
| Reconocimiento del testigo (buenas condiciones) | 5-15 |
| Testigo único en mala iluminación | 1.5-3 |
| Sin coartada | 1.5-2 |
| Coartada con un solo testigo | 0.5-0.7 |
| Coartada documentada (CCTV, peaje) | 0.05-0.1 |

---

## ⚠️ Limitaciones Importantes

1. **Independencia entre evidencias**: el motor asume independencia. Si dos evidencias están correlacionadas (ej: dos testigos que se conocen), se sobrestima la probabilidad. Solución: trata el grupo como una sola evidencia compuesta.
2. **Subjetividad de probabilidades**: garbage in, garbage out. Calibra con casos pasados.
3. **No reemplaza al abogado**: es una herramienta para **explicitar** el razonamiento, no para automatizarlo.
4. **El umbral 90% es conservador**: la condena penal real puede darse con menos en la práctica (sesgo del tribunal). Úsalo como referencia, no como predicción exacta.

---

## 📁 Estructura de Archivos Python

```
src/
├── bayes.py            # Motor Bayesiano (Evidencia, AnalisisBayesiano)
├── teoria_juegos.py    # Motor TJ (JugadorLitigio, MatrizPagos, AnalisisTJ)
├── causa_manager.py    # Crea y actualiza la estructura de causas en el vault
├── knowledge_base.py   # Indexa el vault para cross-referencias
└── main.py             # API de alto nivel (deprecada, usar litigio.sh)

scripts/
├── litigio.sh          # ⭐ Wrapper único — usa este
├── nueva_causa.py      # Crea causa
├── analizar_causa.py   # Ejecuta análisis
└── buscar.py           # Busca en el vault

tests/
├── test_bayes.py
└── test_teoria_juegos.py
```

---

## 🧪 Verificar que Todo Funciona

```bash
# 1. Demo (no toca el vault)
./scripts/litigio.sh demo

# 2. Tests automatizados
pytest -v

# 3. Crear causa de prueba
./scripts/litigio.sh nueva
# (responde con datos ficticios)

# 4. Analizarla
./scripts/litigio.sh completo <RUC-que-acabas-de-crear>
```

---

*[[000-MOC-Principal|← Dashboard]] · [[Como-Usar-Este-Sistema|Cómo usar este sistema]]*
