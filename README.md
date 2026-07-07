# Estrategia de Litigio Penal

AI-powered legal strategy analysis for criminal law cases.

## Quick Start

```bash
pip install -r requirements.txt
python src/main.py
```

## CI/CD Pipeline

GitHub Actions ejecuta automáticamente:
- Linting (flake8, pylint, black)
- Security scanning (bandit, safety)
- Type checking (mypy)
- Tests (pytest)
- Build & deploy

## Módulos

- `src/main.py` — análisis de estrategia (v1.3/v1.4).
- `src/prescripcion.py` — calculadora determinística de prescripción penal
  (arts. 93–105 CP, texto verificado contra XML oficial de LeyChile,
  curatoría 2026-07-06). Suite: `tests/test_prescripcion.py` (24 pruebas).
- `skill/` — paquete completo de la skill `analisis-penal-chile` **v4.0**
  (SKILL.md, ocho módulos de `references/`, tres motores en `scripts/` y
  cinco plantillas). Los módulos normativos están verificados contra XML
  oficiales de LeyChile: `marco-legal.md` (248 artículos CP/CPP, curatoría
  2026-07-06) y `leyes-especiales.md` (177 artículos de las Leyes 21.595,
  20.393, 19.913, 21.459 y 20.000, curatoría 2026-07-07; XML con SHA-256 en
  `curatoria/xml/`).
- `scripts/curar_norma.py` — motor de curatoría (soporte de «Doble
  Articulado» y numeración ordinal; suite en `tests/test_curar_norma.py`).
- `docs/` — actas de aprobación de aprendizajes y perímetro de curatoría.

## Status

- ✅ v2.0.0 — skill `analisis-penal-chile` v4.0 empaquetada (todos los
  módulos de referencia disponibles; pendiente solo el ejemplo trabajado).
- ✅ Suite pytest: prescripción (24) + curatoría (8).
- 🗓️ Revalidación semestral: `marco-legal.md` vence 2027-01-06;
  `leyes-especiales.md` vence 2027-01-07 (recordatorio agendado).

## License

MIT License - See LICENSE file
