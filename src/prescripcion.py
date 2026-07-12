#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Calculadora determinística de prescripción penal chilena.

Base normativa VERIFICADA (extractos XML oficiales de LeyChile, idNorma 1984,
curatoría 2026-07-06, en `references/marco-legal.md` de la skill
`analisis-penal-chile`):

    - Art. 93 CP: causales de extinción (N° 6 prescripción de la acción,
      N° 7 prescripción de la pena).
    - Art. 94 CP: plazos de prescripción de la acción penal (15 años penas
      perpetuas, 10 años demás crímenes, 5 años simples delitos, 6 meses
      faltas); pena compuesta: se está a la privativa de libertad y, a falta
      de ella, a la mayor.
    - Art. 94 bis CP: imprescriptibilidad de ciertos delitos sexuales contra
      menores de edad (la calificación de procedencia es del abogado).
    - Art. 95 CP: el término corre desde el día de comisión del delito.
    - Art. 96 CP: interrupción (nuevo crimen o simple delito, se pierde el
      tiempo transcurrido) y suspensión (desde que el procedimiento se dirige
      contra el responsable); si el procedimiento se paraliza por tres años o
      termina sin condena, la prescripción continúa como si no se hubiere
      interrumpido.
    - Art. 97 CP: plazos de prescripción de la pena (idénticos a los del 94).
    - Art. 98 CP: cómputo desde la sentencia de término o el quebrantamiento.
    - Art. 99 CP: interrupción de la prescripción de la pena por nuevo crimen
      o simple delito, sin perjuicio de que comience a correr otra vez.
    - Art. 100 CP: ausencia del territorio: se cuenta un día por cada dos de
      ausencia; no se consideran ausentes quienes estuvieron sujetos a
      prohibición o impedimento de ingreso (esos períodos NO deben informarse
      como ausencia a este motor).
    - Art. 102 CP: la prescripción se declara de oficio (el motor solo provee
      el cómputo).
    - Art. 103 CP: media prescripción (no aplicable a faltas ni a
      prescripciones especiales de corto tiempo).
    - Art. 104 CP: límite temporal de las agravantes del art. 12 N° 15 y 16.
    - Art. 233 letra a) CPP (verificado): la formalización suspende la
      prescripción conforme al art. 96 CP.
    - Art. 248 letra c) CPP (verificado): la decisión de no perseverar deja
      sin efecto la formalización y la prescripción «continuará corriendo
      como si nunca se hubiere interrumpido».

Convenciones computacionales (declaradas, sujetas al criterio del abogado):

    1. El plazo se computa con aritmética de calendario (`relativedelta`);
       la fecha de cumplimiento es el primer día en que el término se
       encuentra íntegramente transcurrido.
    2. En la regla del art. 100 CP cada día de ausencia aporta medio día de
       prescripción; el déficit resultante se redondea hacia arriba
       (criterio conservador: en caso de fracción, la prescripción se
       cumple un día después).
    3. El motor no captura prescripciones especiales de corto tiempo ni
       reglas de leyes especiales; su salida es un insumo auxiliar que
       jamás sustituye el cómputo definitivo del abogado (feriados, momento
       consumativo en delitos permanentes, continuados o de resultado
       separado).

Casos de control adicionales definidos por el abogado (por ejemplo, los
criterios de los Roles 18.268-2025 y 4.825-2026 en materia tributaria) deben
incorporarse a la suite de pruebas cuando se aporten los antecedentes; no se
codifican de memoria.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from datetime import date, timedelta
from enum import Enum
from typing import List, Optional

from dateutil.relativedelta import relativedelta


class Categoria(Enum):
    """Categoría de la pena para los plazos de los arts. 94 y 97 CP."""

    PERPETUO = "crimen con pena de presidio, reclusión o relegación perpetuos"
    CRIMEN = "demás crímenes"
    SIMPLE_DELITO = "simple delito"
    FALTA = "falta"


PLAZOS = {
    Categoria.PERPETUO: relativedelta(years=15),
    Categoria.CRIMEN: relativedelta(years=10),
    Categoria.SIMPLE_DELITO: relativedelta(years=5),
    Categoria.FALTA: relativedelta(months=6),
}

