"""
Gestor de Causas — crea y gestiona la estructura de una causa en el vault de Obsidian.
"""

import json
import os
from dataclasses import dataclass, field, asdict
from datetime import date, datetime
from pathlib import Path
from typing import Optional


@dataclass
class Causa:
    """Modelo de datos de una causa legal."""
    nombre: str
    ruc: str
    tipo: str               # "penal" | "civil"
    rol_abogado: str        # "defensor" | "querellante" | "demandante" | "demandado"
    tribunal: str
    imputado: str = ""
    victima: str = ""
    fiscal: str = ""
    juez: str = ""
    fecha_inicio: str = field(default_factory=lambda: date.today().isoformat())
    proxima_audiencia: str = ""
    estado: str = "en-proceso"
    prob_condena: float = 0.5
    rol_tribunal: str = ""
    etiquetas: list[str] = field(default_factory=list)

    def carpeta_id(self) -> str:
        """Identificador seguro para nombre de carpeta."""
        return self.ruc.replace("/", "-").replace(" ", "_")

    def to_frontmatter(self) -> str:
        """Convierte la causa a YAML frontmatter de Obsidian."""
        etiquetas = self.etiquetas or ["causa", self.tipo, self.rol_abogado]
        return f"""---
tipo: causa
causa: "{self.nombre}"
ruc: "{self.ruc}"
rol-tribunal: "{self.rol_tribunal}"
tribunal: "{self.tribunal}"
materia: "{self.tipo}"
rol-abogado: "{self.rol_abogado}"
imputado: "{self.imputado}"
victima: "{self.victima}"
fiscal: "{self.fiscal}"
juez: "{self.juez}"
fecha-inicio: {self.fecha_inicio}
proxima-audiencia: {self.proxima_audiencia or self.fecha_inicio}
estado: "{self.estado}"
probabilidad-condena: {self.prob_condena}
recomendacion-estrategia: ""
etiquetas: {json.dumps(etiquetas, ensure_ascii=False)}
---"""


