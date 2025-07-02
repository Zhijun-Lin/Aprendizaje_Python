from biblioteca import Biblioteca
from libro import Libro

if __name__ == "__main__":
    operacion = -1
    bilbioteca = Biblioteca()
    while operacion != 0:

        print("Que quieres hacer?")
        print("1 - Agregar libros")
        print("2 - Buscar por titulo")
        print("3 - Buscar por Autor")
        print("4 - Prestar libro")
        print("5 - Devolver libro")
        print("6 - Listar libro")
        print("0 - Salir")
        operacion = int(input("Indroduce el numero de operacion: "))

        match operacion:
            case 1:
                titulo = input("Indroduce el titulo de libro: ")
                autor = input("Indorduce el autor: ")
                isbn = input("Indroduce el ISBN: ")
                disponible = int(input("Indroduce la cantidad disponible: "))
                bilbioteca.agregar_libros(Libro(titulo, autor, isbn, disponible))
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
