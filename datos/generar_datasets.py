
import csv
import json
import random
from pathlib import Path


RUTA_ORIGEN = Path("datos/origen/board_games.csv")
CARPETA_SALIDA = Path("datos")


def convertir_a_entero(valor, valor_por_defecto=0):
    """Convierte un texto a entero de forma segura."""
    try:
        return int(float(valor))
    except (TypeError, ValueError):
        return valor_por_defecto


def convertir_a_float(valor, valor_por_defecto=0.0):
    """Convierte un texto a decimal de forma segura."""
    try:
        return round(float(valor), 2)
    except (TypeError, ValueError):
        return valor_por_defecto


def convertir_a_lista(valor):
    """
    Convierte un texto separado por comas en una lista.
    Ejemplo: 'Cartas, Estrategia' -> ['Cartas', 'Estrategia']
    """
    if not valor:
        return []

    return [elemento.strip() for elemento in valor.split(",") if elemento.strip()]


def definir_modo(mecanicas):
    """Decide si el juego es cooperativo o competitivo."""
    texto_mecanicas = " ".join(mecanicas).lower()

    if "co-operative" in texto_mecanicas or "cooperative" in texto_mecanicas:
        return "cooperativo"

    return "competitivo"


def convertir_fila(fila):
    """Transforma una fila del CSV al formato que usa Mateydados."""
    categorias = convertir_a_lista(fila["category"])
    mecanicas = convertir_a_lista(fila["mechanic"])

    juego = {
        "id": convertir_a_entero(fila["game_id"]),
        "nombre": fila["name"].strip(),
        "año": convertir_a_entero(fila["year_published"]),
        "min_jugadores": convertir_a_entero(fila["min_players"]),
        "max_jugadores": convertir_a_entero(fila["max_players"]),
        "edad_minima": convertir_a_entero(fila["min_age"]),
        "tiempo_min": convertir_a_entero(fila["min_playtime"]),
        "tiempo_max": convertir_a_entero(fila["max_playtime"]),
        "categorias": categorias,
        "mecanicas": mecanicas,
        "modo": definir_modo(mecanicas),
        "rating": convertir_a_float(fila["average_rating"]),
    }

    return juego


def guardar_json(nombre_archivo, juegos):
    """Guarda una lista de juegos en un archivo JSON."""
    ruta = CARPETA_SALIDA / nombre_archivo

    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(juegos, archivo, ensure_ascii=False, indent=2)

    print(f"Creado: {ruta} ({len(juegos)} juegos)")


def main():
    with open(RUTA_ORIGEN, encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        juegos = [convertir_fila(fila) for fila in lector]

    # Quita registros incompletos o sin identificador.
    juegos = [
        juego
        for juego in juegos
        if juego["id"] > 0
        and juego["nombre"]
        and juego["min_jugadores"] > 0
        and juego["max_jugadores"] > 0
    ]

    # Mezcla siempre de la misma forma: resultados reproducibles.
    random.Random(42).shuffle(juegos)

    guardar_json("juegos_500.json", juegos[:500])
    guardar_json("juegos_10000.json", juegos[:10000])

    # Este archivo es útil para mostrar un BST desbalanceado en TP3/TP4.
    juegos_ordenados = sorted(
        juegos[:10000],
        key=lambda juego: juego["nombre"].casefold()
    )
    guardar_json("juegos_10000_ordenados.json", juegos_ordenados)


if __name__ == "__main__":
    main()