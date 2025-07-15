import pytest
from biblioteca.validaciones import Validaciones


@pytest.mark.parametrize(
    "titulo,esperado,clase_equivalencia",
    [
        ("Don Quijote de la Mancha", True, "V1: Titulo válido"),
        ("", False, "I1: Cadena vacía"),
        (" ", False, "I2: Solo espacios"),
        (None, False, "I3: Valor nulo"),
        (123456789, False, "I4: Entero, no string"),
    ],
)
def test_es_titulo_valido(titulo, esperado: bool, clase_equivalencia: str):
    resultado = Validaciones.es_titulo_valido(titulo)
    assert resultado == esperado, f"Fallo en clase: {clase_equivalencia}"


@pytest.mark.parametrize(
    "autor,esperado,clase_equivalencia",
    [
        ("Gabriel García Márquez", True, "V1: Autor válido"),
        ("", False, "I1: Cadena vacía"),
        ("  ", False, "I2: Solo espacios"),
        (None, False, "I3: Valor nulo"),
        (3.1416, False, "I4: Float, no string"),
        (["Borges"], False, "I5: Lista, no string"),
    ],
)
def test_es_autor_valido(autor, esperado: bool, clase_equivalencia: str):
    resultado = Validaciones.es_autor_valido(autor)
    assert resultado == esperado, f"Fallo en clase: {clase_equivalencia}"


@pytest.mark.parametrize(
    "isbn,esperado,clase_equivalencia",
    [
        ("9780306406157", True, "V1: ISBN numérico válido"),
        ("ABC123XYZ456", True, "V2: ISBN alfanumérico válido"),
        ("", False, "I1: Cadena vacía"),
        ("   ", False, "I2: Solo espacios"),
        ("978 030 640", False, "I3: Contiene espacios"),
        ("@ISBN123!", False, "I4: Caracteres especiales"),
        (None, False, "I5: Valor nulo"),
        (9780306406157, False, "I6: Entero, no string"),
    ],
)
def test_es_isbn_valido(isbn, esperado: bool, clase_equivalencia: str):
    resultado = Validaciones.es_isbn_valido(isbn)
    assert resultado == esperado, f"Fallo en clase: {clase_equivalencia}"


@pytest.mark.parametrize(
    "ejemplares,esperado,clase_equivalencia",
    [
        (5, True, "V1: Cantidad positiva"),
        (0, True, "V2: Límite inferior válido (0)"),
        (-1, False, "I1: Valor negativo"),
        (None, False, "I2: Valor nulo"),
        ("5", False, "I3: String numérico"),
        (3.14, False, "I4: Float no entero"),
        (10_000, True, "V3: Valor grande válido"),
    ],
)
def test_es_ejemplares_validos(ejemplares, esperado: bool, clase_equivalencia: str):
    resultado = Validaciones.es_ejemplares_validos(ejemplares)
    assert resultado == esperado, f"Fallo en clase: {clase_equivalencia}"
