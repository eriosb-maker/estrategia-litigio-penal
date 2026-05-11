"""
Base de Conocimiento — indexa y cruza información entre causas, normas,
jurisprudencia y biblioteca para encontrar conexiones relevantes.
"""

import re
from pathlib import Path
from typing import Optional
from dataclasses import dataclass


@dataclass
class ResultadoBusqueda:
    """Resultado de una búsqueda en la base de conocimiento."""
    archivo: Path
    titulo: str
    tipo: str
    relevancia: float   # 0.0 - 1.0
    fragmento: str      # Extracto relevante del texto
    etiquetas: list[str]


class KnowledgeBase:
    """
    Indexa el vault de Obsidian y permite búsqueda cruzada entre notas.

    Permite encontrar:
    - Normas relevantes para un tipo de causa
    - Jurisprudencia aplicable
    - Papers y libros sobre el tema
    - Estrategias usadas en casos similares
    """

    def __init__(self, vault_path: str | Path):
        self.vault_path = Path(vault_path)
        self._indice: list[dict] = []

    def indexar(self) -> int:
        """
        Construye el índice del vault leyendo todos los archivos markdown.
        Retorna el número de notas indexadas.
        """
        self._indice = []
        for md_file in self.vault_path.rglob("*.md"):
            if ".obsidian" in str(md_file):
                continue
            nota = self._parsear_nota(md_file)
            if nota:
                self._indice.append(nota)
        return len(self._indice)

    def _parsear_nota(self, path: Path) -> Optional[dict]:
        """Parsea una nota markdown extrayendo frontmatter y contenido."""
        try:
            contenido = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, PermissionError):
            return None

        frontmatter = self._extraer_frontmatter(contenido)
        texto_limpio = self._limpiar_markdown(contenido)

        return {
            "path": path,
            "titulo": frontmatter.get("titulo", path.stem),
            "tipo": frontmatter.get("tipo", "desconocido"),
            "materia": frontmatter.get("materia", ""),
            "etiquetas": frontmatter.get("etiquetas", []),
            "contenido": texto_limpio,
            "frontmatter": frontmatter,
        }

    def _extraer_frontmatter(self, contenido: str) -> dict:
        """Extrae campos clave del YAML frontmatter."""
        resultado = {}
        if not contenido.startswith("---"):
            return resultado

        fm_match = re.match(r"^---\n(.*?)\n---", contenido, re.DOTALL)
        if not fm_match:
            return resultado

        fm_texto = fm_match.group(1)

        campos_simples = ["tipo", "titulo", "materia", "causa", "ruc", "tribunal",
                          "autor", "año", "favorece", "rol"]
        for campo in campos_simples:
            m = re.search(rf'^{campo}:\s*"?([^"\n]+)"?', fm_texto, re.MULTILINE)
            if m:
                resultado[campo] = m.group(1).strip()

        etiquetas_m = re.search(r'^etiquetas:\s*\[([^\]]*)\]', fm_texto, re.MULTILINE)
        if etiquetas_m:
            etiquetas_raw = etiquetas_m.group(1)
            resultado["etiquetas"] = [
                e.strip().strip('"').strip("'")
                for e in etiquetas_raw.split(",")
                if e.strip()
            ]

        return resultado

    def _limpiar_markdown(self, texto: str) -> str:
        """Elimina sintaxis markdown para indexar solo el texto."""
        texto = re.sub(r"^---\n.*?\n---\n", "", texto, flags=re.DOTALL)
        texto = re.sub(r"\[\[([^\|]+)\|?[^\]]*\]\]", r"\1", texto)
        texto = re.sub(r"#+\s+", "", texto)
        texto = re.sub(r"\*\*|__|\*|_|`", "", texto)
        texto = re.sub(r"\|[^\n]+", "", texto)
        texto = re.sub(r"\n{3,}", "\n\n", texto)
        return texto.strip()

    def _calcular_relevancia(self, nota: dict, terminos: list[str], materia: str = "") -> float:
        """Calcula relevancia de una nota para una búsqueda."""
        score = 0.0
        contenido_lower = (nota["contenido"] + " " + nota["titulo"]).lower()
        etiquetas_lower = [e.lower() for e in nota.get("etiquetas", [])]

        for termino in terminos:
            t = termino.lower()
            # Coincidencia en título (mayor peso)
            if t in nota["titulo"].lower():
                score += 0.5
            # Coincidencia en etiquetas
            if any(t in etq for etq in etiquetas_lower):
                score += 0.3
            # Coincidencia en contenido (normalizada por frecuencia)
            frecuencia = contenido_lower.count(t)
            score += min(frecuencia * 0.1, 0.3)

        # Boost por materia coincidente
        if materia and nota.get("materia", "").lower() == materia.lower():
            score *= 1.2

        return min(score, 1.0)

    def _extraer_fragmento(self, nota: dict, terminos: list[str]) -> str:
        """Extrae el fragmento más relevante del contenido."""
        contenido = nota["contenido"]
        for termino in terminos:
            idx = contenido.lower().find(termino.lower())
            if idx != -1:
                inicio = max(0, idx - 80)
                fin = min(len(contenido), idx + 160)
                fragmento = contenido[inicio:fin].strip()
                return f"...{fragmento}..."
        return contenido[:200] + "..." if len(contenido) > 200 else contenido

    def buscar(
        self,
        consulta: str,
        tipos: Optional[list[str]] = None,
        materia: str = "",
        limite: int = 10,
        umbral_relevancia: float = 0.1,
    ) -> list[ResultadoBusqueda]:
        """
        Busca notas relevantes para una consulta.

        Args:
            consulta: Texto libre de búsqueda
            tipos: Filtrar por tipo de nota (ej: ["norma", "jurisprudencia"])
            materia: Filtrar por materia ("penal", "civil")
            limite: Número máximo de resultados
            umbral_relevancia: Mínimo score para incluir en resultados

        Returns:
            Lista de ResultadoBusqueda ordenada por relevancia
        """
        if not self._indice:
            self.indexar()

        terminos = [t for t in consulta.split() if len(t) > 2]
        resultados = []

        for nota in self._indice:
            if tipos and nota["tipo"] not in tipos:
                continue

            relevancia = self._calcular_relevancia(nota, terminos, materia)
            if relevancia < umbral_relevancia:
                continue

            resultados.append(ResultadoBusqueda(
                archivo=nota["path"],
                titulo=nota["titulo"],
                tipo=nota["tipo"],
                relevancia=round(relevancia, 3),
                fragmento=self._extraer_fragmento(nota, terminos),
                etiquetas=nota.get("etiquetas", []),
            ))

        return sorted(resultados, key=lambda r: r.relevancia, reverse=True)[:limite]

    def normas_para_causa(self, descripcion_causa: str, materia: str = "penal") -> list[ResultadoBusqueda]:
        """Busca normas legales relevantes para una causa."""
        return self.buscar(descripcion_causa, tipos=["norma"], materia=materia, limite=8)

    def jurisprudencia_para_causa(self, descripcion_causa: str, materia: str = "penal") -> list[ResultadoBusqueda]:
        """Busca jurisprudencia relevante para una causa."""
        return self.buscar(descripcion_causa, tipos=["jurisprudencia"], materia=materia, limite=8)

    def estrategias_similares(self, tipo_caso: str, rol: str = "defensa") -> list[ResultadoBusqueda]:
        """Busca estrategias usadas en casos similares."""
        consulta = f"{tipo_caso} {rol}"
        return self.buscar(consulta, tipos=["estrategia", "estrategia-coleccion"], limite=5)

    def bibliografía_relevante(self, tema: str) -> list[ResultadoBusqueda]:
        """Busca libros y papers relevantes para un tema."""
        return self.buscar(tema, tipos=["libro", "paper"], limite=6)

    def reporte_conexiones(self, ruc: str) -> str:
        """Genera un reporte Markdown con todas las conexiones relevantes para una causa."""
        if not self._indice:
            self.indexar()

        nota_causa = next(
            (n for n in self._indice if n.get("frontmatter", {}).get("ruc") == ruc),
            None
        )
        if not nota_causa:
            return f"# ❌ Causa {ruc} no encontrada en el índice\n"

        causa_texto = nota_causa["contenido"]
        materia = nota_causa.get("materia", "penal")

        normas = self.normas_para_causa(causa_texto[:500], materia)
        jurisprudencia = self.jurisprudencia_para_causa(causa_texto[:500], materia)
        bibliografia = self.bibliografía_relevante(causa_texto[:200])

        nombre_causa = nota_causa["titulo"]
        lineas = [
            f"# 🔗 Conexiones del Conocimiento — {nombre_causa}",
            f"\n**RUC**: {ruc} | **Materia**: {materia}",
            "\n---\n",
            "## 📜 Normas Potencialmente Aplicables\n",
        ]

        if normas:
            for r in normas:
                rel_pct = f"{r.relevancia * 100:.0f}%"
                lineas.append(f"- **[[{r.archivo.stem}]]** (relevancia: {rel_pct})")
                lineas.append(f"  > {r.fragmento[:120]}...")
        else:
            lineas.append("*No se encontraron normas indexadas aún.*")

        lineas += ["\n## 🏛️ Jurisprudencia Relevante\n"]
        if jurisprudencia:
            for r in jurisprudencia:
                rel_pct = f"{r.relevancia * 100:.0f}%"
                lineas.append(f"- **[[{r.archivo.stem}]]** (relevancia: {rel_pct})")
                lineas.append(f"  > {r.fragmento[:120]}...")
        else:
            lineas.append("*No se encontró jurisprudencia indexada aún.*")

        lineas += ["\n## 📚 Bibliografía Relacionada\n"]
        if bibliografia:
            for r in bibliografia:
                lineas.append(f"- **[[{r.archivo.stem}]]** — {r.tipo}")
        else:
            lineas.append("*No se encontraron fuentes en la biblioteca aún.*")

        lineas.append("\n---\n*Generado por el motor de Knowledge Base*")
        return "\n".join(lineas)

    def estadisticas(self) -> dict:
        """Retorna estadísticas del vault indexado."""
        if not self._indice:
            self.indexar()
        tipos = {}
        materias = {}
        for nota in self._indice:
            t = nota.get("tipo", "desconocido")
            tipos[t] = tipos.get(t, 0) + 1
            m = nota.get("materia", "sin-materia")
            materias[m] = materias.get(m, 0) + 1
        return {
            "total_notas": len(self._indice),
            "por_tipo": tipos,
            "por_materia": materias,
        }
