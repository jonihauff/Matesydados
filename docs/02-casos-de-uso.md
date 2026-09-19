## Diagrama de Casos de Uso

```mermaid
graph LR
    subgraph Mateydados ["Sistema Mateydados"]
        CU1(("CU01: Buscar juego por nombre"))
        CU2(("CU02: Filtrar por categoría"))
        CU3(("CU03: Mostrar todos los juegos"))
        CU4(("CU04: Salir del sistema"))
    end

    Usuario((Usuario)) --- CU1
    Usuario --- CU2
    Usuario --- CU3
    Usuario --- CU4
```



  ---

### CU 2: Filtrar por categoría
* **Actor:** Usuario
* **Precondición:** El catálogo de juegos está cargado en memoria.
* **Flujo Principal:**
  1. El usuario selecciona la opción `2` ("Filtrar por categoría") en la terminal.
  2. El sistema solicita ingresar el nombre de la categoría buscada (ej. "Estrategia").
  3. El usuario ingresa la categoría.
  4. El sistema recorre los objetos `Juego` en `Catalogo` recopilando aquellos cuya lista de categorías incluya el texto ingresado.
  5. El sistema imprime en pantalla la lista de juegos filtrados con sus respectivos atributos.
* **Flujo Alternativo:**
  * Si ningún juego coincide con la categoría indicada, el sistema muestra el mensaje: *"No se encontraron juegos pertenecientes a la categoría ingresada"*.

  ---

### CU 3: Mostrar todos los juegos
* **Actor:** Usuario
* **Precondición:** El catálogo de juegos está cargado en memoria.
* **Flujo Principal:**
  1. El usuario selecciona la opción `3` ("Mostrar todos los juegos") en el menú principal.
  2. El sistema invoca al método `mostrar_todos()` de la clase `Catalogo`.
  3. El sistema imprime en la consola la ficha completa de cada uno de los juegos cargados en el dataset.
* **Flujo Alternativo:**
  * Si el catálogo se encuentra vacío, el sistema indica: *"No hay juegos cargados"*.


