#!/usr/bin/env python3
"""
CLI: Análisis estratégico completo de una causa.

Uso:
    python scripts/analizar_causa.py --ruc "2024-1234" --modo bayes
    python scripts/analizar_causa.py --ruc "2024-1234" --modo juegos
    python scripts/analizar_causa.py --ruc "2024-1234" --modo completo
    python scripts/analizar_causa.py --demo
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from bayes import AnalisisBayesiano, Evidencia
from teoria_juegos import AnalisisTJ, JugadorLitigio
from causa_manager import CausaManager

VAULT_PATH = Path(__file__).parent.parent / "vault"


def demo_penal() -> None:
    """Ejecuta un análisis de demostración completo con un caso ficticio."""
    print("\n" + "=" * 60)
    print("  DEMO: Análisis Causa Penal — Robo con Intimidación")
    print("=" * 60)

    # ─── ANÁLISIS BAYESIANO ──────────────────────────────────────
    print("\n📊 ANÁLISIS BAYESIANO")
    print("─" * 40)

    analisis_bayes = AnalisisBayesiano(
        nombre_causa="Robo con Intimidación - Demo",
        ruc="2024-DEMO-001",
        prob_prior=0.72,
        materia="penal",
    )

    analisis_bayes.agregar_evidencias([
        Evidencia(
            nombre="Testigo ocular (condiciones deficientes)",
            descripcion="Testigo que identificó al imputado a 30m, de noche, durante 5 seg.",
            prob_dado_culpable=0.65,
            prob_dado_inocente=0.25,
            tipo="cargo",
        ),
        Evidencia(
            nombre="Huella dactilar parcial en la escena",
            descripcion="Huella con 8 puntos de coincidencia (mínimo legal: 12)",
            prob_dado_culpable=0.55,
            prob_dado_inocente=0.15,
            tipo="cargo",
        ),
        Evidencia(
            nombre="Sin coartada verificable",
            descripcion="El imputado dice que estaba en casa, sin testigos",
            prob_dado_culpable=0.70,
            prob_dado_inocente=0.40,
            tipo="cargo",
        ),
        Evidencia(
            nombre="Coartada parcial: llamada telefónica",
            descripcion="Registro de llamada desde zona diferente 20 min antes del hecho",
            prob_dado_culpable=0.30,
            prob_dado_inocente=0.70,
            tipo="descargo",
        ),
        Evidencia(
            nombre="Sin antecedentes penales",
            descripcion="Primera causa penal. Sin antecedentes previos.",
            prob_dado_culpable=0.25,
            prob_dado_inocente=0.55,
            tipo="descargo",
        ),
    ])

    print(f"P(Condena) prior: {analisis_bayes.prob_prior:.0%}")
    print(f"P(Condena) posterior: {analisis_bayes.prob_posterior:.1%}")
    print(f"Recomendación: {analisis_bayes.recomendacion.upper()}")
    print(f"\nEscenarios:")
    for nombre, val in analisis_bayes.escenarios().items():
        print(f"  {nombre:12s}: {val:.1%}")
    print(f"\nEvidencia más crítica:")
    for s in analisis_bayes.analisis_sensibilidad()[:2]:
        print(f"  - {s['evidencia']}: impacto {s['impacto']:+.1%}")

    # ─── ANÁLISIS TEORÍA DE JUEGOS ───────────────────────────────
    print("\n\n🎮 ANÁLISIS TEORÍA DE JUEGOS")
    print("─" * 40)

    p_condena = analisis_bayes.prob_posterior

    defensa = JugadorLitigio(
        nombre="Defensa",
        rol="defensor",
        prob_ganar_juicio=1 - p_condena,
        costo_juicio=5_000_000,    # CLP
        valor_ganar=50_000_000,    # Valor de la libertad (equivalente monetario)
        valor_perder=-80_000_000,  # Costo de condena (pena equivalente)
        valor_acuerdo_actual=-20_000_000,  # Procedimiento abreviado ofrecido
        costo_emocional_juicio=3_000_000,
    )

    fiscalia = JugadorLitigio(
        nombre="Fiscalía",
        rol="fiscalia",
        prob_ganar_juicio=p_condena,
        costo_juicio=2_000_000,
        valor_ganar=30_000_000,    # Valor político/institucional de la condena
        valor_perder=-5_000_000,   # Costo de perder (reputacional)
        valor_acuerdo_actual=15_000_000,   # Valor del abreviado para la fiscalía
    )

    analisis_tj = AnalisisTJ(
        nombre_causa="Robo con Intimidación - Demo",
        ruc="2024-DEMO-001",
        jugador_nuestro=defensa,
        jugador_contraparte=fiscalia,
        materia="penal",
    )

    print(f"BATNA Defensa:  ${defensa.batna:>12,.0f} CLP")
    print(f"BATNA Fiscalía: ${fiscalia.batna:>12,.0f} CLP")
    print(f"ZOPA existe: {'Sí' if analisis_tj.zopa_existe else 'No'}")
    print(f"Equilibrio Nash: {analisis_tj.equilibrio_nash()}")
    rec, just = analisis_tj.recomendacion()
    print(f"Recomendación: {rec.upper()}")
    print(f"  → {just}")

    print(f"\nAcciones para mejorar posición:")
    for a in analisis_tj.acciones_para_mejorar_posicion():
        print(f"  • {a}")

    print("\n" + "=" * 60)
    print("✅ Demo completado. Use --ruc para analizar una causa real.")
    print("=" * 60 + "\n")


def analisis_bayes_interactivo(ruc: str, vault_path: Path) -> AnalisisBayesiano:
    """Guía al usuario para construir el análisis bayesiano de una causa real."""
    print(f"\n📊 ANÁLISIS BAYESIANO — {ruc}")
    print("─" * 40)

    manager = CausaManager(vault_path)
    carpeta = manager.buscar_causa(ruc)

    if not carpeta:
        print(f"⚠️  Causa {ruc} no encontrada en el vault.")
        print("   Cree la causa primero con: python scripts/nueva_causa.py")
        sys.exit(1)

    nombre = input("Nombre descriptivo de la causa: ").strip() or f"Causa {ruc}"
    materia = input("Materia (penal/civil) [penal]: ").strip() or "penal"
    prior_str = input("Probabilidad inicial de condena (0.0-1.0) [0.5]: ").strip()
    prior = float(prior_str) if prior_str else 0.5

    analisis = AnalisisBayesiano(
        nombre_causa=nombre,
        ruc=ruc,
        prob_prior=prior,
        materia=materia,
    )

    print("\nIngrese las evidencias del caso (enter vacío para terminar):")
    i = 1
    while True:
        print(f"\n--- Evidencia #{i} ---")
        nombre_ev = input("Nombre/descripción breve (o enter para terminar): ").strip()
        if not nombre_ev:
            break

        print("  ¿Esta evidencia es de cargo (c) o descargo (d)? ", end="")
        tipo_ev = "cargo" if input().strip().lower() != "d" else "descargo"

        print(f"  P(esta evidencia | {'culpable' if tipo_ev == 'cargo' else 'inocente'}) = ", end="")
        p_culp_str = input().strip()
        p_culp = float(p_culp_str) if p_culp_str else 0.5

        print(f"  P(esta evidencia | {'inocente' if tipo_ev == 'cargo' else 'culpable'}) = ", end="")
        p_inoc_str = input().strip()
        p_inoc = float(p_inoc_str) if p_inoc_str else 0.5

        if tipo_ev == "cargo":
            analisis.agregar_evidencia(Evidencia(
                nombre=nombre_ev, descripcion=nombre_ev,
                prob_dado_culpable=p_culp, prob_dado_inocente=p_inoc,
                tipo="cargo",
            ))
        else:
            analisis.agregar_evidencia(Evidencia(
                nombre=nombre_ev, descripcion=nombre_ev,
                prob_dado_culpable=p_inoc, prob_dado_inocente=p_culp,
                tipo="descargo",
            ))
        i += 1

    return analisis


def main():
    parser = argparse.ArgumentParser(description="Análisis estratégico de causas legales")
    parser.add_argument("--ruc", help="RUC de la causa a analizar")
    parser.add_argument("--modo", choices=["bayes", "juegos", "completo", "conexiones"],
                        default="completo")
    parser.add_argument("--demo", action="store_true", help="Ejecutar análisis de demostración")
    parser.add_argument("--vault", default=str(VAULT_PATH), help="Path al vault")
    parser.add_argument("--guardar", action="store_true",
                        help="Guardar análisis en el vault de Obsidian")

    args = parser.parse_args()

    if args.demo:
        demo_penal()
        return

    if not args.ruc:
        print("❌ Especifique --ruc o use --demo para un ejemplo")
        parser.print_help()
        sys.exit(1)

    vault_path = Path(args.vault)
    manager = CausaManager(vault_path)

    if args.modo in ["bayes", "completo"]:
        analisis_bayes = analisis_bayes_interactivo(args.ruc, vault_path)
        reporte_bayes = analisis_bayes.generar_reporte()
        print("\n" + reporte_bayes)
        if args.guardar:
            manager.actualizar_analisis_bayes(args.ruc, reporte_bayes)
            print(f"\n✅ Análisis Bayesiano guardado en el vault (causa {args.ruc})")

    if args.modo in ["conexiones"]:
        from knowledge_base import KnowledgeBase
        kb = KnowledgeBase(vault_path)
        n = kb.indexar()
        print(f"\n🔗 Base de conocimiento indexada: {n} notas")
        reporte = kb.reporte_conexiones(args.ruc)
        print(reporte)


if __name__ == "__main__":
    main()
