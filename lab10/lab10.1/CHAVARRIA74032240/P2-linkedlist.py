# Implementa LinkedList básica con cabeza y cola

from P1 import Node  # importamos la clase Node

class LinkedList:
    def __init__(self):
        self.__head = None   # inicio de la lista
        self.__tail = None   # final de la lista
        self.__size = 0      # número de elementos

    # agrega un elemento al inicio
    def addFirst(self, e):
        newNode = Node(e)            # crea nuevo nodo
        newNode.next = self.__head   # enlaza al anterior primero
        self.__head = newNode        # head apunta al nuevo
        self.__size += 1             # aumenta el tamaño
        if self.__tail is None:      # si la lista estaba vacía
            self.__tail = self.__head  # tail apunta igual

    # obtiene el primer elemento
    def getFirst(self):
        if self.__head is None:      # lista vacía
            return None
        return self.__head.element   # retorna dato del head

    # obtiene el último elemento
    def getLast(self):
        if self.__tail is None:      # lista vacía
            return None
        return self.__tail.element   # retorna dato del tail

    # convierte la lista a texto
    def __str__(self):
        elems = []                   # guarda los datos
        cur = self.__head            # empieza desde cabeza
        while cur is not None:       # recorre toda la lista
            elems.append(str(cur.element))  # guarda el dato
            cur = cur.next           # pasa al siguiente nodo
        return "[" + ", ".join(elems) + "]"  # muestra formato lista
