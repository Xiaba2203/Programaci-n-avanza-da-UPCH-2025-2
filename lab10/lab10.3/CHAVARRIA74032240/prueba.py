# Importa las clases Queue de los módulos P1, P2, P3, PrinterQueue y PrintRequest de P4, y QueueUsingStacks de P5.
from P1 import Queue as Queue1
from P2 import Queue as Queue2
from P3 import Queue as Queue3
from P4 import PrinterQueue, PrintRequest
from P5 import QueueUsingStacks

# Prueba la cola básica de P1: agrega dos elementos, elimina uno y muestra el tamaño.
def test_queue1():
    print("== Test P1: Queue básica ==")
    q = Queue1()
    q.enqueue(10)
    q.enqueue(20)
    print("dequeue ->", q.dequeue())
    print("size ->", q.getSize())
    print()

# Prueba la cola de P2: agrega dos elementos, muestra la cola, elimina uno y muestra la cola y su tamaño.
def test_queue2():
    print("== Test P2: Queue con __str__ y __len__ ==")
    q = Queue2()
    q.enqueue("A")
    q.enqueue("B")
    print(q)
    print("len:", len(q))
    print("dequeue ->", q.dequeue())
    print(q)
    print()

# Prueba la cola de P3: agrega tres elementos, muestra la cola antes y después de eliminar uno.
def test_queue3():
    print("== Test P3: Queue sin last ==")
    q = Queue3()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print("antes:", q)
    print("dequeue ->", q.dequeue())
    print("después:", q)
    print()

# Prueba la cola de impresora de P4: agrega dos solicitudes, muestra todas, imprime una y luego todas.
def test_printer():
    print("== Test P4: PrinterQueue ==")
    printer = PrinterQueue()
    printer.addRequest(PrintRequest("PC_1", "file1.pdf"))
    printer.addRequest(PrintRequest("PC_2", "file2.docx"))
    printer.showAll()
    printer.printWork()
    printer.printAll()
    printer.printWork()  # Ya vacía
    print()

# Prueba la cola implementada con pilas de P5: agrega, elimina y verifica si está vacía.
def test_stack_queue():
    print("== Test P5: QueueUsingStacks ==")
    q = QueueUsingStacks()
    q.enqueue("uno")
    q.enqueue("dos")
    print("dequeue ->", q.dequeue())
    q.enqueue("tres")
    print("dequeue ->", q.dequeue())
    print("dequeue ->", q.dequeue())
    print("isEmpty:", q.isEmpty())
    print()

# Ejecuta todas las pruebas si el archivo se ejecuta directamente.
if __name__ == "__main__":
    test_queue1()
    test_queue2()
    test_queue3()
    test_printer()
    test_stack_queue()
