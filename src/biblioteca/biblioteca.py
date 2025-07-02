from libro import Libro


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
