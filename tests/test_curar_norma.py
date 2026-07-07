# -*- coding: utf-8 -*-
"""Pruebas del motor de curatoría normativa (scripts/curar_norma.py).

Cubre la regresión introducida por el «Doble Articulado» (Ley 20.393): los
artículos anidados dentro de un artículo promulgatorio deben inventariarse y
extraerse, sin duplicar ni perder los artículos de primer nivel.
"""

import hashlib
import importlib.util
import pathlib
import sys

import pytest

_RUTA = pathlib.Path(__file__).resolve().parent.parent / "scripts" / "curar_norma.py"
_spec = importlib.util.spec_from_file_location("curar_norma", _RUTA)
curar_norma = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(curar_norma)


XML_SIMPLE = """<?xml version="1.0" encoding="UTF-8"?>
<Norma xmlns="http://www.leychile.cl/esquemas" normaId="999" fechaVersion="2026-01-01" derogado="no derogado">
  <Identificador fechaPublicacion="2020-01-01">
    <TiposNumeros><TipoNumero><Tipo>Ley</Tipo><Numero>999</Numero></TipoNumero></TiposNumeros>
  </Identificador>
  <Metadatos><TituloNorma>LEY DE PRUEBA</TituloNorma></Metadatos>
  <EstructurasFuncionales>
    <EstructuraFuncional tipoParte="Título" fechaVersion="2020-01-01" derogado="no derogado" idParte="1">
      <Metadatos><NombreParte presente="si">I</NombreParte><TituloParte presente="si">TITULO I</TituloParte></Metadatos>
      <EstructurasFuncionales>
        <EstructuraFuncional tipoParte="Artículo" fechaVersion="2020-01-01" derogado="no derogado" idParte="10">
          <Texto>Articulo 1. Texto uno.</Texto>
          <Metadatos><NombreParte presente="si">1</NombreParte></Metadatos>
        </EstructuraFuncional>
        <EstructuraFuncional tipoParte="Artículo" fechaVersion="2021-05-05" derogado="derogado" idParte="11">
          <Texto>Articulo 2. Derogado.</Texto>
          <Metadatos><NombreParte presente="si">2</NombreParte></Metadatos>
        </EstructuraFuncional>
        <EstructuraFuncional tipoParte="Artículo" fechaVersion="2020-01-01" derogado="no derogado" idParte="12">
          <Texto>Articulo 2 bis. Variante.</Texto>
          <Metadatos><NombreParte presente="si">2 BIS</NombreParte></Metadatos>
        </EstructuraFuncional>
      </EstructurasFuncionales>
    </EstructuraFuncional>
  </EstructurasFuncionales>
</Norma>
"""

XML_DOBLE_ARTICULADO = """<?xml version="1.0" encoding="UTF-8"?>
<Norma xmlns="http://www.leychile.cl/esquemas" normaId="1008668" fechaVersion="2023-08-17" derogado="no derogado">
  <Identificador fechaPublicacion="2009-12-02">
    <TiposNumeros><TipoNumero><Tipo>Ley</Tipo><Numero>20393</Numero></TipoNumero></TiposNumeros>
  </Identificador>
  <Metadatos><TituloNorma>LEY ANIDADA DE PRUEBA</TituloNorma></Metadatos>
  <EstructurasFuncionales>
    <EstructuraFuncional tipoParte="Artículo" fechaVersion="2009-12-02" derogado="no derogado" idParte="100">
      <Texto>Articulo PRIMERO. Apruebase la siguiente ley:</Texto>
      <Metadatos><NombreParte presente="si">PRIMERO</NombreParte></Metadatos>
      <EstructurasFuncionales>
        <EstructuraFuncional tipoParte="Doble Articulado" fechaVersion="2009-12-02" derogado="no derogado" idParte="101">
          <EstructurasFuncionales>
            <EstructuraFuncional tipoParte="Artículo" fechaVersion="2023-08-17" derogado="no derogado" idParte="102">
              <Texto>Articulo 1. Contenido interno uno.</Texto>
              <Metadatos><NombreParte presente="si">1</NombreParte></Metadatos>
            </EstructuraFuncional>
            <EstructuraFuncional tipoParte="Artículo" fechaVersion="2023-08-17" derogado="no derogado" idParte="103">
              <Texto>Articulo 2. Contenido interno dos.</Texto>
              <Metadatos><NombreParte presente="si">2</NombreParte></Metadatos>
            </EstructuraFuncional>
          </EstructurasFuncionales>
        </EstructuraFuncional>
      </EstructurasFuncionales>
    </EstructuraFuncional>
    <EstructuraFuncional tipoParte="Artículo" fechaVersion="2009-12-02" derogado="no derogado" idParte="200">
      <Texto>Articulo SEGUNDO. Disposicion final.</Texto>
      <Metadatos><NombreParte presente="si">SEGUNDO</NombreParte></Metadatos>
    </EstructuraFuncional>
  </EstructurasFuncionales>
</Norma>
"""


