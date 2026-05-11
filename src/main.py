#!/usr/bin/env python3
"""
Segundo Cerebro Legal — Motor de Análisis Estratégico
Para abogados en litigios penales y civiles.

Combina:
- Análisis Bayesiano de probabilidades de condena
- Teoría de Juegos para decisiones estratégicas
- Base de Conocimiento con búsqueda cruzada
- Generador de notas para vault Obsidian
"""

import json
import logging
from pathlib import Path
from typing import Optional

from bayes import AnalisisBayesiano, Evidencia
from teoria_juegos import AnalisisTJ, JugadorLitigio
from causa_manager import Causa, CausaManager
from knowledge_base import KnowledgeBase

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

VAULT_PATH = Path(__file__).parent.parent / "vault"


class SegundoCerebroLegal:
    """
    Sistema integrado de segundo cerebro para litigantes.

    Orquesta los motores de análisis bayesiano, teoría de juegos
    y la base de conocimiento, generando análisis exportables
    directamente al vault de Obsidian.
    """

    def __init__(self, vault_path: str | Path = VAULT_PATH):
        self.vault_path = Path(vault_path)
        self.manager = CausaManager(self.vault_path)
        self.kb = KnowledgeBase(self.vault_path)
        logger.info(f"Sistema inicializado. Vault: {self.vault_path}")

    def analisis_rapido(
        self,
        nombre_causa: str,
        ruc: str,
        prob_condena_inicial: float,
        evidencias: list[dict],
        pena_maxima_años: float,
        costo_juicio: float,
        valor_acuerdo_ofrecido: float,
        costo_juicio_contraparte: float = 0.0,
        materia: str = "penal",
    ) -> dict:
        """
        Análisis estratégico completo en un solo llamado.

        Args:
            nombre_causa: Nombre descriptivo del caso
            ruc: RUC o identificador de la causa
            prob_condena_inicial: Probabilidad a priori de condena (0.0-1.0)
            evidencias: Lista de dicts con keys: nombre, prob_dado_culpable,
                        prob_dado_inocente, tipo ('cargo'|'descargo')
            pena_maxima_años: Pena máxima posible en años (para penal)
                              o monto en disputa (para civil)
            costo_juicio: Costo total del juicio para nosotros
            valor_acuerdo_ofrecido: Valor del acuerdo actual en la mesa
                                    (negativo = costo para nosotros)
            costo_juicio_contraparte: Estimado del costo del juicio para ellos
            materia: 'penal' o 'civil'

        Returns:
            Diccionario con análisis completo y recomendaciones
        """
        # ─── ANÁLISIS BAYESIANO ──────────────────────────────────
        analisis_b = AnalisisBayesiano(
            nombre_causa=nombre_causa,
            ruc=ruc,
            prob_prior=prob_condena_inicial,
            materia=materia,
        )

        for ev_data in evidencias:
            analisis_b.agregar_evidencia(Evidencia(
                nombre=ev_data["nombre"],
                descripcion=ev_data.get("descripcion", ev_data["nombre"]),
                prob_dado_culpable=ev_data["prob_dado_culpable"],
                prob_dado_inocente=ev_data["prob_dado_inocente"],
                tipo=ev_data.get("tipo", "cargo"),
            ))

        p_condena = analisis_b.prob_posterior
        escenarios_b = analisis_b.escenarios()
        sensibilidad_b = analisis_b.analisis_sensibilidad()

        # ─── ANÁLISIS TEORÍA DE JUEGOS ───────────────────────────
        valor_año = 20_000_000  # CLP por año de libertad (valor de referencia)

        nosotros = JugadorLitigio(
            nombre="Nosotros",
            rol="defensor" if materia == "penal" else "demandado",
            prob_ganar_juicio=1 - p_condena,
            costo_juicio=costo_juicio,
            valor_ganar=pena_maxima_años * valor_año if materia == "penal" else pena_maxima_años,
            valor_perder=-(pena_maxima_años * valor_año) if materia == "penal" else -pena_maxima_años,
            valor_acuerdo_actual=valor_acuerdo_ofrecido,
        )

        contraparte = JugadorLitigio(
            nombre="Contraparte",
            rol="fiscalia" if materia == "penal" else "demandante",
            prob_ganar_juicio=p_condena,
            costo_juicio=costo_juicio_contraparte or costo_juicio * 0.5,
            valor_ganar=pena_maxima_años * valor_año * 0.4 if materia == "penal" else pena_maxima_años,
            valor_perder=-(costo_juicio * 0.3),
            valor_acuerdo_actual=-valor_acuerdo_ofrecido * 0.8,
        )

        analisis_tj = AnalisisTJ(
            nombre_causa=nombre_causa,
            ruc=ruc,
            jugador_nuestro=nosotros,
            jugador_contraparte=contraparte,
            materia=materia,
        )

        rec_tj, justificacion_tj = analisis_tj.recomendacion()
        equilibrios = analisis_tj.equilibrio_nash()

        # ─── SÍNTESIS ────────────────────────────────────────────
        rec_bayes = analisis_b.recomendacion
        coinciden = rec_bayes.startswith(rec_tj) or rec_tj.startswith(rec_bayes.split("-")[0])

        resultado = {
            "causa": nombre_causa,
            "ruc": ruc,
            "materia": materia,
            "bayesiano": {
                "prob_prior": round(prob_condena_inicial, 4),
                "prob_posterior": round(p_condena, 4),
                "lr_total": round(analisis_b.lr_total, 4),
                "escenarios": escenarios_b,
                "evidencia_mas_critica": sensibilidad_b[0]["evidencia"] if sensibilidad_b else None,
                "recomendacion": rec_bayes,
            },
            "teoria_juegos": {
                "batna_nuestro": round(nosotros.batna),
                "batna_contraparte": round(contraparte.batna),
                "zopa_existe": analisis_tj.zopa_existe,
                "equilibrio_nash": [list(e) for e in equilibrios],
                "recomendacion": rec_tj,
                "justificacion": justificacion_tj,
                "acciones": analisis_tj.acciones_para_mejorar_posicion(),
            },
            "sintesis": {
                "ambos_analis_coinciden": coinciden,
                "recomendacion_final": rec_bayes if coinciden else "evaluar-ambos-analisis",
                "nivel_riesgo": (
                    "bajo" if p_condena < 0.40 else
                    "medio" if p_condena < 0.65 else
                    "alto" if p_condena < 0.80 else
                    "muy-alto"
                ),
            },
        }

        return resultado

    def indexar_vault(self) -> dict:
        """Indexa el vault y retorna estadísticas."""
        n = self.kb.indexar()
        return {"notas_indexadas": n, **self.kb.estadisticas()}

    def buscar_conexiones(self, ruc: str) -> str:
        """Genera reporte de conexiones para una causa."""
        if not self.kb._indice:
            self.kb.indexar()
        return self.kb.reporte_conexiones(ruc)


def ejemplo_uso():
    """Ejemplo de uso del sistema con un caso ficticio."""
    sistema = SegundoCerebroLegal()

    resultado = sistema.analisis_rapido(
        nombre_causa="Robo con Intimidación — Ejemplo",
        ruc="2024-EJEMPLO-001",
        prob_condena_inicial=0.72,
        evidencias=[
            {
                "nombre": "Testigo ocular (condiciones deficientes)",
                "prob_dado_culpable": 0.65,
                "prob_dado_inocente": 0.25,
                "tipo": "cargo",
            },
            {
                "nombre": "Huella dactilar parcial",
                "prob_dado_culpable": 0.55,
                "prob_dado_inocente": 0.10,
                "tipo": "cargo",
            },
            {
                "nombre": "Coartada telefónica parcial",
                "prob_dado_culpable": 0.30,
                "prob_dado_inocente": 0.70,
                "tipo": "descargo",
            },
        ],
        pena_maxima_años=10,
        costo_juicio=5_000_000,
        valor_acuerdo_ofrecido=-20_000_000,
        materia="penal",
    )

    print(json.dumps(resultado, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    ejemplo_uso()
