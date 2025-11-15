# Eliminación de primeros y últimos nodos

from P1 import Node  # usamos Node aunque no estrictamente necesario

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
            self.__tail.next = newNode  # enlaza al final
            self.__tail = newNode       # actualizar cola
        self.__size += 1              # aumentar tamaño

    # elimina y retorna primer elemento
    def removeFirst(self):
        if self.__size == 0:         # nada que eliminar
            return None
        removed = self.__head         # guardar nodo eliminado
        self.__head = self.__head.next # mover cabeza
        self.__size -= 1             # disminuir tamaño
        if self.__size == 0:         # si ahora vacío
            self.__tail = None       # limpiar cola
        return removed.element       # retornar dato

    # elimina y retorna último elemento
    def removeLast(self):
        if self.__size == 0:         # lista vacía
            return None
        elif self.__size == 1:       # un solo nodo
            temp = self.__head
            self.__head = self.__tail = None  # ahora vacío
            self.__size = 0
            return temp.element     # retornar único dato
        else:
            current = self.__head
            # avanzar al penúltimo nodo
            for _ in range(self.__size - 2):
                current = current.next
            temp = self.__tail        # nodo final
            self.__tail = current    # actualizar cola
            self.__tail.next = None  # terminar lista
            self.__size -= 1         # disminuir tamaño
            return temp.element     # retornar dato eliminado

    def __str__(self):
        elems = []
        cur = self.__head
        while cur:
            elems.append(str(cur.element))  # guardar dato
            cur = cur.next                  # siguiente nodo
        return "[" + ", ".join(elems) + "]"  # formato lista
