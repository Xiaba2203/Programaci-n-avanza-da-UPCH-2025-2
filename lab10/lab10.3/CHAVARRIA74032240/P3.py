class Node:
    def __init__(self, data):
        self.data = data      # Guarda el valor del nodo
        self.next = None      # Apunta al siguiente nodo

class Queue:
    def __init__(self):
        self.__head = None   # Inicio de la cola
        self.__size = 0      # Tamaño de la cola

    def isEmpty(self):
        return self.__head is None   # Verifica si la cola está vacía

    def enqueue(self, value):
        new_node = Node(value)       # Crea un nuevo nodo
        if self.isEmpty():
            self.__head = new_node   # Si está vacía, el nuevo nodo es la cabeza
        else:
            current = self.__head
            while current.next:      # Busca el último nodo
                current = current.next
            current.next = new_node  # Agrega el nuevo nodo al final
        self.__size += 1             # Incrementa el tamaño

    def dequeue(self):
        if self.isEmpty():
            return None              # Si está vacía, retorna None
        value = self.__head.data     # Obtiene el valor de la cabeza
        self.__head = self.__head.next  # Mueve la cabeza al siguiente nodo
        self.__size -= 1             # Decrementa el tamaño
        return value                 # Retorna el valor eliminado

    def getSize(self):
        return self.__size           # Retorna el tamaño de la cola
