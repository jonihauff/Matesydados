class Juego :
    def __init__ (
        self,
        id,
        nombre,
        año,
        min_jugadores,
        max_jugadores,
        edad_min,
        tiempo_min,
        tiempo_max,
        categorias,
        mecanicas,
        modo,
        rating,
        ):
        self._id= id
        self._nombre = nombre
        self._año = año
        self._min_jugadores = min_jugadores
        self._max_jugadores = max_jugadores
        self._edad_min = edad_min
        self._tiempo_min = tiempo_min
        self._tiempo_max = tiempo_max
        self._categorias = categorias
        self._mecanicas = mecanicas
        self._modo = modo
        self._rating = rating
        
    def get_id(self):
        return self._id
    def get_nombre(self):
        return self._nombre
    def get_año(self):
        return self._año
    def get_min_jugadores(self):
        return self._min_jugadores
    def get_max_jugadores(self):
        return self._max_jugadores
    def get_edad_min(self):
        return self._edad_min
    def get_tiempo_min(self):
        return self._tiempo_min
    def get_tiempo_max(self):
        return self._tiempo_max
    def get_categorias(self):
        return self._categorias
    def get_mecanicas(self):
        return self._mecanicas
    def get_modo(self):
        return self._modo
    def get_rating(self):
        return self._rating
    
    def __repr__(self):
        return (
            f"ID: {self._id}\n"
            f"Nombre: {self._nombre}\n"
            f"Año: {self._año}\n"
            f"Jugadores: {self._min_jugadores} - {self._max_jugadores}\n"
            f"Edad Mínima: {self._edad_min}+\n"
            f"Tiempo de juego: {self._tiempo_min} - {self._tiempo_max} min\n"
            f"Categorías: {', '.join(self._categorias)}\n"
            f"Mecánicas: {', '.join(self._mecanicas)}\n"
            f"Modo: {self._modo}\n"
            f"Rating: ⭐ {self._rating}\n"
            f"{'-'*30}"
            )