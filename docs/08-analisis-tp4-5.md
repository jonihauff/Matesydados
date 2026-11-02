# Análisis TP4 + TP5 — AVL y Árbol General

## 1. ¿Qué resuelven estas etapas?
En esta etapa incorporamos dos estructuras de datos que resuelven problemas distintos dentro del
sistema:
En TP4 incorporamos un árbol AVL para buscar juegos por nombre manteniendo el árbol balanceado aunque los datos se inserten en orden. 
En TP5 incorporamos un árbol general para representar y explorar una jerarquía de categorías de juegos de mesa.

## 2. TP4 — Árbol AVL

### 2.1 ¿Por qué AVL y no un BST común?
Un árbol binario de búsqueda común puede desbalancearse si se insertan datos ordenados. En ese caso, podria degenerarse en una forma similar a una lista y una búsqueda puede requerir recorrer muchos nodos con complejidad O(n).
El AVL realiza rotaciones automaticas durante la inserción para mantener el árbol balanceado, conservando una complejidad O(log n).

### 2.2 Rotaciones implementadas

- **Izquierda-Izquierda:** rotación simple derecha.
- **Derecha-Derecha:** rotación simple izquierda.
- **Izquierda-Derecha:** rotación doble izquierda-derecha.
- **Derecha-Izquierda:** rotación doble derecha-izquierda.

### 2.3 Caso de desbalance generados
Insertamos datos en orden alfabético (escenario que rompe un BST común) y demostramos que el AVL mantiene la altura controlada.
Datos de prueba:
A, B, C, D, E, F, G, H, I, J (10 elementos en orden)

### 2.4 Comparación BST vs AVL
Se buscó el último elemento insertado (caso mas desfavorable para el BST con claves ordenadas). Se realizan 1000 iteraciones de busqueda.

| Métrica                         | BST común | AVL       |
|---------------------------------|----------:|----------:|
| Altura con datos ordenados      |        10 |         4 |
| Búsqueda con 10 datos ordenados | 2.6457 ms | 0.8879 ms |
| Complejidad peor caso búsqueda  |      O(n) |  O(log n) |
| Complejidad promedio inserción  |  O(log n) |  O(log n) |


Justificación: Insertar 10 elementos ordenados genera un BST con altura 10 (una cadena), mientras
el AVL tiene altura 4 como máximo. La diferencia se amplifica con datasets grandes.

### 2.5 Prueba del AVL
Salida de [python algoritmos/probar_avl](algoritmos/probar_avl.py) 

```text
=== AVL con datos ordenados ===

Altura del AVL: 4
Cantidad de nodos: 10

--- preorder (muestra el balance tras rotaciones) ---
  D(4)
  B(2)
  A(1)
  C(3)
  H(8)
  F(6)
  E(5)
  G(7)
  I(9)
  J(10)

=== Comparación BST vs AVL ===
  Altura BST degenerado: 10
  Altura AVL balanceado: 4
  Tiempo de búsqueda BST (1000 iteraciones): 2.6457 ms
  Tiempo de búsqueda AVL (1000 iteraciones): 0.8879 ms
```
## 3 TP5 - Árbol general

### 3.1 Jerarquia elegida del dominio
La jerarquía se definio a partir de 80 categorias presentes en el dataset de 500 juegos. La raiz es "juegos de mesa", debajo se crearon 9 grupos y las categorias propias de cada grupo.

