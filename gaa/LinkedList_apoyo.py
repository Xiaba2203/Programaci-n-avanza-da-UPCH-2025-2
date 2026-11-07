# ==============================================================
# LinkedList_apoyo.py  -  FUNCIONES DE APOYO PARA LISTAS ENLAZADAS
# ==============================================================
# COMO USAR:
#   Opcion A (importar):  from LinkedList_apoyo import *
#   Opcion B (copiar):    copia la funcion que necesites a tu codigo.
#
# Todas las funciones reciben la lista como PRIMER parametro:
#       posicionDeElemento(mi_lista, 5)
#
# Solo usan nodos y LinkedList (nada de listas de Python).
# Usan solo getHead() y getSize(), porque __head, __tail y __size
# son privados y NO se pueden tocar desde fuera de la clase.
#
# IMPORTANTE: en tu LinkedList.py los metodos get, contains, indexOf,
# lastIndexOf, set y remove estan "left as an exercise" (no hacen nada
# util). Por eso aqui uso funciones propias (obtenerNodo, contiene...).
# Al final del archivo hay una seccion para PEGARLOS DENTRO de la clase.
# ==============================================================

from LinkedList import LinkedList, Node


# ==============================================================
# 1. POSICIONES Y ELEMENTOS (el tema de los "punteros")
# ==============================================================
# Idea: un "puntero" es una variable (actual) que apunta a un nodo.
# Avanzar es:  actual = actual.next
# Las posiciones empiezan en 0 (la cabeza es la posicion 0).

def obtenerNodo(lista, posicion):
    """Devuelve el NODO que esta en 'posicion' (None si no existe)."""
    if posicion < 0 or posicion >= lista.getSize():
        return None
    actual = lista.getHead()
    for i in range(posicion):          # avanzo 'posicion' veces
        actual = actual.next
    return actual


def elementoEnPosicion(lista, posicion):
    """Que ELEMENTO hay en esta POSICION? (None si no existe)."""
    nodo = obtenerNodo(lista, posicion)
    if nodo is None:
        return None
    return nodo.element


def posicionDeElemento(lista, e):
    """En que POSICION esta el elemento e? Primera aparicion. -1 si no esta."""
    actual = lista.getHead()
    posicion = 0
    while actual is not None:
        if actual.element == e:
            return posicion
        actual = actual.next
        posicion += 1
    return -1


def ultimaPosicionDeElemento(lista, e):
    """Posicion de la ULTIMA aparicion de e (-1 si no esta)."""
    actual = lista.getHead()
    posicion = 0
    ultima = -1
    while actual is not None:
        if actual.element == e:
            ultima = posicion          # la guardo y sigo buscando
        actual = actual.next
        posicion += 1
    return ultima


def posicionDeNodo(lista, nodo_buscado):
    """Posicion de un NODO concreto. Se compara con 'is' (mismo objeto)."""
    actual = lista.getHead()
    posicion = 0
    while actual is not None:
        if actual is nodo_buscado:
            return posicion
        actual = actual.next
        posicion += 1
    return -1


def todasLasPosiciones(lista, e):
    """Devuelve una LinkedList con TODAS las posiciones donde aparece e."""
    resultado = LinkedList()
    actual = lista.getHead()
    posicion = 0
    while actual is not None:
        if actual.element == e:
            resultado.addLast(posicion)
        actual = actual.next
        posicion += 1
    return resultado


def posicionDelMayor(lista):
    """Posicion del elemento mayor (-1 si la lista esta vacia)."""
    if lista.getSize() == 0:
        return -1
    actual = lista.getHead()
    mayor = actual.element
    posicionMayor = 0
    posicion = 0
    while actual is not None:
        if actual.element > mayor:
            mayor = actual.element
            posicionMayor = posicion
        actual = actual.next
        posicion += 1
    return posicionMayor


