# P5-linkedlist.py
# removeAt + iterator para LinkedList

from P1 import Node

class LinkedListIterator:
    def __init__(self, head):
        self.current = head  # nodo actual iterador

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None:    # fin de iteración
            raise StopIteration
        element = self.current.element  # dato actual
        self.current = self.current.next  # avanzar
        return element               # devolver dato

class LinkedList:
    def __init__(self):
        self.__head = None   # inicio
        self.__tail = None   # fin
        self.__size = 0      # tamaño

    def addLast(self, e):
        newNode = Node(e)            # crea nodo
        if self.__size == 0:         # lista vacía
            self.__head = self.__tail = newNode
        else:
            self.__tail.next = newNode  # enlazar al final
            self.__tail = newNode       # actualizar cola
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

    # elimina nodo en index y retorna su dato
    def removeAt(self, index):
        if index < 0 or index >= self.__size:  # fuera de rango
            return None
        if index == 0:                          # primer elemento
            return self.removeFirst()
        if index == self.__size - 1:           # último elemento
            return self.removeLast()
        current = self.__head
        for _ in range(1, index):              # avanzar a index-1
            current = current.next
        removed = current.next                 # nodo a eliminar
        current.next = removed.next            # saltar nodo
        self.__size -= 1                       # reducir tamaño
        return removed.element                 # retornar dato

    def __iter__(self):
        return LinkedListIterator(self.__head)  # retorna iterador

    def __str__(self):
        elems = []
        cur = self.__head
        while cur:
            elems.append(str(cur.element))  # guardar dato
            cur = cur.next                  # siguiente nodo
        return "[" + ", ".join(elems) + "]"  # formato lista
