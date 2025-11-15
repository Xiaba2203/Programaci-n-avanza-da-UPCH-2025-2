class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

def mergeSortLista(head):
    if head is None or head.siguiente is None:
        return head

    mitad = dividirMitad(head)
    izquierda = mergeSortLista(head)
    derecha = mergeSortLista(mitad)

    return mezclar(izquierda, derecha)

def dividirMitad(head):
    lento = head
    rapido = head.siguiente

    while rapido and rapido.siguiente:
        lento = lento.siguiente
        rapido = rapido.siguiente.siguiente

    mitad = lento.siguiente
    lento.siguiente = None
    return mitad

def mezclar(l1, l2):
    dummy = Nodo(0)
    tail = dummy

    while l1 and l2:
        if l1.valor <= l2.valor:
            tail.siguiente = l1
            l1 = l1.siguiente
        else:
            tail.siguiente = l2
            l2 = l2.siguiente
        tail = tail.siguiente

    if l1:
        tail.siguiente = l1
    else:
        tail.siguiente = l2

    return dummy.siguiente
print("Prueba MergeSort Lista Enlazada")
# Crear una lista enlazada de ejemplo: 4 -> 2 -> 1 -> 3
head = Nodo(4)
head.siguiente = Nodo(2)
head.siguiente.siguiente = Nodo(1)
head.siguiente.siguiente.siguiente = Nodo(3)
# Ordenar la lista enlazada
sorted_head = mergeSortLista(head)
# Imprimir la lista ordenada
current = sorted_head
while current:
    print(current.valor, end=" -> " if current.siguiente else "\n")
    current = current.siguiente
