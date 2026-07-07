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
- `skill/` — entregables camino a v2.0.0 de la skill `analisis-penal-chile`:
  - `APROBACIONES-PENDIENTES.md` — tres entradas de `aprendizajes.md` a la
    espera de aprobación del abogado.
  - `perimetro-leyes-especiales.md` — perímetro propuesto para la curatoría
    de las Leyes 21.595, 20.393, 19.913, 21.459 y 20.000.
  - `references/calculo-penas.md`, `references/prueba-digital.md`,
    `references/metodologia-detallada.md` — módulos construidos sobre el
    marco normativo verificado; citas no curadas marcadas «pendiente de
    verificación».
  - `references/leyes-especiales.md` — 177 artículos verificados de las
    Leyes 21.595, 20.393, 19.913, 21.459 y 20.000 (curatoría 2026-07-07,
    XML oficiales en `curatoria/xml/` con SHA-256 registrado; revalidación
    vence 2027-01-07).
- `scripts/curar_norma.py` — motor de curatoría (v. repo: soporte de
  «Doble Articulado» y numeración ordinal; suite en
  `tests/test_curar_norma.py`).

## Status

- ✅ Production Ready
- ✅ v1.4 CI/CD Pipeline
- ✅ 40x+ Performance Optimizations
- 🔜 v2.0.0: reempaquetado de la skill tras (a) aprobación de las entradas de
  `aprendizajes.md` y (b) curatoría de leyes especiales con XML aportados por
  el abogado. Revalidación semestral del módulo normativo: vence 2027-01-06.

## License

MIT License - See LICENSE file
