class Stack:
    """Pila simple con lista."""
    def __init__(self):
        self.items = []  # Inicializa la pila como una lista vacía

    def push(self, value):
        self.items.append(value)  # Agrega un elemento al final de la pila

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()  # Elimina y retorna el último elemento
        return None  # Retorna None si la pila está vacía

    def isEmpty(self):
        return len(self.items) == 0  # Verifica si la pila está vacía

class QueueUsingStacks:
    """Cola implementada usando dos pilas."""
    def __init__(self):
        self.stack_in = Stack()  # Pila para ingresar elementos
        self.stack_out = Stack()  # Pila para sacar elementos

    def enqueue(self, value):
        self.stack_in.push(value)  # Inserta el elemento en la pila de entrada

    def dequeue(self):
        if self.stack_out.isEmpty():
            while not self.stack_in.isEmpty():
                self.stack_out.push(self.stack_in.pop())  # Transfiere elementos a la pila de salida
        return self.stack_out.pop()  # Elimina y retorna el elemento más antiguo

    def isEmpty(self):
        return self.stack_in.isEmpty() and self.stack_out.isEmpty()  # Verifica si ambas pilas están vacías

    def __str__(self):
        return f"Entrada: {self.stack_in.items}, Salida: {self.stack_out.items}"  # Muestra el contenido de ambas pilas
