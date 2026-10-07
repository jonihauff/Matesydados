class NodoAVL:
    """Cada nodo del AVL guarda su dato, hijos, y la altura para calcular el balance."""
    
    def __init__(self, dato):
        self.dato = dato
        self.izquierdo = None
        self.derecho = None
        self.altura = 1

class AVL:
    """Árbol AVL: árbol binario de búsqueda que se auto-balancea después de cada inserción."""
    
    def __init__(self):
        self.raiz = None

    # ==================== UTILIDADES DE ALTURA ====================

    def _altura(self, nodo):
        """Retorna la altura de un nodo. Un nodo None tiene altura 0."""
        if nodo is None:
            return 0
        return nodo.altura

    def _factor_balance(self, nodo):
        """Factor de balance = altura(izquierdo) - altura(derecho)."""
        if nodo is None:
            return 0
        return self._altura(nodo.izquierdo) - self._altura(nodo.derecho)

    def _actualizar_altura(self, nodo):
        """Recalcula la altura de un nodo basándose en sus hijos."""
        nodo.altura = 1 + max(self._altura(nodo.izquierdo), self._altura(nodo.derecho))

    # ==================== ROTACIONES ====================

    def _rotacion_izquierda(self, z):
        """Rotación simple izquierda."""
        y = z.derecho
        T2 = y.izquierdo

        y.izquierdo = z
        z.derecho = T2

        self._actualizar_altura(z)
        self._actualizar_altura(y)

        return y

    def _rotacion_derecha(self, z):
        """Rotación simple derecha."""
        y = z.izquierdo
        T2 = y.derecho

        y.derecho = z
        z.izquierdo = T2

        self._actualizar_altura(z)
        self._actualizar_altura(y)

        return y

    def _rotacion_izquierda_derecha(self, nodo):
        """Rotación doble izquierda-derecha."""
        nodo.izquierdo = self._rotacion_izquierda(nodo.izquierdo)
        return self._rotacion_derecha(nodo)

    def _rotacion_derecha_izquierda(self, nodo):
        """Rotación doble derecha-izquierda."""
        nodo.derecho = self._rotacion_derecha(nodo.derecho)
        return self._rotacion_izquierda(nodo)

    # ==================== INSERCIÓN ====================

    def insertar(self, dato, clave):
        """Inserta un dato en el AVL manteniendo el balance."""
        self.raiz = self._insertar_recursivo(self.raiz, dato, clave)

    def _insertar_recursivo(self, nodo, dato, clave):
        """Recursión que inserta y luego balancea el camino de vuelta."""
        if nodo is None:
            return NodoAVL(dato)

        if clave(dato) < clave(nodo.dato):
            nodo.izquierdo = self._insertar_recursivo(nodo.izquierdo, dato, clave)
        elif clave(dato) > clave(nodo.dato):
            nodo.derecho = self._insertar_recursivo(nodo.derecho, dato, clave)
        else:
            return nodo  # Duplicado, no se inserta

        self._actualizar_altura(nodo)
        balance = self._factor_balance(nodo)

        if balance > 1 and clave(dato) < clave(nodo.izquierdo.dato):
            return self._rotacion_derecha(nodo)
        if balance < -1 and clave(dato) > clave(nodo.derecho.dato):
            return self._rotacion_izquierda(nodo)
        if balance > 1 and clave(dato) > clave(nodo.izquierdo.dato):
            return self._rotacion_izquierda_derecha(nodo)
        if balance < -1 and clave(dato) < clave(nodo.derecho.dato):
            return self._rotacion_derecha_izquierda(nodo)

        return nodo

    # ==================== BÚSQUEDA ====================

    def buscar(self, valor, clave):
        """Busca un elemento cuyo valor de clave coincide con 'valor'."""
        return self._buscar_recursivo(self.raiz, valor, clave)

    def _buscar_recursivo(self, nodo, valor, clave):
        if nodo is None:
            return None
        valor_nodo = clave(nodo.dato)
        if valor == valor_nodo:
            return nodo.dato
        if valor < valor_nodo:
            return self._buscar_recursivo(nodo.izquierdo, valor, clave)
        return self._buscar_recursivo(nodo.derecho, valor, clave)

    # ==================== RECORRIDOS ====================

    def inorder(self):
        """Izquierda → raíz → derecha. Devuelve elementos ordenados."""
        resultado = []
        self._inorder_recursivo(self.raiz, resultado)
        return resultado

    def _inorder_recursivo(self, nodo, resultado):
        if nodo is not None:
            self._inorder_recursivo(nodo.izquierdo, resultado)
            resultado.append(nodo.dato)
            self._inorder_recursivo(nodo.derecho, resultado)

    def preorder(self):
        """Raíz → izquierda → derecha."""
        resultado = []
        self._preorder_recursivo(self.raiz, resultado)
        return resultado

    def _preorder_recursivo(self, nodo, resultado):
        if nodo is not None:
            resultado.append(nodo.dato)
            self._preorder_recursivo(nodo.izquierdo, resultado)
            self._preorder_recursivo(nodo.derecho, resultado)

    def postorder(self):
        """Izquierda → derecha → raíz."""
        resultado = []
        self._postorder_recursivo(self.raiz, resultado)
        return resultado

    def _postorder_recursivo(self, nodo, resultado):
        if nodo is not None:
            self._postorder_recursivo(nodo.izquierdo, resultado)
            self._postorder_recursivo(nodo.derecho, resultado)
            resultado.append(nodo.dato)

    # ==================== INFORMACIÓN ====================

    def altura(self):
        """Retorna la altura del árbol. Árbol vacío → 0."""
        return self._altura(self.raiz)

    def esta_vacio(self):
        return self.raiz is None

    def __len__(self):
        """Cantidad de nodos en el árbol."""
        return self._contar_nodos(self.raiz)

    def _contar_nodos(self, nodo):
        if nodo is None:
            return 0
        return 1 + self._contar_nodos(nodo.izquierdo) + self._contar_nodos(nodo.derecho)