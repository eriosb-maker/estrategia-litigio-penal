---
tipo: estrategia-coleccion
titulo: Estrategias de Defensa Penal
materia: penal
rol: defensa
etiquetas: [estrategia, penal, defensa, coleccion]
---

# ⚔️ Estrategias de Defensa Penal

> *"La función del defensor no es probar la inocencia, sino hacer que el Estado pruebe la culpabilidad más allá de toda duda razonable."*

---

## 1. Estrategia de la Duda Razonable

**Premisa**: El estándar de prueba penal exige convicción más allá de toda duda razonable. No es necesario probar inocencia; basta con sembrar duda fundada.

### Implementación
1. **Identificar las grietas** en la cadena de custodia, coherencia de testigos, o razonamiento pericial.
2. **No construir una historia alternativa** (salvo que sea muy sólida). En su lugar, mostrar las inconsistencias de la versión fiscal.
3. **Cerrar con la carga de la prueba**: recordar al tribunal que la duda beneficia al imputado.

### Cuándo aplicar
- Evidencia fiscal circunstancial o testimonial (no física directa)
- Testigos con credibilidad cuestionable
- Cadena de custodia débil

### Análisis Bayesiano
Si logras bajar la probabilidad subjetiva del tribunal de P(Culpable|E) < 0.9, teóricamente deberías ganar.
Ver: [[06-Bayes/Conceptos-Bayesianos-Legales#El Estándar de Prueba como Umbral Bayesiano]]

### Fundamento Legal
- [[02-Marco-Legal/]] Art. 340 CPP (convicción más allá de toda duda razonable)

---

## 2. Estrategia de Ataque a la Credibilidad del Testigo Clave

**Premisa**: Si el caso fiscal descansa principalmente en un testigo, destruir su credibilidad destruye el caso.

### Técnicas de Contraexamen

#### a) Inconsistencias Internas
- Comparar declaración en juicio vs. declaración en fiscalía
- Comparar con otros testigos de la misma parte
- *"¿No dijo usted en [fecha] ante el fiscal que...?"*

#### b) Sesgo o Interés
- Relación con la víctima o el imputado
- Beneficios obtenidos por declarar (inmunidad, acuerdo, etc.)
- *"¿Es cierto que a cambio de su declaración recibió...?"*

#### c) Capacidad Perceptiva
- Condiciones de luz, distancia, tiempo de observación
- Estado emocional en el momento de los hechos
- Consumo de alcohol/drogas si aplica

#### d) Memoria
- Tiempo transcurrido entre el hecho y la declaración
- Influencia de noticias, conversaciones con terceros
- Técnica del "primado" (leading questions before the event)

### Regla de Oro
Nunca atacar a un testigo en algo que no puedas probar. El juez recordará el error.

### Referencia Teórica
Ver: [[03-Biblioteca/]] — Psicología del Testimonio

---

## 3. Estrategia de Exclusión de Prueba Ilícita

**Premisa**: La prueba obtenida con violación de garantías constitucionales es nula y no puede valorarse.

### Fundamento
- Art. 276 y 277 CPP (exclusión de prueba)
- Art. 19 N°4 y N°5 Constitución (intimidad y privacidad)
- Doctrina del fruto del árbol envenenado

### Procedimiento
1. **JUICIO PREVIO**: plantear en audiencia de preparación de juicio oral (Art. 276 CPP)
2. **Argumentar**: la prueba {{tipo}} fue obtenida mediante {{violación de garantía}}
3. **Solicitar**: exclusión de toda la prueba derivada (efecto reflejo)

### Checklist de Vulneraciones
- [ ] Allanamiento sin orden judicial o con orden defectuosa
- [ ] Detención sin flagrancia ni orden judicial
- [ ] Interceptación de comunicaciones sin autorización judicial
- [ ] Declaración del imputado sin advertencia de derechos (Art. 93 CPP)
- [ ] Examen corporal o de ADN sin consentimiento o autorización judicial

---

## 4. Estrategia de Salida Alternativa Negociada

**Premisa**: Cuando la probabilidad de condena es alta (P > 0.65), una salida alternativa minimiza el daño.

### Tipos de Salidas (Chile)
| Salida | Requisitos | Ventajas | Desventajas |
|--------|-----------|---------|------------|
| Suspensión Condicional | Delito < 3 años, sin condenas previas | No registra condena | Condiciones restrictivas |
| Acuerdo Reparatorio | Delitos con bien jurídico disponible | Fin inmediato del caso | Requiere víctima dispuesta |
| Procedimiento Abreviado | Reconocimiento de hechos | Pena menor negociada | Antecedentes penales |

### Negociación con la Fiscalía (Teoría de Juegos)
Ver: [[05-Teoria-Juegos/Equilibrio-Nash-en-Litigios]]

**La clave es la BATNA** (Best Alternative To Negotiated Agreement):
- Si la Fiscalía sabe que puedes ganar el juicio → tiene incentivo a negociar
- Si creen que ganarán → negociarán poco
- **Tu trabajo**: hacer creíble tu fortaleza procesal

### Matriz de Decisión
```
         ┌─────────────────────────────────┐
         │       P(Condena Juicio)         │
         │   < 40%  │ 40-65%  │  > 65%    │
├────────┼──────────┼─────────┼───────────┤
│ Pena   │          │         │           │
│ alta   │  Juicio  │ Evaluar │  Salida   │
│ > 5 a. │          │         │Alternativa│
├────────┼──────────┼─────────┼───────────┤
│ Pena   │  Juicio  │  Juicio │  Evaluar  │
│ < 3 a. │          │         │           │
└────────┴──────────┴─────────┴───────────┘
```

---

## 5. Estrategia de Error en el Tipo / Atipicidad

**Premisa**: Si la conducta no satisface todos los elementos del tipo penal, no hay delito.

### Análisis de Tipicidad
Para cada elemento del tipo imputado:
1. **¿Existe el elemento en el caso concreto?** (análisis fáctico)
2. **¿Puede probarlo la Fiscalía más allá de duda razonable?** (análisis probatorio)

### Atipicidad por Error
- **Error de tipo** (Art. 1 CP): el imputado no sabía que su conducta cumplía el tipo
- **Error de prohibición**: el imputado no sabía que su conducta era ilícita

---

## 6. Estrategia de Legítima Defensa

**Premisa**: La conducta típica estaba justificada por necesidad de defensa.

### Requisitos (Art. 10 N°4 CP)
- [ ] **Agresión ilegítima** previa o inminente
- [ ] **Necesidad racional** del medio empleado para repelerla
- [ ] **Falta de provocación** suficiente por parte del que se defiende

### Defensa Putativa
Si el imputado creyó razonablemente estar siendo agredido, aplica la misma justificante aunque la agresión no fuera real.

---

## Conexiones

> Véase también:
> - [[05-Teoria-Juegos/Equilibrio-Nash-en-Litigios]]
> - [[06-Bayes/Conceptos-Bayesianos-Legales]]
> - [[04-Estrategias/Estrategias-Acusacion-Civil]]

---

*[[04-Estrategias/MOC-Estrategias|← Estrategias]]*
