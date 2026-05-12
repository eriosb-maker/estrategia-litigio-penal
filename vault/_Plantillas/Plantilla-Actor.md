<%*
const nombre = await tp.system.prompt("Nombre completo (ej: María López)");
const rol = await tp.system.suggester(
  ["Juez/a", "Fiscal", "Defensor/a", "Perito", "Testigo experto", "Querellante", "Abogado contraparte"],
  ["juez", "fiscal", "defensor", "perito", "testigo-experto", "querellante", "contraparte"]
);
const institucion = await tp.system.prompt("Tribunal / Institución");
const hoy = tp.date.now("YYYY-MM-DD");
const slug = `${rol[0].toUpperCase()+rol.slice(1)}-${nombre.replace(/\s+/g, "-")}`;
await tp.file.rename(slug);
-%>
---
tipo: actor
nombre: "<% nombre %>"
rol: "<% rol %>"
institucion: "<% institucion %>"
fecha-captura: <% hoy %>
etiquetas: [actor, <% rol %>]
---

# 👤 <% nombre %>

> **Rol**: <% rol %> | **Institución**: <% institucion %>

---

## Estilo Observado

> *¿Cómo actúa? ¿Qué valora? ¿Qué lo molesta?*

- **Puntualidad**: 
- **Tono**: 
- **Preferencias argumentativas**: 
- **Debilidades observadas**: 

---

## Estadísticas

| Indicador | Valor |
|-----------|-------|
| Audiencias observadas | 0 |
| Exclusiones de prueba aceptadas | 0 / 0 |
| Salidas alternativas aceptadas | 0 / 0 |
| Tendencia | — |

---

## Cómo Maximizar Resultados

### ✅ Hacer
- 

### ❌ Evitar
- 

---

## Causas Donde Aparece

```dataview
TABLE rol-abogado, materia, estado
FROM "01-Causas"
WHERE contains(file.outlinks, this.file.link) OR contains(juez, this.file.name) OR contains(fiscal, this.file.name)
```

---

## Audiencias Donde Participó

```dataview
TABLE fecha, tipo-audiencia, resultado
FROM #audiencia
WHERE contains(file.outlinks, this.file.link)
SORT fecha DESC
```

---
*Captura: <% hoy %>*
*[[08-Actores/MOC-Actores|← Actores]]*
