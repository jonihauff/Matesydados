import bisect
import timeit
from modelos.juego import Juego


def generar_juegos(n):
    """Crea una lista de n objetos Juego para probar la búsqueda."""
    juegos = []
    for i in range(n):
        j = Juego(
            id=i,
            nombre=f"Juego {i:06d}",
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


def busqueda_secuencial(lista, nombre_buscado):
    """Búsqueda lineal recorriendo uno por uno los elementos."""
    nombre_lower = nombre_buscado.lower()
    for item in lista:
        if item.get_nombre().lower() == nombre_lower:
            return item
    return None


def busqueda_binaria(lista_ordenada, nombres_ordenados, nombre_buscado):
    """Búsqueda binaria sobre listas previamente ordenadas."""
    idx = bisect.bisect_left(nombres_ordenados, nombre_buscado.lower())
    if (
        idx < len(nombres_ordenados)
        and nombres_ordenados[idx] == nombre_buscado.lower()
    ):
        return lista_ordenada[idx]
    return None


def ejecutar_mediciones():
    tamaños = [100, 1000, 10000, 100000]

    print("=========================================================")
    print("MEDICIÓN 1 Y 2: SECUENCIAL VS. BINARIA")
    print("=========================================================")
    print(f"{'N Elementos':<12} | {'Secuencial (ms)':<15} | {'Binaria (ms)':<15}")
    print("---------------------------------------------------------")

    for n in tamaños:
        lista = generar_juegos(n)
        buscado = f"Juego {n - 1:06d}"  # Peor caso

        # Preparamos la estructura ordenada fuera del cronómetro
        lista_ordenada = sorted(lista, key=lambda j: j.get_nombre().lower())
        nombres_ordenados = [j.get_nombre().lower() for j in lista_ordenada]

        # 1. Medición Búsqueda Secuencial
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

        # 2. Medición Búsqueda Binaria
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

        print(f"{n:<12} | {t_sec:<15.4f} | {t_bin:<15.4f}")

    print("=========================================================")


if __name__ == "__main__":
    ejecutar_mediciones()