```text
Juegos de mesa
├── Épocas históricas (7)
│   ├── Antigüedad
│   ├── Era de la Razón
│   ├── Medieval
│   ├── Napoleónico
│   ├── Posnapoleónico
│   ├── Prehistoria
│   └── Renacimiento
├── Guerras y conflictos (10)
│   ├── Guerra civil
│   ├── Guerra Civil Estadounidense
│   ├── Guerra de Independencia Estadounidense
│   ├── Guerra de Vietnam
│   ├── Guerra moderna
│   ├── Picas y arcabuces
│   ├── Primera Guerra Mundial
│   ├── Segunda Guerra Mundial
│   ├── Combate
│   └── Wargame
├── Ficción y ambientación (13)
│   ├── Aventura
│   ├── Asesinato/Misterio
│   ├── Basado en novelas
│   ├── Ciencia ficción
│   ├── Cómic / Tira cómica
│   ├── Fantasía
│   ├── Libro
│   ├── Mitología
│   ├── Piratas
│   ├── Temática de cine / TV / radio
│   ├── Temática de videojuegos
│   ├── Terror
│   └── Zombis
├── Sociedad y cultura (10)
│   ├── Árabe
│   ├── Deportes
│   ├── Humor
│   ├── Espías/Agentes secretos
│   ├── Industria / Manufactura
│   ├── Lejano Oeste estadounidense
│   ├── Mafia
│   ├── Música
│   ├── Político
│   └── Religioso
├── Naturaleza y viajes (8)
│   ├── Agricultura
│   ├── Animales
│   ├── Aviación / Vuelo
│   ├── Medioambiental
│   ├── Náutico
│   ├── Transporte
│   ├── Trenes
│   └── Viajes
├── Civilización y desarrollo (8)
│   ├── Civilización
│   ├── Economía
│   ├── Construcción de ciudades
│   ├── Construcción de territorios
│   ├── Estrategia abstracta
│   ├── Exploración
│   ├── Exploración espacial
│   └── Sistema de juego
├── Competencia e interacción (7)
│   ├── Acción / Destreza
│   ├── Carreras
│   ├── Faroleo
│   ├── Juego de fiesta
│   ├── Negociación
│   ├── Tiempo real
│   └── Trivia
├── Ingenio y resolución de problemas (7)
│   ├── Deducción
│   ├── Juego de palabras
│   ├── Laberinto
│   ├── Matemáticas
│   ├── Memoria
│   ├── Números
│   └── Rompecabezas
└── Formatos, público y edición (10)
    ├── Componentes coleccionables
    ├── Dados
    ├── Educativo
    ├── Electrónico
    ├── Expansión de juego base
    ├── Imprimir y jugar
    ├── Juego de cartas
    ├── Juego infantil
    ├── Miniaturas
    └── Para adultos
```
Los grupos son una organización propia del proyecto, estos permiten recorrer las categorías por grupos y después seleccionar una categoría concreta que se utiliza para filtrar los juegos del catálogo.

¿Por qué esta jerarquía?
- Los géneros son una clasificación natural del dominio.
- Permite al usuario explorar categorías jerárquicas.
- Se conecta con el árbol AVL: el AVL busca por título, el árbol general organiza por categoría.

### 3.2 Recorridos implementados

| Recorrido | Cómo visita los nodos | Complejidad |
|---|---|---:|
| Amplitud (BFS) | Nivel por nivel, desde la raíz | O(n) |
| Profundidad preorder | Nodo y luego sus hijos | O(n) |
| Profundidad postorder | Hijos y luego el nodo | O(n) |

### 3.3 Prueba del árbol general

=== Árbol General de Categorías ===
Raíz: juegos de mesa
Altura: 3
Cantidad de nodos: 90

--- Recorrido en amplitud ---
['juegos de mesa', 'Épocas históricas', 'Guerras y conflictos', 'Ficción y ambientación', 'Sociedad y cultura', 'Naturaleza y viajes', 'Civilización y desarrollo', 'Competencia e interacción', 'Ingenio y resolución de problemas', 'Formatos, público y edición', 'Antigüedad', 'Era de la Razón', 'Medieval', 'Napoleónico', 'Posnapoleónico', 'Prehistoria', 'Renacimiento', 'Guerra civil', 'Guerra Civil Estadounidense', 'Guerra de Independencia Estadounidense', 'Guerra de Vietnam', 'Guerra moderna', 'Picas y arcabuces', 'Primera Guerra Mundial', 'Segunda Guerra Mundial', 'Combate', 'Wargame', 'Aventura', 'Asesinato/Misterio', 'Basado en novelas', 'Ciencia ficción', 'Cómic / Tira cómica', 'Fantasía', 'Libro', 'Mitología', 'Piratas', 'Temática de cine / TV / radio', 'Temática de videojuegos', 'Terror', 'Zombis', 'Árabe', 'Deportes', 'Humor', 'Espías/Agentes secretos', 'Industria / Manufactura', 'Lejano Oeste estadounidense', 'Mafia', 'Música', 'Político', 'Religioso', 'Agricultura', 'Animales', 'Aviación / Vuelo', 'Medioambiental', 'Náutico', 'Transporte', 'Trenes', 'Viajes', 'Civilización', 'Economía', 'Construcción de ciudades', 'Construcción de territorios', 'Estrategia abstracta', 'Exploración', 'Exploración espacial', 'Sistema de juego', 'Acción / Destreza', 'Carreras', 'Faroleo', 'Juego de fiesta', 'Negociación', 'Tiempo real', 'Trivia', 'Deducción', 'Juego de palabras', 'Laberinto', 'Matemáticas', 'Memoria', 'Números', 'Rompecabezas', 'Componentes coleccionables', 'Dados', 'Educativo', 'Electrónico', 'Expansión de juego base', 'Imprimir y jugar', 'Juego de cartas', 'Juego infantil', 'Miniaturas', 'Para adultos']