@pytest.fixture
def xml_simple(tmp_path):
    p = tmp_path / "simple.xml"
    p.write_text(XML_SIMPLE, encoding="utf-8")
    return str(p)


@pytest.fixture
def xml_doble(tmp_path):
    p = tmp_path / "doble.xml"
    p.write_text(XML_DOBLE_ARTICULADO, encoding="utf-8")
    return str(p)


class TestRecorridoSimple:
    def test_extrae_rango_con_variantes(self, xml_simple):
        md, encontrados, faltantes = curar_norma.generar_extracto(
            xml_simple, "1-2", "LP", idnorma_esperado="999")
        etiquetas = [a["etiqueta"] for a in encontrados]
        assert etiquetas == ["1", "2", "2 BIS"]
        assert not faltantes

    def test_derogado_se_marca_sin_texto(self, xml_simple):
        md, encontrados, _ = curar_norma.generar_extracto(
            xml_simple, "2", "LP")
        derogado = [a for a in encontrados if a["etiqueta"] == "2"][0]
        assert derogado["derogado"]
        assert "[DEROGADO]" in md
        assert "Derogado." not in md  # el texto del derogado se omite

    def test_valida_idnorma(self, xml_simple):
        with pytest.raises(SystemExit):
            curar_norma.generar_extracto(
                xml_simple, "1", "LP", idnorma_esperado="1984")


class TestDobleArticulado:
    def test_inventaria_articulos_anidados(self, xml_doble):
        raiz, _ = curar_norma.cargar_norma(xml_doble)
        nombres = [n for _, n, _ in curar_norma.recorrer_articulos(raiz)]
        assert "PRIMERO" in nombres
        assert "1" in nombres and "2" in nombres
        assert "SEGUNDO" in nombres

    def test_extrae_articulos_internos_por_rango(self, xml_doble):
        md, encontrados, faltantes = curar_norma.generar_extracto(
            xml_doble, "1-2", "L20393", idnorma_esperado="1008668")
        etiquetas = [a["etiqueta"] for a in encontrados]
        assert etiquetas == ["1", "2"]
        assert not faltantes
        assert "Contenido interno uno." in md
        # Los artículos promulgatorios no entran por rango numérico.
        assert "Apruebase" not in md

    def test_ruta_registra_el_articulo_contenedor(self, xml_doble):
        raiz, _ = curar_norma.cargar_norma(xml_doble)
        rutas = {n: r for _, n, r in curar_norma.recorrer_articulos(raiz)}
        assert any("Artículo PRIMERO" in parte for parte in rutas["1"])


class TestNumeracionOrdinal:
    def test_normalizar_elimina_indicador_ordinal(self):
        assert curar_norma._normalizar("1°") == "1"
        assert curar_norma._normalizar("8º") == "8"

    def test_parsea_nombre_con_ordinal(self):
        assert curar_norma.parsear_nombre_parte("1°") == (1, "")
        assert curar_norma.parsear_nombre_parte("9°") == (9, "")