def posicionDelMenor(lista):
    """Posicion del elemento menor (-1 si la lista esta vacia)."""
    if lista.getSize() == 0:
        return -1
    actual = lista.getHead()
    menor = actual.element
    posicionMenor = 0
    posicion = 0
    while actual is not None:
        if actual.element < menor:
            menor = actual.element
            posicionMenor = posicion
        actual = actual.next
        posicion += 1
    return posicionMenor


def elementoSiguiente(lista, e):
    """Elemento que va DESPUES de e (None si e es el ultimo o no existe)."""
    actual = lista.getHead()
    while actual is not None:
        if actual.element == e:
            if actual.next is None:
                return None
            return actual.next.element
        actual = actual.next
    return None


def elementoAnterior(lista, e):
    """Elemento que va ANTES de e (None si e es el primero o no existe).
    Se necesita un 2.o puntero 'anterior' que va un paso atras."""
    anterior = None
    actual = lista.getHead()
    while actual is not None:
        if actual.element == e:
            if anterior is None:
                return None
            return anterior.element
        anterior = actual              # primero guardo...
        actual = actual.next           # ...luego avanzo
    return None


def mostrarConPosiciones(lista):
    """Imprime cada nodo con su posicion."""
    actual = lista.getHead()
    posicion = 0
    while actual is not None:
        print("Posicion", posicion, "->", actual.element)
        actual = actual.next
        posicion += 1


# ==============================================================
# 2. CONSULTAS BASICAS (recorrer y calcular)
# ==============================================================
# Patron: actual = lista.getHead(); while actual is not None: ...; actual = actual.next

def contiene(lista, e):
    """True si e esta en la lista."""
    actual = lista.getHead()
    while actual is not None:
        if actual.element == e:
            return True
        actual = actual.next
    return False


def contarApariciones(lista, e):
    """Cuantas veces aparece e."""
    contador = 0
    actual = lista.getHead()
    while actual is not None:
        if actual.element == e:
            contador += 1
        actual = actual.next
    return contador


def sumarTodos(lista):
    """Suma de todos los elementos (numeros)."""
    suma = 0
    actual = lista.getHead()
    while actual is not None:
        suma += actual.element
        actual = actual.next
    return suma


def obtenerMayor(lista):
    """Elemento mayor (None si esta vacia)."""
    if lista.getSize() == 0:
        return None
    mayor = lista.getHead().element        # supongo que el 1.o es el mayor
    actual = lista.getHead().next
    while actual is not None:
        if actual.element > mayor:
            mayor = actual.element
        actual = actual.next
    return mayor


def obtenerMenor(lista):
    """Elemento menor (None si esta vacia)."""
    if lista.getSize() == 0:
        return None
    menor = lista.getHead().element
    actual = lista.getHead().next
    while actual is not None:
        if actual.element < menor:
            menor = actual.element
        actual = actual.next
    return menor


def estaOrdenada(lista):
    """True si esta ordenada de menor a mayor."""
    actual = lista.getHead()
    while actual is not None and actual.next is not None:
        if actual.element > actual.next.element:
            return False
        actual = actual.next
    return True


# ==============================================================
# 3. DOS PUNTEROS (lento / rapido, adelantado / atrasado)
# ==============================================================

def elementoMedio(lista):
    """Elemento del medio. 'rapido' avanza de 2 en 2 y 'lento' de 1 en 1:
    cuando rapido llega al final, lento esta en el medio.
    Si la cantidad es par devuelve el segundo del medio."""
    lento = lista.getHead()
    rapido = lista.getHead()
    while rapido is not None and rapido.next is not None:
        lento = lento.next
        rapido = rapido.next.next
    if lento is None:
        return None
    return lento.element


def elementoDesdeElFinal(lista, k):
    """Elemento que esta a k posiciones del final (k=1 es el ultimo).
    Adelanto un puntero k pasos y luego muevo ambos juntos."""
    if k < 1 or k > lista.getSize():
        return None
    adelantado = lista.getHead()
    for i in range(k):
        adelantado = adelantado.next
    atrasado = lista.getHead()
    while adelantado is not None:
        adelantado = adelantado.next
        atrasado = atrasado.next
    return atrasado.element


