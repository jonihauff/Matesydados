class MaxHeap:
    def __init__(self, mayor_prioridad=None):
        self._elementos = []
        self._mayor_prioridad = mayor_prioridad or (lambda a, b: a > b)

    def esta_vacio(self):
        return len(self._elementos) == 0

    def __len__(self):
        return len(self._elementos)

    def consultar_maximo(self):
        if self.esta_vacio():
            raise IndexError("el heap está vacío")
        return self._elementos[0]

    def insertar(self, valor):
        self._elementos.append(valor)
        self._subir(len(self._elementos) - 1)

    def extraer_maximo(self):
        if self.esta_vacio():
            raise IndexError("el heap está vacío")

        maximo = self._elementos[0]
        ultimo = self._elementos.pop()

        if not self.esta_vacio():
            self._elementos[0] = ultimo
            self._bajar(0)

        return maximo

    def _subir(self, indice):
        while indice > 0:
            padre = (indice - 1) // 2

            if not self._mayor_prioridad(
                self._elementos[indice],
                self._elementos[padre]
            ):
                break

            self._intercambiar(padre, indice)
            indice = padre

    def _bajar(self, indice):
        cantidad = len(self._elementos)

        while True:
            izquierdo = 2 * indice + 1
            derecho = 2 * indice + 2
            mayor = indice

            if (
                izquierdo < cantidad
                and self._mayor_prioridad(
                    self._elementos[izquierdo],
                    self._elementos[mayor]
                )
            ):
                mayor = izquierdo

            if (
                derecho < cantidad
                and self._mayor_prioridad(
                    self._elementos[derecho],
                    self._elementos[mayor]
                )
            ):
                mayor = derecho

            if mayor == indice:
                break

            self._intercambiar(indice, mayor)
            indice = mayor

    def _intercambiar(self, i, j):
        self._elementos[i], self._elementos[j] = self._elementos[j], self._elementos[i]
    
    def copiar(self):
        copia = MaxHeap(self._mayor_prioridad)
        copia._elementos = self._elementos.copy()
        return copia
    