class _RespuestaFalsa:
    """Simula el objeto devuelto por urlopen dentro de un context manager."""

    def __init__(self, contenido_bytes):
        self._contenido = contenido_bytes

    def read(self):
        return self._contenido

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False


class TestRegistroLocal:
    @pytest.mark.parametrize("consulta,idnorma_esperado", [
        ("CP", 1984),
        ("Código Penal", 1984),
        ("CPP", 176595),
        ("Código Tributario", 6374),
        ("DL 830", 6374),
        ("Ley de Renta", 6368),
        ("DL 824", 6368),
        ("Ley de IVA", 6369),
        ("DL 825", 6369),
        ("Ley 21595", 1195119),
        ("Ley N° 20393", 1008668),
    ])
    def test_resuelve_desde_registro(self, consulta, idnorma_esperado):
        hallazgo = curar_norma.resolver_norma(consulta)
        assert hallazgo["idnorma"] == idnorma_esperado
        assert "registro local" in hallazgo["fuente"]

    def test_no_registrada_y_sin_numero_falla(self):
        with pytest.raises(ValueError):
            curar_norma.resolver_norma("Ley de Bosques")


class TestResolucionEnLinea:
    def test_resuelve_idley_mediante_canonical(self):
        html = (
            b'<html><head><title>Ley Chile - Ley 12345 - Biblioteca del '
            b'Congreso Nacional</title>'
            b'<link rel="canonical" href="https://www.bcn.cl/leychile/'
            b'navegar?idNorma=987654" /></head></html>'
        )
        opener = lambda req: _RespuestaFalsa(html)
        hallazgo = curar_norma.resolver_por_idley(12345, _opener=opener)
        assert hallazgo["idnorma"] == 987654
        assert hallazgo["tipo"] == "Ley"
        assert "no oficial" in hallazgo["fuente"]

    def test_sin_canonical_lanza_error_explicativo(self):
        html = b"<html><head><title>Un error</title></head></html>"
        opener = lambda req: _RespuestaFalsa(html)
        with pytest.raises(ValueError, match="decretos leyes"):
            curar_norma.resolver_por_idley(830, _opener=opener)

    def test_resolver_norma_intenta_idley_si_no_esta_en_registro(self):
        html = (
            b'<link rel="canonical" href="https://www.bcn.cl/leychile/'
            b'navegar?idNorma=555111" />'
        )
        opener = lambda req: _RespuestaFalsa(html)
        hallazgo = curar_norma.resolver_norma("Ley 99999", _opener=opener)
        assert hallazgo["idnorma"] == 555111


class TestDescarga:
    def test_descarga_calcula_hash_y_guarda_archivo(self, tmp_path):
        contenido = b'<?xml version="1.0"?><Norma normaId="42">contenido</Norma>'
        opener = lambda req: _RespuestaFalsa(contenido)
        destino = tmp_path / "norma.xml"
        tamano, sha256 = curar_norma.descargar_xml(42, str(destino), _opener=opener)
        assert tamano == len(contenido)
        assert destino.read_bytes() == contenido
        assert sha256 == hashlib.sha256(contenido).hexdigest()

    def test_descarga_rechaza_respuesta_no_xml(self, tmp_path):
        opener = lambda req: _RespuestaFalsa(b"<html>error 401</html>")
        with pytest.raises(ValueError, match="normaId"):
            curar_norma.descargar_xml(1, str(tmp_path / "x.xml"), _opener=opener)


class TestDisambiguadorDobleArticulado:
    @pytest.mark.parametrize("crudo,esperado", [
        ("97 (DEL ART. 1)", "97"),
        ("100 BIS (DEL ART 1)", "100 BIS"),
        ("111 (DEL ART. 1)", "111"),
        ("SEGUNDO", "SEGUNDO"),
        ("24 BIS", "24 BIS"),
    ])
    def test_limpia_sufijo_del_articulo_contenedor(self, crudo, esperado):
        assert curar_norma._limpiar_disambiguador_articulado(crudo) == esperado