# ==============================================================
# 4. INVERTIR (cambiando enlaces)
# ==============================================================

def invertirEnlaces(cabeza):
    """Invierte una cadena de nodos CAMBIANDO LOS ENLACES (Lab 12.4 ej. 2).
    Recibe la cabeza y DEVUELVE la nueva cabeza.
        1->2->3->None   queda   3->2->1->None
    Usa 3 punteros: anterior, actual, siguiente."""
    anterior = None
    actual = cabeza
    while actual is not None:
        siguiente = actual.next        # 1) guardo el resto para no perderlo
        actual.next = anterior         # 2) doy vuelta el enlace
        anterior = actual              # 3) avanzo anterior
        actual = siguiente             # 4) avanzo actual
    return anterior                    # el ultimo nodo visitado es la nueva cabeza


def invertirLista(lista):
    """Devuelve una LinkedList NUEVA con los elementos al reves.
    (addFirst va poniendo cada elemento adelante, asi se invierte.)
    Se hace asi porque desde fuera no se puede actualizar el __tail."""
    resultado = LinkedList()
    actual = lista.getHead()
    while actual is not None:
        resultado.addFirst(actual.element)
        actual = actual.next
    return resultado


# ==============================================================
# 5. COPIAR, UNIR, FILTRAR, ELIMINAR
# ==============================================================

def copiar(lista):
    """Devuelve una lista nueva con los mismos elementos."""
    copia = LinkedList()
    actual = lista.getHead()
    while actual is not None:
        copia.addLast(actual.element)
        actual = actual.next
    return copia


def concatenar(lista1, lista2):
    """Devuelve una lista nueva: primero lista1 y luego lista2."""
    resultado = copiar(lista1)
    actual = lista2.getHead()
    while actual is not None:
        resultado.addLast(actual.element)
        actual = actual.next
    return resultado


def filtrarMayoresQue(lista, valor):
    """Devuelve una lista nueva solo con los elementos > valor."""
    resultado = LinkedList()
    actual = lista.getHead()
    while actual is not None:
        if actual.element > valor:
            resultado.addLast(actual.element)
        actual = actual.next
    return resultado


def eliminarDuplicados(lista):
    """Devuelve una lista nueva SIN repetidos (deja la 1.a aparicion)."""
    resultado = LinkedList()
    actual = lista.getHead()
    while actual is not None:
        if not contiene(resultado, actual.element):
            resultado.addLast(actual.element)
        actual = actual.next
    return resultado


def eliminarTodas(lista, e):
    """Elimina de la lista (en el lugar) todas las apariciones de e.
    Usa removeAt de tu LinkedList. NO avanzo la posicion al eliminar,
    porque el siguiente nodo ocupa la misma posicion."""
    posicion = 0
    while posicion < lista.getSize():
        if elementoEnPosicion(lista, posicion) == e:
            lista.removeAt(posicion)
        else:
            posicion += 1


def intercambiar(lista, posicion1, posicion2):
    """Intercambia los elementos de dos posiciones (True si pudo)."""
    nodo1 = obtenerNodo(lista, posicion1)
    nodo2 = obtenerNodo(lista, posicion2)
    if nodo1 is None or nodo2 is None:
        return False
    nodo1.element, nodo2.element = nodo2.element, nodo1.element
    return True


def insertarOrdenado(lista, e):
    """Inserta e en una lista YA ORDENADA manteniendo el orden.
    Busco la posicion donde va y uso insert de tu LinkedList."""
    posicion = 0
    actual = lista.getHead()
    while actual is not None and actual.element < e:
        actual = actual.next
        posicion += 1
    lista.insert(posicion, e)


