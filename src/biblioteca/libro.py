class Libro:
    def __init__(self, titulo: str, autor: str, isbn: int, ejemplares_disponibles: int):
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

    def deserializar(diccionario: dict):
        return Libro(diccionario["titulo"], diccionario["autor"], diccionario["isbn"], diccionario["ejemplares_disponibles"])
