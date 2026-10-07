# Análisis TP4 + TP5 — AVL y Árbol General

## 1. ¿Qué resuelven estas etapas?
En esta etapa incorporamos dos estructuras de datos que resuelven problemas distintos dentro del
sistema:
En TP4 incorporamos un árbol AVL para buscar juegos por nombre manteniendo el árbol balanceado aunque los datos se inserten en orden. 
En TP5 incorporaremos un árbol general para representar y explorar una jerarquía de categorías de juegos de mesa.

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