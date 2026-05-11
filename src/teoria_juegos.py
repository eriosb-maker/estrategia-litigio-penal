"""
Motor de Teoría de Juegos para Litigio Legal
Implementa modelos de equilibrio de Nash, análisis de negociación y
cálculo de BATNA para causas penales y civiles.
"""

from dataclasses import dataclass, field
from typing import Optional
from enum import Enum


class Estrategia(str, Enum):
    JUICIO = "juicio"
    NEGOCIAR = "negociar"
    SALIDA_ALTERNATIVA = "salida_alternativa"


@dataclass
class JugadorLitigio:
    """Representa a un jugador en el juego del litigio."""
    nombre: str
    rol: str  # "defensa" | "fiscalia" | "demandante" | "demandado"

    # Parámetros del juicio
    prob_ganar_juicio: float       # Probabilidad estimada de ganar en juicio
    costo_juicio: float            # Costo monetario del juicio (honorarios, tiempo, etc.)
    valor_ganar: float             # Valor de ganar en juicio (pena evitada, monto ganado, etc.)
    valor_perder: float            # Valor de perder en juicio (negativo = costo)

    # Parámetros de negociación
    valor_acuerdo_actual: float    # Valor del acuerdo que está sobre la mesa (o 0 si no hay)
    costo_emocional_juicio: float = 0.0  # Costo no monetario (reputación, estrés, tiempo)

    @property
    def valor_esperado_juicio(self) -> float:
        """Valor esperado puro del juicio (sin costos)."""
        return (self.prob_ganar_juicio * self.valor_ganar +
                (1 - self.prob_ganar_juicio) * self.valor_perder)

    @property
    def valor_neto_juicio(self) -> float:
        """Valor esperado del juicio neto de todos los costos."""
        return self.valor_esperado_juicio - self.costo_juicio - self.costo_emocional_juicio

    @property
    def prefiere_juicio(self) -> bool:
        """¿Prefiere ir a juicio respecto al acuerdo actual?"""
        return self.valor_neto_juicio > self.valor_acuerdo_actual

    @property
    def batna(self) -> float:
        """Best Alternative To Negotiated Agreement = valor neto del juicio."""
        return self.valor_neto_juicio


@dataclass
class MatrizPagos:
    """
    Matriz 2×2 de pagos para el juego del litigio.

    Estrategias: Juicio vs. Negociar
    Formato: (pago_jugador1, pago_jugador2)
    """
    jugador1: JugadorLitigio
    jugador2: JugadorLitigio
    # Pagos cuando ambos van a juicio
    pago_j1_juicio_juicio: float = 0.0
    pago_j2_juicio_juicio: float = 0.0
    # Pagos cuando j1 va a juicio, j2 negocia
    pago_j1_juicio_negocia: float = 0.0
    pago_j2_juicio_negocia: float = 0.0
    # Pagos cuando j1 negocia, j2 va a juicio
    pago_j1_negocia_juicio: float = 0.0
    pago_j2_negocia_juicio: float = 0.0
    # Pagos cuando ambos negocian (llegan a acuerdo)
    pago_j1_negocia_negocia: float = 0.0
    pago_j2_negocia_negocia: float = 0.0

    @classmethod
    def desde_jugadores(cls, j1: JugadorLitigio, j2: JugadorLitigio) -> "MatrizPagos":
        """Construye la matriz de pagos a partir de los parámetros de los jugadores."""
        m = cls(jugador1=j1, jugador2=j2)
        # Ambos van a juicio: reciben su valor neto esperado
        m.pago_j1_juicio_juicio = j1.valor_neto_juicio
        m.pago_j2_juicio_juicio = j2.valor_neto_juicio
        # j1 va a juicio, j2 negocia: j1 obtiene valor del juicio, j2 queda sin acuerdo ni juicio
        m.pago_j1_juicio_negocia = j1.valor_neto_juicio
        m.pago_j2_juicio_negocia = j2.valor_neto_juicio * 0.8  # j2 negocia en desventaja
        # j1 negocia, j2 va a juicio: simétricamente opuesto
        m.pago_j1_negocia_juicio = j1.valor_neto_juicio * 0.8
        m.pago_j2_negocia_juicio = j2.valor_neto_juicio
        # Ambos negocian: reciben el valor del acuerdo (sin costo del juicio)
        m.pago_j1_negocia_negocia = j1.valor_acuerdo_actual
        m.pago_j2_negocia_negocia = j2.valor_acuerdo_actual
        return m


