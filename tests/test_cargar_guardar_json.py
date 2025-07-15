import pytest
import tempfile
import json
from pathlib import Path
from biblioteca.biblioteca import Biblioteca
from biblioteca.libro import Libro
from biblioteca.errorPersonalizado import ErrorPersonalizado

@pytest.fixture
def biblioteca_ejemplo():
    bib = Biblioteca()
    bib.agregar_libros(Libro("Cien años de soledad", "García Márquez", "ABC123", 3))
    bib.agregar_libros(Libro("Rayuela", "Cortázar", "XYZ456", 1))
    return bib

@pytest.fixture
def archivo_temporal():
    with tempfile.NamedTemporaryFile(delete=False, suffix=".json") as tmp:
        yield Path(tmp.name)
    tmp.close()
    

def test_guardar_libros(biblioteca_ejemplo, archivo_temporal):
    biblioteca_ejemplo.guardar(archivo_temporal)
    
    assert archivo_temporal.exists()
    with open(archivo_temporal, "r", encoding="utf-8") as f:
        datos = json.load(f)
        assert len(datos) == 2  # Debe contener 2 libros
        assert datos["ABC123"]["titulo"] == "Cien años de soledad"
        
def test_cargar_libros(biblioteca_ejemplo, archivo_temporal):

    biblioteca_ejemplo.guardar(archivo_temporal)
    
    bib_nueva = Biblioteca()
    bib_nueva.cargar(archivo_temporal)
    
    assert len(bib_nueva.libros) == 2
    assert bib_nueva.libros["ABC123"].autor == "García Márquez"