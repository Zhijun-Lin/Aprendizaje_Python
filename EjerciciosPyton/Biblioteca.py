class Libro:
    def __init__(self,titulo,autor ,isbn,ejemplares_disponibles):
        self.titulo=titulo
        self.autor=autor
        self.isbn=isbn
        self.ejemplares_disponibles=ejemplares_disponibles
        
    def __str__(self):
        return f"Titulo: {self.titulo}, Autor: {self.autor} ISBN: {self.isbn} Disponibles: {self.ejemplares_disponibles}"
    

class Biblioteca:
    def __init__(self):
        self.libros={}
        
    def agregar_libros(self, libro : Libro):
        self.libros[libro.isbn]=libro
        
    def buscar_por_titulo (self, titulo : str):
        librosTitulo= []
        for valor in self.libros.values():
            if valor.titulo == titulo:
                librosTitulo.append(valor)
        return librosTitulo
    
    def buscar_por_autor (self, autor : str):
        librosAutor= []
        for valor in self.libros.values():
            if valor.autor == autor:
                librosAutor.append(valor)
        return librosAutor
            
    def prestar_libro(self, isbn: str):
        for clave,valor in self.libros.items():
            if clave== isbn and valor.ejemplares_disponibles > 0:
                valor.ejemplares_disponibles -= 1
                print("Prestacion exitoso")
                return True
        print("Prestacion fallido")
        return False
        
    def devolver_libro(self, isbn: str):
        for clave,valor in self.libros.items():
            if clave == isbn:
                valor.ejemplares_disponibles += 1
                print("Devolucion exitoso")
                return True
        print("Devolucion fallido")
        return False
        
    def listar_libros(self):
        for libro in self.libros.values():
            print(libro)


operacion = -1
bilbioteca = Biblioteca()
while(operacion != 0):
    
    print("Que quieres hacer?")
    print("1 - Agregar libros")
    print("2 - Buscar por titulo")
    print("3 - Buscar por Autor")
    print("4 - Prestar libro")
    print("5 - Devolver libro")
    print("6 - Listar libro")
    print("0 - Salir")
    operacion= int (input("Indroduce el numero de operacion: "))
    
    match operacion:
        case 1:
            titulo = input("Indroduce el titulo de libro: ")
            autor = input("Indorduce el autor: ")
            isbn = input("Indroduce el ISBN: ")
            disponible = int(input("Indroduce la cantidad disponible: "))
            bilbioteca.agregar_libros(Libro(titulo,autor,isbn,disponible))
        case 2:
            titulo = input("Indroduce el titulo de libro: ")
            librosEncontrado = bilbioteca.buscar_por_titulo(titulo)
            for x in librosEncontrado:
                print(x)
        case 3:
            autor = input("Indroduce el autor de libro: ")
            librosEncontrado = bilbioteca.buscar_por_autor(autor)
            for x in librosEncontrado:
                print(x)
        case 4:
            isbn = input("Indroduce el ISBN de libro: ")
            print(bilbioteca.prestar_libro(isbn))
        case 5:
            isbn = input("Indroduce el ISBN de libro: ")
            print(bilbioteca.devolver_libro(isbn))
        case 6:
            bilbioteca.listar_libros()
        case 0:
            print("Salir de sistema")