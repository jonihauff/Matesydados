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

    class ArbolBST {
        -NodoArbol raiz
        +insertar(dato, clave) None
        +buscar(valor, clave) Juego
        +inorder() list
        +preorder() list
        +postorder() list
        +altura() int
        +esta_vacio() bool
    }

    class Catalogo {
        -list _juegos
        -ArbolBST _arbol_nombre
        +cargar_datos() None
        +mostrar_todos() list
        +filtrar_por_categoria(categoria_buscada) list
        +obtener_categorias_disponibles() list
        +buscar_por_nombre(nombre) Juego
        +__len__() int
    }

    class Terminal {
        -Catalogo _catalogo
        +mostrar_menu() None
        +inicio() None
        -_mostrar_todos() None
        -_filtrar_por_categoria() None
        -_buscar_por_nombre() None
    }

    Terminal --> Catalogo : usa
    Catalogo "1" o-- "*" Juego : contiene
    Catalogo --> ArbolBST : delega búsqueda por nombre
    ArbolBST "1" o-- "*" Juego : ordena por clave nombre
    ```
