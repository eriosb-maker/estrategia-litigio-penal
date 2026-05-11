---
tipo: causa
causa: "{{NOMBRE_CAUSA}}"
ruc: "{{RUC}}"
rol-tribunal: "{{ROL}}"
tribunal: "{{TRIBUNAL}}"
materia: "{{penal | civil}}"
rol-abogado: "{{defensor | querellante | demandante | demandado}}"
imputado: "{{NOMBRE}}"
victima: "{{NOMBRE}}"
fiscal: "{{NOMBRE}}"
juez: "{{NOMBRE}}"
fecha-inicio: {{YYYY-MM-DD}}
proxima-audiencia: {{YYYY-MM-DD}}
estado: "{{en-proceso | suspendida | cerrada | archivada}}"
probabilidad-condena: {{0.0 - 1.0}}
recomendacion-estrategia: "{{ir-a-juicio | negociar | salida-alternativa}}"
etiquetas: [causa, {{penal|civil}}, {{defensa|acusacion}}]
---

# ⚖️ {{NOMBRE_CAUSA}}

> **RUC**: {{RUC}} | **Tribunal**: {{TRIBUNAL}} | **Estado**: {{ESTADO}}

---

## 1. Resumen Ejecutivo

<!-- Una sola paragráfo: qué pasó, quién es el imputado, qué se le imputa, cuál es nuestra posición -->

**Hecho imputado**: 

**Nuestra posición**: 

**Fortalezas principales**: 
- 

**Debilidades principales**: 
- 

**Riesgo estimado**: 🟢 Bajo / 🟡 Medio / 🔴 Alto

---

## 2. Hechos del Caso

### Cronología

| Fecha | Hecho | Fuente | Certeza |
|-------|-------|--------|---------|
| {{YYYY-MM-DD}} | | | Alto/Medio/Bajo |

### Versión de la Fiscalía / Contraparte
> *Descripción de los hechos según la contraparte*

### Nuestra Versión
> *Descripción de los hechos según nuestra defensa/posición*

### Hechos Controvertidos
- [ ] 

### Hechos No Controvertidos
- [ ] 

---

## 3. Marco Jurídico

### Delito / Figura Jurídica Imputada
- **Artículo**: [[02-Marco-Legal/]]
- **Bien jurídico protegido**: 
- **Elementos del tipo**:
  - [ ] Elemento 1:
  - [ ] Elemento 2:

### Normas Aplicables
| Norma | Relevancia | Favorece |
|-------|-----------|---------|
| [[02-Marco-Legal/]] | | Defensa/Acusación |

### Jurisprudencia Relevante
| Caso | Tribunal | Año | Holding | Relevancia |
|------|----------|-----|---------|-----------|
| [[02-Marco-Legal/]] | | | | |

---

## 4. Pruebas

### Pruebas de Cargo
| # | Tipo | Descripción | Peso | Cuestionamiento |
|---|------|-------------|------|----------------|
| 1 | | | Alto/Medio/Bajo | |

### Pruebas de Descargo
| # | Tipo | Descripción | Peso | Observación |
|---|------|-------------|------|------------|
| 1 | | | Alto/Medio/Bajo | |

### Pruebas Pendientes de Obtener
- [ ] 

---

## 5. Testigos

### Testigos de Cargo
| Nombre | Credibilidad | Puntos a Atacar | Estrategia Cross |
|--------|-------------|----------------|-----------------|
| | Alta/Media/Baja | | |

### Testigos de Descargo
| Nombre | Credibilidad | Puntos Clave | Preparación |
|--------|-------------|-------------|------------|
| | Alta/Media/Baja | | |

---

## 6. Análisis Bayesiano

> Ver análisis completo: [[01-Causas/{{CARPETA}}/04-Analisis-Bayes|Análisis Bayesiano Detallado]]

**Probabilidad inicial P(C)**: {{%}}
**Probabilidad posterior P(C|E)**: {{%}}

### Factores que aumentan P(Condena)
- 

### Factores que disminuyen P(Condena)
- 

**Recomendación**: Si P(Condena) > 60% → evaluar salida alternativa

---

## 7. Análisis Teoría de Juegos

> Ver análisis completo: [[01-Causas/{{CARPETA}}/05-Estrategia-TJ|Análisis Teoría de Juegos]]

**Tipo de juego**: Suma cero / No suma cero
**Información**: Completa / Incompleta
**Equilibrio Nash identificado**: 

### Matriz de Pagos Simplificada

|  | Fiscalía: Ir a juicio | Fiscalía: Negociar |
|--|----------------------|-------------------|
| **Defensa: Ir a juicio** | (?, ?) | (?, ?) |
| **Defensa: Negociar** | (?, ?) | (?, ?) |

---

## 8. Estrategia

> Ver estrategia completa: [[04-Estrategias/]]

### Estrategia Principal
**Teoría del caso**: 

**Mensaje central** (una oración que el jurado/juez debe recordar):
> 

### Plan de Audiencias
| Audiencia | Fecha | Objetivo | Preparación |
|-----------|-------|----------|------------|
| Formalización | | | |
| Preparación de Juicio | | | |
| Juicio Oral | | | |

### Salidas Alternativas Evaluadas
- [ ] **Suspensión Condicional**: Condiciones posibles: 
- [ ] **Acuerdo Reparatorio**: Monto estimado: 
- [ ] **Procedimiento Abreviado**: Pena acordada: 

---

## 9. Registro de Audiencias

### Audiencia: {{TIPO}} — {{FECHA}}
**Tribunal**: | **Juez**: | **Duración**:

**Resultado**:

**Próximos pasos**:

---

## 10. Tareas Pendientes

- [ ] 📅 {{fecha}} — 
- [ ] 📅 {{fecha}} — 

---

## Referencias Cruzadas

> Véase también:
> - [[02-Marco-Legal/]]
> - [[03-Biblioteca/]]
> - [[04-Estrategias/]]
> - [[08-Actores/]]

---

*Creado: {{fecha}} | Última actualización: {{fecha}}*
*[[01-Causas/MOC-Causas|← Volver a Causas]]*
