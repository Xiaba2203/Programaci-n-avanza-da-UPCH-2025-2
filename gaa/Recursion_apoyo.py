# ==============================================================
# Recursion_apoyo.py  -  EJERCICIOS TIPICOS DE RECURSION
# ==============================================================
# COMO USAR:   from Recursion_apoyo import *
#
# Toda funcion recursiva tiene dos partes:
#   1) CASO BASE: cuando ya no hay que seguir (evita recursion infinita).
#   2) CASO RECURSIVO: resuelve un pedazo y llama a la funcion con un
#      problema MAS PEQUENO.
# Sin listas de Python. Las de listas enlazadas reciben un NODO
# (se llaman con lista.getHead()); mas funciones de ese tipo estan en
# LinkedList_apoyo.py (sumaRecursiva, contarRecursivo, mayorRecursivo...).
# ==============================================================


# ---------------- Lab 12.4 ejercicio 1 ----------------

def sumaSaltos(n):
    """b) N + (N-2) + (N-4) + ... mientras el termino sea > 0.
    sumaSaltos(9) = 9+7+5+3+1 = 25"""
    if n <= 0:                          # caso base
        return 0
    return n + sumaSaltos(n - 2)


def sumaPotencias(n):
    """c) 1^1 + 2^2 + 3^3 + ... + n^n.   sumaPotencias(3) = 1+4+27 = 32"""
    if n == 0:
        return 0
    return n ** n + sumaPotencias(n - 1)


def sumaSerie(n, termino=1):
    """d) 1 + 11 + 111 + ... (n terminos).
    'termino' es el termino actual; el siguiente es termino*10 + 1.
    sumaSerie(3) = 1 + 11 + 111 = 123"""
    if n == 0:
        return 0
    return termino + sumaSerie(n - 1, termino * 10 + 1)


# (a) la suma de los elementos de una lista enlazada esta en
#     LinkedList_apoyo.py:  sumaRecursiva(lista.getHead())


# ---------------- Clasicos numericos ----------------

def factorial(n):
    """n! = n * (n-1)!"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    """fib(0)=0, fib(1)=1, fib(n)=fib(n-1)+fib(n-2).  (lenta: O(2^n))"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def potencia(base, exponente):
    """base elevado a exponente (exponente entero >= 0)."""
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)


def sumaDigitos(n):
    """Suma de los digitos de n.  sumaDigitos(1234) = 10
    n % 10 = ultimo digito, n // 10 = el numero sin el ultimo digito."""
    if n < 10:
        return n
    return n % 10 + sumaDigitos(n // 10)


def contarDigitos(n):
    if n < 10:
        return 1
    return 1 + contarDigitos(n // 10)


def invertirNumero(n, acumulado=0):
    """invertirNumero(123) = 321"""
    if n == 0:
        return acumulado
    return invertirNumero(n // 10, acumulado * 10 + n % 10)


def mcd(a, b):
    """Maximo comun divisor (Euclides)."""
    if b == 0:
        return a
    return mcd(b, a % b)


def decimalABinarioRec(n):
    """Decimal a binario (texto).  decimalABinarioRec(13) = '1101'"""
    if n < 2:
        return str(n)
    return decimalABinarioRec(n // 2) + str(n % 2)


# ---------------- Texto ----------------

def esPalindromoRec(texto):
    """Compara primero con ultimo y repite con lo de en medio."""
    if len(texto) <= 1:
        return True
    if texto[0] != texto[-1]:
        return False
    return esPalindromoRec(texto[1:-1])


def invertirTextoRec(texto):
    if len(texto) <= 1:
        return texto
    return invertirTextoRec(texto[1:]) + texto[0]


# ---------------- Torres de Hanoi ----------------

def hanoi(n, origen, destino, auxiliar):
    """Imprime los movimientos para pasar n discos de origen a destino.
    Necesita 2^n - 1 movimientos."""
    if n == 1:
        print("Mover disco 1 de", origen, "a", destino)
        return
    hanoi(n - 1, origen, auxiliar, destino)      # muevo los n-1 de arriba al auxiliar
    print("Mover disco", n, "de", origen, "a", destino)
    hanoi(n - 1, auxiliar, destino, origen)      # y los paso encima


# ==============================================================
# PRUEBA RAPIDA: python Recursion_apoyo.py
# ==============================================================
if __name__ == "__main__":
    print("sumaSaltos(9)    =", sumaSaltos(9))
    print("sumaPotencias(3) =", sumaPotencias(3))
    print("sumaSerie(4)     =", sumaSerie(4))
    print("factorial(5)     =", factorial(5))
    print("fibonacci(10)    =", fibonacci(10))
    print("decimalABinarioRec(13) =", decimalABinarioRec(13))
