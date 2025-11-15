# La clase Node representa un nodo en la cola, guarda un dato y la referencia al siguiente nodo.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# La clase Queue implementa una cola con nodos enlazados, permite agregar, quitar y mostrar elementos.
class Queue:
    def __init__(self):
        self.__head = None
        self.__last = None
        self.__size = 0

    def isEmpty(self):
        return self.__size == 0

    def enqueue(self, value):
        # Agrega un nuevo nodo al final de la cola.
        new_node = Node(value)
        if self.isEmpty():
            self.__head = new_node
        else:
            self.__last.next = new_node
        self.__last = new_node
        self.__size += 1

    def dequeue(self):
        # Quita el primer nodo de la cola y devuelve su dato.
        if self.isEmpty():
            return None
        value = self.__head.data
        self.__head = self.__head.next
        self.__size -= 1
        if self.__size == 0:
            self.__last = None
        return value

    def getSize(self):
        # Devuelve el tamaño actual de la cola.
        return self.__size

    def showAll(self):
        # Muestra todos los elementos de la cola.
        current = self.__head
        while current:
            print(current.data)
            current = current.next

# La clase PrintRequest representa una solicitud de impresión con id de máquina y nombre de archivo.
class PrintRequest:
    def __init__(self, machine_id, filename):
        self.machine_id = machine_id
        self.filename = filename

    def __str__(self):
        return f"{self.machine_id} -> {self.filename}"

# La clase PrinterQueue gestiona las solicitudes de impresión usando la cola, permite agregar, imprimir y mostrar trabajos.
class PrinterQueue:
    def __init__(self):
        self.queue = Queue()

    def addRequest(self, request):
        # Agrega una solicitud de impresión a la cola.
        self.queue.enqueue(request)

    def printWork(self):
        # Simula la impresión de la primera solicitud en la cola.
        request = self.queue.dequeue()
        if request:
            print(f"Imprimiendo: {request}")
        else:
            print("No hay peticiones.")

    def getNumRequest(self):
        # Devuelve el número de solicitudes en la cola.
        return self.queue.getSize()

    def showAll(self):
        # Muestra todas las solicitudes en la cola.
        print("Cola actual de peticiones:")
        self.queue.showAll()

    def printAll(self):
        # Imprime todas las solicitudes de la cola una por una.
        while not self.queue.isEmpty():
            self.printWork()
