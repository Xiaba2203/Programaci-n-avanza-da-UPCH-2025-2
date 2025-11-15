# ListaEnlazada_Extendida.py
# Lista simplemente enlazada - nombres en español (camelCase)
# Clase: ListaEnlazada
# Nodo: Nodo

class Nodo:
    def __init__(self, elemento):
        self.elemento = elemento
        self.siguiente = None


class ListaEnlazada:
    """Lista simplemente enlazada extensa (nombres en español, camelCase).

    Uso: from ListaEnlazada_Extendida import ListaEnlazada
    """

    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    # ------------------------- getters / setters -------------------------
    def getHead(self):
        return self.__head

    def setHead(self, node):
        self.__head = node
        # actualizar tail y size no se hace automáticamente

    def getTail(self):
        return self.__tail

    def setTail(self, node):
        self.__tail = node

    # ------------------------- básicos del profe (traducidos) -------------------------
    def obtenerPrimero(self):
        if self.__size == 0:
            return None
        return self.__head.elemento

    def obtenerUltimo(self):
        if self.__size == 0:
            return None
        return self.__tail.elemento

    def agregarInicio(self, e):
        newNode = Nodo(e)
        newNode.siguiente = self.__head
        self.__head = newNode
        if self.__tail is None:
            self.__tail = newNode
        self.__size += 1

    def agregarFinal(self, e):
        newNode = Nodo(e)
        if self.__tail is None:
            self.__head = self.__tail = newNode
        else:
            self.__tail.siguiente = newNode
            self.__tail = newNode
        self.__size += 1

    def agregar(self, e):
        self.agregarFinal(e)

    def insertar(self, index, e):
        if index <= 0:
            self.agregarInicio(e)
            return
        if index >= self.__size:
            self.agregarFinal(e)
            return
        current = self.__head
        for _ in range(1, index):
            current = current.siguiente
        temp = current.siguiente
        current.siguiente = Nodo(e)
        current.siguiente.siguiente = temp
        self.__size += 1

    def eliminarInicio(self):
        if self.__size == 0:
            return None
        temp = self.__head
        self.__head = self.__head.siguiente
        if self.__head is None:
            self.__tail = None
        self.__size -= 1
        return temp.elemento

    def eliminarFinal(self):
        if self.__size == 0:
            return None
        if self.__size == 1:
            temp = self.__head
            self.__head = self.__tail = None
            self.__size = 0
            return temp.elemento
        current = self.__head
        for _ in range(self.__size - 2):
            current = current.siguiente
        temp = self.__tail
        self.__tail = current
        self.__tail.siguiente = None
        self.__size -= 1
        return temp.elemento

    def eliminarEn(self, index):
        if index < 0 or index >= self.__size:
            return None
        if index == 0:
            return self.eliminarInicio()
        if index == self.__size - 1:
            return self.eliminarFinal()
        prev = self.__head
        for _ in range(1, index):
            prev = prev.siguiente
        current = prev.siguiente
        prev.siguiente = current.siguiente
        self.__size -= 1
        return current.elemento

    def estaVacia(self):
        return self.__size == 0

    def tamanio(self):
        return self.__size

    def __str__(self):
        return self.convertirAString()

    def convertirAString(self):
        res = "["
        cur = self.__head
        while cur:
            res += str(cur.elemento)
            cur = cur.siguiente
            if cur:
                res += ", "
        res += "]"
        return res

    def limpiar(self):
        self.__head = self.__tail = None
        self.__size = 0

    # ------------------------- métodos que faltaban (implementados) -------------------------
    def contiene(self, e):
        return self.buscarLineal(e) != -1

    def eliminarValor(self, e):
        idx = self.indiceDe(e)
        if idx == -1:
            return False
        self.eliminarEn(idx)
        return True

    def obtener(self, index):
        if index < 0 or index >= self.__size:
            return None
        cur = self.__head
        for _ in range(index):
            cur = cur.siguiente
        return cur.elemento

    def indiceDe(self, e):
        cur = self.__head
        i = 0
        while cur:
            if cur.elemento == e:
                return i
            cur = cur.siguiente
            i += 1
        return -1

    def ultimoIndiceDe(self, e):
        cur = self.__head
        i = 0
        last = -1
        while cur:
            if cur.elemento == e:
                last = i
            cur = cur.siguiente
            i += 1
        return last

    def reemplazar(self, index, e):
        if index < 0 or index >= self.__size:
            return False
        cur = self.__head
        for _ in range(index):
            cur = cur.siguiente
        cur.elemento = e
        return True

    def __iter__(self):
        self._iterNode = self.__head
        return self

    def __next__(self):
        if not hasattr(self, '_iterNode') or self._iterNode is None:
            raise StopIteration
        val = self._iterNode.elemento
        self._iterNode = self._iterNode.siguiente
        return val

    # ------------------------- funciones nuevas -------------------------
    def convertirALista(self):
        arr = []
        cur = self.__head
        while cur:
            arr.append(cur.elemento)
            cur = cur.siguiente
        return arr

    def invertir(self):
        prev = None
        cur = self.__head
        self.__tail = self.__head
        while cur:
            nxt = cur.siguiente
            cur.siguiente = prev
            prev = cur
            cur = nxt
        self.__head = prev

    def obtenerMaximo(self):
        if self.__size == 0:
            return None
        cur = self.__head
        mx = cur.elemento
        while cur:
            if cur.elemento > mx:
                mx = cur.elemento
            cur = cur.siguiente
        return mx

    def obtenerMinimo(self):
        if self.__size == 0:
            return None
        cur = self.__head
        mn = cur.elemento
        while cur:
            if cur.elemento < mn:
                mn = cur.elemento
            cur = cur.siguiente
        return mn

    def sumar(self):
        cur = self.__head
        s = 0
        while cur:
            s += cur.elemento
            cur = cur.siguiente
        return s

    def contar(self, valor):
        cur = self.__head
        c = 0
        while cur:
            if cur.elemento == valor:
                c += 1
            cur = cur.siguiente
        return c

    def obtenerNodoEn(self, index):
        if index < 0 or index >= self.__size:
            return None
        cur = self.__head
        for _ in range(index):
            cur = cur.siguiente
        return cur

    def clonar(self):
        nueva = ListaEnlazada()
        cur = self.__head
        while cur:
            nueva.agregarFinal(cur.elemento)
            cur = cur.siguiente
        return nueva

    def fusionar(self, otra):
        """Concatena otra ListaEnlazada al final (no hace copia profunda de nodos)."""
        if not isinstance(otra, ListaEnlazada):
            raise TypeError("fusionar espera otra ListaEnlazada")
        cur = otra.__head
        while cur:
            self.agregarFinal(cur.elemento)
            cur = cur.siguiente

    def eliminarTodos(self, valor):
        removed = 0
        while self.contiene(valor):
            self.eliminarValor(valor)
            removed += 1
        return removed

    def obtenerMediana(self):
        arr = self.convertirALista()
        if not arr:
            return None
        arr.sort()
        n = len(arr)
        mid = n // 2
        if n % 2 == 1:
            return arr[mid]
        return (arr[mid-1] + arr[mid]) / 2

    def promedio(self):
        if self.__size == 0:
            return None
        return self.sumar() / self.__size

    def obtenerKDesdeFinal(self, k):
        # k=0 -> último, k=1 -> penúltimo
        if k < 0 or k >= self.__size:
            return None
        objetivo = self.__size - 1 - k
        return self.obtener(objetivo)

    def eliminarKDesdeFinal(self, k):
        idx = self.__size - 1 - k
        return self.eliminarEn(idx)

    def intercalar(self, otra):
        """Intercala elementos con otra lista: a0,b0,a1,b1..."""
        if not isinstance(otra, ListaEnlazada):
            raise TypeError("intercalar espera otra ListaEnlazada")
        a = self.__head
        b = otra.__head
        nueva = ListaEnlazada()
        while a or b:
            if a:
                nueva.agregarFinal(a.elemento)
                a = a.siguiente
            if b:
                nueva.agregarFinal(b.elemento)
                b = b.siguiente
        return nueva

    def esIgual(self, otra):
        if not isinstance(otra, ListaEnlazada):
            return False
        a = self.__head
        b = otra.__head
        while a and b:
            if a.elemento != b.elemento:
                return False
            a = a.siguiente
            b = b.siguiente
        return a is None and b is None

    def ordenar(self):
        arr = self.convertirALista()
        arr.sort()
        self.limpiar()
        for v in arr:
            self.agregarFinal(v)

    def buscarLineal(self, valor):
        return self.indiceDe(valor)

    def eliminarDuplicados(self):
        seen = set()
        cur = self.__head
        prev = None
        while cur:
            if cur.elemento in seen:
                # eliminar cur
                prev.siguiente = cur.siguiente
                self.__size -= 1
                if cur == self.__tail:
                    self.__tail = prev
                cur = prev.siguiente
            else:
                seen.add(cur.elemento)
                prev = cur
                cur = cur.siguiente

    def toStringDetallado(self):
        lines = []
        cur = self.__head
        idx = 0
        while cur:
            nxt = cur.siguiente.elemento if cur.siguiente else None
            lines.append(f"[{idx}] {cur.elemento} -> {nxt}")
            cur = cur.siguiente
            idx += 1
        return "\n".join(lines)


# README final (en el mismo archivo)
# Métodos principales (camelCase):
# obtenerPrimero, obtenerUltimo, agregarInicio, agregarFinal, agregar, insertar,
# eliminarInicio, eliminarFinal, eliminarEn, estaVacia, tamanio, convertirAString,
# limpiar, contiene, eliminarValor, obtener, indiceDe, ultimoIndiceDe, reemplazar,
# convertirALista, invertir, obtenerMaximo, obtenerMinimo, sumar, contar, obtenerNodoEn,
# clonar, fusionar, eliminarTodos, obtenerMediana, promedio, obtenerKDesdeFinal,
# eliminarKDesdeFinal, intercalar, esIgual, ordenar, buscarLineal, eliminarDuplicados,
# toStringDetallado

# Ejemplo corto de uso:
# from ListaEnlazada_Extendida import ListaEnlazada
# l = ListaEnlazada()
# l.agregarFinal(10); l.agregarFinal(20); l.agregarInicio(5)
# print(l.convertirAString())  # -> [5, 10, 20]
