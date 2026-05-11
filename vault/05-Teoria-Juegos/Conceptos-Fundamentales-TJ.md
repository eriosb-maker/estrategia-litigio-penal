---
tipo: concepto
titulo: Conceptos Fundamentales de Teoría de Juegos para Litigio
materia: teoria
etiquetas: [teoria-juegos, conceptos, estrategia, decision]
---

# 🎮 Teoría de Juegos para Abogados Litigantes

> *La teoría de juegos estudia situaciones en las que el resultado para cada participante depende no solo de sus propias decisiones, sino también de las decisiones de otros.*

---

## ¿Por qué la Teoría de Juegos importa en el litigio?

El litigio es fundamentalmente un **juego estratégico**:
- Tus decisiones (presentar prueba, hacer una oferta, apelar) afectan las decisiones de la contraparte
- Las decisiones de la contraparte afectan tus resultados
- El juez/árbitro tiene sus propias preferencias y restricciones

Sin TJ, los abogados usan intuición. Con TJ, usan modelos formales para predecir comportamiento.

---

## Conceptos Clave

### 1. Jugadores (Players)
En un litigio típico:
- **Defensa / Demandado**
- **Fiscalía / Demandante**  
- **Juez** (con preferencias propias)
- **Tribunal de alzada** (shadow of the law)
- **Medios / Opinión pública** (en casos de alto perfil)

### 2. Estrategias
Una estrategia es un **plan completo de acción** para cada situación posible del juego.

**Estrategia pura**: elegir una acción determinada (ej: "siempre ir a juicio")
**Estrategia mixta**: randomizar entre acciones con ciertas probabilidades (ej: "ir a juicio con 70% de probabilidad")

### 3. Pagos (Payoffs)
Los pagos representan el **valor que cada jugador asigna a cada resultado**.

En litigio penal (para el imputado):
- Absolución = mejor resultado (payoff: alto)
- Suspensión condicional = resultado medio (payoff: medio)
- Condena grave = peor resultado (payoff: muy bajo)

**Importante**: los pagos incluyen costos económicos, tiempo, reputación y riesgo.

### 4. Equilibrio de Nash
Un conjunto de estrategias donde **ningún jugador tiene incentivo de cambiar unilateralmente su estrategia**, dado lo que hace la contraparte.

> En equilibrio, cada jugador está haciendo lo mejor que puede dado lo que hace el otro.

**Implicación para el litigio**: Si identificas el equilibrio Nash, sabes qué esperar de la contraparte y puedes diseñar tu estrategia alrededor de ese conocimiento.

---

## Tipos de Juegos Relevantes en Litigio

### Juego de Suma Cero vs. No Suma Cero

| Tipo | Característica | Ejemplo en Litigio |
|------|---------------|-------------------|
| **Suma cero** | Lo que uno gana, el otro pierde exactamente | Disputas de propiedad donde el título va a uno u otro |
| **No suma cero** | Existen resultados que benefician a ambos más que ir a juicio | Acuerdos de divorcio, mediaciones exitosas |

**Conclusión práctica**: La mayoría de los litigios son **no suma cero**, lo que significa que **hay espacio para negociar** un resultado que a ambos les convenga más que el juicio.

### Juego Secuencial vs. Simultáneo

- **Simultáneo**: las partes eligen sin saber qué eligió la otra (ej: primera oferta de transacción)
- **Secuencial**: hay turnos de acción (ej: la Fiscalía formaliza, la Defensa responde, etc.)

En juegos secuenciales, se puede razonar **hacia atrás** (backward induction):
1. ¿Qué hará cada parte en el último turno?
2. Dado eso, ¿qué hará cada parte en el penúltimo turno?
3. Y así sucesivamente hasta el primer movimiento.

### Juego de Información Completa vs. Incompleta

- **Completa**: todos conocen los pagos de todos (raro en la práctica)
- **Incompleta**: no se conocen los pagos o "tipos" del adversario (lo normal)

En litigio, la información incompleta es la norma:
- No sabes con certeza cuánto le cuesta al fiscal ir a juicio
- No sabes cuánto le duele al imputado una condena vs. la incertidumbre
- No sabes cómo valorará el juez la prueba

---

## El Juego del Litigio: Modelo Básico

```
Imputado
  ├── Acepta negociar
  │     └── Fiscalía: ¿qué ofrece?
  │           ├── Oferta buena → Acuerdo (ambos ganan vs. juicio)
  │           └── Oferta mala → Rechazar → JUICIO
  └── Rechaza negociar → JUICIO
                           ├── Absolución (D gana, F pierde)
                           └── Condena (F gana, D pierde)
```

### El Modelo de Cooter-Ulen (Equilibrio en Litigio)

El litigio ocurre cuando:
```
Expectativa del Demandante > Expectativa del Demandado
```

Formalmente:
```
P_d × M - c_d > P_f × M + c_f
```

Donde:
- `P_d` = probabilidad de ganar según el demandante
- `P_f` = probabilidad de ganar según el demandado (desde la perspectiva contraria)
- `M` = monto en disputa
- `c_d, c_f` = costos del litigio para cada parte

Si ambos tienen la misma estimación de P → siempre hay espacio para transacción.
El litigio ocurre por **divergencia en las estimaciones** de probabilidad.

---

## Juego de Bargaining (Regateo): El Modelo Nash

Para una negociación, el **acuerdo Nash** maximiza:
```
(U_A - d_A) × (U_B - d_B)
```

Donde:
- `U_A` y `U_B` son los pagos en el acuerdo
- `d_A` y `d_B` son los pagos si no hay acuerdo (BATNA)

**Implicación práctica**: Mejorar tu BATNA (hacer más creíble tu victoria en juicio) te da más poder de negociación.

---

## Estrategia Dominante

Una estrategia es **dominante** si es mejor que todas las alternativas **independientemente** de lo que haga la contraparte.

**Ejemplo**: Si la evidencia en tu contra es abrumadora, "negociar" puede ser estrategia dominante (es mejor que "ir a juicio" sin importar lo que haga la Fiscalía).

### Cómo identificar estrategias dominadas
1. Para cada estrategia tuya, ¿hay otra tuya que siempre la supera?
2. Si sí, elimina la dominada.
3. Repite para la contraparte.
4. Lo que queda es el "espacio de estrategias razonables".

---

## Señalización (Signaling)

En juegos de información incompleta, los jugadores envían **señales** sobre su "tipo".

**Señales costosas en litigio**:
- Presentar un perito de alto costo (señaliza seriedad)
- Apelar todas las resoluciones (señaliza resistencia)
- Rechazar todas las ofertas (señaliza alta valoración del caso)

**Cuidado**: Una señal solo es creíble si es costosa de falsificar.

---

## Aplicación: ¿Ir a Juicio o Negociar?

Ver análisis detallado: [[05-Teoria-Juegos/Equilibrio-Nash-en-Litigios]]

Ver herramienta Python: `scripts/analizar_causa.py --modo juegos`

---

## Referencias

- [[03-Biblioteca/]] — Tirole & Fudenberg, "Game Theory" (1991)
- [[03-Biblioteca/]] — Mnookin, Peppet & Tulumello, "Beyond Winning" (2000)
- [[03-Biblioteca/]] — Cooter & Ulen, "Law and Economics" (2016)

---

*[[05-Teoria-Juegos/MOC-Teoria-Juegos|← Teoría de Juegos]]*
