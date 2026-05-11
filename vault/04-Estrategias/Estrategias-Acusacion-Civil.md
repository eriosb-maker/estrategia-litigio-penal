---
tipo: estrategia-coleccion
titulo: Estrategias en Litigio Civil
materia: civil
rol: demandante
etiquetas: [estrategia, civil, demandante, demandado, coleccion]
---

# ⚖️ Estrategias en Litigio Civil

> *"En lo civil, quien mejor organiza y presenta su evidencia, generalmente gana."*

---

## 1. Estrategia de Máxima Presión Inicial (Demandante)

**Premisa**: La demanda inicial debe ser lo suficientemente robusta y amenazante para generar presión a negociar antes del juicio.

### Implementación
1. **Cuantificar con precisión**: Daño emergente + Lucro cesante + Daño moral (con respaldo pericial)
2. **Solicitar medidas cautelares**: Prohibición de enajenar, retención de fondos, embargo preventivo
3. **Demandar a todos los potencialmente responsables** (responsabilidad solidaria donde aplique)
4. **Publicitar estratégicamente** si hay interés público (daño reputacional al demandado)

### Análisis de Teoría de Juegos
Si el demandado percibe un costo esperado alto del juicio, tiene incentivo a transar.
Costo esperado = P(Condena) × Monto + Costas + Daño reputacional

Ver: [[05-Teoria-Juegos/Equilibrio-Nash-en-Litigios]]

---

## 2. Estrategia Defensiva: Dilación Legítima (Demandado)

**Premisa**: El tiempo puede ser aliado del demandado si la contraparte enfrenta costos de oportunidad o prescripción de otros derechos.

### Herramientas
- Excepciones dilatorias (incompetencia, ineptitud de la libelo)
- Recursos legítimos en cada resolución
- Solicitar plazos para contestar, rendir prueba, alegar

### Ética: ¿Cuándo es legítimo?
- Cuando genuinamente se cree que la demanda es improcedente
- Para dar tiempo a obtener prueba propia
- **No es legítimo** cuando el único fin es forzar un transo abusivo

---

## 3. Estrategia de Responsabilidad Compartida

**Premisa**: Distribuir la responsabilidad entre múltiples actores reduce la condena individual.

### Técnicas
- **Llamada de terceros**: incorporar al proceso a otros responsables
- **Culpa concurrente de la víctima**: demostrar que el demandante contribuyó al daño
- **Caso fortuito o fuerza mayor**: la cadena causal se interrumpe

### Análisis Bayesiano
Cada elemento de responsabilidad compartida que probamos reduce la estimación del monto final.
Ver: [[06-Bayes/]]

---

## 4. Estrategia del Perito Propio

**Premisa**: En disputas técnicas (daños, valuaciones, responsabilidad médica), el perito es frecuentemente decisivo.

### Selección del Perito
- Credenciales verificables y sólidas
- Experiencia en juicios (no solo academia)
- Capacidad de comunicar en lenguaje simple
- Sin conflictos de interés visibles

### Preparación del Perito
1. Brief completo de los hechos
2. Simulación de contraexamen
3. Alinear metodología con estándares reconocidos (Daubert-equivalent)

### Contraexamen del Perito Contrario
- ¿Qué metodología usó? ¿Es la estándar en la disciplina?
- ¿Tuvo acceso a todos los antecedentes?
- ¿Ha llegado a conclusiones similares en casos con hechos distintos? (sesgo de confirmación)

---

## 5. Estrategia de Prueba Documental Masiva

**Premisa**: En lo civil, la prueba documental es reina. Quien mejor la organiza y presenta, convence.

### Organización
```
Carpeta Digital:
├── 01-Contratos y Acuerdos
├── 02-Comunicaciones (emails, WhatsApp)
├── 03-Registros Financieros
├── 04-Fotografías y Videos
├── 05-Informes Técnicos
└── 06-Registros Administrativos
```

### Presentación en Juicio
- Crear un "libro de prueba" ordenado cronológicamente
- Cada documento con ficha de referencia (quién lo creó, cuándo, qué prueba)
- Resumen ejecutivo para el juez (no más de 2 páginas)

---

## 6. Estrategia de Transacción Óptima

**Premisa**: La mayoría de los casos civiles se resuelven antes de juicio. El objetivo es lograr el mejor acuerdo posible.

### Cuándo Transar
| Situación | Recomendación |
|-----------|--------------|
| P(ganar) > 75% y monto alto | Ir a juicio |
| P(ganar) 50-75% | Negociar, pedir más del 70% del monto |
| P(ganar) 25-50% | Negociar, aceptar 40-60% del monto |
| P(ganar) < 25% | Transacción urgente, minimizar daño |

### Cálculo del Valor de Transacción (para el demandante)
```
VT_mínimo = P(ganar) × Monto_demandado × (1 - % costas) - Costos_litigio_propios
```

### Cálculo para el Demandado
```
VT_máximo = P(perder) × Monto_demandado + Costos_litigio_propios
```

Si VT_mínimo(demandante) < VT_máximo(demandado) → **hay espacio para transar**.

Ver análisis completo: [[05-Teoria-Juegos/Equilibrio-Nash-en-Litigios]]

---

## 7. Estrategia en Responsabilidad Médica

**Premisa especial**: Casos de mayor complejidad probatoria. La carga de la prueba varía por doctrina de res ipsa loquitur y cargas dinámicas.

### Elementos a Probar
- [ ] **Existencia de la relación médico-paciente** (contrato o cuasidelito)
- [ ] **Lex artis** (estándar de cuidado médico) definida por perito
- [ ] **Incumplimiento** de la lex artis
- [ ] **Daño** causalmente vinculado al incumplimiento

### Inversión de la Carga de la Prueba
En algunos tribunales, cuando el daño ocurre en circunstancias que normalmente no ocurren sin negligencia, se invierte la carga (res ipsa loquitur).

---

## Conexiones

> Véase también:
> - [[04-Estrategias/Estrategias-Defensa-Penal]]
> - [[05-Teoria-Juegos/Equilibrio-Nash-en-Litigios]]
> - [[06-Bayes/Conceptos-Bayesianos-Legales]]

---

*[[04-Estrategias/MOC-Estrategias|← Estrategias]]*
