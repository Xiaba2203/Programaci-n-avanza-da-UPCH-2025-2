# ==============================================================
# Busqueda_apoyo.py  -  ALGORITMOS DE BUSQUEDA SOBRE LinkedList
# ==============================================================
# COMO USAR:   from Busqueda_apoyo import *
#
# Todas devuelven POSICIONES (empiezan en 0) o -1 si no se encuentra.
# Necesita: LinkedList.py y LinkedList_apoyo.py
#
# COMPLEJIDAD
#   nuestroMin         : O(n)  siempre recorre toda la lista una vez.
#   Busqueda LINEAL    : peor O(n) (esta al final o no esta)
#                        mejor O(1) (esta en la 1.a posicion)
#                        intermedio O(n) (en promedio ~n/2 comparaciones)
#   Busqueda BINARIA   : peor O(log n), mejor O(1) (esta justo en el medio),
#                        intermedio O(log n). REQUIERE lista ORDENADA.
#                        (En LISTA ENLAZADA llegar al medio cuesta O(n), asi que
#                        en la practica es peor; en un arreglo si es O(log n).)
#   Mas repetido (fuerza bruta)   : O(n^2)
#   Mas repetido (ordenando antes): O(n log n) ordenar + O(n) contar = O(n log n)
# ==============================================================

from LinkedList import LinkedList
from LinkedList_apoyo import obtenerNodo


def nuestroMin(lista):
    """Posicion del valor minimo (la lista no debe estar vacia).
    Asumo que la posicion 0 es la menor y la voy corrigiendo."""
    minimo = lista.getHead().element
    posicionMin = 0
    actual = lista.getHead().next
    posicion = 1
    while actual is not None:
        if actual.element < minimo:
            minimo = actual.element
            posicionMin = posicion
        actual = actual.next
        posicion += 1
    return posicionMin


def busquedaLineal(objetivo, lista):
    """Recorre nodo por nodo hasta encontrar el objetivo."""
    actual = lista.getHead()
    posicion = 0
    while actual is not None:
        if actual.element == objetivo:
            return posicion
        actual = actual.next
        posicion += 1
    return -1


def busquedaBinaria(objetivo, lista):
    """Lista ORDENADA. Miro el medio: si es el objetivo termino; si el
    objetivo es menor descarto la mitad derecha; si es mayor, la izquierda."""
    izquierda = 0
    derecha = lista.getSize() - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        valorMedio = obtenerNodo(lista, medio).element
        if objetivo == valorMedio:
            return medio
        elif objetivo < valorMedio:
            derecha = medio - 1             # busco a la izquierda
        else:
            izquierda = medio + 1           # busco a la derecha
    return -1


def busquedaBinariaRecursiva(objetivo, lista, izquierda, derecha):
    """Version recursiva. Uso: busquedaBinariaRecursiva(x, lista, 0, lista.getSize()-1)"""
    if izquierda > derecha:                 # caso base: no esta
        return -1
    medio = (izquierda + derecha) // 2
    valorMedio = obtenerNodo(lista, medio).element
    if objetivo == valorMedio:
        return medio
    elif objetivo < valorMedio:
        return busquedaBinariaRecursiva(objetivo, lista, izquierda, medio - 1)
    return busquedaBinariaRecursiva(objetivo, lista, medio + 1, derecha)


def trazaBusquedaBinaria(objetivo, lista):
    """Imprime left, right y midpoint en cada paso (Lab 11.1 ej. 4)."""
    izquierda = 0
    derecha = lista.getSize() - 1
    print("left  right  midpoint  valor")
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        valorMedio = obtenerNodo(lista, medio).element
        print(izquierda, "    ", derecha, "    ", medio, "       ", valorMedio)
        if objetivo == valorMedio:
            print("Encontrado en la posicion", medio)
            return medio
        elif objetivo < valorMedio:
            derecha = medio - 1
        else:
            izquierda = medio + 1
    print("left", izquierda, "> right", derecha, "-> no esta (-1)")
    return -1


def masRepetido(lista):
    """Elemento que mas se repite, FUERZA BRUTA O(n^2): para cada nodo
    cuento cuantas veces aparece recorriendo toda la lista."""
    mejorElemento = None
    mejorCuenta = 0
    actual = lista.getHead()
    while actual is not None:
        cuenta = 0
        buscador = lista.getHead()
        while buscador is not None:
            if buscador.element == actual.element:
                cuenta += 1
            buscador = buscador.next
        if cuenta > mejorCuenta:
            mejorCuenta = cuenta
            mejorElemento = actual.element
        actual = actual.next
    return mejorElemento


def masRepetidoOrdenada(lista):
    """Con la lista YA ORDENADA los iguales quedan juntos: una sola pasada O(n)
    contando cada grupo. (Ordena antes con ordenarMerge de Ordenamiento_apoyo)."""
    mejorElemento = None
    mejorCuenta = 0
    actual = lista.getHead()
    while actual is not None:
        cuenta = 1
        siguiente = actual.next
        while siguiente is not None and siguiente.element == actual.element:
            cuenta += 1
            siguiente = siguiente.next
        if cuenta > mejorCuenta:
            mejorCuenta = cuenta
            mejorElemento = actual.element
        actual = siguiente                  # salto todo el grupo
    return mejorElemento


# ==============================================================
# PRUEBA RAPIDA: python Busqueda_apoyo.py
# ==============================================================
if __name__ == "__main__":
    lista = LinkedList()
    for v in (20, 44, 48, 55, 62, 66, 74, 88, 93, 99):
        lista.addLast(v)
    print("Traza objetivo 90:")
    trazaBusquedaBinaria(90, lista)
    print("Traza objetivo 44:")
    trazaBusquedaBinaria(44, lista)
    print("Lineal 74:", busquedaLineal(74, lista), "| Binaria 74:", busquedaBinaria(74, lista))
