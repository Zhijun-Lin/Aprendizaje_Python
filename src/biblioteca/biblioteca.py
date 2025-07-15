from biblioteca.libro import Libro
from biblioteca.validaciones import Validaciones
from biblioteca.errorPersonalizado import ErrorPersonalizado
import orjson


class Biblioteca:
    def __init__(self):
        self.libros = {}

    def agregar_libros(self, libro: Libro):
        try:
            if not (Validaciones.es_titulo_valido(libro.titulo) and 
                Validaciones.es_autor_valido(libro.autor) and 
                Validaciones.es_isbn_valido(libro.isbn) and 
                Validaciones.es_ejemplares_validos(libro.ejemplares_disponibles)):
                raise ErrorPersonalizado("El libro contiene datos inválidos")
            self.libros[libro.isbn] = libro
        except ErrorPersonalizado as e:
            print(f"Error: {e}")

    def buscar_por_titulo(self, titulo: str):
        try:
            if not Validaciones.es_titulo_valido(titulo):
                raise ErrorPersonalizado("El titulo no puede ser vacio o numerico")
            librosTitulo = []
            for valor in self.libros.values():
                if valor.titulo == titulo:
                    librosTitulo.append(valor)
            return librosTitulo
        except ErrorPersonalizado as e:
            print(f"Error: {e}")

    def buscar_por_autor(self, autor: str):
        try:
            if not Validaciones.es_autor_valido(autor):
                raise ErrorPersonalizado("El autor no puede ser vacio o numerico")
            librosAutor = []
            for valor in self.libros.values():
                if valor.autor == autor:
                    librosAutor.append(valor)
            return librosAutor
        except ErrorPersonalizado as e:
                print(f"Error: {e}")

    def prestar_libro(self, isbn: str):
        try:
            if not Validaciones.es_isbn_valido(isbn):
                raise ErrorPersonalizado("El ISBN no puede ser vacio y debe de ser alfanumerico sin espacio")
            for clave, valor in self.libros.items():
                if clave == isbn and valor.ejemplares_disponibles > 0:
                    valor.ejemplares_disponibles -= 1
                    print("Prestacion exitoso")
                    return True
            print("Prestacion fallido")
            return False
        except ErrorPersonalizado as e:
            print(f"Error: {e}")

    def devolver_libro(self, isbn: str):
        try:
            if not Validaciones.es_isbn_valido(isbn):
                raise ErrorPersonalizado("El ISBN no puede ser vacio y debe de ser alfanumerico sin espacio")
            for clave, valor in self.libros.items():
                if clave == isbn:
                    valor.ejemplares_disponibles += 1
                    print("Devolucion exitoso")
                    return True
            print("Devolucion fallido")
            return False
        except ErrorPersonalizado as e:
            print(f"Error: {e}")

    def listar_libros(self):
        for libro in self.libros.values():
            print(libro)

    def guardar(self, filename: str):
        opciones = orjson.OPT_INDENT_2 | orjson.OPT_NON_STR_KEYS
        datos = {}
        for clave, valor in self.libros.items():
            datos[clave] = valor.serializar()
        with open(filename, "wb") as f:
            f.write(orjson.dumps(datos, option=opciones))
        print("Libro guardado con exito")

    def cargar(self, filename: str):
        try:
            with open(filename, "rb") as f:
                contenido = f.read()
                libros = orjson.loads(contenido)
                for item in libros.values():
                    libro = Libro.deserializar(item)
                    self.agregar_libros(libro)
                print("Libro cargado con exito")
        except ErrorPersonalizado as e:
            print(f"Error: {e}")
    
