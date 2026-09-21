import json
from estructuras.arbol_binario import ArbolBST
from modelos.juego import Juego

class Catalogo:
    
    def __init__(self):
        self._juegos = []
        self._arbol_nombre = ArbolBST()
        
    def cargar_datos(self):
        with open('datos/juegos.json',"r",encoding="UTF-8" ) as archivo:
            datos= json.load(archivo)
        
        self._juegos.clear()
        self._arbol_nombre = ArbolBST()
        
        clave_nombre = lambda j: j.get_nombre().lower()
    
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
            self._arbol_nombre.insertar(juego, clave_nombre)
        
        print(f"se cargaron {len(self._juegos)} juegos")

    def mostrar_todos(self):
        return list(self._juegos)
    
    # Devuelve una lista filtrada por la categoria que elige el usuario.
    def filtrar_por_categoria(self, categoria_buscada):
        cat_bus = categoria_buscada.lower().strip()
        
        resultado_filtrado = filter(lambda juego: cat_bus in [c.lower() for c in juego.get_categorias()],self._juegos
        )
        return list(resultado_filtrado)
    
    #Devuelve una lista ordenada para indicar al usuario que categorias puede elegir.
    def obtener_categorias_disponibles(self) -> list[str]:
        
        categorias_set = set()
        
        for juego in self._juegos:
            for cat in juego.get_categorias():
                categorias_set.add(cat.strip())
                
        return sorted(list(categorias_set))
    
    #Busca un juego por nombre utilizando la estructura de Árbol BST.
    def buscar_por_nombre(self, nombre: str):
        
        clave_nombre = lambda j: j.get_nombre().lower()
        return self._arbol_nombre.buscar(nombre.strip().lower(), clave_nombre)    
    
    def __len__(self):
        return len(self._juegos)
    
    