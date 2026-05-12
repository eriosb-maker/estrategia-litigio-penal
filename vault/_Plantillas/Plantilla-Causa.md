<%*
// Plantilla interactiva de Causa — Templater
const nombre = await tp.system.prompt("Nombre de la causa (ej: Robo Banco Central)");
const ruc = await tp.system.prompt("RUC / Rol (ej: 2024-001 o C-12345-2024)");
const materia = await tp.system.suggester(
  ["penal", "civil", "laboral", "familia"],
  ["penal", "civil", "laboral", "familia"]
);
const rolAbogado = await tp.system.suggester(
  ["defensor", "querellante", "demandante", "demandado", "tercero"],
  ["defensor", "querellante", "demandante", "demandado", "tercero"]
);
const tribunal = await tp.system.prompt("Tribunal (ej: TOP Santiago)");
const juez = await tp.system.prompt("Juez/a (deja vacío si aún no asignado)", "");
const fiscal = await tp.system.prompt("Fiscal o contraparte", "");
const imputado = await tp.system.prompt("Imputado / Demandado", "");
const victima = await tp.system.prompt("Víctima / Demandante (si aplica)", "");
const probInicial = await tp.system.prompt("Probabilidad inicial de condena (0.0 - 1.0)", "0.5");

const hoy = tp.date.now("YYYY-MM-DD");
const audPrep = tp.user.plazos.audienciaPreparatoria(hoy);
const limiteInvestigacion = tp.user.plazos.cierreInvestigacion(hoy);

await tp.file.rename(ruc);
-%>
---
tipo: causa
causa: "<% nombre %>"
ruc: "<% ruc %>"
tribunal: "<% tribunal %>"
materia: "<% materia %>"
rol-abogado: "<% rolAbogado %>"
imputado: "<% imputado %>"
victima: "<% victima %>"
fiscal: "<% fiscal %>"
juez: "<% juez %>"
fecha-inicio: <% hoy %>
proxima-audiencia: <% audPrep %>
limite-investigacion: <% limiteInvestigacion %>
estado: "en-proceso"
probabilidad-condena: <% probInicial %>
recomendacion-estrategia: ""
etiquetas: [causa, <% materia %>, <% rolAbogado %>]
---

# ⚖️ <% nombre %>

> **RUC**: <% ruc %> | **Tribunal**: <% tribunal %> | **Estado**: en-proceso | **Creada**: <% hoy %>

---

## 1. Resumen Ejecutivo

**Hecho imputado / Materia**:

**Nuestra posición**:

**Fortalezas principales**:
-

**Debilidades principales**:
-

**Riesgo estimado**: 🟡 Por determinar

---

## 2. Registro de Audiencias

*(Usa `Ctrl+Shift+A` para agregar audiencias rápido)*

---

## 3. Plazos Procesales Críticos

| Hito | Fecha estimada | Estado |
|------|---------------|--------|
| Inicio de la causa | <% hoy %> | ✅ |
| Audiencia preparatoria (estimada) | <% audPrep %> | ⏳ |
| Cierre de investigación (máximo legal) | <% limiteInvestigacion %> | ⏳ |

---

## 4. Tareas Pendientes

- [ ] 📅 <% tp.date.now("YYYY-MM-DD", "+3d") %> — Revisar antecedentes iniciales
- [ ] 📅 <% tp.date.now("YYYY-MM-DD", "+7d") %> — Reunión con cliente
- [ ] 📅 <% tp.date.now("YYYY-MM-DD", "+14d") %> — Solicitar copia de carpeta investigativa

---

## 5. Análisis Estratégico

> Ejecutar desde terminal:
> ```bash
> python scripts/analizar_causa.py --ruc <% ruc %> --modo bayes --guardar
> python scripts/analizar_causa.py --ruc <% ruc %> --modo juegos --guardar
> ```

**P(Condena) inicial**: <% probInicial %>
**P(Condena) posterior**: *(se actualiza con análisis Bayesiano)*

---

## Referencias

- [[<% ruc %>/01-Hechos|Hechos]]
- [[<% ruc %>/02-Pruebas|Pruebas]]
- [[<% ruc %>/03-Testigos|Testigos]]
- [[<% ruc %>/04-Analisis-Bayes|Análisis Bayesiano]]
- [[<% ruc %>/05-Estrategia-TJ|Estrategia (Teoría de Juegos)]]

### Actores
- Juez: [[<% juez %>]]
- Fiscal: [[<% fiscal %>]]

### Marco legal aplicable
- [[]]

---
*[[01-Causas/MOC-Causas|← Causas]]*
