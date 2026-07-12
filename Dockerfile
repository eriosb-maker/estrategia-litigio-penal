FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential curl git && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ src/
COPY skill/ skill/
COPY tests/ tests/

RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

# Contenedor de utilidad para ejecutar la suite de pruebas y los motores
# deterministas de forma reproducible; el repositorio no expone servicio
# HTTP alguno (no hay servidor que sostenga un HEALTHCHECK ni un CMD de
# larga duración), de modo que el comando por defecto es la suite de
# pruebas y cada motor se invoca explícitamente según se requiera, p. ej.:
#   docker run --rm estrategia-litigio-penal python skill/scripts/prescripcion.py --demo
CMD ["python", "-m", "pytest", "tests/", "-v"]
