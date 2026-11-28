# TP9 — Caminos mínimos con Dijkstra

## 1. Objetivo
En TP9 agregamos la búsqueda del camino de menor costo entre dos juegos del grafo de relaciones. El resultado incluye la secuencia completa de juegos y el costo acumulado.

## 2. Modelo de costo
Cada vértice representa un juego, dos juegos están unidos si comparten al menos una categoría o mecánica.
El peso de una arista se define como: peso = 1 / cantidad de etiquetas compartidas
Por ejemplo, si dos juegos comparten cuatro categorías o mecánicas, el peso de su arista es 0,25. Si comparten una, el peso es 1. Por lo tanto, un peso menor representa una relación directa más fuerte.
El costo de un camino es la suma de los pesos de sus aristas. Dijkstra busca minimizar ese costo acumulado; no busca necesariamente el camino con menos saltos.

## 3. Algoritmo elegido
Se eligió Dijkstra porque el grafo es ponderado y todos sus pesos son positivos. El grafo es no dirigido, así que cada relación se puede recorrer en ambas direcciones.

## 4. Complejidad
Sea `V` la cantidad de vértices y `E` la cantidad de aristas alcanzables desde el origen.
La función usa una lista de adyacencia y una cola de prioridad. Como puede insertar nuevas entradas al heap cuando mejora una distancia, su complejidad temporal es O((V + E) log E). En un grafo simple, también se suele expresar como O((V + E) log V).
Las distancias y los predecesores ocupan O(V). El heap puede acumular entradas pendientes repetidas, hasta O(E), por lo que el espacio auxiliar es O(V + E). Reconstruir la ruta requiere O(V) como máximo.
La construcción del grafo es un proceso separado: actualmente compara pares de juegos y tiene costo O(n²). Ese costo no está incluido en la complejidad de Dijkstra.

## 5. Caso de prueba controlado
El algoritmo se comprobó con un grafo ponderado pequeño definido en `algoritmos/probar_dijkstra.py`. La prueba busca el camino de menor costo desde el vértice `0` hasta el vértice `3`.
El resultado esperado es la ruta `[0, 2, 3]`, con costo total `1.5`. Esta ruta es más económica que las alternativas: `0 → 1 → 3`, de costo `2`, y `0 → 1 → 2 → 3`, de costo `1.75`.
Resultado obtenido en terminal:
Camino de 0 a 3
Esperado: ([0, 2, 3], 1.5)
Obtenido: ([0, 2, 3], 1.5)
Prueba correcta.
Se confirma que dlista obtiene la ruta con el costo minimo esperado para el grafo.