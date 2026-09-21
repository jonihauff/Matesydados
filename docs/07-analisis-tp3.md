# Análisis TP3 — Árbol Binario de Búsqueda
## 1. ¿Qué resolvimos?
Incorporamos un **árbol binario de búsqueda (BST)** para resolver la
búsqueda por título de forma más eficiente.
## 2. Clave de ordenamiento
Utilizo el ordenamiento por nombre del juego porque es el principal metodo que va a utilizar el usuario para buscar.
## 3. Prueba del árbol
Salida de `python algoritmos/probar_bst.py`:
Altura del árbol: 3

--- inorder (ordenado alfabéticamente) ---
  Azul (rating 8.5)
  Carcassonne (rating 7.8)
  Catan (rating 8.0)
  Dixit (rating 7.5)
  Pandemic (rating 8.2)

--- preorder ---
  Catan
  Carcassonne
  Azul
  Dixit
  Pandemic

--- postorder ---
  Azul
  Carcassonne
  Pandemic
  Dixit
  Catan

--- búsquedas ---
Buscar 'catan': Catan (rating 8.0)
Buscar 'zzz': None
## 4. Comparación de tiempos
En la tabla siguiente, los tiempos son **reales**, sacados con nuestro
script `algoritmos/medir_tiempos.py`. NO inventar números.
| N elementos | Secuencial (ms) | Binaria (ms) | Árbol BST (ms) |
|---|---:|---:|---:|
| 100 | [0.0087] | [0.0003] | [0.0016] |
| 1.000 | [0.0679] | [0.0003] | [0.0023] |
| 10.000 | [0.6845] | [0.0003] | [0.0033] |
| 100.000 | [7.3185] | [0.0004] | [0.0018] |
## 5. Análisis de complejidad
- **Búsqueda secuencial:** O(n). Recorre toda la lista en el peor caso.
- **Búsqueda binaria:** O(log n) pero exige lista ordenada (ordenar cuesta O(n log n) una s
- **Búsqueda en árbol:** O(log n) promedio si el árbol está balanceado;
O(n) en el peor caso si está degenerado (como una lista).
- **Inserción en árbol:** O(log n) promedio, O(n) peor caso.
- **Recorridos (inorder, preorder, postorder):** O(n), porque visitan cada nodo 1 vez.
## 6. Conclusión
La elección es el arbol binario BST. Si bien para 100 elementos una busqueda secuencial puede parecer suficiente en grandes volumenes de datos como en 100.000 se ve una diferencia de velocidad notable (7.3185 vs 0.0018). Con respecto a la busqueda binaria si bien tiene un velocidad muy similar $O(\log n)$, tiene una diferencia de costo en la modificacion y estructura: insertar o eliminar tiene costo $O(n)$ por el desplazamiento de elementos en la memoria mientras que el arbol BST permite inserciones mas eficienetes $O(\log n)$. Si pienso en un catalogo que va a ir creciendo con nuevos juegos, expanciones,actualizaciones etc. conviene el arból.
## 7. Errores o dudas que tuvimos
Dificultades en terminar de comprender la conveniencia del arbol sobre la busqueda binaria por tener resultados similares en el test. se soluciono profundizando sobre la eficiencia, en modificacion y inicializacion. 
Al integrar la búsqueda por BST en la terminal, se presentó un error TypeError: object of type 'Juego' has no len() debido a que la interfaz esperaba una lista para iterar, cuando la función buscar() del árbol devuelve directamente un único objeto Juego (o None). Se corrigió adaptando la función _buscar_por_nombre() en la Terminal para validar la existencia con is None.