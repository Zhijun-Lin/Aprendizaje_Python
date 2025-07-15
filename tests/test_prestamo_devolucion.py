import pytest
from biblioteca.biblioteca import Biblioteca
from biblioteca.libro import Libro


@pytest.fixture
def biblioteca_con_libros():
    bib = Biblioteca()
    bib.agregar_libros(Libro("El Principito", "Saint-Exupéry", "PRIN123", 1))
    bib.agregar_libros(Libro("1984", "Orwell", "NOVE1984", 0))
    return bib


def test_prestamo_exitoso(biblioteca_con_libros):
    resultado = biblioteca_con_libros.prestar_libro("PRIN123")
    assert resultado is True
    assert biblioteca_con_libros.libros["PRIN123"].ejemplares_disponibles == 0


def test_prestamo_sin_ejemplares(biblioteca_con_libros):
    resultado = biblioteca_con_libros.prestar_libro("NOVE1984")
    assert resultado is False
    assert biblioteca_con_libros.libros["NOVE1984"].ejemplares_disponibles == 0


def test_prestamo_isbn_inexistente(biblioteca_con_libros):
    resultado = biblioteca_con_libros.prestar_libro("ISBN_INEXISTENTE")
    assert resultado is None


def test_devolucion_exitosa(biblioteca_con_libros):
    """Devolución incrementa ejemplares disponibles"""
    # Prestar primero para luego devolver
    biblioteca_con_libros.prestar_libro("PRIN123")

    ejemplares_antes = biblioteca_con_libros.libros["PRIN123"].ejemplares_disponibles
    resultado = biblioteca_con_libros.devolver_libro("PRIN123")

    assert resultado is True
    assert (
        biblioteca_con_libros.libros["PRIN123"].ejemplares_disponibles
        == ejemplares_antes + 1
    )
