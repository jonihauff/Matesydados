import time
from estructuras.avl import AVL
from estructuras.arbol_binario import ArbolBST  # Asegurate de que el nombre del archivo del BST coincida con tu proyecto

def comparar_bst_vs_avl(lista_datos, clave):
    bst = ArbolBST()
    for d in lista_datos:
        bst.insertar(d, clave=clave)

    avl = AVL()
    for d in lista_datos:
        avl.insertar(d, clave=clave)

    valor_test = clave(lista_datos[-1])

    inicio = time.time()
    for _ in range(1000):
        bst.buscar(valor_test, clave=clave)
    tiempo_bst = (time.time() - inicio) * 1000

    inicio = time.time()
    for _ in range(1000):
        avl.buscar(valor_test, clave=clave)
    tiempo_avl = (time.time() - inicio) * 1000

    return {
        "altura_bst": bst.altura(),
        "altura_avl": avl.altura(),
        "tiempo_bst_ms": tiempo_bst,
        "tiempo_avl_ms": tiempo_avl,
        "mejor_balance": avl.altura() < bst.altura(),
    }

if __name__ == "__main__":
    class Elemento:
        def __init__(self, nombre, valor):
            self.nombre = nombre
            self.valor = valor

        def __repr__(self):
            return f"{self.nombre}({self.valor})"

    # Insertar en ORDEN ALFABÉTICO para mostrar el desbalance del BST
    datos = [
        Elemento("A", 1), Elemento("B", 2), Elemento("C", 3),
        Elemento("D", 4), Elemento("E", 5), Elemento("F", 6),
        Elemento("G", 7), Elemento("H", 8), Elemento("I", 9),
        Elemento("J", 10),
    ]

    avl = AVL()
    for d in datos:
        avl.insertar(d, clave=lambda x: x.nombre.lower())

    print("=== AVL con datos ordenados ===")
    print("Altura del AVL:", avl.altura())
    print("Cantidad de nodos:", len(avl))
    print()
    
    print("--- preorder (muestra el balance tras rotaciones) ---")
    for e in avl.preorder():
        print(" ", e)

    print("\n=== Comparación BST vs AVL ===")
    resultado = comparar_bst_vs_avl(datos, clave=lambda x: x.nombre.lower())
    print(f"  Altura BST degenerado: {resultado['altura_bst']}")
    print(f"  Altura AVL balanceado: {resultado['altura_avl']}")
    print(f"  Tiempo de búsqueda BST (1000 iteraciones): {resultado['tiempo_bst_ms']:.4f} ms")
    print(f"  Tiempo de búsqueda AVL (1000 iteraciones): {resultado['tiempo_avl_ms']:.4f} ms")