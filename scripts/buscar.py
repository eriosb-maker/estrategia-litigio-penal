#!/usr/bin/env python3
"""
CLI: Busca en la base de conocimiento del vault.

Uso:
    python scripts/buscar.py "robo con intimidación"
    python scripts/buscar.py "legítima defensa" --tipo norma
    python scripts/buscar.py "daño moral" --materia civil --tipo jurisprudencia
    python scripts/buscar.py --estadisticas
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from knowledge_base import KnowledgeBase

VAULT_PATH = Path(__file__).parent.parent / "vault"


def main():
    parser = argparse.ArgumentParser(description="Búsqueda en la base de conocimiento legal")
    parser.add_argument("consulta", nargs="?", help="Texto a buscar")
    parser.add_argument("--tipo", nargs="+",
                        choices=["norma", "jurisprudencia", "libro", "paper",
                                 "estrategia", "concepto", "causa"],
                        help="Filtrar por tipo de nota")
    parser.add_argument("--materia", choices=["penal", "civil", "procesal", "teoria"],
                        help="Filtrar por materia")
    parser.add_argument("--limite", type=int, default=10, help="Número máximo de resultados")
    parser.add_argument("--estadisticas", action="store_true",
                        help="Mostrar estadísticas del vault")
    parser.add_argument("--vault", default=str(VAULT_PATH), help="Path al vault")

    args = parser.parse_args()
    vault_path = Path(args.vault)

    kb = KnowledgeBase(vault_path)
    print(f"📚 Indexando vault en {vault_path}...")
    n = kb.indexar()
    print(f"   {n} notas indexadas\n")

    if args.estadisticas:
        stats = kb.estadisticas()
        print("📊 Estadísticas del Vault")
        print("─" * 30)
        print(f"Total de notas: {stats['total_notas']}")
        print("\nPor tipo:")
        for tipo, count in sorted(stats["por_tipo"].items(), key=lambda x: -x[1]):
            print(f"  {tipo:20s}: {count}")
        print("\nPor materia:")
        for materia, count in sorted(stats["por_materia"].items(), key=lambda x: -x[1]):
            print(f"  {materia:20s}: {count}")
        return

    if not args.consulta:
        parser.print_help()
        sys.exit(1)

    resultados = kb.buscar(
        consulta=args.consulta,
        tipos=args.tipo,
        materia=args.materia or "",
        limite=args.limite,
    )

    if not resultados:
        print(f"❌ No se encontraron resultados para: '{args.consulta}'")
        print("   Verifique que el vault tenga notas del tipo buscado.")
        return

    print(f"🔍 Resultados para: '{args.consulta}'")
    print("─" * 50)

    for i, r in enumerate(resultados, 1):
        etiquetas_str = ", ".join(r.etiquetas[:3]) if r.etiquetas else ""
        print(f"\n{i}. [{r.tipo.upper()}] {r.titulo}")
        print(f"   Relevancia: {'█' * int(r.relevancia * 10)}{'░' * (10 - int(r.relevancia * 10))} {r.relevancia:.0%}")
        if etiquetas_str:
            print(f"   Etiquetas: {etiquetas_str}")
        print(f"   {r.fragmento[:200]}")
        print(f"   📄 {r.archivo.relative_to(vault_path)}")


if __name__ == "__main__":
    main()
