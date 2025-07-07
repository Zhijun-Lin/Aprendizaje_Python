from errorPersonalizado import ErrorPersonalizado

class Libro:
    def __init__(self, titulo: str, autor: str, isbn: str, ejemplares_disponibles: int):
        Libro.validarLibro(titulo, autor, isbn, ejemplares_disponibles)
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
        Libro.validarLibro(diccionario["titulo"], diccionario["autor"], diccionario["isbn"], diccionario["ejemplares_disponibles"])
        return Libro(diccionario["titulo"], diccionario["autor"], diccionario["isbn"], diccionario["ejemplares_disponibles"])
    
    @staticmethod
    def validarLibro( titulo: str, autor: str, isbn: str, ejemplares_disponibles: int):
        if not isinstance(titulo,str) or not titulo.strip():
            raise ErrorPersonalizado("El titulo no puede ser vacio o numerico")
        if not isinstance(autor,str) or not autor.strip():
            raise ErrorPersonalizado("El autor no puede ser vacio o numerico")
        if not isinstance(isbn,str) or not isbn.strip() or not isbn.isalnum():
            raise ErrorPersonalizado("El autor no puede ser vacio y debe de ser alfanumerico sin espacio ")
        if not isinstance(ejemplares_disponibles,int) or not ejemplares_disponibles>0:
            raise ErrorPersonalizado("El ejemplares disponibles debe ser mayor que 0")
        
