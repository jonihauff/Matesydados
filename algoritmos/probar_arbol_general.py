from servicios.jerarquia_categorias import jerarquia_categorias, crear_arbol_categorias

if __name__ == "__main__":
    # Crear un árbol de categorías de películas
    arbol = crear_arbol_categorias()
    cantidad_categorias =sum(
        len(categorias) for categorias in jerarquia_categorias.values()
    )
    print("=== Árbol General de Categorías ===")
    print("Raíz:", arbol.raiz.dato)
    print("Altura:", arbol.altura())
    print("Cantidad de nodos:", arbol.cantidad_nodos())
    print()

    print("--- Recorrido en amplitud ---")
    print(arbol.amplitud())
    print()

    print("--- Recorrido en profundidad (preorder) ---")
    print(arbol.profundidad_preorder())
    print()

    print("--- Recorrido en profundidad (postorder) ---")
    print(arbol.profundidad_postorder())
    print()

    print("--- Niveles ---")
    for i, nivel in enumerate(arbol.obtener_niveles()):
        print(f"  Nivel {i}: {nivel}")
    print()

    print("--- Hijos de 'Ficción y ambientación' ---")
    nodo_ficcion = arbol.buscar("Ficción y ambientación")
    if nodo_ficcion:
        print(arbol.listar_hijos(nodo_ficcion))

    print()
    print("--- Buscar 'Sociedad y cultura' ---")
    resultado = arbol.buscar("Sociedad y cultura")
    print("Encontrado:", resultado)
