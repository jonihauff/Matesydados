import json
from modelos.juego import Juego

class Catalogo:
    def __init__(self):
        self._juegos = []
    
    def cargar_datos(self):
        with open('datos/juegos.json',"r",encoding="UTF-8" ) as archivo:
            datos= json.load(archivo)
        
        self._juegos.clear()
    
        for item in datos:
            juego = Juego(
                id=item["id"],
                nombre=item["nombre"],
                año=item["año"],
                min_jugadores=item["min_jugadores"],
                max_jugadores=item["max_jugadores"],
                edad_min=item["edad_minima"],
                tiempo_min=item["tiempo_min"],
                tiempo_max=item["tiempo_max"],
                categorias=item["categorias"],
                mecanicas=item["mecanicas"],
                modo=item["modo"],
                rating=item["rating"]
    )
            self._juegos.append(juego)
        
        print(f"se cargaron {len(self._juegos)} juegos")

    def mostrar_todos(self):
        return list(self._juegos)
    
    def filtrar_por_categoria(self, categoria_buscada):
        cat_bus = categoria_buscada.lower().strip()
        
        resultado_filtrado = filter(lambda juego: cat_bus in [c.lower() for c in juego.get_categorias()],self._juegos
        )
        return list(resultado_filtrado)
    
    def __len__(self):
        return len(self._juegos)
    
    