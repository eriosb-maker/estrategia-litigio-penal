"""
Motor de Análisis Bayesiano para Litigio Legal
Implementa el teorema de Bayes para evaluar probabilidades de condena/responsabilidad
"""

from dataclasses import dataclass, field
from typing import Optional
import math


@dataclass
class Evidencia:
    """Representa una pieza de evidencia con sus razones de verosimilitud."""
    nombre: str
    descripcion: str
    prob_dado_culpable: float    # P(E | Culpable)
    prob_dado_inocente: float    # P(E | Inocente)
    tipo: str = "cargo"          # "cargo" | "descargo"
    independiente: bool = True   # Asume independencia respecto a otras evidencias

    @property
    def likelihood_ratio(self) -> float:
        """LR = P(E|H) / P(E|¬H). LR > 1 apoya culpabilidad, LR < 1 apoya inocencia."""
        if self.prob_dado_inocente == 0:
            return float('inf')
        return self.prob_dado_culpable / self.prob_dado_inocente

    @property
    def interpretacion_lr(self) -> str:
        lr = self.likelihood_ratio
        if lr > 100:
            return "Evidencia decisiva de culpabilidad"
        elif lr > 10:
            return "Evidencia fuerte de culpabilidad"
        elif lr > 2:
            return "Evidencia moderada de culpabilidad"
        elif lr > 0.5:
            return "Evidencia débil / neutral"
        elif lr > 0.1:
            return "Evidencia moderada de inocencia"
        else:
            return "Evidencia fuerte de inocencia"


