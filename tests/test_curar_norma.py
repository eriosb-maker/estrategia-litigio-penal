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


# ---------------------------------------------------------------------------
# Modo --tratado (v4.14, aprobación del titular del 2026-09-30): tratados que
# LeyChile publica como «Artículo s/n» promulgatorio + texto íntegro en Anexo.
# ---------------------------------------------------------------------------

XML_TRATADO = """<?xml version="1.0" encoding="UTF-8"?>
<Norma xmlns="http://www.leychile.cl/esquemas" normaId="777" fechaVersion="1991-01-05" derogado="no derogado">
  <Identificador fechaPublicacion="1991-01-05">
    <TiposNumeros><TipoNumero><Tipo>Decreto</Tipo><Numero>1</Numero></TipoNumero></TiposNumeros>
  </Identificador>
  <Metadatos><TituloNorma>APRUEBA TRATADO DE PRUEBA</TituloNorma></Metadatos>
  <EstructurasFuncionales>
    <EstructuraFuncional tipoParte="Artículo" fechaVersion="1991-01-05" derogado="no derogado" idParte="1">
      <Texto>POR TANTO, dispongo y mando que se cumpla.</Texto>
      <Metadatos><NombreParte presente="no"></NombreParte></Metadatos>
    </EstructuraFuncional>
  </EstructurasFuncionales>
  <Anexos>
    <Anexo fechaVersion="1991-01-05" derogado="no derogado" idParte="900" transitorio="no transitorio">
      <Metadatos><Titulo>TRATADO DE PRUEBA</Titulo></Metadatos>
      <Texto>TRATADO DE PRUEBA

    Preámbulo que menciona el artículo 2 sin ser encabezado.

    Parte I - Deberes

    CAPITULO I - PRIMERO Y

                   SEGUNDO

    Artículo 1. Obligación de Respetar

    1. Texto del artículo uno.

    Artículo 2, Título con Coma
      en Dos Líneas

    2. Texto del artículo dos.

    Parte II - Medios

    Sección 1. Organización

    Art�culo 3

    Texto del artículo tres, cuyo encabezado viene dañado en la fuente.

    EN FE DE LO CUAL, los plenipotenciarios firman.</Texto>
    </Anexo>
  </Anexos>
</Norma>
"""


@pytest.fixture
def xml_tratado(tmp_path):
    ruta = tmp_path / "tratado.xml"
    ruta.write_text(XML_TRATADO, encoding="utf-8")
    return str(ruta)


