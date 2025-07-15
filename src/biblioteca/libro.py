from biblioteca.errorPersonalizado import ErrorPersonalizado
from biblioteca.validaciones import Validaciones

class Libro:
    def __init__(self, titulo: str, autor: str, isbn: str, ejemplares_disponibles: int):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.ejemplares_disponibles = ejemplares_disponibles

    def __str__(self):
        return f"Titulo: {self.titulo}, Autor: {self.autor} ISBN: {self.isbn} Disponibles: {self.ejemplares_disponibles}"

    def serializar(self):
        return {
            "titulo": self.titulo,
            "autor": self.autor,
            "isbn": self.isbn,
            "ejemplares_disponibles": self.ejemplares_disponibles,
        }
        
    @staticmethod
    def deserializar(diccionario: dict):
        if not (Validaciones.es_titulo_valido(diccionario["titulo"]) and 
                Validaciones.es_autor_valido(diccionario["autor"]) and 
                Validaciones.es_isbn_valido(diccionario["isbn"]) and 
                Validaciones.es_ejemplares_validos(diccionario["ejemplares_disponibles"])):
                raise ErrorPersonalizado("El libro contiene datos inválidos")
        return Libro(diccionario["titulo"], diccionario["autor"], diccionario["isbn"], diccionario["ejemplares_disponibles"])
