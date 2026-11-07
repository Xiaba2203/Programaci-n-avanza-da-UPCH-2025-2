# ==============================================================
# PilaCola_apoyo.py  -  MINI LIBRERIA DE PILAS Y COLAS + PROBLEMAS TIPICOS
# ==============================================================
# COMO USAR:   from PilaCola_apoyo import *
#
# Esta libreria es INDEPENDIENTE de LinkedList.py: tiene su propio Node.
# Nada de listas de Python: todo con nodos enlazados.
#
# PILA (Stack) = LIFO: el ULTIMO en entrar es el PRIMERO en salir.
# COLA (Queue) = FIFO: el PRIMERO en entrar es el PRIMERO en salir.
#
# Los labs usan los nombres Stack y Queue; al final de la clase hay alias:
#       Stack = Pila      Queue = Cola
# ==============================================================


class Node:
    """Un nodo guarda un elemento y apunta al siguiente."""
    def __init__(self, element):
        self.element = element
        self.next = None


# ==============================================================
# 1. PILA
# ==============================================================
class Pila:
    def __init__(self):
        self.__tope = None      # nodo de arriba (el unico que se ve)
        self.__size = 0

    def push(self, e):
        """Apila e en el tope."""
        nuevo = Node(e)
        nuevo.next = self.__tope    # 1.o: el nuevo apunta al tope actual
        self.__tope = nuevo         # 2.o: el nuevo pasa a ser el tope
        self.__size += 1

    def pop(self):
        """Saca y devuelve el elemento del tope (None si esta vacia)."""
        if self.__size == 0:
            return None
        eliminado = self.__tope
        self.__tope = eliminado.next    # el tope baja un nodo
        self.__size -= 1
        return eliminado.element

    def peek(self):
        """Devuelve el tope SIN sacarlo (None si esta vacia)."""
        if self.__size == 0:
            return None
        return self.__tope.element

    def isEmpty(self):
        return self.__size == 0

    def getSize(self):
        return self.__size

    def __len__(self):                  # permite usar len(pila)
        return self.__size

    def clear(self):
        self.__tope = None
        self.__size = 0

    def contains(self, e):
        """True si e esta en la pila."""
        actual = self.__tope
        while actual is not None:
            if actual.element == e:
                return True
            actual = actual.next
        return False

    def reverse(self):
        """Invierte la pila cambiando los enlaces (Lab 10.2 ej. 6)."""
        anterior = None
        actual = self.__tope
        while actual is not None:
            siguiente = actual.next
            actual.next = anterior
            anterior = actual
            actual = siguiente
        self.__tope = anterior

    def __str__(self):
        """Muestra de la cima hacia la base:  3 | 2 | 1"""
        texto = ""
        actual = self.__tope
        while actual is not None:
            texto += str(actual.element)
            if actual.next is not None:
                texto += " | "
            actual = actual.next
        return texto


# ==============================================================
# 2. COLA
# ==============================================================
class Cola:
    def __init__(self):
        self.__frente = None    # de aqui se SACA
        self.__final = None     # aqui se AGREGA
        self.__size = 0

    def enqueue(self, e):
        """Agrega e al final de la cola."""
        nuevo = Node(e)
        if self.__final is None:            # cola vacia
            self.__frente = self.__final = nuevo
        else:
            self.__final.next = nuevo       # enlazo detras del ultimo
            self.__final = nuevo
        self.__size += 1

    def dequeue(self):
        """Saca y devuelve el elemento del frente (None si esta vacia)."""
        if self.__size == 0:
            return None
        eliminado = self.__frente
        self.__frente = eliminado.next
        if self.__frente is None:           # quedo vacia: tambien limpio el final
            self.__final = None
        self.__size -= 1
        return eliminado.element

    def peek(self):
        """Devuelve el frente SIN sacarlo."""
        if self.__size == 0:
            return None
        return self.__frente.element

    def isEmpty(self):
        return self.__size == 0

    def getSize(self):
        return self.__size

    def __len__(self):
        return self.__size

    def clear(self):
        self.__frente = self.__final = None
        self.__size = 0

    def contains(self, e):
        actual = self.__frente
        while actual is not None:
            if actual.element == e:
                return True
            actual = actual.next
        return False

    def __str__(self):
        """Muestra del frente hacia el final:  1 | 2 | 3"""
        texto = ""
        actual = self.__frente
        while actual is not None:
            texto += str(actual.element)
            if actual.next is not None:
                texto += " | "
            actual = actual.next
        return texto


# Alias para que funcionen los nombres de los labs
Stack = Pila
Queue = Cola