def mezclarOrdenadas(lista1, lista2):
    """Une dos listas YA ORDENADAS en una nueva tambien ordenada
    (es la idea del 'merge' de MergeSort)."""
    resultado = LinkedList()
    a = lista1.getHead()
    b = lista2.getHead()
    while a is not None and b is not None:
        if a.element <= b.element:
            resultado.addLast(a.element)
            a = a.next
        else:
            resultado.addLast(b.element)
            b = b.next
    while a is not None:               # sobras de lista1
        resultado.addLast(a.element)
        a = a.next
    while b is not None:               # sobras de lista2
        resultado.addLast(b.element)
        b = b.next
    return resultado


def listaEsPalindromo(lista):
    """True si la lista se lee igual al derecho y al reves."""
    inversa = invertirLista(lista)
    a = lista.getHead()
    b = inversa.getHead()
    while a is not None:
        if a.element != b.element:
            return False
        a = a.next
        b = b.next
    return True


# ==============================================================
# 6. SUMAR DOS NUMEROS CON LISTAS (Lab 10.2 ejercicio 2)
# ==============================================================

def numeroALista(texto):
    """'538' -> lista 8,3,5  (las unidades quedan primero: se suma desde ahi)."""
    lista = LinkedList()
    for caracter in texto:             # recorrer un string si esta permitido
        lista.addFirst(int(caracter))
    return lista


def sumarListas(lista1, lista2):
    """Suma dos numeros guardados digito a digito (unidades primero).
    El resultado queda con las unidades primero tambien."""
    resultado = LinkedList()
    nodo1 = lista1.getHead()
    nodo2 = lista2.getHead()
    acarreo = 0
    while nodo1 is not None or nodo2 is not None or acarreo > 0:
        suma = acarreo
        if nodo1 is not None:
            suma += nodo1.element
            nodo1 = nodo1.next
        if nodo2 is not None:
            suma += nodo2.element
            nodo2 = nodo2.next
        resultado.addLast(suma % 10)   # digito que se queda
        acarreo = suma // 10           # lo que "llevo"
    return resultado


def listaANumeroTexto(lista):
    """Convierte la lista (unidades primero) a texto legible: 8,3,5 -> '538'."""
    texto = ""
    actual = lista.getHead()
    while actual is not None:
        texto = str(actual.element) + texto    # cada digito va adelante
        actual = actual.next
    return texto


# ==============================================================
# 7. RECURSION SOBRE NODOS (se llama con lista.getHead())
# ==============================================================

def sumaRecursiva(nodo):
    """Suma de elementos. Uso: sumaRecursiva(lista.getHead())"""
    if nodo is None:                   # caso base
        return 0
    return nodo.element + sumaRecursiva(nodo.next)


def contarRecursivo(nodo):
    """Cantidad de nodos."""
    if nodo is None:
        return 0
    return 1 + contarRecursivo(nodo.next)


def mayorRecursivo(nodo):
    """Mayor elemento (la lista no debe estar vacia)."""
    if nodo.next is None:
        return nodo.element
    mayorResto = mayorRecursivo(nodo.next)
    if nodo.element > mayorResto:
        return nodo.element
    return mayorResto


def buscarRecursivo(nodo, e):
    """True si e esta en la cadena de nodos."""
    if nodo is None:
        return False
    if nodo.element == e:
        return True
    return buscarRecursivo(nodo.next, e)


def imprimirAlReves(nodo):
    """Imprime los elementos de atras hacia adelante (primero llama, luego imprime)."""
    if nodo is not None:
        imprimirAlReves(nodo.next)
        print(nodo.element, end=" ")


# ==============================================================
# 8. METODOS PARA PEGAR DENTRO DE LA CLASE LinkedList
# ==============================================================
# Estos SI pueden usar self.__head, self.__tail y self.__size.
# Copia el texto (sin las comillas triples) dentro de tu clase LinkedList.
# Se dejan en un string para que este archivo siga siendo ejecutable.

