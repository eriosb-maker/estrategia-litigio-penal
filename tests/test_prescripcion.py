# -*- coding: utf-8 -*-
"""Suite de control de la calculadora de prescripción (arts. 93-105 CP).

Cada caso indica la regla verificada que ejercita. Los casos de control
jurisprudenciales definidos por el abogado (p. ej., Roles 18.268-2025 y
4.825-2026, materia tributaria) se incorporarán cuando se aporten los
antecedentes de cada fallo; no se codifican de memoria.
"""

from datetime import date

import pytest

from src.prescripcion import (
    Ausencia,
    Categoria,
    Estado,
    Interrupcion,
    Suspension,
    limite_agravantes_reincidencia,
    prescripcion_accion,
    prescripcion_pena,
)


# --- Plazos del art. 94 CP ------------------------------------------------

class TestPlazosAccion:
    def test_simple_delito_cinco_anios_vigente_el_dia_previo(self):
        informe = prescripcion_accion(
            Categoria.SIMPLE_DELITO, date(2020, 1, 1), date(2024, 12, 31)
        )
        assert informe.estado is Estado.VIGENTE
        assert informe.fecha_cumplimiento == date(2025, 1, 1)

    def test_simple_delito_prescrito_al_enterarse_el_plazo(self):
        informe = prescripcion_accion(
            Categoria.SIMPLE_DELITO, date(2020, 1, 1), date(2025, 1, 1)
        )
        assert informe.estado is Estado.PRESCRITA

    def test_falta_seis_meses(self):
        informe = prescripcion_accion(
            Categoria.FALTA, date(2026, 1, 1), date(2026, 7, 1)
        )
        assert informe.fecha_cumplimiento == date(2026, 7, 1)
        assert informe.estado is Estado.PRESCRITA

    def test_crimen_diez_anios(self):
        informe = prescripcion_accion(
            Categoria.CRIMEN, date(2016, 7, 7), date(2026, 7, 6)
        )
        assert informe.fecha_cumplimiento == date(2026, 7, 7)
        assert informe.estado is Estado.VIGENTE

    def test_pena_perpetua_quince_anios(self):
        informe = prescripcion_accion(
            Categoria.PERPETUO, date(2010, 1, 1), date(2025, 1, 1)
        )
        assert informe.fecha_cumplimiento == date(2025, 1, 1)
        assert informe.estado is Estado.PRESCRITA


# --- Suspensión del art. 96 CP (formalización, art. 233 a) CPP) -----------

class TestSuspension:
    def test_formalizacion_suspende(self):
        informe = prescripcion_accion(
            Categoria.SIMPLE_DELITO,
            date(2020, 1, 1),
            date(2026, 1, 1),
            suspensiones=[Suspension(date(2023, 1, 1))],
        )
        assert informe.estado is Estado.SUSPENDIDA
        assert informe.fecha_cumplimiento is None

    def test_no_perseverar_deja_correr_retroactivamente(self):
        # Art. 248 letra c) CPP: continúa como si nunca se hubiere
        # interrumpido.
        informe = prescripcion_accion(
            Categoria.SIMPLE_DELITO,
            date(2020, 1, 1),
            date(2025, 6, 1),
            suspensiones=[Suspension(date(2023, 1, 1), sin_efecto=True)],
        )
        assert informe.estado is Estado.PRESCRITA
        assert informe.fecha_cumplimiento == date(2025, 1, 1)

    def test_suspension_posterior_al_plazo_no_obsta(self):
        informe = prescripcion_accion(
            Categoria.SIMPLE_DELITO,
            date(2020, 1, 1),
            date(2026, 1, 1),
            suspensiones=[Suspension(date(2025, 6, 1))],
        )
        assert informe.estado is Estado.PRESCRITA


# --- Interrupción del art. 96 CP ------------------------------------------

class TestInterrupcion:
    def test_nuevo_delito_reinicia_el_computo(self):
        informe = prescripcion_accion(
            Categoria.SIMPLE_DELITO,
            date(2020, 1, 1),
            date(2026, 1, 1),
            interrupciones=[Interrupcion(date(2022, 1, 1))],
        )
        assert informe.inicio_efectivo == date(2022, 1, 1)
        assert informe.fecha_cumplimiento == date(2027, 1, 1)
        assert informe.estado is Estado.VIGENTE

    def test_interrupcion_posterior_al_cumplimiento_se_ignora(self):
        informe = prescripcion_accion(
            Categoria.SIMPLE_DELITO,
            date(2020, 1, 1),
            date(2026, 1, 1),
            interrupciones=[Interrupcion(date(2025, 6, 1))],
        )
        assert informe.inicio_efectivo == date(2020, 1, 1)
        assert informe.estado is Estado.PRESCRITA


# --- Ausencia del territorio (art. 100 CP) ---------------------------------

