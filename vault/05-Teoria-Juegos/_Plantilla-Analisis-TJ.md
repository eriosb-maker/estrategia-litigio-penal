---
tipo: analisis-tj
causa: "{{NOMBRE_CAUSA}}"
ruc: "{{RUC}}"
fecha: {{YYYY-MM-DD}}
etiquetas: [teoria-juegos, analisis, {{ruc}}]
equilibrio-recomendado: "{{juicio | negociar | salida-alternativa}}"
---

# 🎮 Análisis Teoría de Juegos — {{NOMBRE_CAUSA}}

> Análisis generado el {{FECHA}} | Causa: [[01-Causas/|{{RUC}}]]

---

## Jugadores y Estrategias

| Jugador | Estrategias Disponibles |
|---------|------------------------|
| **{{ROL_NUESTRO}}** | Ir a juicio / Negociar / Salida alternativa |
| **{{ROL_CONTRAPARTE}}** | Ir a juicio / Negociar / Ofrecer acuerdo |

---

## Parámetros del Análisis

| Parámetro | Valor | Fuente |
|-----------|-------|--------|
| P(Condena) según análisis Bayes | {{%}} | [[01-Causas/{{CARPETA}}/04-Analisis-Bayes]] |
| Pena máxima esperada | {{N}} años / ${{M}} | |
| Costo estimado del juicio (nosotros) | ${{X}} | |
| Costo estimado del juicio (contraparte) | ${{X}} | Estimado |
| Oferta actual de la contraparte | {{DESCRIPCIÓN}} | |

---

## Cálculo de Pagos

### Para Nosotros ({{ROL}})

| Resultado | Probabilidad | Valor | Valor Esperado |
|-----------|-------------|-------|----------------|
| Ganar en juicio | {{1-p}} | {{+V}} | {{(1-p)×V}} |
| Perder en juicio | {{p}} | {{-V}} | {{-p×V}} |
| **Valor Esperado Juicio** | | | **{{VEJ}}** |
| Acuerdo actual | 1.0 (seguro) | {{VA}} | **{{VA}}** |

### Para la Contraparte

| Resultado | Probabilidad | Valor | Valor Esperado |
|-----------|-------------|-------|----------------|
| Ganar en juicio | {{p}} | {{+V_c}} | {{p×V_c}} |
| Perder en juicio | {{1-p}} | {{-V_c}} | {{-(1-p)×V_c}} |
| **Valor Esperado Juicio** | | | **{{VEJ_c}}** |
| Acuerdo actual | 1.0 | {{VA_c}} | **{{VA_c}}** |

---

## Matriz de Pagos

```
                      CONTRAPARTE
                    Juicio    Negociar
NOSOTROS  Juicio │ (X, Y)   │ (X', Y')│
          Negocia│ (X'', Y'')│ (X''', Y''')│
```

---

## Identificación del Equilibrio

### ¿Tiene algún jugador estrategia dominante?
- Nosotros: {{Sí/No}} — {{Descripción}}
- Contraparte: {{Sí/No}} — {{Descripción}}

### Equilibrio de Nash identificado:
**Nosotros**: {{ESTRATEGIA}} | **Contraparte**: {{ESTRATEGIA}}

---

## BATNA (Mejor Alternativa al Acuerdo Negociado)

| Nuestra BATNA | Valor | BATNA Contraparte | Valor |
|--------------|-------|------------------|-------|
| {{Descripción}} | {{V}} | {{Descripción}} | {{V}} |

**¿Existe ZOPA (Zona de Posible Acuerdo)?**
- Mínimo aceptable nosotros: {{VALOR}}
- Máximo aceptable contraparte: {{VALOR}}
- **ZOPA**: {{Sí: [$X, $Y] / No}}

---

## Recomendación Estratégica

### Decisión recomendada: {{JUICIO / NEGOCIAR / SALIDA ALTERNATIVA}}

**Razonamiento**:


**Condiciones bajo las cuales cambiaría la recomendación**:
- Si P(Condena) baja a {{%}} → cambiar a Juicio
- Si la oferta mejora a {{DESCRIPCIÓN}} → reconsiderar

---

## Cómo Mejorar Nuestra Posición Negociadora

1. 
2. 
3. 

---

*Análisis complementario: [[01-Causas/{{CARPETA}}/04-Analisis-Bayes|Análisis Bayesiano]]*
*[[05-Teoria-Juegos/MOC-Teoria-Juegos|← Teoría de Juegos]]*
