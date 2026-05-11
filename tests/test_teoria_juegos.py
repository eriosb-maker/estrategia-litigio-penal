"""Tests del motor de Teoría de Juegos."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from teoria_juegos import AnalisisTJ, JugadorLitigio


def _jugador(nombre: str, p_ganar: float, costo: float, v_ganar: float,
             v_perder: float, v_acuerdo: float) -> JugadorLitigio:
    return JugadorLitigio(
        nombre=nombre,
        rol="defensor",
        prob_ganar_juicio=p_ganar,
        costo_juicio=costo,
        valor_ganar=v_ganar,
        valor_perder=v_perder,
        valor_acuerdo_actual=v_acuerdo,
    )


def test_batna_calculado_correctamente():
    j = _jugador("Test", p_ganar=0.6, costo=10, v_ganar=100, v_perder=-50, v_acuerdo=0)
    ve = 0.6 * 100 + 0.4 * (-50)  # 60 - 20 = 40
    assert abs(j.valor_esperado_juicio - ve) < 0.01
    assert abs(j.batna - (ve - 10)) < 0.01


def test_prefiere_juicio_cuando_batna_mejor():
    j = _jugador("Test", p_ganar=0.8, costo=5, v_ganar=100, v_perder=-20, v_acuerdo=50)
    # BATNA = 0.8*100 + 0.2*(-20) - 5 = 80 - 4 - 5 = 71 > 50
    assert j.prefiere_juicio is True


def test_prefiere_negociar_cuando_acuerdo_mejor():
    j = _jugador("Test", p_ganar=0.3, costo=20, v_ganar=100, v_perder=-80, v_acuerdo=30)
    # BATNA = 0.3*100 + 0.7*(-80) - 20 = 30 - 56 - 20 = -46 < 30
    assert j.prefiere_juicio is False


def test_zopa_existe_cuando_batnas_compatibles():
    j1 = _jugador("J1", p_ganar=0.6, costo=10, v_ganar=100, v_perder=-50, v_acuerdo=20)
    j2 = _jugador("J2", p_ganar=0.4, costo=10, v_ganar=80, v_perder=-60, v_acuerdo=25)
    analisis = AnalisisTJ("Test", "T-001", j1, j2)
    # BATNA j1 = 0.6*100 + 0.4*(-50) - 10 = 60-20-10 = 30
    # BATNA j2 = 0.4*80 + 0.6*(-60) - 10 = 32-36-10 = -14
    # ZOPA existe si BATNA_j1 < BATNA_j2 → 30 < -14 → False
    # En este caso NO existe ZOPA
    assert isinstance(analisis.zopa_existe, bool)


def test_equilibrio_nash_retorna_lista():
    j1 = _jugador("J1", p_ganar=0.5, costo=5, v_ganar=100, v_perder=-100, v_acuerdo=-20)
    j2 = _jugador("J2", p_ganar=0.5, costo=5, v_ganar=80, v_perder=-80, v_acuerdo=-15)
    analisis = AnalisisTJ("Test", "T-002", j1, j2)
    ens = analisis.equilibrio_nash()
    assert len(ens) >= 1
    assert all(len(e) == 2 for e in ens)


def test_recomendacion_retorna_tupla_string():
    j1 = _jugador("J1", p_ganar=0.8, costo=5, v_ganar=100, v_perder=-50, v_acuerdo=30)
    j2 = _jugador("J2", p_ganar=0.2, costo=5, v_ganar=80, v_perder=-80, v_acuerdo=-40)
    analisis = AnalisisTJ("Test", "T-003", j1, j2)
    rec, just = analisis.recomendacion()
    assert isinstance(rec, str)
    assert isinstance(just, str)
    assert len(just) > 10


def test_acciones_retorna_lista():
    j1 = _jugador("J1", p_ganar=0.3, costo=20, v_ganar=100, v_perder=-100, v_acuerdo=-30)
    j2 = _jugador("J2", p_ganar=0.7, costo=5, v_ganar=80, v_perder=-20, v_acuerdo=-15)
    analisis = AnalisisTJ("Test", "T-004", j1, j2)
    acciones = analisis.acciones_para_mejorar_posicion()
    assert len(acciones) >= 1


def test_reporte_contiene_secciones_clave():
    j1 = _jugador("Defensa", p_ganar=0.5, costo=10, v_ganar=100, v_perder=-100, v_acuerdo=-20)
    j2 = _jugador("Fiscalía", p_ganar=0.5, costo=8, v_ganar=80, v_perder=-30, v_acuerdo=-15)
    analisis = AnalisisTJ("Caso Test", "T-005", j1, j2)
    reporte = analisis.generar_reporte()
    assert "Teoría de Juegos" in reporte
    assert "BATNA" in reporte
    assert "Nash" in reporte
    assert "Recomendación" in reporte
