from servicios.catalogo import Catalogo
from ui.terminal import Terminal


def main():
    
    catalogo = Catalogo()
    
    catalogo.cargar_datos()
    
    app = Terminal(catalogo)
    app.inicio()
    
if __name__ == "__main__":
    main()