class TestTratado:
    def test_sin_modo_tratado_conserva_comportamiento(self, xml_tratado):
        _md, encontrados, _f = curar_norma.generar_extracto(xml_tratado, "1-3", "T")
        assert encontrados == []

    def test_segmenta_articulos_del_anexo(self, xml_tratado):
        md, encontrados, faltantes = curar_norma.generar_extracto(
            xml_tratado, "1-3", "T", idnorma_esperado=777, tratado=True)
        assert [a["numero"] for a in encontrados] == [1, 2, 3]
        assert faltantes == []
        assert "Advertencia de segmentación" not in md

    def test_titulos_con_punto_coma_y_varias_lineas(self, xml_tratado):
        _md, enc, _f = curar_norma.generar_extracto(xml_tratado, "1-3", "T", tratado=True)
        titulos = {a["numero"]: a["titulo"] for a in enc}
        assert titulos == {1: "Obligación de Respetar",
                           2: "Título con Coma en Dos Líneas", 3: ""}

    def test_rutas_con_agrupadores_y_rotulo_partido(self, xml_tratado):
        _md, enc, _f = curar_norma.generar_extracto(xml_tratado, "1-3", "T", tratado=True)
        rutas = {a["numero"]: a["ruta"] for a in enc}
        assert rutas[1] == ("TRATADO DE PRUEBA › Parte I - Deberes › "
                            "CAPITULO I - PRIMERO Y SEGUNDO")
        # Una nueva Parte reinicia los niveles inferiores (Capítulo).
        assert rutas[3] == "TRATADO DE PRUEBA › Parte II - Medios › Sección 1. Organización"

    def test_excluye_preambulo_cierre_y_agrupadores_del_cuerpo(self, xml_tratado):
        _md, enc, _f = curar_norma.generar_extracto(xml_tratado, "1-3", "T", tratado=True)
        cuerpos = " ".join(a["texto"] for a in enc)
        for ajeno in ("Preámbulo", "EN FE DE LO CUAL", "Parte II", "Sección 1"):
            assert ajeno not in cuerpos
        assert enc[2]["texto"].startswith("    Texto del artículo tres")

    def test_encabezado_danado_se_reconoce_sin_corregir_la_fuente(self, xml_tratado):
        md, enc, _f = curar_norma.generar_extracto(xml_tratado, "3", "T", tratado=True)
        assert [a["numero"] for a in enc] == [3]
        assert "cuyo encabezado viene dañado en la fuente" in md

    def test_trazabilidad_del_anexo(self, xml_tratado):
        md, _e, _f = curar_norma.generar_extracto(xml_tratado, "1", "T", tratado=True)
        assert "### T — Art. 1. Obligación de Respetar" in md
        assert "Anexo idParte 900" in md and "segmentado por curar_norma.py" in md

    def test_anomalias_de_secuencia(self):
        assert curar_norma.anomalias_secuencia([1, 2, 3]) == []
        assert curar_norma.anomalias_secuencia([1, 3]) == ["artículos no detectados: 2"]
        assert "artículo 2 duplicado" in curar_norma.anomalias_secuencia([1, 2, 2])

    def test_xml_sin_anexo_en_modo_tratado_falla(self, xml_simple):
        with pytest.raises(SystemExit):
            curar_norma.generar_extracto(xml_simple, "1", "T", tratado=True)


_XML_OFICIAL = pathlib.Path(__file__).resolve().parent.parent / "curatoria" / "xml"


@pytest.mark.parametrize("archivo,idnorma,sha256,total", [
    ("cadh-d873-idNorma-16022.xml", 16022,
     "b5287e29c6026e64e5f24f798b5ea794cfe1cd0e163fed11f8a585d0ee524c54", 82),
    ("pidcp-d778-idNorma-15551.xml", 15551,
     "6d857285d1cf860d7d1fd74543735d63af8e2b8bbc265cd15cc059575760afe5", 53),
])
def test_tratados_oficiales_segmentacion_integra(archivo, idnorma, sha256, total):
    ruta = _XML_OFICIAL / archivo
    assert hashlib.sha256(ruta.read_bytes()).hexdigest() == sha256
    md, enc, faltantes = curar_norma.generar_extracto(
        str(ruta), f"1-{total}", "T", idnorma_esperado=idnorma, tratado=True)
    assert [a["numero"] for a in enc] == list(range(1, total + 1))
    assert faltantes == [] and "Advertencia de segmentación" not in md
    assert all(a["texto"].strip() for a in enc)


def test_cadh_art_8_2_y_pidcp_art_14_3():
    cadh = curar_norma.generar_extracto(
        str(_XML_OFICIAL / "cadh-d873-idNorma-16022.xml"), "8", "CADH", tratado=True)[1][0]
    assert cadh["titulo"] == "Garantías Judiciales"
    assert "2. Toda persona inculpada de delito tiene derecho a que se presuma su inocencia" \
        in cadh["texto"]
    pidcp = curar_norma.generar_extracto(
        str(_XML_OFICIAL / "pidcp-d778-idNorma-15551.xml"), "14", "PIDCP", tratado=True)[1][0]
    assert "3. Durante el proceso, toda persona acusada de un delito tendrá derecho" \
        in pidcp["texto"]


@pytest.mark.parametrize("consulta,idnorma", [
    ("CPR", 242302), ("COT", 25563), ("CADH", 16022), ("PIDCP", 15551),
])
def test_registro_ampliado_2026_09_30(consulta, idnorma):
    assert curar_norma.resolver_desde_registro(consulta)["idnorma"] == idnorma
