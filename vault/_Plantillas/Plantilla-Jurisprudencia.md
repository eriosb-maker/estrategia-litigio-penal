---
tipo: jurisprudencia
titulo: "{{TITULO DEL CASO}}"
tribunal: "{{CS | CA | TOP | TJOP}}"
sala: "{{Primera | Segunda | Constitucional}}"
fecha-fallo: {{YYYY-MM-DD}}
rol: "{{XXXX-YYYY}}"
materia: "{{penal | civil | procesal}}"
resultado: "{{acoge | rechaza | confirma | revoca}}"
normas-aplicadas: []
etiquetas: [jurisprudencia, {{materia}}, {{tribunal}}]
favorece: "{{defensa | acusacion | ambos | ninguno}}"
---

# 🏛️ {{TÍTULO}} — {{TRIBUNAL}} {{AÑO}}

## Datos del Fallo

| Campo | Valor |
|-------|-------|
| **Tribunal** | {{TRIBUNAL}} |
| **Rol** | {{ROL}} |
| **Fecha** | {{FECHA}} |
| **Sala** | {{SALA}} |
| **Redactor** | {{MINISTRO}} |

---

## Hechos Relevantes

> *Descripción concisa de los hechos del caso*

---

## Cuestión Jurídica

> *¿Cuál fue la pregunta legal que resolvió este fallo?*

---

## Holding (Ratio Decidendi)

> **La regla del caso**:
> 
> *"{{CITA TEXTUAL DEL HOLDING}}"*

---

## Razonamiento del Tribunal

### Argumentos Principales
1. 
2. 
3. 

### Normas Citadas
- [[02-Marco-Legal/]]

---

## Obiter Dicta

> *Observaciones del tribunal que no son parte del holding pero son relevantes*

---

## Votos Disidentes / Prevenciones

**Ministro {{NOMBRE}}**:
> *"{{ARGUMENTO DISIDENTE}}"*

---

## Análisis Crítico

### Por qué es relevante para nosotros


### Limitaciones del precedente


### Distinguishing (cómo diferenciarlo si nos perjudica)


---

## Causas Donde Aplica

```dataview
LIST FROM "01-Causas"
WHERE tipo = "causa" AND contains(jurisprudencia-relevante, this.file.name)
```

---

## Jurisprudencia Relacionada

> Véase también:
> - [[02-Marco-Legal/]]

---

*[[02-Marco-Legal/MOC-Marco-Legal|← Marco Legal]]*