MITADES = {
    Categoria.PERPETUO: relativedelta(months=90),
    Categoria.CRIMEN: relativedelta(years=5),
    Categoria.SIMPLE_DELITO: relativedelta(months=30),
    Categoria.FALTA: relativedelta(months=3),
}


class Estado(Enum):
    VIGENTE = "vigente (no prescrita)"
    SUSPENDIDA = "suspendida (art. 96 CP)"
    PRESCRITA = "prescrita"
    IMPRESCRIPTIBLE = "imprescriptible (art. 94 bis CP)"


@dataclass(frozen=True)
class Ausencia:
    """Período de ausencia del territorio (art. 100 CP).

    No incluir períodos de prohibición o impedimento de ingreso dispuestos
    por la autoridad (art. 100 inc. 2° CP): esos días se cuentan íntegros.
    """

    inicio: date
    fin: date

    def __post_init__(self) -> None:
        if self.fin < self.inicio:
            raise ValueError("Ausencia con fin anterior al inicio")

    def dias_en(self, desde: date, hasta: date) -> int:
        """Días de ausencia comprendidos en [desde, hasta)."""
        ini = max(self.inicio, desde)
        fin = min(self.fin, hasta)
        return max(0, (fin - ini).days)


@dataclass(frozen=True)
class Suspension:
    """Suspensión del art. 96 CP (el procedimiento se dirige contra el
    responsable; típicamente la formalización, art. 233 letra a) CPP).

    `sin_efecto` se marca cuando el procedimiento se paralizó por tres años
    o terminó sin condena (art. 96 CP; art. 248 letra c) CPP): la
    prescripción continúa «como si no se hubiere interrumpido», es decir,
    la suspensión se ignora retroactivamente. La verificación del supuesto
    (paralización efectiva, no perseverar, sobreseimiento) es del abogado.
    """

    fecha: date
    motivo: str = "formalización de la investigación"
    sin_efecto: bool = False


@dataclass
class Interrupcion:
    """Interrupción por comisión de nuevo crimen o simple delito
    (arts. 96 y 99 CP). El motor asume acreditado el supuesto; la exigencia
    jurisprudencial de condena firme por el nuevo delito queda a criterio
    del abogado."""

    fecha: date
    descripcion: str = "nuevo crimen o simple delito"


@dataclass
class Informe:
    tipo: str
    categoria: Categoria
    fecha_inicio: date
    fecha_consulta: date
    estado: Estado
    fecha_cumplimiento: Optional[date]
    fecha_media_prescripcion: Optional[date]
    media_prescripcion_aplicable: bool
    media_prescripcion_alcanzada: bool
    inicio_efectivo: date
    notas: List[str] = field(default_factory=list)

    def resumen(self) -> str:
        lineas = [
            f"Prescripción de la {self.tipo} — {self.categoria.value}",
            f"Inicio del cómputo: {self.fecha_inicio.isoformat()} "
            f"(efectivo: {self.inicio_efectivo.isoformat()})",
            f"Estado al {self.fecha_consulta.isoformat()}: {self.estado.value}",
        ]
        if self.fecha_cumplimiento:
            lineas.append(
                f"Fecha de cumplimiento del plazo: "
                f"{self.fecha_cumplimiento.isoformat()}"
            )
        if self.media_prescripcion_aplicable and self.fecha_media_prescripcion:
            marca = "alcanzada" if self.media_prescripcion_alcanzada else "no alcanzada"
            lineas.append(
                f"Media prescripción (art. 103 CP): "
                f"{self.fecha_media_prescripcion.isoformat()} ({marca})"
            )
        lineas.extend(f"Nota: {n}" for n in self.notas)
        return "\n".join(lineas)


def _fin_plazo_con_ausencias(
    inicio: date, plazo: relativedelta, ausencias: List[Ausencia]
) -> date:
    """Fecha en que se entera el plazo, corregida por el art. 100 CP.

    Cada día de ausencia dentro del período aporta medio día de cómputo, de
    modo que el término se extiende en la mitad de los días de ausencia
    (redondeo hacia arriba). La extensión puede contener nuevas ausencias,
    por lo que se itera hasta el punto fijo.
    """
    fin = inicio + plazo
    while True:
        dias_ausencia = sum(a.dias_en(inicio, fin) for a in ausencias)
        deficit = math.ceil(dias_ausencia / 2)
        nuevo_fin = inicio + plazo + timedelta(days=deficit)
        if nuevo_fin == fin:
            return fin
        fin = nuevo_fin