--- Recorrido en profundidad (preorder) ---
['juegos de mesa', 'Épocas históricas', 'Antigüedad', 'Era de la Razón', 'Medieval', 'Napoleónico', 'Posnapoleónico', 'Prehistoria', 'Renacimiento', 'Guerras y conflictos', 'Guerra civil', 'Guerra Civil Estadounidense', 'Guerra de Independencia Estadounidense', 'Guerra de Vietnam', 'Guerra moderna', 'Picas y arcabuces', 'Primera Guerra Mundial', 'Segunda Guerra Mundial', 'Combate', 'Wargame', 'Ficción y ambientación', 'Aventura', 'Asesinato/Misterio', 'Basado en novelas', 'Ciencia ficción', 'Cómic / Tira cómica', 'Fantasía', 'Libro', 'Mitología', 'Piratas', 'Temática de cine / TV / radio', 'Temática de videojuegos', 'Terror', 'Zombis', 'Sociedad y cultura', 'Árabe', 'Deportes', 'Humor', 'Espías/Agentes secretos', 'Industria / Manufactura', 'Lejano Oeste estadounidense', 'Mafia', 'Música', 'Político', 'Religioso', 'Naturaleza y viajes', 'Agricultura', 'Animales', 'Aviación / Vuelo', 'Medioambiental', 'Náutico', 'Transporte', 'Trenes', 'Viajes', 'Civilización y desarrollo', 'Civilización', 'Economía', 'Construcción de ciudades', 'Construcción de territorios', 'Estrategia abstracta', 'Exploración', 'Exploración espacial', 'Sistema de juego', 'Competencia e interacción', 'Acción / Destreza', 'Carreras', 'Faroleo', 'Juego de fiesta', 'Negociación', 'Tiempo real', 'Trivia', 'Ingenio y resolución de problemas', 'Deducción', 'Juego de palabras', 'Laberinto', 'Matemáticas', 'Memoria', 'Números', 'Rompecabezas', 'Formatos, público y edición', 'Componentes coleccionables', 'Dados', 'Educativo', 'Electrónico', 'Expansión de juego base', 'Imprimir y jugar', 'Juego de cartas', 'Juego infantil', 'Miniaturas', 'Para adultos']

--- Recorrido en profundidad (postorder) ---
['Antigüedad', 'Era de la Razón', 'Medieval', 'Napoleónico', 'Posnapoleónico', 'Prehistoria', 'Renacimiento', 'Épocas históricas', 'Guerra civil', 'Guerra Civil Estadounidense', 'Guerra de Independencia Estadounidense', 'Guerra de Vietnam', 'Guerra moderna', 'Picas y arcabuces', 'Primera Guerra Mundial', 'Segunda Guerra Mundial', 'Combate', 'Wargame', 'Guerras y conflictos', 'Aventura', 'Asesinato/Misterio', 'Basado en novelas', 'Ciencia ficción', 'Cómic / Tira cómica', 'Fantasía', 'Libro', 'Mitología', 'Piratas', 'Temática de cine / TV / radio', 'Temática de videojuegos', 'Terror', 'Zombis', 'Ficción y ambientación', 'Árabe', 'Deportes', 'Humor', 'Espías/Agentes secretos', 'Industria / Manufactura', 'Lejano Oeste estadounidense', 'Mafia', 'Música', 'Político', 'Religioso', 'Sociedad y cultura', 'Agricultura', 'Animales', 'Aviación / Vuelo', 'Medioambiental', 'Náutico', 'Transporte', 'Trenes', 'Viajes', 'Naturaleza y viajes', 'Civilización', 'Economía', 'Construcción de ciudades', 'Construcción de territorios', 'Estrategia abstracta', 'Exploración', 'Exploración espacial', 'Sistema de juego', 'Civilización y desarrollo', 'Acción / Destreza', 'Carreras', 'Faroleo', 'Juego de fiesta', 'Negociación', 'Tiempo real', 'Trivia', 'Competencia e interacción', 'Deducción', 'Juego de palabras', 'Laberinto', 'Matemáticas', 'Memoria', 'Números', 'Rompecabezas', 'Ingenio y resolución de problemas', 'Componentes coleccionables', 'Dados', 'Educativo', 'Electrónico', 'Expansión de juego base', 'Imprimir y jugar', 'Juego de cartas', 'Juego infantil', 'Miniaturas', 'Para adultos', 'Formatos, público y edición', 'juegos de mesa']