@dataclass
class AnalisisTJ:
    """
    Análisis completo de Teoría de Juegos para una causa.

    Calcula equilibrios de Nash, ZOPA, y recomienda estrategia óptima.
    """
    nombre_causa: str
    ruc: str
    jugador_nuestro: JugadorLitigio
    jugador_contraparte: JugadorLitigio
    tipo_juego: str = "secuencial"  # "simultaneo" | "secuencial"
    materia: str = "penal"

    def __post_init__(self):
        self._matriz = MatrizPagos.desde_jugadores(
            self.jugador_nuestro, self.jugador_contraparte
        )

    @property
    def zopa_existe(self) -> bool:
        """
        Zona de Posible Acuerdo: existe si el mínimo aceptable del que pide
        es menor que el máximo que pagaría el otro.
        """
        return self.jugador_nuestro.batna < self.jugador_contraparte.batna

    @property
    def punto_nash_negociacion(self) -> Optional[float]:
        """
        Punto de acuerdo según el modelo Nash de negociación.
        Maximiza el producto de las ganancias sobre el BATNA.
        El acuerdo se divide entre BATNAs proporcional al punto medio.
        """
        if not self.zopa_existe:
            return None
        batna_n = self.jugador_nuestro.batna
        batna_c = self.jugador_contraparte.batna
        # El acuerdo Nash divide el excedente igualmente
        excedente_total = batna_n + batna_c
        return excedente_total / 2

    def estrategia_dominante_nuestro(self) -> Optional[str]:
        """Identifica si el jugador nuestro tiene estrategia dominante."""
        m = self._matriz
        juicio_mejor = (
            m.pago_j1_juicio_juicio >= m.pago_j1_negocia_juicio and
            m.pago_j1_juicio_negocia >= m.pago_j1_negocia_negocia
        )
        negociar_mejor = (
            m.pago_j1_negocia_juicio >= m.pago_j1_juicio_juicio and
            m.pago_j1_negocia_negocia >= m.pago_j1_juicio_negocia
        )
        if juicio_mejor:
            return "juicio"
        elif negociar_mejor:
            return "negociar"
        return None

    def estrategia_dominante_contraparte(self) -> Optional[str]:
        """Identifica si la contraparte tiene estrategia dominante."""
        m = self._matriz
        juicio_mejor = (
            m.pago_j2_juicio_juicio >= m.pago_j2_juicio_negocia and
            m.pago_j2_negocia_juicio >= m.pago_j2_negocia_negocia
        )
        negociar_mejor = (
            m.pago_j2_juicio_negocia >= m.pago_j2_juicio_juicio and
            m.pago_j2_negocia_negocia >= m.pago_j2_negocia_juicio
        )
        if juicio_mejor:
            return "juicio"
        elif negociar_mejor:
            return "negociar"
        return None

    def equilibrio_nash(self) -> list[tuple[str, str]]:
        """
        Encuentra todos los equilibrios de Nash en estrategias puras.
        Un EN es un perfil donde ningún jugador puede mejorar desviándose unilateralmente.
        """
        m = self._matriz
        equilibrios = []

        # Verificar (Juicio, Juicio)
        j1_no_desvia = m.pago_j1_juicio_juicio >= m.pago_j1_negocia_juicio
        j2_no_desvia = m.pago_j2_juicio_juicio >= m.pago_j2_juicio_negocia
        if j1_no_desvia and j2_no_desvia:
            equilibrios.append(("juicio", "juicio"))

        # Verificar (Juicio, Negociar)
        j1_no_desvia = m.pago_j1_juicio_negocia >= m.pago_j1_negocia_negocia
        j2_no_desvia = m.pago_j2_juicio_negocia >= m.pago_j2_juicio_juicio
        if j1_no_desvia and j2_no_desvia:
            equilibrios.append(("juicio", "negociar"))

        # Verificar (Negociar, Juicio)
        j1_no_desvia = m.pago_j1_negocia_juicio >= m.pago_j1_juicio_juicio
        j2_no_desvia = m.pago_j2_negocia_juicio >= m.pago_j2_negocia_negocia
        if j1_no_desvia and j2_no_desvia:
            equilibrios.append(("negociar", "juicio"))

        # Verificar (Negociar, Negociar)
        j1_no_desvia = m.pago_j1_negocia_negocia >= m.pago_j1_juicio_negocia
        j2_no_desvia = m.pago_j2_negocia_negocia >= m.pago_j2_negocia_juicio
        if j1_no_desvia and j2_no_desvia:
            equilibrios.append(("negociar", "negociar"))

        return equilibrios if equilibrios else [("indefinido", "indefinido")]

    def recomendacion(self) -> tuple[str, str]:
        """
        Recomendación estratégica basada en el análisis.
        Retorna (estrategia_recomendada, justificacion).
        """
        n = self.jugador_nuestro
        c = self.jugador_contraparte
        ens = self.equilibrio_nash()

        if n.prefiere_juicio and not c.prefiere_juicio:
            return ("juicio", "Tenemos ventaja: preferimos juicio y ellos prefieren negociar. "
                    "Desde esta posición de fuerza, negociar puede rendir mejores términos.")

        if not n.prefiere_juicio and c.prefiere_juicio:
            return ("negociar", "Ellos prefieren juicio; debemos buscar acuerdo urgentemente "
                    "mientras mejoramos nuestra posición procesal.")

        if n.prefiere_juicio and c.prefiere_juicio:
            return ("juicio", "Ambas partes prefieren juicio: probable que el caso llegue a juicio. "
                    "Preparar juicio a fondo.")

        if not n.prefiere_juicio and not c.prefiere_juicio:
            return ("negociar", "Ambas partes prefieren negociar: hay condiciones para un acuerdo "
                    "beneficioso para ambos. Iniciar conversaciones de inmediato.")

        return ("evaluar", "Situación compleja. Realizar más análisis antes de decidir.")

    def acciones_para_mejorar_posicion(self) -> list[str]:
        """Sugerencias para mejorar la posición negociadora."""
        acciones = []
        n = self.jugador_nuestro
        c = self.jugador_contraparte

        if n.prob_ganar_juicio < 0.5:
            acciones.append(
                "Obtener nueva evidencia o peritos que mejoren P(ganar juicio) "
                f"(actual: {n.prob_ganar_juicio:.0%})"
            )
        if n.costo_juicio > c.costo_juicio * 1.5:
            acciones.append(
                "Nuestros costos de juicio son significativamente mayores. "
                "Considerar litigación más eficiente o gestión de la causa."
            )
        if not self.zopa_existe:
            acciones.append(
                "No existe ZOPA actual. Para crearla: aumentar la percepción de riesgo de la "
                "contraparte o reducir nuestras expectativas mínimas de acuerdo."
            )
        if c.prob_ganar_juicio > 0.7:
            acciones.append(
                "La contraparte tiene alta confianza en ganar. Buscar evidencia que genere duda "
                "sobre su probabilidad de éxito."
            )
        if not acciones:
            acciones.append("Posición sólida. Mantener estrategia actual.")
        return acciones

    def generar_reporte(self) -> str:
        """Genera texto en Markdown del análisis completo."""
        n = self.jugador_nuestro
        c = self.jugador_contraparte
        ens = self.equilibrio_nash()
        rec, justificacion = self.recomendacion()
        acciones = self.acciones_para_mejorar_posicion()

        en_str = ", ".join(f"({e[0].upper()} / {e[1].upper()})" for e in ens)
        zopa_str = "✅ Existe" if self.zopa_existe else "❌ No existe"

        lineas = [
            f"# 🎮 Análisis Teoría de Juegos — {self.nombre_causa}",
            f"\n**RUC**: {self.ruc} | **Materia**: {self.materia}",
            "\n---\n",
            "## Jugadores\n",
            f"| Parámetro | {n.nombre} (Nosotros) | {c.nombre} (Contraparte) |",
            f"|-----------|{'─'*20}|{'─'*20}|",
            f"| P(Ganar Juicio) | {n.prob_ganar_juicio:.0%} | {c.prob_ganar_juicio:.0%} |",
            f"| Valor Esperado Juicio | {n.valor_esperado_juicio:,.0f} | {c.valor_esperado_juicio:,.0f} |",
            f"| Costo del Juicio | {n.costo_juicio:,.0f} | {c.costo_juicio:,.0f} |",
            f"| **BATNA (Valor Neto Juicio)** | **{n.batna:,.0f}** | **{c.batna:,.0f}** |",
            f"| Valor Acuerdo Actual | {n.valor_acuerdo_actual:,.0f} | {c.valor_acuerdo_actual:,.0f} |",
            f"| ¿Prefiere Juicio? | {'SÍ' if n.prefiere_juicio else 'NO'} | {'SÍ' if c.prefiere_juicio else 'NO'} |",
            "\n---\n",
            "## Matriz de Pagos\n",
            "```",
            f"                          {c.nombre}",
            f"                    Juicio      Negociar",
            f"{n.nombre:12s} Juicio │ ({n.valor_neto_juicio:+.0f}, {c.valor_neto_juicio:+.0f}) │ ({n.valor_neto_juicio:+.0f}, {c.valor_acuerdo_actual:+.0f}) │",
            f"             Negocia│ ({n.valor_acuerdo_actual:+.0f}, {c.valor_neto_juicio:+.0f}) │ ({n.valor_acuerdo_actual:+.0f}, {c.valor_acuerdo_actual:+.0f}) │",
            "```\n",
            "## Equilibrio(s) de Nash\n",
            f"**{en_str}**\n",
            "## Zona de Posible Acuerdo (ZOPA)\n",
            f"**{zopa_str}**\n",
        ]

        if self.zopa_existe:
            punto_nash = self.punto_nash_negociacion
            lineas.append(
                f"Punto de acuerdo Nash (división equitativa del excedente): {punto_nash:,.0f}\n"
            )

        lineas += [
            "## Estrategia Dominante\n",
            f"- **Nosotros**: {self.estrategia_dominante_nuestro() or 'Ninguna (depende de la contraparte)'}",
            f"- **Contraparte**: {self.estrategia_dominante_contraparte() or 'Ninguna'}",
            "\n---\n",
            f"## Recomendación: `{rec.upper()}`\n",
            f"> {justificacion}\n",
            "## Acciones para Mejorar Posición\n",
        ]
        for i, a in enumerate(acciones, 1):
            lineas.append(f"{i}. {a}")

        return "\n".join(lineas)