# ==============================================================
# 3. COLA SIN ATRIBUTO "final" (Lab 10.3 ejercicio 3)
# ==============================================================
# Solo cambia enqueue: ahora hay que RECORRER toda la cola para hallar
# el ultimo nodo (O(n) en vez de O(1)). dequeue se simplifica.
class ColaSinFinal:
    def __init__(self):
        self.__head = None
        self.__size = 0

    def enqueue(self, e):
        nuevo = Node(e)
        if self.__head is None:
            self.__head = nuevo
        else:
            actual = self.__head
            while actual.next is not None:      # busco el ultimo nodo
                actual = actual.next
            actual.next = nuevo
        self.__size += 1

    def dequeue(self):
        if self.__size == 0:
            return None
        eliminado = self.__head
        self.__head = eliminado.next
        self.__size -= 1
        return eliminado.element

    def isEmpty(self):
        return self.__size == 0

    def getSize(self):
        return self.__size

    def __len__(self):
        return self.__size


# ==============================================================
# 4. COLA USANDO DOS PILAS (Lab 10.3 ejercicio 5)
# ==============================================================
# 'entrada' recibe los nuevos. Cuando hay que sacar y 'salida' esta vacia,
# paso todo de entrada a salida: el orden se INVIERTE y el mas antiguo
# queda arriba.
class ColaConPilas:
    def __init__(self):
        self.__entrada = Pila()
        self.__salida = Pila()

    def enqueue(self, e):
        self.__entrada.push(e)

    def dequeue(self):
        if self.__salida.isEmpty():
            while not self.__entrada.isEmpty():
                self.__salida.push(self.__entrada.pop())
        return self.__salida.pop()

    def isEmpty(self):
        return self.__entrada.isEmpty() and self.__salida.isEmpty()

    def getSize(self):
        return self.__entrada.getSize() + self.__salida.getSize()


# ==============================================================
# 5. PROBLEMAS TIPICOS CON PILAS
# ==============================================================

def trasladarPila(origen, destino):
    """Pasa todo de origen a destino (el orden queda invertido)."""
    while not origen.isEmpty():
        destino.push(origen.pop())


def copiarPila(origen):
    """Devuelve una pila copia (mismo orden) y deja 'origen' intacta."""
    auxiliar = Pila()
    copia = Pila()
    trasladarPila(origen, auxiliar)         # auxiliar: invertida
    while not auxiliar.isEmpty():
        elemento = auxiliar.pop()
        origen.push(elemento)               # restauro la original
        copia.push(elemento)
    return copia


def invertirPilaIterativo(pila):
    """Invierte una pila con 2 pilas auxiliares (Lab 10.2 ej. 5a).
    Cada traspaso invierte el orden: 3 traspasos = pila invertida."""
    aux1 = Pila()
    aux2 = Pila()
    trasladarPila(pila, aux1)
    trasladarPila(aux1, aux2)
    trasladarPila(aux2, pila)


def insert_at_bottom(pila, valor):
    """Inserta valor en la BASE de la pila (recursivo, Lab 10.2 ej. 5b)."""
    if pila.isEmpty():
        pila.push(valor)                    # caso base: la base es el tope
    else:
        tope = pila.pop()                   # saco el de arriba
        insert_at_bottom(pila, valor)       # inserto en la base de lo que queda
        pila.push(tope)                     # devuelvo el de arriba


def reverse_stack(pila):
    """Invierte la pila con recursion usando insert_at_bottom."""
    if not pila.isEmpty():
        tope = pila.pop()
        reverse_stack(pila)                 # invierto el resto
        insert_at_bottom(pila, tope)        # el que saque va a la base


def ordenarPila(pila):
    """Ordena la pila con una pila auxiliar. El MENOR queda en el tope."""
    auxiliar = Pila()
    while not pila.isEmpty():
        temporal = pila.pop()
        while not auxiliar.isEmpty() and auxiliar.peek() > temporal:
            pila.push(auxiliar.pop())       # devuelvo los que estorban
        auxiliar.push(temporal)
    trasladarPila(auxiliar, pila)


def parentesisBalanceados(texto):
    """Parentesis/corchetes/llaves balanceados. Ej: '{[()]}' -> True.
    Abre -> apilo. Cierra -> el tope debe ser su pareja."""
    pila = Pila()
    for caracter in texto:
        if caracter in "([{":
            pila.push(caracter)
        elif caracter in ")]}":
            if pila.isEmpty():
                return False                # cierre sin apertura
            tope = pila.pop()
            if caracter == ")" and tope != "(":
                return False
            if caracter == "]" and tope != "[":
                return False
            if caracter == "}" and tope != "{":
                return False
    return pila.isEmpty()                   # si sobro algo, faltaba cerrar


def invertirTexto(texto):
    """Invierte un texto usando una pila."""
    pila = Pila()
    for caracter in texto:
        pila.push(caracter)
    resultado = ""
    while not pila.isEmpty():
        resultado += pila.pop()
    return resultado