--- Niveles ---
  Nivel 0: ['juegos de mesa']
  Nivel 1: ['Épocas históricas', 'Guerras y conflictos', 'Ficción y ambientación', 'Sociedad y cultura', 'Naturaleza y viajes', 'Civilización y desarrollo', 'Competencia e interacción', 'Ingenio y resolución de problemas', 'Formatos, público y edición']
  Nivel 2: ['Antigüedad', 'Era de la Razón', 'Medieval', 'Napoleónico', 'Posnapoleónico', 'Prehistoria', 'Renacimiento', 'Guerra civil', 'Guerra Civil Estadounidense', 'Guerra de Independencia Estadounidense', 'Guerra de Vietnam', 'Guerra moderna', 'Picas y arcabuces', 'Primera Guerra Mundial', 'Segunda Guerra Mundial', 'Combate', 'Wargame', 'Aventura', 'Asesinato/Misterio', 'Basado en novelas', 'Ciencia ficción', 'Cómic / Tira cómica', 'Fantasía', 'Libro', 'Mitología', 'Piratas', 'Temática de cine / TV / radio', 'Temática de videojuegos', 'Terror', 'Zombis', 'Árabe', 'Deportes', 'Humor', 'Espías/Agentes secretos', 'Industria / Manufactura', 'Lejano Oeste estadounidense', 'Mafia', 'Música', 'Político', 'Religioso', 'Agricultura', 'Animales', 'Aviación / Vuelo', 'Medioambiental', 'Náutico', 'Transporte', 'Trenes', 'Viajes', 'Civilización', 'Economía', 'Construcción de ciudades', 'Construcción de territorios', 'Estrategia abstracta', 'Exploración', 'Exploración espacial', 'Sistema de juego', 'Acción / Destreza', 'Carreras', 'Faroleo', 'Juego de fiesta', 'Negociación', 'Tiempo real', 'Trivia', 'Deducción', 'Juego de palabras', 'Laberinto', 'Matemáticas', 'Memoria', 'Números', 'Rompecabezas', 'Componentes coleccionables', 'Dados', 'Educativo', 'Electrónico', 'Expansión de juego base', 'Imprimir y jugar', 'Juego de cartas', 'Juego infantil', 'Miniaturas', 'Para adultos']

--- Hijos de 'Ficción y ambientación' ---
['Aventura', 'Asesinato/Misterio', 'Basado en novelas', 'Ciencia ficción', 'Cómic / Tira cómica', 'Fantasía', 'Libro', 'Mitología', 'Piratas', 'Temática de cine / TV / radio', 'Temática de videojuegos', 'Terror', 'Zombis']

--- Buscar 'Sociedad y cultura' ---
Encontrado: Nodo(Sociedad y cultura)

### 3.4 Análisis de complejidad

| Operación | AVL | Árbol General |
|---|---|---|
| Inserción | O(log n) | O(1) (agregar hijo a un nodo conocido) |
| Búsqueda | O(log n) | O(n) (recorrido completo) |
| Recorrido inorder | O(n) | O(n) |
| Recorrido amplitud | O(n) | O(n) |
| Altura (peor caso) | O(log n) | O(n) (árbol degenerado) |

## 4 Conclusión
- El AVL garantiza búsquedas eficientes sin importar el orden de inserción, resolviendo el problema
principal de desbalance del BST.
- El árbol general permite organizar el dominio en jerarquías significativas que mejoran la
experiencia del usuario al explorar categorías.
- Ambas estructuras se complementan: el AVL resuelve búsqueda eficiente por clave, el árbol general
organiza la navegación por categorías.
- Ninguna de las dos se usó "por cumplir": el AVL resuelve un problema real (desbalance) y el árbol
general resuelve otro (jerarquización del dominio).

## 5 Errores o dudas que tuvimos:
La mayor dificultad fue la creación de los grupos y la organización de las categorías de manera equilibrada, que dada su gran cantidad (80), fue difícil que los grupos sean representativos de manera natural de las categorías que contienen. 
Además, el dataset utilizado (y otros disponibles), contenían estos datos en inglés, múltiples categorías similares y juegos sin categorizar, por lo que fue necesario trabajar con el dataset para adaptarlo para este trabajo.
En la búsqueda por categorías utilizada anteriormente el usuario debía escribir el nombre exacto de la categoría en el input. Se optó por una selección numérica para agilizar el acceso y evitar posibles errores de escritura del usuario.

## Datos y evidencia
- [Script de prueba del AVL](../algoritmos/probar_avl.py)
- [Script de prueba del árbol general](../algoritmos/probar_arbol_general.py)