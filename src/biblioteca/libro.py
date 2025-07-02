class Libro:
    def __init__(self, titulo: str, autor: str, isbn: int, ejemplares_disponibles: int):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.ejemplares_disponibles = ejemplares_disponibles

    def __str__(self):
        return f"Titulo: {self.titulo}, Autor: {self.autor} ISBN: {self.isbn} Disponibles: {self.ejemplares_disponibles}"
