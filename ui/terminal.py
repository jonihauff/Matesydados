from servicios.catalogo import Catalogo

class Terminal:
    def __init__(self, catalogo):
        self._catalogo = catalogo
    
    def mostrar_menu(self):
        print("="*30)
        print("Recomendador de juegos de mesa")
        print ("="*30)
        print("1 - Buscar juego por nombre")
        print("2 - Buscar por categoria")
        print("3 - Mostrar todos los juegos")
        print("4 - Mostrar ranking TOP 10")
        print("5 - Salir")
        print("-"*30)
        
    def inicio(self):
        while True :
            self.mostrar_menu()
            opcion = input("ingrese el n° de la opcion elegida: ").strip()
            
            if opcion == "1":
                self._buscar_por_nombre()
            elif opcion == "2":
                self._buscar_por_categoria()
            elif opcion == "3":
                self._mostrar_todos()
            elif opcion == "4":
                self._mostrar_top_10()
            elif opcion == "5":
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
                
    def _buscar_por_categoria(self):
                
        grupos = self._catalogo.obtener_grupos_categorias()
        
        if not grupos:
            print("No hay grupos de categorías disponibles.")
            return
        
        print("\nGrupos disponibles:")
        for indice, grupo in enumerate(grupos, start=1):
            print(f"{indice} - {grupo}")
        print("0 - Volver")
        
        seleccion = input("Elegí un grupo: ").strip()
        
        if seleccion == "0":
            return
        
        try:
            indice_grupo = int(seleccion) - 1
        except ValueError:
            print("La opción ingresada no es válida.")
            return
        
        if indice_grupo < 0 or indice_grupo >= len(grupos):
            print("La opción ingresada no es válida.")
            return
        
        grupo_elegido = grupos[indice_grupo]
        categorias = self._catalogo.obtener_categorias_de_grupo(grupo_elegido)
        
        if not categorias:
            print(f"El grupo '{grupo_elegido}' no tiene categorías.")
            return
        
        print(f"\nCategorías de '{grupo_elegido}':")
        for indice, categoria in enumerate(categorias, start=1):
            print(f"{indice} - {categoria}")
        print("0 - Volver")
        
        seleccion = input("Elegí una categoría: ").strip()
        
        if seleccion == "0":
            return
        
        try:
            indice_categoria = int(seleccion) - 1
        except ValueError:
            print("La opción ingresada no es válida.")
            return
        
        if indice_categoria < 0 or indice_categoria >= len(categorias):
            print("La opción ingresada no es válida.")
            return
        
        categoria_elegida = categorias[indice_categoria]
        juegos = self._catalogo.filtrar_por_categoria(categoria_elegida)
        
        if not juegos:
            print(f"No hay juegos en la categoría '{categoria_elegida}'.")
        else:
            print(
                f"\nJuegos de la categoría '{categoria_elegida}' "
                f"({len(juegos)}):"
            )
            for juego in juegos:
                print(juego)
                print()
        
                
    def _buscar_por_nombre(self):
        nombre = input("Ingrese el nombre del juego: ").strip()
        if not nombre:
            print("No ha ingresado ningún nombre.")
            return
        
        juego_buscado = self._catalogo.buscar_por_nombre(nombre)
        
        if juego_buscado is None:
            print(f"No se encontró el juego '{nombre}'.")
        else:
            print(f"\n- Juego encontrado que coincide con '{nombre}':\n")
            print(juego_buscado)
            print()
            
    def _mostrar_top_10(self):
        juegos = self._catalogo.obtener_top(10)
        
        if not juegos:
            print("No hay juegos cargados.")
            return
        
        print("\nTop 10 juegos por rating:")
        for indice, juego in enumerate(juegos, start=1):
            print(f"{indice}. {juego.get_nombre()} — rating {juego.get_rating()}")    
