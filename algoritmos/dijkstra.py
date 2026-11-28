import heapq

def dlista(grafo, origen, destino):
    if origen not in grafo or destino not in grafo:
        return None

    distancias = {nodo: float("inf") for nodo in grafo}
    anteriores = {nodo: None for nodo in grafo}

    distancias[origen] = 0
    colaheap = [(0, origen)]

    while colaheap:
        distancia_actual, nodo_actual = heapq.heappop(colaheap)

        if distancia_actual > distancias[nodo_actual]:
            continue

        if nodo_actual == destino:
            break

        for vecino, peso in grafo[nodo_actual].items():
            nueva_distancia = distancia_actual + peso

            if nueva_distancia < distancias[vecino]:
                distancias[vecino] = nueva_distancia
                anteriores[vecino] = nodo_actual
                heapq.heappush(
                    colaheap,
                    (nueva_distancia, vecino)
                )

    if distancias[destino] == float("inf"):
        return None

    ruta = []
    actual = destino

    while actual is not None:
        ruta.append(actual)
        if actual == origen:
            break
        actual = anteriores[actual]

    ruta.reverse()
    return ruta, distancias[destino]