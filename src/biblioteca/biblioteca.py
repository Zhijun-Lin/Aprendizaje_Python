from libro import Libro
import orjson

class Biblioteca:
    def __init__(self):
        self.libros = {}

    def agregar_libros(self, libro: Libro):
        self.libros[libro.isbn] = libro

    def buscar_por_titulo(self, titulo: str):
        librosTitulo = []
        for valor in self.libros.values():
            if valor.titulo == titulo:
                librosTitulo.append(valor)
        return librosTitulo

    def buscar_por_autor(self, autor: str):
        librosAutor = []
        for valor in self.libros.values():
            if valor.autor == autor:
                librosAutor.append(valor)
        return librosAutor

    def prestar_libro(self, isbn: str):
        for clave, valor in self.libros.items():
            if clave == isbn and valor.ejemplares_disponibles > 0:
                valor.ejemplares_disponibles -= 1
                print("Prestacion exitoso")
                return True
        print("Prestacion fallido")
        return False

    def devolver_libro(self, isbn: str):
        for clave, valor in self.libros.items():
            if clave == isbn:
                valor.ejemplares_disponibles += 1
                print("Devolucion exitoso")
                return True
        print("Devolucion fallido")
        return False

    def listar_libros(self):
        for libro in self.libros.values():
            print(libro)

    def guardar(self, filename: str):
        opciones = orjson.OPT_INDENT_2 | orjson.OPT_NON_STR_KEYS
        
        datos = {}
        for clave,valor in self.libros.items():
            datos[clave]=valor.serializar()
        
        with open(filename, "wb") as f:
            f.write(orjson.dumps(datos, option=opciones))
            
        print("Libro guardado con exito")
    
    def cargar(self, filename: str):
        with open(filename, "rb") as f:
            contenido = f.read()
            libros = orjson.loads(contenido)
            for item in libros.values():
                libro = Libro.deserializar(item)
                self.agregar_libros(libro)
                
            
            print("Libro cargado con exito")

