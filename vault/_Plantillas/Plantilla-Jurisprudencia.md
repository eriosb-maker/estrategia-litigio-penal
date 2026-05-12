<%*
const tribunal = await tp.system.suggester(
  ["Corte Suprema", "Corte de Apelaciones", "TOP", "TJOP", "Tribunal Constitucional", "Tribunal Civil"],
  ["CS", "CA", "TOP", "TJOP", "TC", "TC-Civil"]
);
const rol = await tp.system.prompt("Rol del fallo (ej: 12345-2023)");
const fecha = await tp.system.prompt("Fecha del fallo (YYYY-MM-DD)", tp.date.now("YYYY-MM-DD"));
const materia = await tp.system.suggester(
  ["penal", "civil", "procesal", "constitucional", "laboral"],
  ["penal", "civil", "procesal", "constitucional", "laboral"]
);
const favorece = await tp.system.suggester(
  ["Defensa", "Acusación / Demandante", "Neutral / Mixto"],
  ["defensa", "acusacion", "mixto"]
);
const relevancia = await tp.system.suggester(["Alta", "Media", "Baja"], ["alta", "media", "baja"]);
const hoy = tp.date.now("YYYY-MM-DD");
await tp.file.rename(`${tribunal}-Rol-${rol}`);
-%>
---
tipo: jurisprudencia
tribunal: "<% tribunal %>"
rol: "<% rol %>"
fecha-fallo: <% fecha %>
materia: "<% materia %>"
favorece: "<% favorece %>"
relevancia: "<% relevancia %>"
normas-aplicadas: []
fecha-captura: <% hoy %>
etiquetas: [jurisprudencia, <% materia %>, <% tribunal.toLowerCase() %>]
---

# ⚖️ <% tribunal %> Rol <% rol %> — <% fecha %>

> **Materia**: <% materia %> | **Favorece**: <% favorece %> | **Relevancia**: <% relevancia %>

---

## Hechos Relevantes

> *Resumen en 3-5 líneas*

---

## Cuestión Debatida

> *¿Qué se discutía?*

---

## Holding (Regla del Caso)

> *La regla jurídica que se desprende del fallo, citada textualmente cuando sea posible*

---

## Razonamiento del Tribunal

> *Considerandos clave*

---

## Voto Disidente (si aplica)

---

## Por Qué Es Relevante Para Nosotros

> *¿En qué causas y argumentos podemos usarla?*

---

## Cómo Distinguirla (Si Perjudica)

> *¿Qué hechos son distintos a los nuestros? ¿Qué hace que no aplique?*

---

## Normas Aplicadas

- [[02-Marco-Legal/]]
- [[02-Marco-Legal/]]

---

## Causas Donde la Hemos Citado

```dataview
LIST FROM "01-Causas"
WHERE contains(file.outlinks, this.file.link)
```

---
*Capturada: <% hoy %>*
*[[02-Marco-Legal/MOC-Marco-Legal|← Marco Legal]]*
