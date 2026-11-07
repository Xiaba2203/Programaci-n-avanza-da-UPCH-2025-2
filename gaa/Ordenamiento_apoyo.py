# ==============================================================
# Ordenamiento_apoyo.py  -  ALGORITMOS DE ORDENACION SOBRE LinkedList
# ==============================================================
# COMO USAR:   from Ordenamiento_apoyo import *
#
# Ordenan de MENOR a MAYOR trabajando con nodos (sin listas de Python).
# Los que dicen "en el lugar" modifican la misma lista (intercambian los
# elementos de los nodos). Los que dicen "devuelve" crean una lista nueva.
#
# Parametro opcional traza=True: imprime la lista despues de cada pasada,
# ideal para hacer/verificar las TRAZAS A MANO (Lab 11.2 ej. 6).
#
# Necesita: LinkedList.py y LinkedList_apoyo.py
# ==============================================================

from LinkedList import LinkedList, Node
from LinkedList_apoyo import obtenerNodo, copiar


# ==============================================================
# TABLA DE COMPLEJIDAD (para las preguntas teoricas)
# ==============================================================
# Algoritmo   | Peor    | Mejor              | Intermedio | Nota
# ------------+---------+--------------------+------------+----------------------
# Seleccion   | O(n^2)  | O(n^2)             | O(n^2)     | Pocos intercambios (max n-1),
#             |         |                    |            | pero SIEMPRE hace todas las comparaciones.
# Burbuja     | O(n^2)  | O(n^2); O(n) con   | O(n^2)     | Muchos intercambios. Muy simple.
#             |         | version mejorada   |            |
# Insercion   | O(n^2)  | O(n) (ya ordenada) | O(n^2)     | Buena en listas casi ordenadas, estable.
# QuickSort   | O(n^2)  | O(n log n)         | O(n log n) | Peor caso: pivote siempre el menor/mayor
#             |         |                    |            | (lista ya ordenada con pivote 1.o o ultimo).
# MergeSort   | O(n log n) siempre           | O(n log n) | Necesita memoria extra; estable.
#
# Si un algoritmo O(n^2) tarda t con n elementos, con k*n tarda k^2 * t.
#   Ej: 3.1 ms con 200 -> 400 elem: 3.1*4 = 12.4 ms | 40000 elem: 3.1*200^2 = 124000 ms = 124 s
# Si es O(n log n) el calculo es: t * (n2 log n2) / (n1 log n1).


# ==============================================================
# 1. SELECCION
# ==============================================================
def ordenSeleccion(lista, traza=False):
    """En cada pasada busco el MENOR de lo que falta y lo intercambio con
    el que esta en la posicion actual. En el lugar."""
    actual = lista.getHead()
    pasada = 1
    while actual is not None:
        menor = actual                      # supongo que el actual es el menor
        buscador = actual.next
        while buscador is not None:         # busco el menor hasta el final
            if buscador.element < menor.element:
                menor = buscador
            buscador = buscador.next
        if menor is not actual:             # intercambio solo si hace falta
            actual.element, menor.element = menor.element, actual.element
        if traza:
            print("Pasada", pasada, ":", lista)
        actual = actual.next
        pasada += 1


# ==============================================================
# 2. BURBUJA
# ==============================================================
def ordenBurbuja(lista, traza=False):
    """Comparo vecinos y los intercambio si estan al reves; en cada pasada
    el mayor 'sube' hasta el final. En el lugar."""
    n = lista.getSize()
    for i in range(n - 1):
        actual = lista.getHead()
        for j in range(n - i - 1):          # lo ultimo ya esta ordenado
            siguiente = actual.next
            if actual.element > siguiente.element:
                actual.element, siguiente.element = siguiente.element, actual.element
            actual = siguiente
        if traza:
            print("Pasada", i + 1, ":", lista)


def ordenBurbujaMejorada(lista, traza=False):
    """Igual, pero si una pasada completa NO hizo intercambios la lista ya
    esta ordenada y se detiene (mejor caso O(n)). Lab 11.2 ej. 2."""
    n = lista.getSize()
    for i in range(n - 1):
        huboIntercambio = False
        actual = lista.getHead()
        for j in range(n - i - 1):
            siguiente = actual.next
            if actual.element > siguiente.element:
                actual.element, siguiente.element = siguiente.element, actual.element
                huboIntercambio = True
            actual = siguiente
        if traza:
            print("Pasada", i + 1, ":", lista)
        if not huboIntercambio:
            break


# ==============================================================
# 3. INSERCION
# ==============================================================
def ordenInsercion(lista, traza=False):
    """Tomo cada elemento desde la 2.a posicion y lo meto en su lugar dentro
    de la parte izquierda (ya ordenada), corriendo los demas a la derecha."""
    if lista.getSize() < 2:
        return
    actual = lista.getHead().next
    pasada = 1
    while actual is not None:
        valor = actual.element
        # 1) busco donde va 'valor' dentro de la parte ordenada
        buscador = lista.getHead()
        while buscador is not actual and buscador.element <= valor:
            buscador = buscador.next
        # 2) corro todo una posicion a la derecha desde ese lugar hasta 'actual'
        if buscador is not actual:
            llevado = valor
            nodo = buscador
            while True:
                nodo.element, llevado = llevado, nodo.element
                if nodo is actual:
                    break
                nodo = nodo.next
        if traza:
            print("Pasada", pasada, ":", lista)
        actual = actual.next
        pasada += 1


