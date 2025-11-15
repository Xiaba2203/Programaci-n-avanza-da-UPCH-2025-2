"""
Módulo completo: estructuras_ordenamiento_busqueda.py
Incluye:
- TODOS los ordenamientos (bubble, selection, insertion, merge, quick).
- TODAS las búsquedas básicas (lineal, binaria).
- TODAS las búsquedas avanzadas (jump, exponential, ternaria, interpolación).
- Hashing implementado a mano.

IMPORTACIÓN:
    from estructuras_ordenamiento_busqueda import *
"""

# ------------------------------------------------------------
# ORDENAMIENTOS
# ------------------------------------------------------------

def bubble_sort(lista):
    lista = lista.copy()
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


def selection_sort(lista):
    lista = lista.copy()
    n = len(lista)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]
    return lista


def insertion_sort(lista):
    lista = lista.copy()
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        while j >= 0 and clave < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave
    return lista


def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    mid = len(lista) // 2
    left = merge_sort(lista[:mid])
    right = merge_sort(lista[mid:])
    return _merge(left, right)


def _merge(a, b):
    res = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            res.append(a[i]); i += 1
        else:
            res.append(b[j]); j += 1
    res.extend(a[i:])
    res.extend(b[j:])
    return res


def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivot = lista[len(lista) // 2]
    left = [x for x in lista if x < pivot]
    mid = [x for x in lista if x == pivot]
    right = [x for x in lista if x > pivot]
    return quicksort(left) + mid + quicksort(right)


# ------------------------------------------------------------
# BÚSQUEDAS BÁSICAS
# ------------------------------------------------------------

def busqueda_lineal(lista, objetivo):
    for i, valor in enumerate(lista):
        if valor == objetivo:
            return i
    return -1


def busqueda_binaria(lista, objetivo):
    izq, der = 0, len(lista) - 1
    while izq <= der:
        mid = (izq + der) // 2
        if lista[mid] == objetivo: return mid
        elif lista[mid] < objetivo: izq = mid + 1
        else: der = mid - 1
    return -1


# ------------------------------------------------------------
# BÚSQUEDAS AVANZADAS
# ------------------------------------------------------------

import math

def jump_search(lista, objetivo):
    n = len(lista)
    paso = int(math.sqrt(n))
    prev = 0
    while prev < n and lista[min(paso, n) - 1] < objetivo:
        prev = paso
        paso += int(math.sqrt(n))
        if prev >= n: return -1
    for i in range(prev, min(paso, n)):
        if lista[i] == objetivo: return i
    return -1


def exponential_search(lista, objetivo):
    if lista[0] == objetivo: return 0
    i = 1
    while i < len(lista) and lista[i] <= objetivo:
        i *= 2
    return busqueda_binaria_rango(lista, objetivo, i//2, min(i, len(lista)-1))


def busqueda_binaria_rango(lista, objetivo, izq, der):
    while izq <= der:
        mid = (izq+der)//2
        if lista[mid] == objetivo: return mid
        elif lista[mid] < objetivo: izq = mid+1
        else: der = mid-1
    return -1


def busqueda_ternaria(lista, objetivo):
    return _ternaria(lista, objetivo, 0, len(lista)-1)


def _ternaria(lista, objetivo, izq, der):
    if izq > der: return -1
    t1 = izq + (der - izq)//3
    t2 = der - (der - izq)//3
    if lista[t1] == objetivo: return t1
    if lista[t2] == objetivo: return t2
    if objetivo < lista[t1]: return _ternaria(lista, objetivo, izq, t1-1)
    elif objetivo > lista[t2]: return _ternaria(lista, objetivo, t2+1, der)
    return _ternaria(lista, objetivo, t1+1, t2-1)


def busqueda_interpolacion(lista, objetivo):
    izq, der = 0, len(lista)-1
    while izq <= der and lista[izq] <= objetivo <= lista[der]:
        if lista[izq] == lista[der]: break
        pos = izq + int(((objetivo - lista[izq]) * (der - izq)) / (lista[der] - lista[izq]))
        if lista[pos] == objetivo: return pos
        elif lista[pos] < objetivo: izq = pos + 1
        else: der = pos - 1
    return -1


# ------------------------------------------------------------
# HASHING IMPLEMENTADO A MANO
# ------------------------------------------------------------

class TablaHash:
    def __init__(self, capacidad=50):
        self.capacidad = capacidad
        self.tabla = [None] * capacidad

    def _hash(self, clave):
        return hash(clave) % self.capacidad

    def insertar(self, clave, valor):
        idx = self._hash(clave)
        if self.tabla[idx] is None:
            self.tabla[idx] = []
        self.tabla[idx].append((clave, valor))

    def obtener(self, clave):
        idx = self._hash(clave)
        bucket = self.tabla[idx]
        if bucket:
            for c, v in bucket:
                if c == clave: return v
        return None

    def eliminar(self, clave):
        idx = self._hash(clave)
        bucket = self.tabla[idx]
        if bucket:
            for i, (c, _) in enumerate(bucket):
                if c == clave:
                    bucket.pop(i)
                    return


# ------------------------------------------------------------
# README
# ------------------------------------------------------------
"""
README – Contenido del módulo completo

ORDENAMIENTOS:
- bubble_sort: Burbuja, simple pero lento.
- selection_sort: Selección, busca el mínimo.
- insertion_sort: Inserción, como ordenar cartas.
- merge_sort: Divide y conquista, O(n log n).
- quicksort: Muy rápido en promedio.

BÚSQUEDAS BÁSICAS:
- busqueda_lineal: Recorre toda la lista.
- busqueda_binaria: Divide entre 2 (lista ordenada).

BÚSQUEDAS AVANZADAS:
- jump_search: Saltos grandes + búsqueda lineal.
- exponential_search: Aumenta rango exponencialmente.
- busqueda_ternaria: Divide la lista en 3 partes.
- busqueda_interpolacion: Usa fórmula basada en distribución.

HASHING:
- TablaHash: Inserción y búsqueda O(1) promedio.

EJEMPLO:
    from estructuras_ordenamiento_busqueda import *
    datos = [9,3,1,7,5]
    print(merge_sort(datos))
    print(busqueda_binaria(sorted(datos), 7))
    tabla = TablaHash(); tabla.insertar("Luis", 22)
    print(tabla.obtener("Luis"))
"""
