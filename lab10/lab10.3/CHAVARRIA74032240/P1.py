class Node:
    def __init__(self, data):
        self.data = data      # Guarda el valor del nodo
        self.next = None      # Apunta al siguiente nodo

class Queue:
    def __init__(self):
        self.__head = None   # Primer nodo de la cola
        self.__last = None   # Último nodo de la cola
        self.__size = 0      # Tamaño de la cola

    def isEmpty(self):
        return self.__size == 0   # Verifica si la cola está vacía

    def enqueue(self, value):
        new_node = Node(value)    # Crea un nuevo nodo
        if self.isEmpty():
            self.__head = new_node   # Si está vacía, el nuevo nodo es el primero
        else:
            self.__last.next = new_node   # Si no, lo agrega al final
        self.__last = new_node      # Actualiza el último nodo
        self.__size += 1            # Incrementa el tamaño

    def dequeue(self):
        if self.isEmpty():
            return None             # Si está vacía, retorna None
        value = self.__head.data    # Obtiene el valor del primer nodo
        self.__head = self.__head.next   # Elimina el primer nodo
        self.__size -= 1            # Decrementa el tamaño
        if self.__size == 0:
            self.__last = None      # Si queda vacía, actualiza el último nodo
        return value                # Retorna el valor eliminado

    def getSize(self):
        return self.__size          # Retorna el tamaño de la cola
