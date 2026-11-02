# Matesydados

## Flujo de Datos del Sistema

```mermaid
flowchart LR
    subgraph Datos
        JSON["datos/juegos_500.json"]
        JER["jerarquia_categorias<br/>servicios/jerarquia_categorias.py"]
        FACTORY["crear_arbol_categorias()"]
    end

    subgraph Catalogo_y_dominio
        CAT["Catalogo"]
        JUEGO["Objetos Juego<br/>categorias y mecanicas"]
        LISTA["Lista _juegos"]
    end

    subgraph Estructuras
        AVL["AVL _arbol_nombre<br/>ordenado por nombre"]
        ARBOL["ArbolGeneral _arbol_categorias<br/>grupos y categorías"]
    end

    subgraph Interfaz
        TERMINAL["Terminal"]
        BUSCAR["Buscar juego por nombre"]
        CATEGORIAS["Buscar por categoría"]
        TODOS["Mostrar todos los juegos"]
    end

    JSON -->|"cargar_datos()"| CAT
    CAT -->|"crea"| JUEGO
    JUEGO -->|"append"| LISTA
    JUEGO -->|"insertar por nombre"| AVL

    JER --> FACTORY
    CAT -->|"inicializa categorías"| FACTORY
    FACTORY -->|"construye"| ARBOL

    TERMINAL --> BUSCAR
    BUSCAR -->|"buscar_por_nombre()"| CAT
    CAT -->|"buscar()"| AVL
    AVL -->|"Juego o None"| CAT
    CAT --> TERMINAL

    TERMINAL --> CATEGORIAS
    CATEGORIAS -->|"solicita grupos y categorías"| CAT
    CAT -->|"consulta"| ARBOL
    ARBOL -->|"devuelve grupos y categorías"| CAT
    CAT --> TERMINAL
    TERMINAL -->|"categoría elegida"| CAT
    CAT -->|"filtrar_por_categoria()"| LISTA
    LISTA -->|"compara con Juego.categorias"| CAT
    CAT -->|"juegos encontrados"| TERMINAL

    TERMINAL --> TODOS
    TODOS -->|"mostrar_todos()"| CAT
    CAT --> LISTA
    LISTA -->|"lista de juegos"| CAT
    CAT --> TERMINAL
```
