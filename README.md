# Sistema de Gestión de Biblioteca

Este proyecto implementa una clase `Biblioteca` para gestionar una colección de libros. Permite agregar libros, buscar por título o autor, prestar y devolver ejemplares, y listar todos los libros registrados.


## Funcionalidades

### `agregar_libros(libro: Libro)`
Agrega un libro a la biblioteca usando su ISBN como clave única.

### `buscar_por_titulo(titulo: str) -> list`
Devuelve una lista de libros cuyo título coincide exactamente con el proporcionado.

### `buscar_por_autor(autor: str) -> list`
Devuelve una lista de libros escritos por el autor proporcionado.

### `prestar_libro(isbn: str) -> bool`
Disminuye en uno la cantidad de ejemplares disponibles si hay disponibilidad. Devuelve `True` si fue exitoso.

### `devolver_libro(isbn: str) -> bool`
Aumenta en uno la cantidad de ejemplares disponibles. Devuelve `True` si la devolución fue exitosa.

### `listar_libros()`
Muestra todos los libros disponibles en la biblioteca.
