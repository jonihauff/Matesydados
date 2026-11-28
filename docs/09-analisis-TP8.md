# TP8 — Recorridos BFS y DFS

## 1. Objetivo
Se incorporan los recorridos BFS y DFS sobre el grafo de juegos relacionados. Ambos partiendo de un juego inicial y visitan los juegos alcanzables desde él pero en distinto orden.
Para el proyecto cada vértice representa un juego y las aristas las relaciones que pueden existir si comparten por lo menos una categoría o mecánica.

## 2. Recorrido BFS
BFS (búsqueda en amplitud) visita primero el vértice inicial y luego sus vecinos directos. Después visita los vecinos de esos vecinos y continúa por niveles.
La implementación usa una cola (FIFO). Cada vértice se marca como visitado cuando se agrega a la cola, para evitar agregarlo varias veces. El método devuelve los índices de los juegos en el orden en que fueron visitados; luego el catálogo los convierte en objetos Juego.
La implementación actual recorre todos los vértices alcanzables desde el inicio, no registra explícitamente la distancia de cada juego.

## 3. Recorrido DFS
DFS (búsqueda en profundidad) avanza por una conexión y continúa desde allí todo lo posible antes de retroceder y explorar otras conexiones.
La implementación usada por el catálogo es iterativa y emplea una pila LIFO. También existe una variante recursiva en Recorridos, pero el catálogo llama a dfs_iterativo().
En la aplicación, la opción “Demostración DFS” permite observar una exploración en profundidad desde un juego elegido y al igual que BFS, recorre todos los vértices alcanzables desde el inicio y no usa los pesos de las aristas.

## 4. Comparación
BFS puede encontrar caminos con la menor cantidad de aristas en un grafo no ponderado si se registra la distancia o se detiene al encontrar el objetivo. La versión actual solo devuelve el orden de visita; no devuelve un camino ni una distancia.
DFS es útil para recorrer una componente conectada y observar una ruta de exploración profunda, pero no garantiza encontrar el camino con menos aristas.

## 5. Complejidad
Ambos algoritmos examinan los vecinos de cada vértice alcanzado, por lo que su tiempo es O(V + E). El tiempo depende de la parte del grafo alcanzable desde el vértice inicial; en el peor caso, esa parte puede incluir todo el grafo.
BFS marca los vértices al agregarlos a la cola, por lo que no agrega repetidamente el mismo vértice. En la versión iterativa actual de DFS, algunos vértices pueden quedar repetidos temporalmente en la pila porque se marcan como visitados al extraerlos. Por eso la pila puede contener hasta O(E) entradas pendientes en el peor caso.
La construcción actual del grafo compara pares de juegos y tiene un costo separado de O(n²).