class TestAusencia:
    def test_dos_dias_de_ausencia_cuentan_por_uno(self):
        informe = prescripcion_accion(
            Categoria.SIMPLE_DELITO,
            date(2020, 1, 1),
            date(2026, 1, 1),
            ausencias=[Ausencia(date(2021, 1, 1), date(2021, 1, 3))],
        )
        # 2 días de ausencia => 1 día de extensión.
        assert informe.fecha_cumplimiento == date(2025, 1, 2)

    def test_ausencia_prolongada(self):
        # 731 días ausente (2020-01-01 a 2022-01-01) => extensión de 366.
        informe = prescripcion_accion(
            Categoria.SIMPLE_DELITO,
            date(2020, 1, 1),
            date(2027, 1, 1),
            ausencias=[Ausencia(date(2020, 1, 1), date(2022, 1, 1))],
        )
        assert informe.fecha_cumplimiento == date(2025, 1, 1) + \
            (date(2026, 1, 2) - date(2025, 1, 1))
        assert informe.fecha_cumplimiento == date(2026, 1, 2)

    def test_ausencia_fuera_del_periodo_no_afecta(self):
        informe = prescripcion_accion(
            Categoria.SIMPLE_DELITO,
            date(2020, 1, 1),
            date(2026, 1, 1),
            ausencias=[Ausencia(date(2026, 1, 1), date(2026, 6, 1))],
        )
        assert informe.fecha_cumplimiento == date(2025, 1, 1)

    def test_ausencia_invalida(self):
        with pytest.raises(ValueError):
            Ausencia(date(2022, 1, 1), date(2021, 1, 1))


# --- Media prescripción (art. 103 CP) --------------------------------------

class TestMediaPrescripcion:
    def test_mitad_de_simple_delito_treinta_meses(self):
        informe = prescripcion_accion(
            Categoria.SIMPLE_DELITO, date(2020, 1, 1), date(2023, 1, 1)
        )
        assert informe.media_prescripcion_aplicable
        assert informe.fecha_media_prescripcion == date(2022, 7, 1)
        assert informe.media_prescripcion_alcanzada

    def test_mitad_no_alcanzada_si_suspende_antes(self):
        informe = prescripcion_accion(
            Categoria.SIMPLE_DELITO,
            date(2020, 1, 1),
            date(2026, 1, 1),
            suspensiones=[Suspension(date(2022, 1, 1))],
        )
        assert informe.estado is Estado.SUSPENDIDA
        assert not informe.media_prescripcion_alcanzada

    def test_no_aplica_a_faltas(self):
        informe = prescripcion_accion(
            Categoria.FALTA, date(2026, 1, 1), date(2026, 5, 1)
        )
        assert not informe.media_prescripcion_aplicable

    def test_mitad_de_perpetuo_siete_anios_y_medio(self):
        informe = prescripcion_accion(
            Categoria.PERPETUO, date(2018, 1, 1), date(2026, 1, 1)
        )
        assert informe.fecha_media_prescripcion == date(2025, 7, 1)
        assert informe.media_prescripcion_alcanzada


# --- Imprescriptibilidad (art. 94 bis CP) ----------------------------------

class TestImprescriptibilidad:
    def test_accion_imprescriptible(self):
        informe = prescripcion_accion(
            Categoria.CRIMEN,
            date(2000, 1, 1),
            date(2026, 1, 1),
            imprescriptible=True,
        )
        assert informe.estado is Estado.IMPRESCRIPTIBLE
        assert informe.fecha_cumplimiento is None


# --- Prescripción de la pena (arts. 97-99 CP) -------------------------------

class TestPrescripcionPena:
    def test_computa_desde_sentencia_de_termino(self):
        informe = prescripcion_pena(
            Categoria.SIMPLE_DELITO, date(2019, 3, 15), date(2024, 3, 15)
        )
        assert informe.fecha_cumplimiento == date(2024, 3, 15)
        assert informe.estado is Estado.PRESCRITA

    def test_interrupcion_por_nuevo_delito(self):
        informe = prescripcion_pena(
            Categoria.SIMPLE_DELITO,
            date(2019, 3, 15),
            date(2025, 1, 1),
            interrupciones=[Interrupcion(date(2021, 1, 1))],
        )
        assert informe.inicio_efectivo == date(2021, 1, 1)
        assert informe.estado is Estado.VIGENTE
        assert informe.fecha_cumplimiento == date(2026, 1, 1)


# --- Art. 104 CP ------------------------------------------------------------

class TestLimiteReincidencia:
    def test_crimen_diez_anios(self):
        assert limite_agravantes_reincidencia(
            Categoria.CRIMEN, date(2016, 5, 1)
        ) == date(2026, 5, 1)

    def test_simple_delito_cinco_anios(self):
        assert limite_agravantes_reincidencia(
            Categoria.SIMPLE_DELITO, date(2022, 5, 1)
        ) == date(2027, 5, 1)

    def test_falta_sin_regla(self):
        assert limite_agravantes_reincidencia(
            Categoria.FALTA, date(2022, 5, 1)
        ) is None
