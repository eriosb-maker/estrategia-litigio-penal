# -*- coding: utf-8 -*-
"""Casos dorados — suite de regresión de los motores deterministas.

Propósito (línea V del plan de mejoras, sesión de reconciliación 2026-07-12):
detectar regresiones de comportamiento entre versiones de `prescripcion.py`
y `estrategia_litigio.py` mediante escenarios fácticos íntegramente
FICTICIOS, con resultado esperado fijado por ejecución de control y
fundamento normativo declarado caso a caso. Estos casos NO validan criterio
jurídico nuevo: fijan el comportamiento ya verificado de los motores como
línea de base, de modo que cualquier divergencia futura sea detectable de
inmediato en CI.

Disciplina de higiene: ningún caso contiene datos de causas reales, RUC/RIT
reales ni nombres de personas naturales. Los identificadores «CASO-DORADO-N»
son puramente sintéticos.

Regla de mantenimiento: un cambio deliberado de criterio jurídico que altere
el resultado esperado de un caso dorado es, por definición, un «cambio de
criterio» (SKILL.md, sección 15.3.b) y requiere aprobación expresa del
titular antes de actualizar el valor esperado en este archivo.
"""

from datetime import date

import pytest

from src.prescripcion import (
    Ausencia,
    Categoria,
    Estado,
    Interrupcion,
    Suspension,
    prescripcion_accion,
)

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "skill", "scripts"))
from estrategia_litigio import Parametros, analizar  # noqa: E402


class TestCasoDoradoA_SimpleDelitoSinIncidencias:
    """Caso dorado A — prescripción de acción por simple delito, sin
    interrupción ni suspensión (arts. 94 N° 3 y 95 CP).

    Hecho ficticio: administración desleal simple (art. 470 N° 11 CP,
    hipótesis de simple delito) cometida el 15-01-2020. Sin formalización.
    Consulta al 12-07-2026: transcurridos más de cinco años sin incidencia
    alguna que altere el cómputo.
    """

    def test_prescripcion_cumplida_a_los_cinco_anios(self):
        informe = prescripcion_accion(
            Categoria.SIMPLE_DELITO, date(2020, 1, 15), date(2026, 7, 12)
        )
        assert informe.estado == Estado.PRESCRITA
        assert informe.fecha_cumplimiento == date(2025, 1, 15)

    def test_media_prescripcion_alcanzada_a_los_dos_anios_y_medio(self):
        informe = prescripcion_accion(
            Categoria.SIMPLE_DELITO, date(2020, 1, 15), date(2026, 7, 12)
        )
        assert informe.media_prescripcion_alcanzada is True
        assert informe.fecha_media_prescripcion == date(2022, 7, 15)


class TestCasoDoradoB_CrimenConFormalizacionSuspensiva:
    """Caso dorado B — suspensión por formalización (art. 96 CP, en
    relación con el art. 233 letra a) CPP).

    Hecho ficticio: figura culposa de lavado de activos (art. 27 inciso
    cuarto Ley 19.913, hipótesis de crimen) cometida el 01-01-2018.
    Formalización el 10-01-2024, antes del vencimiento del plazo decenal
    (que habría operado el 01-01-2028 de no mediar la suspensión). Al
    12-07-2026 el procedimiento permanece activo: la acción no puede estar
    prescrita mientras la suspensión no cese.
    """

    def test_suspension_impide_computo_de_cumplimiento(self):
        susp = Suspension(fecha=date(2024, 1, 10), sin_efecto=False)
        informe = prescripcion_accion(
            Categoria.CRIMEN, date(2018, 1, 1), date(2026, 7, 12), suspensiones=[susp]
        )
        assert informe.estado == Estado.SUSPENDIDA
        assert informe.fecha_cumplimiento is None

    def test_cese_de_la_suspension_por_no_perseverar_reactiva_el_computo(self):
        """Art. 96 CP en relación con el art. 248 letra c) CPP: si el
        procedimiento termina sin condena, la prescripción continúa
        «como si no se hubiere interrumpido» — la suspensión se ignora
        retroactivamente (`sin_efecto=True`)."""
        susp = Suspension(fecha=date(2024, 1, 10), sin_efecto=True)
        informe = prescripcion_accion(
            Categoria.CRIMEN, date(2018, 1, 1), date(2026, 7, 12), suspensiones=[susp]
        )
        assert informe.estado == Estado.VIGENTE
        assert informe.fecha_cumplimiento == date(2028, 1, 1)