def _computar(
    tipo: str,
    categoria: Categoria,
    fecha_inicio: date,
    fecha_consulta: date,
    interrupciones: List[Interrupcion],
    suspensiones: List[Suspension],
    ausencias: List[Ausencia],
    imprescriptible: bool,
) -> Informe:
    notas: List[str] = []

    if imprescriptible:
        return Informe(
            tipo=tipo,
            categoria=categoria,
            fecha_inicio=fecha_inicio,
            fecha_consulta=fecha_consulta,
            estado=Estado.IMPRESCRIPTIBLE,
            fecha_cumplimiento=None,
            fecha_media_prescripcion=None,
            media_prescripcion_aplicable=False,
            media_prescripcion_alcanzada=False,
            inicio_efectivo=fecha_inicio,
            notas=[
                "Acción declarada imprescriptible por el usuario conforme al "
                "art. 94 bis CP; la calificación del supuesto es del abogado."
            ],
        )

    plazo = PLAZOS[categoria]

    # Interrupciones (arts. 96 y 99 CP): se pierde el tiempo transcurrido y
    # el término comienza a correr de nuevo. Solo surten efecto las que
    # ocurren antes de enterarse el plazo en curso.
    inicio_efectivo = fecha_inicio
    for interrupcion in sorted(interrupciones, key=lambda i: i.fecha):
        fin_parcial = _fin_plazo_con_ausencias(inicio_efectivo, plazo, ausencias)
        if inicio_efectivo <= interrupcion.fecha < fin_parcial:
            inicio_efectivo = interrupcion.fecha
            notas.append(
                f"Interrupción el {interrupcion.fecha.isoformat()} "
                f"({interrupcion.descripcion}): se pierde el tiempo "
                "transcurrido (arts. 96/99 CP)."
            )
        else:
            notas.append(
                f"Interrupción informada el {interrupcion.fecha.isoformat()} "
                "no considerada: fuera del término en curso."
            )

    fecha_cumplimiento = _fin_plazo_con_ausencias(inicio_efectivo, plazo, ausencias)

    # Suspensión (art. 96 CP, solo prescripción de la acción): si una
    # suspensión vigente (no dejada sin efecto) comienza antes de enterarse
    # el plazo, éste no corre desde esa fecha.
    suspension_activa: Optional[Suspension] = None
    for suspension in sorted(suspensiones, key=lambda s: s.fecha):
        if suspension.sin_efecto:
            notas.append(
                f"Suspensión de {suspension.fecha.isoformat()} "
                f"({suspension.motivo}) dejada sin efecto: la prescripción "
                "continúa como si no se hubiere interrumpido "
                "(art. 96 CP; art. 248 letra c) CPP)."
            )
            continue
        if inicio_efectivo <= suspension.fecha < fecha_cumplimiento:
            suspension_activa = suspension
            notas.append(
                f"Suspensión desde el {suspension.fecha.isoformat()} "
                f"({suspension.motivo}), art. 96 CP en relación con el "
                "art. 233 letra a) CPP: el término no corre mientras subsista."
            )
            break

    # Media prescripción (art. 103 CP): mitad del término, con la misma
    # corrección por ausencia. No aplica a faltas ni a prescripciones de
    # corto tiempo. La suspensión del procedimiento no obsta al transcurso
    # ya cumplido; el motor informa la fecha en que la mitad quedó enterada.
    media_aplicable = categoria is not Categoria.FALTA
    fecha_media: Optional[date] = None
    media_alcanzada = False
    if media_aplicable:
        fecha_media = _fin_plazo_con_ausencias(
            inicio_efectivo, MITADES[categoria], ausencias
        )
        limite = (
            min(fecha_consulta, suspension_activa.fecha)
            if suspension_activa
            else fecha_consulta
        )
        media_alcanzada = fecha_media <= limite
    else:
        notas.append("Media prescripción no aplicable a faltas (art. 103 CP).")

    if suspension_activa is not None:
        estado = Estado.SUSPENDIDA
        fecha_cumplimiento_informada = None
        notas.append(
            "Mientras la suspensión subsista, el plazo no se entera; si el "
            "procedimiento se paraliza por tres años o termina sin condena, "
            "recalcular marcando la suspensión como sin efecto (art. 96 CP)."
        )
    else:
        fecha_cumplimiento_informada = fecha_cumplimiento
        estado = (
            Estado.PRESCRITA if fecha_consulta >= fecha_cumplimiento else Estado.VIGENTE
        )

    notas.append(
        "Cómputo auxiliar conforme a los arts. 93-105 CP verificados; el "
        "cómputo definitivo queda sujeto al criterio del abogado (art. 102 CP)."
    )

    return Informe(
        tipo=tipo,
        categoria=categoria,
        fecha_inicio=fecha_inicio,
        fecha_consulta=fecha_consulta,
        estado=estado,
        fecha_cumplimiento=fecha_cumplimiento_informada,
        fecha_media_prescripcion=fecha_media,
        media_prescripcion_aplicable=media_aplicable,
        media_prescripcion_alcanzada=media_alcanzada,
        inicio_efectivo=inicio_efectivo,
        notas=notas,
    )


