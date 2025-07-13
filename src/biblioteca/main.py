from biblioteca import Biblioteca
from libro import Libro
from errorPersonalizado import ErrorPersonalizado

if __name__ == "__main__":
    operacion = -1
    biblioteca = Biblioteca()
    nombreFichero: str = "data/biblioteca.json"
    while operacion != 0:

        print("Que quieres hacer?")
        print("1 - Agregar libros")
        print("2 - Buscar por titulo")
        print("3 - Buscar por Autor")
        print("4 - Prestar libro")
        print("5 - Devolver libro")
        print("6 - Listar libro")
        print("7 - Guardar libros")
        print("8 - Cargar libros")
        print("0 - Salir")
        operacion = int(input("Indroduce el numero de operacion: "))

        match operacion:
            case 1:
                titulo = input("Indroduce el titulo de libro: ")
                autor = input("Indorduce el autor: ")
                isbn = input("Indroduce el ISBN: ")
                disponible = int(input("Indroduce la cantidad disponible: "))
                biblioteca.agregar_libros(Libro(titulo, autor, isbn, disponible))
            case 2:
                titulo = input("Indroduce el titulo de libro: ")
                librosEncontrado = biblioteca.buscar_por_titulo(titulo)
                if librosEncontrado.__len__ == 0:
                    print ("No existe libro")
                else:
                    for x in librosEncontrado:
                        print(x)
            case 3:
                autor = input("Indroduce el autor de libro: ")
                librosEncontrado = biblioteca.buscar_por_autor(autor)
                if librosEncontrado.__len__ == 0:
                    print ("No existe libro")
                else:
                    for x in librosEncontrado:
                        print(x)
            case 4:
                isbn = input("Indroduce el ISBN de libro: ")
                print(biblioteca.prestar_libro(isbn))
            case 5:
                isbn = input("Indroduce el ISBN de libro: ")
                print(biblioteca.devolver_libro(isbn))
            case 6:
                biblioteca.listar_libros()
            case 7:
                biblioteca.guardar(nombreFichero)
            case 8:
                biblioteca.cargar(nombreFichero)
            case 0:
                print("Salir de sistema")
