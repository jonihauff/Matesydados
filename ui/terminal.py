from servicios.catalogo import Catalogo

class Terminal:
    def __init__(self, catalogo):
        self._catalogo = catalogo
    
    def mostrar_menu(self):
        print("="*30)
        print("Recomendador de juegos de mesa")
        print ("="*30)
        print("1 - Buscar juego por nombre")
        print("2 - Filtrar por categoria")
        print("3 - Mostrar todos los juegos")
        print("4 - Salir")
        print("-"*30)
        
    def inicio(self):
        while True :
            self.mostrar_menu()
            opcion = input("ingrese el n° de la opcion elegida: ").strip()
            
            if opcion == "1":
                self._buscar_por_nombre()
            elif opcion == "2":
                self._filtrar_por_categoria()
            elif opcion == "3":
                self._mostrar_todos()
            elif opcion == "4":
                print("Gracias por visitarnos! Hasta luego.")
                break
            else:
                print("opción ingresada no valida, intente nuevamente")
                
    def _mostrar_todos(self):
        juegos = self._catalogo.mostrar_todos()
        if not juegos:
            print("no hay juegos cargados")
        
        else:
            for juego in juegos:
                print(juego)
                print()
                
    def _filtrar_por_categoria(self):
        categorias = self._catalogo.obtener_categorias_disponibles()
        if categorias:
            print("\nCategorías disponibles:", ", ".join(categorias))
            print("-" * 30)
        
        categoria = input("Ingrese la categoría a buscar (ej. Estrategia):  ").strip()
        if not categoria:
            print("No ingresaste ninguna categoría.")
            return

        juegos_filtrados = self._catalogo.filtrar_por_categoria(categoria)
        
        if not juegos_filtrados:
            print(f"No se encontraron juegos pertenecientes a la categoría ingresada'{categoria}'.")
        else:
            print(f"\n- Juegos en la categoría '{categoria}' ({len(juegos_filtrados)}): ")
            for juego in juegos_filtrados:
                print(juego)
                print()
                
    def _buscar_por_nombre(self):
        nombre = input("ingrese el nombre del juego:  " ).strip()
        if not nombre:
            print("No ha ingresado ningun nombre.")
            return
        
        juego_buscado = self._catalogo.buscar_por_nombre(nombre)
        
        if not juego_buscado:
            print(f"No se encontro el juego '{nombre}'.")
        else:
            print(f"\n- Se encontraron ({len(juego_buscado)}) juegos que coinciden con '{nombre}' : ")
            for juego in juego_buscado:
                print(juego)
                print()
