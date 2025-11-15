# P3-linkedlist.py
# Agregar y insertar en lista enlazada

from P1 import Node  # usamos la clase Node

class LinkedList:
    def __init__(self):
        self.__head = None   # inicio de la lista
        self.__tail = None   # fin de la lista
        self.__size = 0      # cantidad de nodos

    # agrega nodo al inicio (ya usado)
    def addFirst(self, e):
        newNode = Node(e)            # crea nodo
        newNode.next = self.__head   # enlaza con cabeza
        self.__head = newNode        # nueva cabeza
        self.__size += 1             # aumentar tamaño
        if self.__tail is None:      # si estaba vacío
            self.__tail = self.__head  # cola igual cabeza

    # agrega nodo al final
    def addLast(self, e):
        newNode = Node(e)            # crea nodo
        if self.__size == 0:         # lista vacía
            self.__head = self.__tail = newNode  # único nodo
        else:
            self.__tail.next = newNode  # enlaza al final
            self.__tail = newNode       # actualiza cola
        self.__size += 1              # aumentar tamaño

    # alias de addLast
    def add(self, e):
        self.addLast(e)              # reutiliza addLast

    # inserta en posición index
    def insert(self, index, e):
        if index <= 0:               # al inicio o negativo
            self.addFirst(e)
        elif index >= self.__size:   # al final o mayor
            self.addLast(e)
        else:
            current = self.__head    # nodo temporal
            for _ in range(1, index):# avanzar hasta index-1
                current = current.next
            temp = current.next      # guardar siguiente
            current.next = Node(e)   # insertar nuevo nodo
            current.next.next = temp # enlazar resto
            self.__size += 1         # aumentar tamaño

    # representación textual
    def __str__(self):
        elems = []
        cur = self.__head
        while cur:
            elems.append(str(cur.element))  # guardar dato
            cur = cur.next                  # siguiente nodo
        return "[" + ", ".join(elems) + "]"  # formato lista
