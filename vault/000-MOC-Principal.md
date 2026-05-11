---
tipo: moc
titulo: Segundo Cerebro Legal - Dashboard Principal
fecha-creacion: 2026-01-01
fecha-actualizacion: <% tp.date.now("YYYY-MM-DD") %>
etiquetas: [moc, dashboard, principal]
---

# ⚖️ Segundo Cerebro Legal

> *"El abogado que conoce la ley gana el argumento. El que conoce los hechos gana el caso. El que conoce al juez gana el juicio."*

---

## 🗂️ Navegación Principal

| Área | Descripción | Notas |
|------|-------------|-------|
| [[01-Causas/MOC-Causas\|📁 Causas]] | Casos activos y archivados | `INPUT` |
| [[02-Marco-Legal/MOC-Marco-Legal\|📜 Marco Legal]] | Leyes, códigos, normas | `REFERENCIA` |
| [[03-Biblioteca/MOC-Biblioteca\|📚 Biblioteca]] | Libros, papers, doctrina | `CONOCIMIENTO` |
| [[04-Estrategias/MOC-Estrategias\|♟️ Estrategias]] | Tácticas y estrategias probadas | `HERRAMIENTA` |
| [[05-Teoria-Juegos/MOC-Teoria-Juegos\|🎮 Teoría de Juegos]] | Modelos de decisión estratégica | `ANÁLISIS` |
| [[06-Bayes/MOC-Bayes\|📊 Análisis Bayesiano]] | Probabilidades y evidencia | `ANÁLISIS` |
| [[07-Conceptos/MOC-Conceptos\|💡 Conceptos]] | Conceptos legales atómicos | `BASE` |
| [[08-Actores/MOC-Actores\|👥 Actores]] | Jueces, fiscales, peritos | `CONTEXTO` |

---

## 📊 Estado del Sistema

```dataview
TABLE WITHOUT ID
  link(file.link, causa) AS "Causa",
  tribunal AS "Tribunal",
  estado AS "Estado",
  probabilidad-condena AS "P(Condena)",
  proxima-audiencia AS "Próxima Audiencia"
FROM "01-Causas"
WHERE tipo = "causa" AND estado != "archivado"
SORT proxima-audiencia ASC
```

---

## 🔥 Causas Urgentes (próximos 7 días)

```dataview
LIST FROM "01-Causas"
WHERE tipo = "causa" AND proxima-audiencia <= date(today) + dur(7 days)
SORT proxima-audiencia ASC
```

---

## 📈 Análisis Global de Probabilidades

```dataview
TABLE WITHOUT ID
  link(file.link, causa) AS "Causa",
  round(probabilidad-condena * 100, 1) + "%" AS "P(Condena)",
  round((1 - probabilidad-condena) * 100, 1) + "%" AS "P(Absolución)",
  recomendacion-estrategia AS "Estrategia Recomendada"
FROM "01-Causas"
WHERE tipo = "causa" AND probabilidad-condena != null
SORT probabilidad-condena ASC
```

---

## 🧠 Flujo de Trabajo Karpathy

### 1. CAPTURAR → [[00-Inicio/Como-Usar-Este-Sistema|Cómo usar el sistema]]
Todo hecho, ley, observación o idea va primero como nota atómica.

### 2. ORGANIZAR
- Causas nuevas → `01-Causas/`
- Normas y jurisprudencia → `02-Marco-Legal/`
- Fuentes externas → `03-Biblioteca/`

### 3. CONECTAR
Cada nota debe enlazar con al menos 2 otras notas relevantes.

### 4. ANALIZAR
- Ejecutar análisis Bayesiano con `scripts/analizar_causa.py`
- Modelar negociaciones con Teoría de Juegos

### 5. SINTETIZAR → `04-Estrategias/`
Crear nota de estrategia que integre todo el análisis.

---

## 🔗 Conceptos Clave Recientes

```dataview
LIST FROM "07-Conceptos"
WHERE tipo = "concepto"
SORT file.mtime DESC
LIMIT 10
```

---

## 📝 Últimas Notas Modificadas

```dataview
TABLE file.mtime AS "Modificado", tipo AS "Tipo"
FROM ""
WHERE tipo != null
SORT file.mtime DESC
LIMIT 15
```

---

*Sistema basado en el método Karpathy de segundo cerebro. Ver [[00-Inicio/Como-Usar-Este-Sistema]] para instrucciones completas.*