METODOS_PARA_PEGAR_EN_LA_CLASE = r'''
    # --- Reemplazan a los "left as an exercise" ---

    def contains(self, e):
        actual = self.__head
        while actual is not None:
            if actual.element == e:
                return True
            actual = actual.next
        return False

    def get(self, index):
        if index < 0 or index >= self.__size:
            return None
        actual = self.__head
        for i in range(index):
            actual = actual.next
        return actual.element

    def indexOf(self, e):
        actual = self.__head
        posicion = 0
        while actual is not None:
            if actual.element == e:
                return posicion
            actual = actual.next
            posicion += 1
        return -1

    def lastIndexOf(self, e):
        actual = self.__head
        posicion = 0
        ultima = -1
        while actual is not None:
            if actual.element == e:
                ultima = posicion
            actual = actual.next
            posicion += 1
        return ultima

    def set(self, index, e):
        if index < 0 or index >= self.__size:
            return None
        actual = self.__head
        for i in range(index):
            actual = actual.next
        anterior = actual.element
        actual.element = e
        return anterior

    def remove(self, e):
        posicion = self.indexOf(e)
        if posicion == -1:
            return False
        self.removeAt(posicion)
        return True

    # --- CORRECCION: el clear original no reiniciaba el tamano ---
    def clear(self):
        self.__head = self.__tail = None
        self.__size = 0

    # --- Invertir en el lugar (actualiza head y tail) ---
    def invertir(self):
        anterior = None
        actual = self.__head
        self.__tail = self.__head          # el head viejo sera el tail
        while actual is not None:
            siguiente = actual.next
            actual.next = anterior
            anterior = actual
            actual = siguiente
        self.__head = anterior

    # --- Insertar / eliminar usando un NODO como referencia ---
    def insertarDespuesDe(self, nodo_referencia, e):
        if nodo_referencia is None:
            return False
        nuevo = Node(e)
        nuevo.next = nodo_referencia.next  # 1.o enlazo el nuevo con el resto
        nodo_referencia.next = nuevo       # 2.o enlazo la referencia con el nuevo
        if nodo_referencia is self.__tail:
            self.__tail = nuevo
        self.__size += 1
        return True

    def eliminarSiguienteDe(self, nodo_referencia):
        if nodo_referencia is None or nodo_referencia.next is None:
            return None
        eliminado = nodo_referencia.next
        nodo_referencia.next = eliminado.next
        if eliminado is self.__tail:
            self.__tail = nodo_referencia
        self.__size -= 1
        return eliminado.element

    # --- MergeSort sobre la lista enlazada (Lab 12.1 ej. 9) ---
    def ordenarMerge(self):
        self.__head = self._mergeSortNodos(self.__head)
        actual = self.__head               # reubico el tail
        while actual is not None and actual.next is not None:
            actual = actual.next
        self.__tail = actual

    def _mergeSortNodos(self, cabeza):
        if cabeza is None or cabeza.next is None:
            return cabeza
        lento = cabeza
        rapido = cabeza.next
        while rapido is not None and rapido.next is not None:
            lento = lento.next
            rapido = rapido.next.next
        mitadDerecha = lento.next
        lento.next = None                  # corto la lista en dos
        izquierda = self._mergeSortNodos(cabeza)
        derecha = self._mergeSortNodos(mitadDerecha)
        return self._mezclarNodos(izquierda, derecha)

    def _mezclarNodos(self, a, b):
        ficticio = Node(None)
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
'''


# ==============================================================
# PRUEBA RAPIDA: python LinkedList_apoyo.py
# ==============================================================
if __name__ == "__main__":
    lista = LinkedList()
    for valor in (5, 3, 8, 3, 1):
        lista.addLast(valor)
    print("Lista:", lista)
    print("Posicion de 8:", posicionDeElemento(lista, 8))
    print("Elemento en pos 2:", elementoEnPosicion(lista, 2))
    print("Posiciones de 3:", todasLasPosiciones(lista, 3))
    print("Invertida:", invertirLista(lista))
    print("Sin duplicados:", eliminarDuplicados(lista))
    print("Medio:", elementoMedio(lista))
    print("Suma 538 + 4791 =", listaANumeroTexto(sumarListas(numeroALista("538"), numeroALista("4791"))))