def decimalABinario(numero):
    """Decimal a binario con pila: los restos salen en orden inverso."""
    if numero == 0:
        return "0"
    pila = Pila()
    while numero > 0:
        pila.push(numero % 2)
        numero = numero // 2
    resultado = ""
    while not pila.isEmpty():
        resultado += str(pila.pop())
    return resultado


def evaluarPostfix(expresion):
    """Evalua una expresion postfix (Lab 10.2 ej. 8). Ej: '2 3 1 * + 9 -' -> -4
    Numero -> push. Operador -> pop dos y push del resultado.
    OJO: el primer pop es el 2.o operando (b), el segundo pop es el 1.o (a).
    No uso split() porque devuelve lista de Python: armo cada token a mano."""
    pila = Pila()
    token = ""
    for caracter in expresion + " ":        # el espacio final cierra el ultimo token
        if caracter != " ":
            token += caracter
        elif token != "":
            if token in ("+", "-", "–", "*", "/"):
                b = pila.pop()
                a = pila.pop()
                if token == "+":
                    pila.push(a + b)
                elif token == "-" or token == "–":
                    pila.push(a - b)
                elif token == "*":
                    pila.push(a * b)
                else:
                    pila.push(a / b)
            else:
                if "." in token:
                    pila.push(float(token))
                else:
                    pila.push(int(token))
            token = ""
    return pila.pop()


# ==============================================================
# 6. PROBLEMAS TIPICOS CON COLAS
# ==============================================================

def invertirCola(cola):
    """Invierte una cola usando una pila."""
    pila = Pila()
    while not cola.isEmpty():
        pila.push(cola.dequeue())
    while not pila.isEmpty():
        cola.enqueue(pila.pop())


def esPalindromoTexto(texto):
    """Palindromo con pila + cola: la pila entrega el ultimo caracter y la
    cola el primero; si siempre coinciden, es palindromo."""
    pila = Pila()
    cola = Cola()
    for caracter in texto:
        pila.push(caracter)
        cola.enqueue(caracter)
    while not pila.isEmpty():
        if pila.pop() != cola.dequeue():
            return False
    return True


def rotarCola(cola, veces):
    """Pasa el frente al final 'veces' veces (simula turnos)."""
    for i in range(veces):
        cola.enqueue(cola.dequeue())


def josephus(cantidad, salto):
    """Josephus: personas en circulo, cada 'salto' se elimina una.
    Devuelve el numero del sobreviviente."""
    cola = Cola()
    for i in range(1, cantidad + 1):
        cola.enqueue(i)
    while cola.getSize() > 1:
        for i in range(salto - 1):
            cola.enqueue(cola.dequeue())    # se salvan, pasan al final
        cola.dequeue()                      # este es eliminado
    return cola.dequeue()


# ==============================================================
# 7. IMPRESORA (Lab 10.3 ejercicio 4)
# ==============================================================
class Peticion:
    """Una peticion: que maquina la pidio y que archivo imprimir."""
    def __init__(self, idMaquina, archivo):
        self.idMaquina = idMaquina
        self.archivo = archivo

    def __str__(self):
        return self.idMaquina + " - " + self.archivo


class Impresora:
    def __init__(self):
        self.__peticiones = Cola()

    def addRequest(self, peticion):
        """Agrega una peticion al final."""
        self.__peticiones.enqueue(peticion)

    def printWork(self):
        """Imprime (simula) la primera peticion y la elimina."""
        if self.__peticiones.isEmpty():
            print("No hay peticiones")
            return
        peticion = self.__peticiones.dequeue()
        print("Imprimiendo:", peticion)

    def getNumRequest(self):
        return self.__peticiones.getSize()

    def showAll(self):
        """Muestra las peticiones pendientes (usa el __str__ de Cola)."""
        print(self.__peticiones)

    def printAll(self):
        while not self.__peticiones.isEmpty():
            self.printWork()


# ==============================================================
# PRUEBA RAPIDA: python PilaCola_apoyo.py
# ==============================================================
if __name__ == "__main__":
    p = Pila()
    for x in (1, 2, 3):
        p.push(x)
    print("Pila (cima primero):", p)
    reverse_stack(p)
    print("Invertida:", p)
    c = Cola()
    for x in (1, 2, 3):
        c.enqueue(x)
    print("Cola:", c)
    print("Balanceado '{[()]}':", parentesisBalanceados("{[()]}"))
    print("Postfix '2 3 1 * + 9 -':", evaluarPostfix("2 3 1 * + 9 -"))
    print("13 en binario:", decimalABinario(13))
    print("Josephus(7,3):", josephus(7, 3))
