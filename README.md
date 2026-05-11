# ⚖️ Segundo Cerebro Legal

> Sistema de gestión del conocimiento para abogados litigantes, basado en el método de segundo cerebro de Andrej Karpathy, con motores de análisis Bayesiano y Teoría de Juegos.

## ¿Qué es esto?

Un **segundo cerebro legal** que combina:

1. **Vault de Obsidian** — base de conocimiento enlazada (causas, normas, jurisprudencia, libros)
2. **Motor Bayesiano** — calcula P(Condena|Evidencia) con razones de verosimilitud
3. **Motor de Teoría de Juegos** — identifica equilibrios Nash y ZOPA para negociaciones
4. **Knowledge Base** — búsqueda cruzada entre causas, normas y bibliografía

## Instalación

```bash
pip install -r requirements.txt
```

Abrir la carpeta `vault/` como vault en [Obsidian](https://obsidian.md).

## Uso Rápido

```bash
# Crear una causa nueva
python scripts/nueva_causa.py --ruc "2024-1234" --nombre "Caso X" --tipo penal

# Ver demostración de análisis completo
python scripts/analizar_causa.py --demo

# Buscar en la base de conocimiento
python scripts/buscar.py "legítima defensa" --tipo norma
python scripts/buscar.py --estadisticas
```

## Estructura

```
vault/          ← Vault de Obsidian (abrir con Obsidian)
src/            ← Motores Python (bayes, teoria_juegos, causa_manager, knowledge_base)
scripts/        ← CLI (nueva_causa, analizar_causa, buscar)
tests/          ← 18 tests unitarios
```

## Tests

```bash
pytest tests/ -v   # 18 tests, todos pasando
```

## Plugins Obsidian Requeridos

Dataview, Templater, Tasks, QuickAdd, Calendar.

## License

MIT License - See LICENSE file
