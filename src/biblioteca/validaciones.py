
class Validaciones:
    
    @staticmethod
    def es_titulo_valido(titulo: str):
        return isinstance(titulo, str) and  titulo.strip()

    @staticmethod
    def es_autor_valido(autor: str):
        return isinstance(autor, str) and  autor.strip()

    @staticmethod
    def es_isbn_valido(isbn: str):
        return isinstance(isbn, str) and isbn.strip() and isbn.isalnum()

    @staticmethod
    def es_ejemplares_validos(ejemplares_disponibles: int):
        return isinstance(ejemplares_disponibles, int) and ejemplares_disponibles >= 0
