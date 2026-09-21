from estructuras.arbol_binario import ArbolBST


class Juego:
    def __init__(self, titulo, rating):
        self.titulo = titulo
        self.rating = rating

    def __repr__(self):
        return f"{self.titulo} (rating {self.rating})"


def main():
    arbol = ArbolBST()
    # Lo construimos SIN orden, para que el árbol ordene solo
    datos = [
        Juego("Catan", 8.0),
        Juego("Carcassonne", 7.8),
        Juego("Dixit", 7.5),
        Juego("Pandemic", 8.2),
        Juego("Azul", 8.5),
    ]
    for d in datos:
        arbol.insertar(d, clave=lambda e: e.titulo.lower())

    print("Altura del árbol:", arbol.altura())

    print("\n--- inorder (ordenado alfabéticamente) ---")
    for e in arbol.inorder():
        print(" ", e)

    print("\n--- preorder ---")
    for e in arbol.preorder():
        print(" ", e.titulo)

    print("\n--- postorder ---")
    for e in arbol.postorder():
        print(" ", e.titulo)

    print("\n--- búsquedas ---")
    encontrado = arbol.buscar("catan", clave=lambda e: e.titulo.lower())
    print("Buscar 'catan':", encontrado)
    no_encontrado = arbol.buscar("zzz", clave=lambda e: e.titulo.lower())
    print("Buscar 'zzz':", no_encontrado)


if __name__ == "__main__":
    main()
    