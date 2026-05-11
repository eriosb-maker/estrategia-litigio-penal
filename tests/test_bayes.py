"""Tests del motor Bayesiano."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from bayes import AnalisisBayesiano, Evidencia


def _causa_base(prior: float = 0.5) -> AnalisisBayesiano:
    return AnalisisBayesiano(
        nombre_causa="Test",
        ruc="2024-TEST",
        prob_prior=prior,
        materia="penal",
    )


def test_sin_evidencia_retorna_prior():
    analisis = _causa_base(0.6)
    assert abs(analisis.prob_posterior - 0.6) < 0.001


def test_evidencia_neutral_no_cambia_prob():
    analisis = _causa_base(0.5)
    analisis.agregar_evidencia(Evidencia(
        nombre="Neutral",
        descripcion="LR=1",
        prob_dado_culpable=0.5,
        prob_dado_inocente=0.5,
    ))
    assert abs(analisis.prob_posterior - 0.5) < 0.001


def test_evidencia_fuerte_aumenta_prob():
    analisis = _causa_base(0.5)
    analisis.agregar_evidencia(Evidencia(
        nombre="ADN",
        descripcion="LR alto",
        prob_dado_culpable=0.999,
        prob_dado_inocente=0.001,
    ))
    assert analisis.prob_posterior > 0.99


def test_evidencia_descargo_reduce_prob():
    analisis = _causa_base(0.8)
    analisis.agregar_evidencia(Evidencia(
        nombre="Coartada sólida",
        descripcion="LR < 1",
        prob_dado_culpable=0.10,
        prob_dado_inocente=0.90,
    ))
    assert analisis.prob_posterior < 0.8


def test_recomendacion_salida_alternativa_con_prob_alta():
    analisis = _causa_base(0.95)
    analisis.agregar_evidencia(Evidencia(
        nombre="Evidencia abrumadora",
        descripcion="",
        prob_dado_culpable=0.99,
        prob_dado_inocente=0.01,
    ))
    assert analisis.recomendacion == "salida-alternativa-urgente"


def test_recomendacion_juicio_con_prob_baja():
    analisis = _causa_base(0.15)
    analisis.agregar_evidencia(Evidencia(
        nombre="Evidencia débil",
        descripcion="",
        prob_dado_culpable=0.40,
        prob_dado_inocente=0.35,
    ))
    assert analisis.recomendacion == "ir-a-juicio"


def test_escenarios_orden():
    analisis = _causa_base(0.5)
    analisis.agregar_evidencia(Evidencia(
        nombre="Ev1",
        descripcion="",
        prob_dado_culpable=0.70,
        prob_dado_inocente=0.30,
    ))
    esc = analisis.escenarios()
    assert esc["pesimista"] >= esc["base"] >= esc["optimista"]


def test_sensibilidad_identifica_evidencia_critica():
    analisis = _causa_base(0.5)
    analisis.agregar_evidencia(Evidencia(
        nombre="ADN (LR=100)",
        descripcion="",
        prob_dado_culpable=0.999,
        prob_dado_inocente=0.01,
    ))
    analisis.agregar_evidencia(Evidencia(
        nombre="Testigo débil (LR=1.5)",
        descripcion="",
        prob_dado_culpable=0.60,
        prob_dado_inocente=0.40,
    ))
    sens = analisis.analisis_sensibilidad()
    assert sens[0]["evidencia"] == "ADN (LR=100)"
    assert sens[0]["es_critica"] is True


def test_lr_evidencia_inocente_infinita_no_crash():
    ev = Evidencia(
        nombre="Test",
        descripcion="",
        prob_dado_culpable=0.5,
        prob_dado_inocente=0.0,
    )
    assert ev.likelihood_ratio == float('inf')


def test_genera_reporte_markdown():
    analisis = _causa_base(0.6)
    analisis.agregar_evidencia(Evidencia(
        nombre="Testigo",
        descripcion="",
        prob_dado_culpable=0.7,
        prob_dado_inocente=0.3,
    ))
    reporte = analisis.generar_reporte()
    assert "Análisis Bayesiano" in reporte
    assert "Evidencias" in reporte
    assert "Recomendación" in reporte
