#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Estrategia de Litigio Penal — Motor determinista de decisión.
Skill: analisis-penal-chile (v3.2). Origen conceptual: repositorio
eriosb-maker/estrategia-litigio-penal, reimplementado con lógica analítica real.

ADVERTENCIA: Este script produce un insumo cuantitativo auxiliar. No sustituye
el criterio del abogado ni la decisión informada del cliente. Los umbrales
normativos incluidos (arts. 237, 241 y 406 y ss. CPP) deben verificarse contra
el texto legal vigente antes de fundar en ellos cualquier decisión.

Uso:
    python estrategia_litigio.py --json '<parámetros>'
    python estrategia_litigio.py --demo
"""

import argparse
import json
import sys
from dataclasses import dataclass, asdict
from typing import Optional


@dataclass
class Parametros:
    caso: str                       # identificador (RUC/RIT o nombre de trabajo)
    perspectiva: str                # "defensa" | "querellante" | "fiscal"
    prob_condena: float             # probabilidad estimada de condena en juicio oral [0-1]
    pena_probable_anios: float      # pena concreta probable en caso de condena (años)
    pena_solicitada_anios: Optional[float] = None  # pena requerida por el MP (para abreviado)
    condenas_previas: bool = False  # condena anterior por crimen o simple delito
    suspension_vigente: bool = False
    bien_juridico_disponible: bool = False  # patrimonial disponible / lesiones menos graves / culposo
    costo_juicio: float = 0.0       # costo económico total estimado del juicio oral
    costo_salida: float = 0.0       # costo de la salida alternativa (reparación, condiciones)
    oferta_abreviado_anios: Optional[float] = None  # pena ofrecida/esperable en abreviado
    prob_sustitutiva_en_condena: float = 0.0  # prob. de pena sustitutiva (Ley 18.216) si hay condena


def _viabilidad_salidas(p: Parametros) -> dict:
    """Filtros de procedencia legal — VERIFICAR texto vigente antes de decidir."""
    return {
        "suspension_condicional_art237_cpp": {
            "procede_prima_facie": (
                p.pena_probable_anios <= 3
                and not p.condenas_previas
                and not p.suspension_vigente
            ),
            "requisitos": [
                "pena probable no superior a 3 años (art. 237 letra a) CPP)",
                "sin condena previa por crimen o simple delito (letra b)",
                "sin suspensión condicional vigente (letra c)",
            ],
            "nota": "Verificar hipótesis de improcedencia y audiencia con presencia "
                    "del fiscal regional cuando la ley lo exige.",
        },
        "acuerdo_reparatorio_art241_cpp": {
            "procede_prima_facie": p.bien_juridico_disponible,
            "requisitos": [
                "bien jurídico disponible de carácter patrimonial, lesiones menos "
                "graves o delito culposo (art. 241 inc. 2° CPP)",
                "consentimiento libre e informado de la víctima",
            ],
            "nota": "Verificar exclusiones legales según el tipo penal concreto.",
        },
        "procedimiento_abreviado_art406_cpp": {
            "procede_prima_facie": (
                p.pena_solicitada_anios is not None and p.pena_solicitada_anios <= 5
            ),
            "requisitos": [
                "pena solicitada no superior a 5 años de presidio o reclusión "
                "menor en su grado máximo (art. 406 CPP; umbral ampliado para "
                "ciertos delitos contra la propiedad — verificar)",
                "aceptación de hechos y antecedentes por el imputado",
            ],
            "nota": "El umbral ampliado (Ley 20.931) y las reglas especiales de la "
                    "Ley 21.595 deben verificarse para el delito concreto.",
        },
    }


def _valor_esperado(p: Parametros) -> dict:
    """Comparación de valor esperado entre juicio oral y salidas negociadas.
    Convención: valores expresados como 'años-equivalentes de exposición penal'
    y costos monetarios separados; no se agregan magnitudes heterogéneas."""
    exposicion_juicio = p.prob_condena * p.pena_probable_anios
    exposicion_efectiva_juicio = exposicion_juicio * (1 - p.prob_sustitutiva_en_condena)

    resultado = {
        "exposicion_penal_esperada_juicio_anios": round(exposicion_juicio, 3),
        "exposicion_privativa_esperada_juicio_anios": round(exposicion_efectiva_juicio, 3),
        "costo_economico_juicio": p.costo_juicio,
    }
    if p.oferta_abreviado_anios is not None:
        resultado["exposicion_abreviado_anios"] = p.oferta_abreviado_anios
        resultado["diferencial_abreviado_vs_juicio_anios"] = round(
            p.oferta_abreviado_anios - exposicion_juicio, 3
        )
        # Probabilidad de condena que iguala la oferta (punto de equilibrio)
        if p.pena_probable_anios > 0:
            resultado["prob_condena_de_equilibrio"] = round(
                min(1.0, p.oferta_abreviado_anios / p.pena_probable_anios), 3
            )
    return resultado


def _sensibilidad(p: Parametros) -> list:
    """Análisis de sensibilidad: exposición esperada ante variaciones de ±10 y ±20
    puntos porcentuales en la probabilidad de condena."""
    filas = []
    for delta in (-0.20, -0.10, 0.0, 0.10, 0.20):
        prob = max(0.0, min(1.0, p.prob_condena + delta))
        filas.append({
            "prob_condena": round(prob, 2),
            "exposicion_esperada_anios": round(prob * p.pena_probable_anios, 3),
        })
    return filas


def analizar(p: Parametros) -> dict:
    if not (0.0 <= p.prob_condena <= 1.0):
        raise ValueError("prob_condena debe estar en [0, 1]")
    if p.pena_probable_anios < 0:
        raise ValueError("pena_probable_anios no puede ser negativa")

    ve = _valor_esperado(p)
    salidas = _viabilidad_salidas(p)
    sens = _sensibilidad(p)

    observaciones = []
    if "prob_condena_de_equilibrio" in ve:
        eq = ve["prob_condena_de_equilibrio"]
        if p.prob_condena > eq:
            observaciones.append(
                f"La probabilidad estimada de condena ({p.prob_condena:.2f}) supera el "
                f"punto de equilibrio ({eq:.2f}): en términos de exposición esperada, "
                "la salida negociada domina al juicio oral. Ponderar factores "
                "cualitativos no capturados por el modelo."
            )
        else:
            observaciones.append(
                f"La probabilidad estimada de condena ({p.prob_condena:.2f}) es inferior "
                f"al punto de equilibrio ({eq:.2f}): en términos de exposición esperada, "
                "el juicio oral domina a la oferta. Ponderar aversión al riesgo del "
                "cliente y varianza del resultado."
            )
    if p.prob_sustitutiva_en_condena > 0:
        observaciones.append(
            "La estimación de pena sustitutiva (Ley 18.216) reduce la exposición "
            "privativa esperada; su procedencia concreta debe verificarse."
        )
    observaciones.append(
        "Los umbrales normativos son filtros prima facie y requieren verificación "
        "contra el texto legal vigente y el tipo penal concreto. La decisión "
        "estratégica corresponde exclusivamente al abogado y su cliente."
    )

    return {
        "caso": p.caso,
        "perspectiva": p.perspectiva,
        "parametros": asdict(p),
        "valor_esperado": ve,
        "viabilidad_salidas_procesales": salidas,
        "sensibilidad_prob_condena": sens,
        "observaciones": observaciones,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="Análisis estratégico de litigio penal")
    ap.add_argument("--json", help="Parámetros en JSON (claves de la dataclass Parametros)")
    ap.add_argument("--demo", action="store_true", help="Ejecuta un caso de demostración")
    args = ap.parse_args()

    if args.demo:
        p = Parametros(
            caso="DEMO-0000000000-0", perspectiva="defensa",
            prob_condena=0.65, pena_probable_anios=4.0,
            pena_solicitada_anios=4.0, oferta_abreviado_anios=3.0,
            costo_juicio=8_000_000, costo_salida=1_500_000,
            prob_sustitutiva_en_condena=0.5,
        )
    elif args.json:
        p = Parametros(**json.loads(args.json))
    else:
        ap.print_help()
        return 1

    print(json.dumps(analizar(p), indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
