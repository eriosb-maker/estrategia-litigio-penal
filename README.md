# Estrategia de Litigio Penal

AI-powered legal strategy analysis for criminal law cases.

## Quick Start

```bash
pip install -r requirements.txt
python -m pytest tests/ -v
```

## CI/CD Pipeline

GitHub Actions ejecuta automáticamente:
- Linting (flake8, pylint, black)
- Security scanning (bandit, safety)
- Type checking (mypy)
- Tests (pytest)
- Build & deploy

## Módulos

- `src/prescripcion.py` — calculadora determinística de prescripción penal
  (arts. 93–105 CP, texto verificado contra XML oficial de LeyChile,
  curatoría 2026-07-06). Suite: `tests/test_prescripcion.py` (24 pruebas).
- `tests/test_casos_dorados.py` — suite de regresión sobre hechos ficticios
  para `prescripcion.py` y `skill/scripts/estrategia_litigio.py` (8 casos,
  línea V del plan de mejoras, 2026-07-12).
- `scripts/verificar_sincronia_motores.py` — cotejo de hash entre cada motor
  canónico y su copia empaquetada en `skill/scripts/` (aprendizaje A-022).
- `scripts/vigilar_revalidacion.py` — vigilancia de los plazos de
  revalidación semestral declarados en los módulos normativos curados.
- `skill/` — paquete completo de la skill `analisis-penal-chile` **v4.2**
  (SKILL.md, nueve módulos de `references/`, tres motores en `scripts/`,
  cinco plantillas y un ejemplo trabajado). Los módulos normativos están
  verificados contra XML oficiales de LeyChile: `marco-legal.md` (248
  artículos CP/CPP, curatoría 2026-07-06), `leyes-especiales.md` (177
  artículos de las Leyes 21.595, 20.393, 19.913, 21.459 y 20.000, curatoría
  2026-07-07) y `tributario.md` (52 artículos del Código Tributario, la Ley
  de IVA y la Ley de Renta, curatoría 2026-07-07); XML con SHA-256 en
  `curatoria/xml/`.

Detalle de la capa de evaluación y CI: `docs/capa-evaluacion-ci.md`.
- `scripts/curar_norma.py` — motor de curatoría, con soporte de estructura
  «Doble Articulado» (Ley 20.393, Código Tributario, Ley de Renta) y
  numeración ordinal; incorpora **resolución automática de idNorma**
  (`--resolver "Ley 21595"`, registro local + resolución en línea vía
  LeyChile) y **descarga con verificación de hash** (`--descargar <idNorma>
  --out <archivo>`). Suite en `tests/test_curar_norma.py` (54 pruebas).
- `docs/` — actas de aprobación de aprendizajes y perímetro de curatoría.

## Status

- ✅ v2.0.0 — skill `analisis-penal-chile` v4.2 empaquetada: catálogo
  íntegro de `references/`, `assets/templates/`, `scripts/` y `examples/`
  en **[disponible]**, incluido el módulo tributario y el resolver
  automático de idNorma.
- ✅ Suite pytest: prescripción (24) + curatoría (54) = 78 pruebas.
- 🗓️ Revalidación semestral: `marco-legal.md` vence 2027-01-06;
  `leyes-especiales.md` y `tributario.md` vencen 2027-01-07 (recordatorio
  agendado).

## License

MIT License - See LICENSE file