def prescripcion_accion(
    categoria: Categoria,
    fecha_comision: date,
    fecha_consulta: date,
    interrupciones: Optional[List[Interrupcion]] = None,
    suspensiones: Optional[List[Suspension]] = None,
    ausencias: Optional[List[Ausencia]] = None,
    imprescriptible: bool = False,
) -> Informe:
    """Prescripción de la acción penal (arts. 94 a 96 CP).

    `fecha_comision`: día de comisión del delito (art. 95 CP); en delitos
    permanentes o continuados el momento consumativo lo fija el abogado.
    """
    return _computar(
        tipo="acción penal",
        categoria=categoria,
        fecha_inicio=fecha_comision,
        fecha_consulta=fecha_consulta,
        interrupciones=interrupciones or [],
        suspensiones=suspensiones or [],
        ausencias=ausencias or [],
        imprescriptible=imprescriptible,
    )


def prescripcion_pena(
    categoria: Categoria,
    fecha_sentencia_o_quebrantamiento: date,
    fecha_consulta: date,
    interrupciones: Optional[List[Interrupcion]] = None,
    ausencias: Optional[List[Ausencia]] = None,
) -> Informe:
    """Prescripción de la pena (arts. 97 a 99 CP).

    El cómputo corre desde la sentencia de término o desde el
    quebrantamiento de la condena (art. 98 CP). No existe suspensión para
    la prescripción de la pena; solo interrupción por nuevo crimen o simple
    delito (art. 99 CP).
    """
    return _computar(
        tipo="pena",
        categoria=categoria,
        fecha_inicio=fecha_sentencia_o_quebrantamiento,
        fecha_consulta=fecha_consulta,
        interrupciones=interrupciones or [],
        suspensiones=[],
        ausencias=ausencias or [],
        imprescriptible=False,
    )


def limite_agravantes_reincidencia(
    categoria_hecho_anterior: Categoria, fecha_hecho: date
) -> Optional[date]:
    """Art. 104 CP: las agravantes del art. 12 N° 15 y 16 no se consideran
    tratándose de crímenes después de diez años desde el hecho, ni después
    de cinco en los simples delitos. Devuelve la fecha desde la cual ya no
    pueden tomarse en cuenta (None para faltas, a las que no se refiere la
    regla)."""
    if categoria_hecho_anterior in (Categoria.PERPETUO, Categoria.CRIMEN):
        return fecha_hecho + relativedelta(years=10)
    if categoria_hecho_anterior is Categoria.SIMPLE_DELITO:
        return fecha_hecho + relativedelta(years=5)
    return None


if __name__ == "__main__":
    # Demostración mínima: simple delito cometido el 01-03-2020,
    # formalizado el 01-06-2023 y con decisión de no perseverar el
    # 01-06-2024.
    demo = prescripcion_accion(
        categoria=Categoria.SIMPLE_DELITO,
        fecha_comision=date(2020, 3, 1),
        fecha_consulta=date(2026, 7, 7),
        suspensiones=[
            Suspension(
                date(2023, 6, 1),
                sin_efecto=True,
                motivo="formalización dejada sin efecto por decisión "
                "de no perseverar (art. 248 letra c) CPP)",
            )
        ],
    )
    print(demo.resumen())
