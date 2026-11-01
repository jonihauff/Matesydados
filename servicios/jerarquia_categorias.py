from estructuras.arbol_general import ArbolGeneral

jerarquia_categorias = {
    "Épocas históricas": [
        "Antigüedad",
        "Era de la Razón",
        "Medieval",
        "Napoleónico",
        "Posnapoleónico",
        "Prehistoria",
        "Renacimiento",
    ],
    "Guerras y conflictos": [
        "Guerra civil",
        "Guerra Civil Estadounidense",
        "Guerra de Independencia Estadounidense",
        "Guerra de Vietnam",
        "Guerra moderna",
        "Picas y arcabuces",
        "Primera Guerra Mundial",
        "Segunda Guerra Mundial",
        "Combate",
        "Wargame",
    ],
    "Ficción y ambientación": [
        "Aventura",
        "Asesinato/Misterio",
        "Basado en novelas",
        "Ciencia ficción",
        "Cómic / Tira cómica",
        "Fantasía",
        "Libro",
        "Mitología",
        "Piratas",
        "Temática de cine / TV / radio",
        "Temática de videojuegos",
        "Terror",
        "Zombis",
    ],
    "Sociedad y cultura": [
        "Árabe",
        "Deportes",
        "Humor",
        "Espías/Agentes secretos",
        "Industria / Manufactura",
        "Lejano Oeste estadounidense",
        "Mafia",
        "Música",
        "Político",
        "Religioso",
    ],
    "Naturaleza y viajes": [
        "Agricultura",
        "Animales",
        "Aviación / Vuelo",
        "Medioambiental",
        "Náutico",
        "Transporte",
        "Trenes",
        "Viajes",
    ],
    "Civilización y desarrollo": [
        "Civilización",
        "Economía",
        "Construcción de ciudades",
        "Construcción de territorios",
        "Estrategia abstracta",
        "Exploración",
        "Exploración espacial",
        "Sistema de juego",
    ],
    "Competencia e interacción": [
        "Acción / Destreza",
        "Carreras",
        "Faroleo",
        "Juego de fiesta",
        "Negociación",
        "Tiempo real",
        "Trivia",
    ],
    "Ingenio y resolución de problemas": [
        "Deducción",
        "Juego de palabras",
        "Laberinto",
        "Matemáticas",
        "Memoria",
        "Números",
        "Rompecabezas",
    ],
    "Formatos, público y edición": [
        "Componentes coleccionables",
        "Dados",
        "Educativo",
        "Electrónico",
        "Expansión de juego base",
        "Imprimir y jugar",
        "Juego de cartas",
        "Juego infantil",
        "Miniaturas",
        "Para adultos",
    ],
}

def crear_arbol_categorias ():
    arbol = ArbolGeneral()
    arbol.insertar_raiz("juegos de mesa")
    
    for categoria, subcategorias in jerarquia_categorias.items():
        nodo_cat = arbol.agregar_hijo(arbol.raiz, categoria)
        
        for subcategoria in subcategorias:
            arbol.agregar_hijo(nodo_cat, subcategoria)
    
    return arbol