# ==============================================================
# 4. QUICKSORT (usa posiciones; en el lugar)
# ==============================================================
# Uso:  quickSortLista(lista, 0, lista.getSize() - 1)
# Elige un PIVOTE, deja a su izquierda los menores y a su derecha los mayores,
# y repite recursivamente en cada lado (divide y venceras).
# pivote puede ser "ultimo" (Version 1 del lab), "primero" (Version 2) o "medio".

def _valorEn(lista, i):
    return obtenerNodo(lista, i).element

def _intercambiarPos(lista, i, j):
    nodoI = obtenerNodo(lista, i)
    nodoJ = obtenerNodo(lista, j)
    nodoI.element, nodoJ.element = nodoJ.element, nodoI.element

def particion(lista, bajo, alto, pivote="medio"):
    """Deja el pivote en su posicion final y devuelve esa posicion."""
    if pivote == "medio":
        _intercambiarPos(lista, (bajo + alto) // 2, alto)   # llevo el pivote al final
    elif pivote == "primero":
        _intercambiarPos(lista, bajo, alto)
    valorPivote = _valorEn(lista, alto)
    i = bajo - 1                                  # i = ultimo indice de los menores
    for j in range(bajo, alto):
        if _valorEn(lista, j) <= valorPivote:
            i += 1
            _intercambiarPos(lista, i, j)
    _intercambiarPos(lista, i + 1, alto)          # pivote a su lugar
    return i + 1

def quickSortLista(lista, bajo, alto, pivote="medio"):
    if bajo < alto:
        pi = particion(lista, bajo, alto, pivote)
        quickSortLista(lista, bajo, pi - 1, pivote)
        quickSortLista(lista, pi + 1, alto, pivote)


# ==============================================================
# 5. MERGESORT (sobre nodos)
# ==============================================================
# Divide la lista por la mitad (con punteros lento/rapido), ordena cada
# mitad recursivamente y las mezcla. Siempre O(n log n).

def mergeSortNodos(cabeza):
    """Recibe la cabeza de una cadena de nodos y devuelve la nueva cabeza
    ordenada. ATENCION: reorganiza los enlaces de esos nodos."""
    if cabeza is None or cabeza.next is None:     # 0 o 1 nodo: ya esta ordenado
        return cabeza
    lento = cabeza
    rapido = cabeza.next
    while rapido is not None and rapido.next is not None:
        lento = lento.next
        rapido = rapido.next.next
    mitadDerecha = lento.next
    lento.next = None                             # corto en dos
    izquierda = mergeSortNodos(cabeza)
    derecha = mergeSortNodos(mitadDerecha)
    return mezclarNodos(izquierda, derecha)

def mezclarNodos(a, b):
    """Mezcla dos cadenas YA ORDENADAS en una sola ordenada."""
    ficticio = Node(None)                         # nodo auxiliar de arranque
    ultimo = ficticio
    while a is not None and b is not None:
        if a.element <= b.element:
            ultimo.next = a
            a = a.next
        else:
            ultimo.next = b
            b = b.next
        ultimo = ultimo.next
    if a is not None:
        ultimo.next = a
    else:
        ultimo.next = b
    return ficticio.next

def ordenarMerge(lista):
    """DEVUELVE una LinkedList nueva ordenada con MergeSort (la original
    queda intacta). Trabajo sobre una copia y reconstruyo el resultado
    para que head, tail y size queden bien."""
    copia = copiar(lista)
    cabeza = mergeSortNodos(copia.getHead())
    resultado = LinkedList()
    actual = cabeza
    while actual is not None:
        resultado.addLast(actual.element)
        actual = actual.next
    return resultado


# ==============================================================
# PRUEBA RAPIDA: python Ordenamiento_apoyo.py
# ==============================================================
if __name__ == "__main__":
    def crear(*valores):
        lista = LinkedList()
        for v in valores:
            lista.addLast(v)
        return lista

    A = (44, 88, 55, 99, 66, 33, 22, 88, 77)      # lista del Lab 11.2 ej. 6
    print("Seleccion con traza:")
    l = crear(*A)
    ordenSeleccion(l, traza=True)
    print("Burbuja   :", end=" "); l = crear(*A); ordenBurbuja(l); print(l)
    print("Insercion :", end=" "); l = crear(*A); ordenInsercion(l); print(l)
    print("Quick     :", end=" "); l = crear(*A); quickSortLista(l, 0, l.getSize() - 1); print(l)
    print("Merge     :", ordenarMerge(crear(*A)))