class CausaManager:
    """
    Gestiona causas en el vault de Obsidian.
    Crea estructura de carpetas y notas base para cada causa.
    """

    def __init__(self, vault_path: str | Path):
        self.vault_path = Path(vault_path)
        self.causas_path = self.vault_path / "01-Causas"
        self.causas_path.mkdir(parents=True, exist_ok=True)

    def crear_causa(self, causa: Causa) -> Path:
        """
        Crea la estructura completa de una causa nueva en el vault.
        Retorna el path de la carpeta creada.
        """
        carpeta = self.causas_path / causa.carpeta_id()
        if carpeta.exists():
            raise FileExistsError(f"Ya existe una causa con RUC {causa.ruc} en {carpeta}")
        carpeta.mkdir(parents=True)

        self._crear_nota_resumen(carpeta, causa)
        self._crear_nota_hechos(carpeta, causa)
        self._crear_nota_pruebas(carpeta, causa)
        self._crear_nota_testigos(carpeta, causa)
        self._crear_nota_bayes_placeholder(carpeta, causa)
        self._crear_nota_tj_placeholder(carpeta, causa)

        self._registrar_causa(causa)
        return carpeta

    def _crear_nota_resumen(self, carpeta: Path, c: Causa) -> None:
        contenido = f"""{c.to_frontmatter()}

# ⚖️ {c.nombre}

> **RUC**: {c.ruc} | **Tribunal**: {c.tribunal} | **Estado**: {c.estado}

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

*(Ir añadiendo audiencias aquí)*

---

## 3. Tareas Pendientes

- [ ] 📅 {c.fecha_inicio} — Revisar antecedentes iniciales

---

## Referencias

- [[{c.carpeta_id()}/01-Hechos|Hechos]]
- [[{c.carpeta_id()}/02-Pruebas|Pruebas]]
- [[{c.carpeta_id()}/03-Testigos|Testigos]]
- [[{c.carpeta_id()}/04-Analisis-Bayes|Análisis Bayesiano]]
- [[{c.carpeta_id()}/05-Estrategia-TJ|Estrategia (Teoría de Juegos)]]

---

*[[01-Causas/MOC-Causas|← Causas]]*
"""
        (carpeta / "00-Resumen.md").write_text(contenido, encoding="utf-8")

    def _crear_nota_hechos(self, carpeta: Path, c: Causa) -> None:
        contenido = f"""---
tipo: hechos
causa: "{c.nombre}"
ruc: "{c.ruc}"
etiquetas: [hechos, {c.tipo}]
---

# 📋 Hechos — {c.nombre}

## Cronología

| Fecha | Hecho | Fuente | Certeza |
|-------|-------|--------|---------|
| {c.fecha_inicio} | | | Alto/Medio/Bajo |

## Versión de la Contraparte / Fiscalía

> *Descripción de los hechos según la contraparte*

## Nuestra Versión

> *Descripción de los hechos según nuestra posición*

## Hechos Controvertidos
- [ ]

## Hechos No Controvertidos
- [ ]

---
*[[00-Resumen|← Resumen de la Causa]]*
"""
        (carpeta / "01-Hechos.md").write_text(contenido, encoding="utf-8")

    def _crear_nota_pruebas(self, carpeta: Path, c: Causa) -> None:
        contenido = f"""---
tipo: pruebas
causa: "{c.nombre}"
ruc: "{c.ruc}"
etiquetas: [pruebas, {c.tipo}]
---

# 🔍 Pruebas — {c.nombre}

## Pruebas de Cargo

| # | Tipo | Descripción | Peso | Cuestionamiento Posible |
|---|------|-------------|------|------------------------|
| 1 | | | Alto/Medio/Bajo | |

## Pruebas de Descargo

| # | Tipo | Descripción | Peso | Observación |
|---|------|-------------|------|------------|
| 1 | | | Alto/Medio/Bajo | |

## Pendientes de Obtener
- [ ]

## Pruebas a Impugnar
- [ ] Impugnar [prueba] por:

---
*[[00-Resumen|← Resumen de la Causa]]*
"""
        (carpeta / "02-Pruebas.md").write_text(contenido, encoding="utf-8")

    def _crear_nota_testigos(self, carpeta: Path, c: Causa) -> None:
        contenido = f"""---
tipo: testigos
causa: "{c.nombre}"
ruc: "{c.ruc}"
etiquetas: [testigos, {c.tipo}]
---

# 👥 Testigos — {c.nombre}

## Testigos de Cargo

| Nombre | Credibilidad | Puntos a Atacar | Estrategia Cross |
|--------|-------------|----------------|-----------------|
| | Alta/Media/Baja | | |

## Testigos de Descargo

| Nombre | Credibilidad | Puntos Clave | Preparación |
|--------|-------------|-------------|------------|
| | Alta/Media/Baja | | |

## Notas de Preparación de Testigos


---
*[[00-Resumen|← Resumen de la Causa]]*
"""
        (carpeta / "03-Testigos.md").write_text(contenido, encoding="utf-8")

    def _crear_nota_bayes_placeholder(self, carpeta: Path, c: Causa) -> None:
        contenido = f"""---
tipo: analisis-bayes
causa: "{c.nombre}"
ruc: "{c.ruc}"
fecha: {c.fecha_inicio}
probabilidad-prior: {c.prob_condena}
probabilidad-posterior: {c.prob_condena}
recomendacion: "por-determinar"
etiquetas: [bayes, analisis]
---

# 📊 Análisis Bayesiano — {c.nombre}

> ⚙️ Ejecutar para generar análisis completo:
> ```bash
> python scripts/analizar_causa.py --ruc "{c.ruc}" --modo bayes
> ```

**Probabilidad A Priori**: {c.prob_condena:.0%}

*(El análisis detallado se genera automáticamente con el script)*

Ver conceptos: [[06-Bayes/Conceptos-Bayesianos-Legales]]

---
*[[00-Resumen|← Resumen de la Causa]]*
"""
        (carpeta / "04-Analisis-Bayes.md").write_text(contenido, encoding="utf-8")

    def _crear_nota_tj_placeholder(self, carpeta: Path, c: Causa) -> None:
        contenido = f"""---
tipo: analisis-tj
causa: "{c.nombre}"
ruc: "{c.ruc}"
fecha: {c.fecha_inicio}
equilibrio-recomendado: "por-determinar"
etiquetas: [teoria-juegos, analisis]
---

# 🎮 Estrategia (Teoría de Juegos) — {c.nombre}

> ⚙️ Ejecutar para generar análisis completo:
> ```bash
> python scripts/analizar_causa.py --ruc "{c.ruc}" --modo juegos
> ```

*(El análisis detallado se genera automáticamente con el script)*

Ver conceptos: [[05-Teoria-Juegos/Equilibrio-Nash-en-Litigios]]

---
*[[00-Resumen|← Resumen de la Causa]]*
"""
        (carpeta / "05-Estrategia-TJ.md").write_text(contenido, encoding="utf-8")

    def _registrar_causa(self, causa: Causa) -> None:
        """Guarda el registro JSON de causas para búsqueda cruzada."""
        registro_path = self.causas_path / ".causas-registro.json"
        registro = {}
        if registro_path.exists():
            registro = json.loads(registro_path.read_text(encoding="utf-8"))
        registro[causa.ruc] = {
            "nombre": causa.nombre,
            "tipo": causa.tipo,
            "carpeta": causa.carpeta_id(),
            "fecha_creacion": datetime.now().isoformat(),
        }
        registro_path.write_text(
            json.dumps(registro, ensure_ascii=False, indent=2),
            encoding="utf-8"
        )

    def listar_causas(self) -> list[dict]:
        """Lista todas las causas registradas."""
        registro_path = self.causas_path / ".causas-registro.json"
        if not registro_path.exists():
            return []
        return list(json.loads(registro_path.read_text(encoding="utf-8")).values())

    def buscar_causa(self, ruc: str) -> Optional[Path]:
        """Encuentra la carpeta de una causa por su RUC."""
        registro_path = self.causas_path / ".causas-registro.json"
        if registro_path.exists():
            registro = json.loads(registro_path.read_text(encoding="utf-8"))
            if ruc in registro:
                return self.causas_path / registro[ruc]["carpeta"]
        carpeta_directa = self.causas_path / ruc.replace("/", "-").replace(" ", "_")
        if carpeta_directa.exists():
            return carpeta_directa
        return None

    def actualizar_analisis_bayes(self, ruc: str, reporte_markdown: str) -> None:
        """Actualiza la nota de análisis Bayesiano de una causa."""
        carpeta = self.buscar_causa(ruc)
        if not carpeta:
            raise FileNotFoundError(f"Causa {ruc} no encontrada")
        nota_path = carpeta / "04-Analisis-Bayes.md"
        nota_path.write_text(reporte_markdown, encoding="utf-8")

    def actualizar_analisis_tj(self, ruc: str, reporte_markdown: str) -> None:
        """Actualiza la nota de análisis de Teoría de Juegos de una causa."""
        carpeta = self.buscar_causa(ruc)
        if not carpeta:
            raise FileNotFoundError(f"Causa {ruc} no encontrada")
        nota_path = carpeta / "05-Estrategia-TJ.md"
        nota_path.write_text(reporte_markdown, encoding="utf-8")
