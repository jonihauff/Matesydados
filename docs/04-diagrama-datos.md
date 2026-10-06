# Matesydados

## Flujo de Datos del Sistema

```mermaid
graph LR
    subgraph Origen de Datos
        JSON[datos/juegos.json]
    end

    subgraph Dominio
        LISTA[Lista _juegos]
        OBJETO[Objetos Juego]
    end

    subgraph Estructuras de Datos
        BST[ArbolBST — ordenado por nombre]
    end

    subgraph Servicios / Lógica
        CATALOGO[Catalogo]
    end

    subgraph Interfaz de Usuario
        UI[Terminal]
    end

    JSON -->|cargar_datos| CATALOGO
    CATALOGO -->|Instancia| OBJETO
    OBJETO -->|Almacena en| LISTA
    OBJETO -->|insertar con clave_nombre| BST

    UI -->|1. Buscar por nombre| CATALOGO
    CATALOGO -->|buscar_por_nombre| BST
    BST -->|Devuelve objeto Juego / None| CATALOGO
    CATALOGO -->|Muestra resultado| UI