class TestCasoDoradoC_AusenciaDelTerritorio:
    """Caso dorado C — ausencia del territorio (art. 100 CP: un día de
    prescripción por cada dos de ausencia).

    Hecho ficticio: estafa simple (art. 467 CP, hipótesis de simple
    delito) cometida el 01-01-2020. El imputado permanece fuera del
    territorio nacional entre el 01-01-2021 y el 01-01-2023 (730 días),
    lo que aporta 365 días de prescripción y desplaza el vencimiento del
    plazo quinquenal (que habría operado el 01-01-2025) en un año.
    """

    def test_ausencia_extiende_el_plazo_en_un_anio(self):
        aus = Ausencia(inicio=date(2021, 1, 1), fin=date(2023, 1, 1))
        informe = prescripcion_accion(
            Categoria.SIMPLE_DELITO, date(2020, 1, 1), date(2026, 7, 12), ausencias=[aus]
        )
        assert informe.estado == Estado.PRESCRITA
        assert informe.fecha_cumplimiento == date(2026, 1, 1)
        assert informe.media_prescripcion_alcanzada is True
        assert informe.fecha_media_prescripcion == date(2023, 7, 1)


class TestCasoDoradoD_InterrupcionPorNuevoDelito:
    """Caso dorado D — interrupción por nuevo crimen o simple delito
    (arts. 96 y 99 CP): se pierde íntegramente el tiempo transcurrido y el
    cómputo se reinicia desde la fecha del nuevo hecho.

    Hecho ficticio: apropiación indebida (simple delito) cometida el
    01-01-2015. El 01-06-2019 el mismo imputado comete un nuevo simple
    delito, lo que interrumpe el cómputo. El plazo quinquenal se reinicia
    desde esa fecha y se cumple el 01-06-2024, con más de dos años de
    holgura respecto de la fecha de consulta.
    """

    def test_interrupcion_reinicia_el_computo(self):
        interr = Interrupcion(fecha=date(2019, 6, 1))
        informe = prescripcion_accion(
            Categoria.SIMPLE_DELITO,
            date(2015, 1, 1),
            date(2026, 7, 12),
            interrupciones=[interr],
        )
        assert informe.inicio_efectivo == date(2019, 6, 1)
        assert informe.estado == Estado.PRESCRITA
        assert informe.fecha_cumplimiento == date(2024, 6, 1)


class TestCasoDoradoE_PuntoDeEquilibrioEstrategico:
    """Caso dorado E — motor de estrategia de litigio: punto de equilibrio
    entre juicio oral y procedimiento abreviado (arts. 237, 241 y 406 CPP).

    Escenario ficticio de defensa con probabilidad de condena estimada en
    0.65, pena probable de 5 años en caso de condena, oferta de abreviado
    de 3 años, bien jurídico patrimonial disponible y sin condenas previas.
    Fija como línea de base: (a) el acuerdo reparatorio resulta viable
    prima facie y la suspensión condicional y el abreviado no lo son, dado
    el umbral de pena; y (b) el punto de equilibrio de exposición esperada
    se sitúa en 0.60 de probabilidad de condena, por debajo del escenario
    planteado.
    """

    @staticmethod
    def _parametros():
        return Parametros(
            caso="CASO-DORADO-E",
            perspectiva="defensa",
            prob_condena=0.65,
            pena_probable_anios=5.0,
            pena_solicitada_anios=8.0,
            condenas_previas=False,
            suspension_vigente=False,
            bien_juridico_disponible=True,
            costo_juicio=25_000_000,
            costo_salida=6_000_000,
            oferta_abreviado_anios=3.0,
            prob_sustitutiva_en_condena=0.3,
        )

    def test_viabilidad_prima_facie_de_salidas(self):
        resultado = analizar(self._parametros())
        salidas = resultado["viabilidad_salidas_procesales"]
        assert salidas["suspension_condicional_art237_cpp"]["procede_prima_facie"] is False
        assert salidas["acuerdo_reparatorio_art241_cpp"]["procede_prima_facie"] is True
        assert salidas["procedimiento_abreviado_art406_cpp"]["procede_prima_facie"] is False

    def test_punto_de_equilibrio_y_exposicion_esperada(self):
        resultado = analizar(self._parametros())
        ve = resultado["valor_esperado"]
        assert ve["prob_condena_de_equilibrio"] == pytest.approx(0.60)
        assert ve["exposicion_penal_esperada_juicio_anios"] == pytest.approx(3.25)
        assert ve["diferencial_abreviado_vs_juicio_anios"] == pytest.approx(-0.25)
