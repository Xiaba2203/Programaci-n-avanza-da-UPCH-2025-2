class Node:
    def __init__(self, data):
        # Nodo de la cola, guarda el dato y el siguiente nodo
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        # Inicializa la cola vacía, con cabeza, último y tamaño
        self.__head = None
        self.__last = None
        self.__size = 0

    def isEmpty(self):
        # Verifica si la cola está vacía
        return self.__size == 0

    def enqueue(self, value):
        # Agrega un elemento al final de la cola
        new_node = Node(value)
        if self.isEmpty():
            self.__head = new_node
        else:
            self.__last.next = new_node
        self.__last = new_node
        self.__size += 1

    def dequeue(self):
        # Elimina y retorna el primer elemento de la cola
        if self.isEmpty():
            return None
        value = self.__head.data
        self.__head = self.__head.next
        self.__size -= 1
        if self.__size == 0:
            self.__last = None
        return value

    def getSize(self):
        # Retorna el tamaño actual de la cola
        return self.__size

    def __str__(self):
        # Devuelve una representación en texto de la cola
        items = []
        current = self.__head
        while current:
            items.append(str(current.data))
            current = current.next
        return " <- ".join(items) if items else "Cola vacía"

    def __len__(self):
        """Permite usar len(cola)."""
        # Permite obtener el tamaño usando len()
        return self.__size
