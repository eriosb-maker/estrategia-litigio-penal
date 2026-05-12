<%*
const ruc = await tp.system.prompt("RUC de la causa (ej: 2024-001)");
const tipoAud = await tp.system.suggester(
  ["Formalización", "Cautelar", "Preparatoria de JO", "Juicio Oral", "Lectura de sentencia", "Apelación", "Civil (única)", "Civil (prueba)"],
  ["formalizacion", "cautelar", "preparatoria", "juicio-oral", "sentencia", "apelacion", "civil-unica", "civil-prueba"]
);
const resultado = await tp.system.suggester(
  ["Favorable", "Desfavorable", "Parcial", "Pendiente"],
  ["favorable", "desfavorable", "parcial", "pendiente"]
);
const juez = await tp.system.prompt("Juez/a", "");
const fiscal = await tp.system.prompt("Fiscal / Contraparte", "");
const duracion = await tp.system.prompt("Duración (ej: 1h 30min)", "");

const hoy = tp.date.now("YYYY-MM-DD");
const plazoApelacion = tp.user.plazos.apelacion(hoy);
const plazoNulidad = tp.user.plazos.recursoNulidad(hoy);
const plazoReposicion = tp.user.plazos.recursoReposicion(hoy);
await tp.file.rename(`Audiencia-${ruc}-${hoy}-${tipoAud}`);
-%>
---
tipo: audiencia
causa-ruc: "<% ruc %>"
fecha: <% hoy %>
tipo-audiencia: "<% tipoAud %>"
resultado: "<% resultado %>"
juez: "<% juez %>"
fiscal: "<% fiscal %>"
duracion: "<% duracion %>"
etiquetas: [audiencia, <% tipoAud %>]
---

# 🏛️ Audiencia <% tipoAud %> — <% hoy %>

> **Causa**: [[01-Causas/<% ruc %>/00-Resumen|<% ruc %>]] | **Resultado**: <% resultado %>

---

## Participantes

| Rol | Nombre |
|-----|--------|
| Juez/a | <% juez %> |
| Fiscal / Contraparte | <% fiscal %> |
| Defensor/a | |
| Testigos presentes | |

---

## Decisiones del Tribunal

1. 
2. 

---

## Pruebas / Solicitudes

| N° | Solicitud | Resultado | Fundamento |
|----|-----------|-----------|------------|
| 1  | | Acogida / Rechazada | |

---

## Observaciones Tácticas

- **Juez/a**: 
- **Fiscal**: 
- **Testigos**: 
- **Mi propio desempeño**: 

---

## Plazos Derivados

| Plazo | Vence | Acción requerida |
|-------|-------|-----------------|
| Reposición (3 d. hábiles) | <% plazoReposicion %> | Evaluar |
| Apelación (5 d. hábiles) | <% plazoApelacion %> | Evaluar recurso |
| Recurso de nulidad (10 d. hábiles) | <% plazoNulidad %> | Evaluar recurso |

---

## Próximos Pasos

- [ ] 📅 <% tp.date.now("YYYY-MM-DD", "+1d") %> — Subir notas al expediente
- [ ] 📅 <% plazoApelacion %> — Decisión sobre apelación
- [ ] 📅 — Próxima audiencia

---

## Conexiones

- Causa: [[01-Causas/<% ruc %>/00-Resumen]]
- Normas invocadas: [[]]
- Jurisprudencia citada: [[]]
- Actores: [[<% juez %>]] · [[<% fiscal %>]]

---
*Registrada: <% hoy %>*
