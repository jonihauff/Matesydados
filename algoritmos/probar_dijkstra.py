from algoritmos.dijkstra import dlista


def main():
    # Grafo no dirigido de ejemplo:
    # 0-1 cuesta 1; 0-2 cuesta 1; 1-2 cuesta 0.25;
    # 1-3 cuesta 1; 2-3 cuesta 0.5.
    grafo = {
        0: {1: 1.0, 2: 1.0},
        1: {0: 1.0, 2: 0.25, 3: 1.0},
        2: {0: 1.0, 1: 0.25, 3: 0.5},
        3: {1: 1.0, 2: 0.5},
    }

    origen = 0
    destino = 3
    esperado = ([0, 2, 3], 1.5)

    resultado = dlista(grafo, origen, destino)

    print(f"Camino de {origen} a {destino}")
    print("Esperado:", esperado)
    print("Obtenido:", resultado)

    if resultado == esperado:
        print("Prueba correcta.")
    else:
        print("La prueba no coincide con el resultado esperado.")


if __name__ == "__main__":
    main()
    