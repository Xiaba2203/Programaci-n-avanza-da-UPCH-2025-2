# LinkedList completa y pruebas simples

from P1 import Node

class LinkedListFull:
    def __init__(self):
        self.__head = None   # inicio
        self.__tail = None   # fin
        self.__size = 0      # tamaño

    def isEmpty(self):
        return self.__size == 0    # True si vacía

    def getSize(self):
        return self.__size         # retorna tamaño

    def addFirst(self, e):
        newNode = Node(e)          # crea nodo
        newNode.next = self.__head # enlaza con cabeza
        self.__head = newNode      # nueva cabeza
        self.__size += 1           # aumentar tamaño
        if self.__tail is None:    # si antes vacío
            self.__tail = self.__head  # actualizar cola

    def addLast(self, e):
        newNode = Node(e)          # crea nodo
        if self.__size == 0:       # lista vacía
            self.__head = self.__tail = newNode
        else:
            self.__tail.next = newNode  # enlazar al final
            self.__tail = newNode       # actualizar cola
        self.__size += 1           # aumentar tamaño

    def add(self, e):
        self.addLast(e)            # alias addLast

    def getFirst(self):
        if self.__head is None:
            return None
        return self.__head.element  # retornar cabeza

    def getLast(self):
        if self.__tail is None:
            return None
        return self.__tail.element  # retornar cola

    def insert(self, index, e):
        if index <= 0:
            self.addFirst(e)       # insertar al inicio
        elif index >= self.__size:
            self.addLast(e)        # insertar al final
        else:
            current = self.__head
            for _ in range(1, index):  # avanzar a index-1
                current = current.next
            temp = current.next
            current.next = Node(e)     # insertar nodo
            current.next.next = temp
            self.__size += 1

    def removeFirst(self):
        if self.__size == 0:
            return None
        removed = self.__head
        self.__head = self.__head.next
        self.__size -= 1
        if self.__size == 0:
            self.__tail = None
        return removed.element

    def removeLast(self):
        if self.__size == 0:
            return None
        elif self.__size == 1:
            temp = self.__head
            self.__head = self.__tail = None
            self.__size = 0
            return temp.element
        else:
            current = self.__head
            for _ in range(self.__size - 2):
                current = current.next
            temp = self.__tail
            self.__tail = current
            self.__tail.next = None
            self.__size -= 1
            return temp.element

    def removeAt(self, index):
        if index < 0 or index >= self.__size:
            return None
        if index == 0:
            return self.removeFirst()
        if index == self.__size - 1:
            return self.removeLast()
        current = self.__head
        for _ in range(1, index):
            current = current.next
        removed = current.next
        current.next = removed.next
        self.__size -= 1
        return removed.element

    def contains(self, e):
        cur = self.__head
        while cur:
            if cur.element == e:
                return True          # encontrado
            cur = cur.next
        return False                 # no encontrado

    def indexOf(self, e):
        cur = self.__head
        idx = 0
        while cur:
            if cur.element == e:
                return idx          # retornar índice
            cur = cur.next
            idx += 1
        return -1                    # no está

    def lastIndexOf(self, e):
        cur = self.__head
        idx = 0
        last = -1
        while cur:
            if cur.element == e:
                last = idx          # actualizar último
            cur = cur.next
            idx += 1
        return last                  # índice o -1

    def set(self, index, e):
        if index < 0 or index >= self.__size:
            return None
        cur = self.__head
        for _ in range(index):       # avanzar al índice
            cur = cur.next
        old = cur.element            # guardar antiguo
        cur.element = e              # reemplazar dato
        return old                   # devolver reemplazado

    def clear(self):
        self.__head = None           # eliminar referencias
        self.__tail = None
        self.__size = 0              # tamaño a cero

    def __iter__(self):
        cur = self.__head
        while cur:
            yield cur.element        # producir elemento
            cur = cur.next

    def __str__(self):
        return "[" + ", ".join(str(x) for x in self) + "]"

# ---------------------------
# Bloque de pruebas (ejecución)
# ---------------------------
if __name__ == "__main__":
    lst = LinkedListFull()
    print("Vacía?", lst.isEmpty())        # True
    lst.addLast("A")                      # agregar al final
    lst.addLast("B")                      # agregar al final
    lst.addFirst("X")                     # agregar al inicio
    print("Lista:", lst)                  # [X, A, B]
    lst.insert(1, "Y")                    # insertar en índice 1
    print("Después insert:", lst)         # [X, Y, A, B]
    print("removeAt 2:", lst.removeAt(2)) # elimina y muestra
    print("Después removeAt:", lst)       # [X, Y, B]
    print("removeFirst:", lst.removeFirst()) # X
    print("removeLast:", lst.removeLast())   # B
    print("Queda:", lst)                  # [Y]
    print("Contains Y?", lst.contains("Y")) # True
    print("Index of Y:", lst.indexOf("Y"))  # 0
    lst.set(0, "Z")                       # reemplazar elemento
    print("set ->", lst)                  # [Z]
    lst.clear()                           # limpiar lista
    print("Vacía tras clear?", lst.isEmpty()) # True
