import bisect
import random
import timeit
from estructuras.arbol_binario import ArbolBST
from modelos.juego import Juego


def generar_juegos(n: int) -> list[Juego]:
    """Crea una lista de n objetos Juego para probar las búsquedas."""
    juegos = []
    for i in range(n):
        j = Juego(
            id=i,
            nombre=f"Juego {i:06d}",  # Nombres formateados para mantener orden alfabético estricto
            año=2024,
            min_jugadores=2,
            max_jugadores=4,
            edad_min=10,
            tiempo_min=30,
            tiempo_max=60,
            categorias=["Estrategia"],
            mecanicas=["Mano"],
            modo="Competitivo",
            rating=8.0,
        )
        juegos.append(j)
    return juegos


def busqueda_secuencial(lista: list[Juego], nombre_buscado: str) -> Juego | None:
    """Búsqueda lineal O(n)."""
    nombre_lower = nombre_buscado.lower()
    for item in lista:
        if item.get_nombre().lower() == nombre_lower:
            return item
    return None


def busqueda_binaria(
    lista_ordenada: list[Juego],
    nombres_ordenados: list[str],
    nombre_buscado: str,
) -> Juego | None:
    """Búsqueda binaria O(log n) sobre lista ordenada."""
    idx = bisect.bisect_left(nombres_ordenados, nombre_buscado.lower())
    if (
        idx < len(nombres_ordenados)
        and nombres_ordenados[idx] == nombre_buscado.lower()
    ):
        return lista_ordenada[idx]
    return None


def ejecutar_mediciones():
    tamaños = [100, 1000, 10000, 100000]

    print("===================================================================")
    print("MEDICIÓN COMPLETA: SECUENCIAL VS. BINARIA VS. ÁRBOL BST")
    print("===================================================================")
    print(
        f"{'N Elementos':<11} | {'Secuencial (ms)':<15} | {'Binaria (ms)':<13} | {'Árbol BST (ms)':<14}"
    )
    print("-------------------------------------------------------------------")

    clave_nombre = lambda j: j.get_nombre().lower()

    for n in tamaños:
        lista = generar_juegos(n)
        buscado = f"Juego {n - 1:06d}"  # Peor caso: el último elemento

        # --- PREPARACIÓN DE ESTRUCTURAS (FUERA DEL CRONÓMETRO) ---
        # 1. Búsqueda binaria
        lista_ordenada = sorted(lista, key=clave_nombre)
        nombres_ordenados = [clave_nombre(j) for j in lista_ordenada]

        # 2. Árbol BST (mezclamos para evitar el caso degenerado en BST)
        lista_mezclada = list(lista)
        random.seed(42)
        random.shuffle(lista_mezclada)

        arbol = ArbolBST()
        for juego in lista_mezclada:
            arbol.insertar(juego, clave_nombre)

        # --- MEDICIONES CON TIMEIT ---
        # 1. Secuencial
        t_sec = (
            min(
                timeit.repeat(
                    lambda: busqueda_secuencial(lista, buscado),
                    number=10,
                    repeat=5,
                )
            )
            / 10
            * 1000
        )

        # 2. Binaria
        t_bin = (
            min(
                timeit.repeat(
                    lambda: busqueda_binaria(
                        lista_ordenada, nombres_ordenados, buscado
                    ),
                    number=10,
                    repeat=5,
                )
            )
            / 10
            * 1000
        )

        # 3. Árbol BST
        t_arbol = (
            min(
                timeit.repeat(
                    lambda: arbol.buscar(buscado.lower(), clave_nombre),
                    number=10,
                    repeat=5,
                )
            )
            / 10
            * 1000
        )

        print(
            f"{n:<11} | {t_sec:<15.4f} | {t_bin:<13.4f} | {t_arbol:<14.4f}"
        )

    print("===================================================================")


if __name__ == "__main__":
    ejecutar_mediciones()