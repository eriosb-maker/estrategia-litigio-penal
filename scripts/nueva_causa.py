#!/usr/bin/env python3
"""
CLI: Crea una nueva causa en el vault de Obsidian.

Uso:
    python scripts/nueva_causa.py --ruc "2024-1234" --nombre "Caso Ejemplo" --tipo penal
    python scripts/nueva_causa.py --interactivo
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from causa_manager import Causa, CausaManager

VAULT_PATH = Path(__file__).parent.parent / "vault"


def modo_interactivo() -> Causa:
    print("\n⚖️  NUEVA CAUSA — Modo Interactivo\n")
    print("─" * 40)
    nombre = input("Nombre descriptivo de la causa: ").strip()
    ruc = input("RUC (ej: 2024-1234567-8): ").strip()

    print("\nTipo de causa:")
    print("  1. Penal")
    print("  2. Civil")
    tipo_input = input("Seleccione (1/2): ").strip()
    tipo = "penal" if tipo_input == "1" else "civil"

    print("\nRol del abogado:")
    if tipo == "penal":
        print("  1. Defensor")
        print("  2. Querellante")
        roles = {"1": "defensor", "2": "querellante"}
    else:
        print("  1. Demandante")
        print("  2. Demandado")
        roles = {"1": "demandante", "2": "demandado"}
    rol_input = input("Seleccione: ").strip()
    rol = roles.get(rol_input, "defensor")

    tribunal = input("Tribunal: ").strip()
    imputado = input("Nombre del imputado/demandado (opcional): ").strip()
    fiscal = input("Fiscal/Abogado contraparte (opcional): ").strip()
    juez = input("Juez asignado (opcional): ").strip()

    print("\nProbabilidad inicial estimada de condena/responsabilidad (0.0 a 1.0):")
    print("  (0.5 = desconocida, 0.3 = baja, 0.7 = alta)")
    prob_str = input("P(condena) estimada [0.5]: ").strip()
    try:
        prob = float(prob_str) if prob_str else 0.5
    except ValueError:
        prob = 0.5

    return Causa(
        nombre=nombre,
        ruc=ruc,
        tipo=tipo,
        rol_abogado=rol,
        tribunal=tribunal,
        imputado=imputado,
        fiscal=fiscal,
        juez=juez,
        prob_condena=prob,
    )


def main():
    parser = argparse.ArgumentParser(
        description="Crea una nueva causa en el vault de Obsidian"
    )
    parser.add_argument("--ruc", help="RUC de la causa")
    parser.add_argument("--nombre", help="Nombre descriptivo")
    parser.add_argument("--tipo", choices=["penal", "civil"], default="penal")
    parser.add_argument("--rol", default="defensor",
                        choices=["defensor", "querellante", "demandante", "demandado"])
    parser.add_argument("--tribunal", default="Por determinar")
    parser.add_argument("--imputado", default="")
    parser.add_argument("--fiscal", default="")
    parser.add_argument("--juez", default="")
    parser.add_argument("--prob", type=float, default=0.5,
                        help="Probabilidad inicial de condena (0.0-1.0)")
    parser.add_argument("--interactivo", action="store_true",
                        help="Modo interactivo con prompts")
    parser.add_argument("--vault", default=str(VAULT_PATH),
                        help="Path al vault de Obsidian")

    args = parser.parse_args()

    if args.interactivo or not args.ruc:
        causa = modo_interactivo()
    else:
        causa = Causa(
            nombre=args.nombre or f"Causa {args.ruc}",
            ruc=args.ruc,
            tipo=args.tipo,
            rol_abogado=args.rol,
            tribunal=args.tribunal,
            imputado=args.imputado,
            fiscal=args.fiscal,
            juez=args.juez,
            prob_condena=args.prob,
        )

    manager = CausaManager(args.vault)

    print(f"\n📁 Creando estructura para: {causa.nombre} ({causa.ruc})")
    try:
        carpeta = manager.crear_causa(causa)
        print(f"✅ Causa creada exitosamente en: {carpeta}")
        print(f"\nArchivos creados:")
        for f in sorted(carpeta.iterdir()):
            print(f"   📄 {f.name}")
        print(f"\n💡 Próximo paso: abre Obsidian y navega a 01-Causas/{causa.carpeta_id()}/00-Resumen.md")
    except FileExistsError as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
