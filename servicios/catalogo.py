import json
from estructuras.avl import AVL
from modelos.juego import Juego
from servicios.jerarquia_categorias import crear_arbol_categorias
from estructuras.heap import MaxHeap
from estructuras.grafo import GrafoLista
from algoritmos.recorridos import Recorridos

class Catalogo:
    
    def __init__(self):
        self._juegos = []
        self._arbol_nombre = AVL()
        self._arbol_categorias = crear_arbol_categorias()
        self._heap_juegos = MaxHeap(mayor_prioridad=mayor_prioridad_juego)
        self._grafo = None
        
    def cargar_datos(self):
        with open('datos/juegos_500.json',"r",encoding="UTF-8" ) as archivo:
            datos= json.load(archivo)
        
        self._juegos.clear()
        self._arbol_nombre = AVL()
        self._heap_juegos = MaxHeap(mayor_prioridad=mayor_prioridad_juego)
        
        
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
            self._heap_juegos.insertar(juego)
        
        self._grafo = self._construir_grafo()
        
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
    #Devuelve las 9 categorias principales
    def obtener_grupos_categorias(self):
        return self._arbol_categorias.listar_hijos(
            self._arbol_categorias.raiz
        )
    #Busca una categoria y devuelve las subcategorias hijas
    def obtener_categorias_de_grupo(self, nombre_grupo):
        nodo_grupo = self._arbol_categorias.buscar(nombre_grupo)
        if nodo_grupo is None:
            return []
        return self._arbol_categorias.listar_hijos(nodo_grupo)
    
    #Busca un juego por nombre utilizando la estructura de Árbol AVL.
    def buscar_por_nombre(self, nombre: str):
        
        clave_nombre = lambda j: j.get_nombre().lower()
        return self._arbol_nombre.buscar(nombre.strip().lower(), clave_nombre)    
    
    def __len__(self):
        return len(self._juegos)
    
    #Obtener juegos del heap
    def obtener_top(self, cantidad=10):
        if cantidad <= 0:
            return []
        
        heap_copia = self._heap_juegos.copiar()
        resultado = []
        
        while len(resultado) < cantidad and not heap_copia.esta_vacio():
            resultado.append(heap_copia.extraer_maximo())
        
        return resultado
    
    #recorridos BFS y DFS
    def recorrer_bfs(self, nombre):
        juego_inicio = self.buscar_por_nombre(nombre)
        if juego_inicio is None or self._grafo is None:
            return None

        indice_inicio = self._juegos.index(juego_inicio)
        indices = Recorridos(self._grafo).bfs(indice_inicio)
        return [self._juegos[i] for i in indices]

    def recorrer_dfs(self, nombre):
        juego_inicio = self.buscar_por_nombre(nombre)
        if juego_inicio is None or self._grafo is None:
            return None

        indice_inicio = self._juegos.index(juego_inicio)
        indices = Recorridos(self._grafo).dfs_iterativo(indice_inicio)
        return [self._juegos[i] for i in indices]
    
    #construye el grafo
    def _construir_grafo(self):
        cantidad = len(self._juegos)
        grafo = GrafoLista(cantidad, dirigido=False)
    
        etiquetas = []
        for juego in self._juegos:
            etiquetas_juego = {
                etiqueta.strip().casefold()
                for etiqueta in juego.get_categorias() + juego.get_mecanicas()
                if etiqueta and etiqueta.strip()
            }
            etiquetas.append(etiquetas_juego)
        
        for i in range(cantidad):
            for j in range(i + 1, cantidad):
                compartidas = etiquetas[i] & etiquetas[j]
                
                if compartidas:
                    peso = 1 / len(compartidas)
                    grafo.agregar_arista(i, j, peso)
        
        return grafo
    
    
#Ordena juego por rating, en caso de empate por órden alfabetico.
def mayor_prioridad_juego(a, b):
    if a.get_rating() != b.get_rating():
        return a.get_rating() > b.get_rating()
    
    nombre_a = a.get_nombre().strip().casefold()
    nombre_b = b.get_nombre().strip().casefold()
    return nombre_a < nombre_b