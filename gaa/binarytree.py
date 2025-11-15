class NodoArbol:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None


class ArbolBinario:
    """
    Árbol Binario de Búsqueda (BST) totalmente en ESPAÑOL.
    Métodos claros y con nombres en español para usar en prácticas.
    """

    def __init__(self):
        self.raiz = None
        self.tamano = 0

    # ------------------------
    # Inserción
    # ------------------------
    def insertar(self, valor):
        """Inserta valor en el BST. Devuelve True si se insertó, False si ya existe."""
        if self.raiz is None:
            self.raiz = NodoArbol(valor)
            self.tamano = 1
            return True

        padre = None
        actual = self.raiz
        while actual:
            if valor < actual.valor:
                padre = actual
                actual = actual.izquierda
            elif valor > actual.valor:
                padre = actual
                actual = actual.derecha
            else:
                return False  # duplicado

        if valor < padre.valor:
            padre.izquierda = NodoArbol(valor)
        else:
            padre.derecha = NodoArbol(valor)
        self.tamano += 1
        return True

    # ------------------------
    # Búsqueda
    # ------------------------
    def buscar(self, valor):
        actual = self.raiz
        while actual:
            if valor < actual.valor:
                actual = actual.izquierda
            elif valor > actual.valor:
                actual = actual.derecha
            else:
                return True
        return False

    # ------------------------
    # Recorridos que devuelven listas
    # ------------------------
    def preorden(self):
        res = []
        self._preorden(self.raiz, res)
        return res

    def _preorden(self, nodo, res):
        if nodo:
            res.append(nodo.valor)
            self._preorden(nodo.izquierda, res)
            self._preorden(nodo.derecha, res)

    def inorden(self):
        res = []
        self._inorden(self.raiz, res)
        return res

    def _inorden(self, nodo, res):
        if nodo:
            self._inorden(nodo.izquierda, res)
            res.append(nodo.valor)
            self._inorden(nodo.derecha, res)

    def postorden(self):
        res = []
        self._postorden(self.raiz, res)
        return res

    def _postorden(self, nodo, res):
        if nodo:
            self._postorden(nodo.izquierda, res)
            self._postorden(nodo.derecha, res)
            res.append(nodo.valor)

    # ------------------------
    # Información básica
    # ------------------------
    def altura(self):
        return self._altura(self.raiz)

    def _altura(self, nodo):
        if nodo is None:
            return 0
        return 1 + max(self._altura(nodo.izquierda), self._altura(nodo.derecha))

    def cantidad_nodos(self):
        return self.tamano

    def esta_vacio(self):
        return self.raiz is None

    # ------------------------
    # Hojas, mínimo y máximo
    # ------------------------
    def contar_hojas(self):
        return self._contar_hojas(self.raiz)

    def _contar_hojas(self, nodo):
        if nodo is None:
            return 0
        if nodo.izquierda is None and nodo.derecha is None:
            return 1
        return self._contar_hojas(nodo.izquierda) + self._contar_hojas(nodo.derecha)

    def minimo(self):
        if self.raiz is None:
            return None
        actual = self.raiz
        while actual.izquierda:
            actual = actual.izquierda
        return actual.valor

    def maximo(self):
        if self.raiz is None:
            return None
        actual = self.raiz
        while actual.derecha:
            actual = actual.derecha
        return actual.valor

    # ------------------------
    # Eliminación
    # ------------------------
    def eliminar(self, valor):
        """Elimina valor si existe y actualiza tamaño. Devuelve True si eliminó."""
        eliminado, nueva_raiz = self._eliminar(self.raiz, valor)
        if eliminado:
            self.raiz = nueva_raiz
            self.tamano -= 1
        return eliminado

    def _eliminar(self, nodo, valor):
        if nodo is None:
            return (False, nodo)
        if valor < nodo.valor:
            eliminado, nodo.izquierda = self._eliminar(nodo.izquierda, valor)
            return (eliminado, nodo)
        elif valor > nodo.valor:
            eliminado, nodo.derecha = self._eliminar(nodo.derecha, valor)
            return (eliminado, nodo)
        else:
            # nodo a eliminar encontrado
            # caso 1: hoja
            if nodo.izquierda is None and nodo.derecha is None:
                return (True, None)
            # caso 2: un hijo
            if nodo.izquierda is None:
                return (True, nodo.derecha)
            if nodo.derecha is None:
                return (True, nodo.izquierda)
            # caso 3: dos hijos -> reemplazar por sucesor (mínimo en subárbol derecho)
            sucesor = self._min_nodo(nodo.derecha)
            nodo.valor = sucesor.valor
            eliminado, nodo.derecha = self._eliminar(nodo.derecha, sucesor.valor)
            return (True, nodo)

    def _min_nodo(self, nodo):
        actual = nodo
        while actual.izquierda:
            actual = actual.izquierda
        return actual

    # ------------------------
    # Camino desde la raíz hasta un valor (lista de valores)
    # ------------------------
    def camino(self, valor):
        ruta = []
        actual = self.raiz
        while actual:
            ruta.append(actual.valor)
            if valor < actual.valor:
                actual = actual.izquierda
            elif valor > actual.valor:
                actual = actual.derecha
            else:
                return ruta
        return None

    # ------------------------
    # Profundidad (nivel) de un valor
    # ------------------------
    def profundidad(self, valor):
        nivel = 0
        actual = self.raiz
        while actual:
            if valor < actual.valor:
                actual = actual.izquierda
            elif valor > actual.valor:
                actual = actual.derecha
            else:
                return nivel
            nivel += 1
        return None

    # ------------------------
    # k-ésimo elemento (0-index) en orden (inorden)
    # ------------------------
    def k_esimo_menor(self, k):
        arr = self.inorden()
        if 0 <= k < len(arr):
            return arr[k]
        return None

    # ------------------------
    # Suma de todos los valores (asume elementos numéricos)
    # ------------------------
    def suma(self):
        return self._suma(self.raiz)

    def _suma(self, nodo):
        if nodo is None:
            return 0
        return nodo.valor + self._suma(nodo.izquierda) + self._suma(nodo.derecha)

    # ------------------------
    # Contar menores/mayores a un valor
    # ------------------------
    def contar_menores_que(self, valor):
        return self._contar_menores(self.raiz, valor)

    def _contar_menores(self, nodo, valor):
        if nodo is None:
            return 0
        if nodo.valor < valor:
            return 1 + self._contar_menores(nodo.izquierda, valor) + self._contar_menores(nodo.derecha, valor)
        return self._contar_menores(nodo.izquierda, valor)

    def contar_mayores_que(self, valor):
        return self._contar_mayores(self.raiz, valor)

    def _contar_mayores(self, nodo, valor):
        if nodo is None:
            return 0
        if nodo.valor > valor:
            return 1 + self._contar_mayores(nodo.izquierda, valor) + self._contar_mayores(nodo.derecha, valor)
        return self._contar_mayores(nodo.derecha, valor)

    # ------------------------
    # Sucesor y predecesor en valor
    # ------------------------
    def sucesor(self, valor):
        actual = self.raiz
        sucesor = None
        while actual:
            if valor < actual.valor:
                sucesor = actual
                actual = actual.izquierda
            else:
                actual = actual.derecha
        return sucesor.valor if sucesor else None

    def predecesor(self, valor):
        actual = self.raiz
        predecesor = None
        while actual:
            if valor > actual.valor:
                predecesor = actual
                actual = actual.derecha
            else:
                actual = actual.izquierda
        return predecesor.valor if predecesor else None

    # ------------------------
    # Ver si está balanceado (por alturas)
    # ------------------------
    def es_balanceado(self):
        ok, _ = self._es_balanceado(self.raiz)
        return ok

    def _es_balanceado(self, nodo):
        if nodo is None:
            return (True, 0)
        izq_ok, alt_izq = self._es_balanceado(nodo.izquierda)
        der_ok, alt_der = self._es_balanceado(nodo.derecha)
        return (izq_ok and der_ok and abs(alt_izq - alt_der) <= 1, 1 + max(alt_izq, alt_der))

    # ------------------------
    # Recorrido por niveles (BFS)
    # ------------------------
    def recorrido_por_niveles(self):
        if self.raiz is None:
            return []
        cola = [self.raiz]
        res = []
        while cola:
            actual = cola.pop(0)
            res.append(actual.valor)
            if actual.izquierda:
                cola.append(actual.izquierda)
            if actual.derecha:
                cola.append(actual.derecha)
        return res

    # ------------------------
    # Limpiar árbol
    # ------------------------
    def limpiar(self):
        self.raiz = None
        self.tamano = 0
