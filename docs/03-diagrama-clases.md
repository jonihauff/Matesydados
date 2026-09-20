# Diagrama de Clases (Notación UML)

```mermaid
classDiagram
    class Juego {
        -int _id
        -str _nombre
        -int _año
        -int _min_jugadores
        -int _max_jugadores
        -int _edad_min
        -int _tiempo_min
        -int _tiempo_max
        -list _categorias
        -list _mecanicas
        -str _modo
        -float _rating
        +get_id() int
        +get_nombre() str
        +get_año() int
        +get_min_jugadores() int
        +get_max_jugadores() int
        +get_edad_min() int
        +get_tiempo_min() int
        +get_tiempo_max() int
        +get_categorias() list
        +get_mecanicas() list
        +get_modo() str
        +get_rating() float
        +__repr__() str
    }

    class Catalogo {
        -list _juegos
        +cargar_datos() void
        +mostrar_todos() list
        +filtrar_por_categoria(categoria_buscada) list
        +obtener_categorias_disponibles() list
        +buscar_por_nombre(nombre) list
        +__len__() int
    }

    class Terminal {
        -Catalogo _catalogo
        +mostrar_menu() void
        +inicio() void
        -_mostrar_todos() void
        -_filtrar_por_categoria() void
        -_buscar_por_nombre() void
    }

    Terminal --> Catalogo : usa
    Catalogo "1" o-- "*" Juego : contiene
    ```