@dataclass
class AnalisisBayesiano:
    """
    Análisis bayesiano completo de una causa legal.

    Calcula P(Culpable | Evidencia) usando el teorema de Bayes mediante
    el método de odds ratio acumulativo.
    """
    nombre_causa: str
    ruc: str
    prob_prior: float           # P(Culpable) antes de examinar evidencia (0.0 - 1.0)
    umbral_condena: float = 0.90  # Umbral estándar "más allá de duda razonable"
    umbral_civil: float = 0.51    # Umbral "preponderancia de la prueba"
    materia: str = "penal"        # "penal" | "civil"
    evidencias: list[Evidencia] = field(default_factory=list)

    def agregar_evidencia(self, evidencia: Evidencia) -> None:
        self.evidencias.append(evidencia)

    def agregar_evidencias(self, evidencias: list[Evidencia]) -> None:
        self.evidencias.extend(evidencias)

    def _prob_a_odds(self, prob: float) -> float:
        if prob >= 1.0:
            return float('inf')
        if prob <= 0.0:
            return 0.0
        return prob / (1.0 - prob)

    def _odds_a_prob(self, odds: float) -> float:
        if odds == float('inf'):
            return 1.0
        return odds / (1.0 + odds)

    @property
    def odds_prior(self) -> float:
        return self._prob_a_odds(self.prob_prior)

    @property
    def lr_total(self) -> float:
        """Producto de todos los likelihood ratios (asumiendo independencia)."""
        lr = 1.0
        for e in self.evidencias:
            lr *= e.likelihood_ratio
        return lr

    @property
    def odds_posterior(self) -> float:
        return self.odds_prior * self.lr_total

    @property
    def prob_posterior(self) -> float:
        return self._odds_a_prob(self.odds_posterior)

    @property
    def umbral_activo(self) -> float:
        return self.umbral_condena if self.materia == "penal" else self.umbral_civil

    @property
    def supera_umbral(self) -> bool:
        return self.prob_posterior >= self.umbral_activo

    @property
    def recomendacion(self) -> str:
        p = self.prob_posterior
        if self.materia == "penal":
            if p < 0.40:
                return "ir-a-juicio"
            elif p < 0.65:
                return "evaluar-caso-a-caso"
            elif p < 0.80:
                return "negociar-fuertemente"
            else:
                return "salida-alternativa-urgente"
        else:
            if p < 0.35:
                return "ir-a-juicio"
            elif p < 0.60:
                return "negociar"
            else:
                return "transaccion"

    def analisis_sensibilidad(self) -> list[dict]:
        """Calcula el impacto de excluir cada evidencia individualmente."""
        resultados = []
        for e in self.evidencias:
            lr_sin = self.lr_total / e.likelihood_ratio if e.likelihood_ratio != 0 else float('inf')
            odds_sin = self.odds_prior * lr_sin
            prob_sin = self._odds_a_prob(odds_sin)
            resultados.append({
                "evidencia": e.nombre,
                "lr": round(e.likelihood_ratio, 3),
                "prob_sin_esta_evidencia": round(prob_sin, 4),
                "impacto": round(self.prob_posterior - prob_sin, 4),
                "es_critica": abs(self.prob_posterior - prob_sin) > 0.10,
            })
        return sorted(resultados, key=lambda x: abs(x["impacto"]), reverse=True)

    def escenarios(self) -> dict[str, float]:
        """Calcula probabilidades en escenarios pesimista, base y optimista."""
        evidencias_cargo = [e for e in self.evidencias if e.likelihood_ratio >= 1.0]
        evidencias_descargo = [e for e in self.evidencias if e.likelihood_ratio < 1.0]

        lr_pesimista = 1.0
        for e in self.evidencias:
            lr_pesimista *= max(e.likelihood_ratio, 1.0)
        prob_pesimista = self._odds_a_prob(self.odds_prior * lr_pesimista)

        lr_optimista = 1.0
        for e in self.evidencias:
            lr_optimista *= min(e.likelihood_ratio, 1.0)
        prob_optimista = self._odds_a_prob(self.odds_prior * lr_optimista)

        return {
            "pesimista": round(prob_pesimista, 4),
            "base": round(self.prob_posterior, 4),
            "optimista": round(prob_optimista, 4),
        }

    def calcular_batna_imputado(
        self,
        pena_maxima_años: float,
        costo_juicio: float,
        valor_año_libertad: float = 100_000,
    ) -> float:
        """
        Valor esperado del juicio para el imputado.
        Negativo = costo. El imputado prefiere el mínimo valor absoluto.
        """
        costo_condena = self.prob_posterior * (pena_maxima_años * valor_año_libertad)
        return -(costo_condena + costo_juicio)

    def recomendar_oferta_minima(
        self,
        pena_maxima_años: float,
        costo_juicio: float,
        valor_año_libertad: float = 100_000,
    ) -> float:
        """
        Pena máxima que el imputado debería aceptar en un acuerdo,
        expresada en años de pena efectiva equivalente.
        El imputado acepta si el acuerdo es mejor que el valor esperado del juicio.
        """
        batna = self.calcular_batna_imputado(pena_maxima_años, costo_juicio, valor_año_libertad)
        pena_equivalente_batna = abs(batna + costo_juicio) / valor_año_libertad
        return round(pena_equivalente_batna, 2)

    def generar_reporte(self) -> str:
        """Genera texto en Markdown del análisis completo."""
        p = self.prob_posterior
        escenarios = self.escenarios()
        sensibilidad = self.analisis_sensibilidad()
        p_pct = f"{p * 100:.1f}%"
        prior_pct = f"{self.prob_prior * 100:.1f}%"
        umbral_pct = f"{self.umbral_activo * 100:.0f}%"

        lineas = [
            f"# 📊 Análisis Bayesiano — {self.nombre_causa}",
            f"\n**RUC**: {self.ruc} | **Materia**: {self.materia} | **Generado**: automático",
            "\n---\n",
            "## Resultado Principal\n",
            f"| Métrica | Valor |",
            f"|---------|-------|",
            f"| **Probabilidad A Priori** | {prior_pct} |",
            f"| **Probabilidad A Posteriori** | **{p_pct}** |",
            f"| **Umbral del estándar de prueba** | {umbral_pct} |",
            f"| **¿Supera el umbral?** | {'⚠️ SÍ' if self.supera_umbral else '✅ NO'} |",
            f"| **Recomendación** | `{self.recomendacion}` |",
            "\n---\n",
            "## Evidencias Analizadas\n",
            "| N° | Evidencia | LR | Interpretación |",
            "|----|-----------|-----|----------------|",
        ]

        for i, e in enumerate(self.evidencias, 1):
            lr_str = f"{e.likelihood_ratio:.2f}" if e.likelihood_ratio != float('inf') else "∞"
            lineas.append(f"| {i} | {e.nombre} | {lr_str} | {e.interpretacion_lr} |")

        lineas += [
            "\n---\n",
            "## Cálculo Detallado\n",
            f"```",
            f"Odds Prior       = {self.odds_prior:.4f}",
            f"LR Total         = {self.lr_total:.4f}",
            f"Odds Posterior   = {self.odds_posterior:.4f}",
            f"P(Condena|E)     = {p:.4f} ({p_pct})",
            "```\n",
            "## Escenarios\n",
            "| Escenario | P(Condena) |",
            "|-----------|-----------|",
            f"| 🔴 Pesimista | {escenarios['pesimista'] * 100:.1f}% |",
            f"| 🟡 Base | **{escenarios['base'] * 100:.1f}%** |",
            f"| 🟢 Optimista | {escenarios['optimista'] * 100:.1f}% |",
            "\n---\n",
            "## Análisis de Sensibilidad\n",
            "*(Impacto de excluir cada evidencia)*\n",
            "| Evidencia | LR | P(Condena) sin ella | Impacto | ¿Crítica? |",
            "|-----------|-----|---------------------|---------|-----------|",
        ]

        for s in sensibilidad:
            critica = "🔴 Sí" if s["es_critica"] else "No"
            lineas.append(
                f"| {s['evidencia']} | {s['lr']} | {s['prob_sin_esta_evidencia'] * 100:.1f}% | "
                f"{s['impacto']:+.1%} | {critica} |"
            )

        lineas += [
            "\n---\n",
            f"## Recomendación: `{self.recomendacion.upper()}`\n",
        ]

        if self.recomendacion == "ir-a-juicio":
            lineas.append(
                "> ✅ La probabilidad de condena es suficientemente baja. "
                "Ir a juicio es la estrategia recomendada."
            )
        elif self.recomendacion == "salida-alternativa-urgente":
            lineas.append(
                "> 🔴 La probabilidad de condena es muy alta. "
                "Se recomienda con urgencia explorar salidas alternativas."
            )
        else:
            lineas.append(
                "> 🟡 La situación es intermedia. Evaluar opciones de negociación "
                "mientras se trabaja en mejorar la posición procesal."
            )

        return "\n".join(lineas)
