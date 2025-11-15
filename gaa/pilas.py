# pilas_colas_utiles.py
# Biblioteca simple e intuitiva en español para PILAS y COLAS
# Puedes usar: from pilas_colas_utiles import *

########################
#        PILA          #
########################

class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, elemento):
        """Agrega un elemento arriba (push)"""
        self.items.append(elemento)

    def desapilar(self):
        """Saca el elemento de arriba (pop)"""
        if not self.esta_vacia():
            return self.items.pop()
        return None

    def mirar(self):
        """Devuelve el elemento de arriba sin sacarlo"""
        if not self.esta_vacia():
            return self.items[-1]
        return None

    def tamanio(self):
        """Devuelve cuántos elementos hay"""
        return len(self.items)

    def esta_vacia(self):
        """Indica si la pila está vacía"""
        return len(self.items) == 0

    def limpiar(self):
        """Borra todo"""
        self.items.clear()

    def como_lista(self):
        """Devuelve una copia interna como lista"""
        return list(self.items)


########################
#        COLA          #
########################

class Cola:
    def __init__(self):
        self.items = []

    def encolar(self, elemento):
        """Agrega un elemento al final (enqueue)"""
        self.items.append(elemento)

    def desencolar(self):
        """Saca el primer elemento (dequeue)"""
        if not self.esta_vacia():
            return self.items.pop(0)
        return None

    def mirar(self):
        """Devuelve el primer elemento sin sacarlo"""
        if not self.esta_vacia():
            return self.items[0]
        return None

    def tamanio(self):
        """Devuelve cuántos elementos hay"""
        return len(self.items)

    def esta_vacia(self):
        """Indica si la cola está vacía"""
        return len(self.items) == 0

    def limpiar(self):
        """Borra todos los elementos"""
        self.items.clear()

    def como_lista(self):
        """Devuelve una copia interna como lista"""
        return list(self.items)


########################
#      DEQUE (Doble)   #
########################

class Deque:
    def __init__(self):
        self.items = []

    # Inserciones
    def encolar_adelante(self, elemento):
        self.items.insert(0, elemento)

    def encolar_atras(self, elemento):
        self.items.append(elemento)

    # Extracciones
    def desencolar_adelante(self):
        if not self.esta_vacia():
            return self.items.pop(0)
        return None

    def desencolar_atras(self):
        if not self.esta_vacia():
            return self.items.pop()
        return None

    # Utilidades
    def mirar_adelante(self):
        if not self.esta_vacia():
            return self.items[0]
        return None

    def mirar_atras(self):
        if not self.esta_vacia():
            return self.items[-1]
        return None

    def tamanio(self):
        return len(self.items)

    def esta_vacia(self):
        return len(self.items) == 0

    def limpiar(self):
        self.items.clear()

    def como_lista(self):
        return list(self.items)

############################################
# README - Descripción de cada función     #
############################################
#
# --- PILA ---
# apilar(x): Agrega un elemento arriba de la pila.
# desapilar(): Quita y devuelve el elemento arriba.
# mirar(): Muestra el elemento de arriba sin quitarlo.
# tamanio(): Devuelve cuántos elementos hay.
# esta_vacia(): Dice si la pila está vacía.
# limpiar(): Borra todos los elementos.
# como_lista(): Devuelve los elementos como lista.
#
# --- COLA ---
# encolar(x): Agrega un elemento al final.
# desencolar(): Quita y devuelve el primero.
# mirar(): Devuelve el primer elemento sin quitarlo.
# tamanio(): Número de elementos.
# esta_vacia(): Dice si está vacía.
# limpiar(): Borra la cola completa.
# como_lista(): Devuelve la cola como lista.
#
# --- DEQUE ---
# encolar_adelante(x): Agrega al inicio.
# encolar_atras(x): Agrega al final.
# desencolar_adelante(): Quita el primero.
# desencolar_atras(): Quita el último.
# mirar_adelante(): Ve el primero sin quitar.
# mirar_atras(): Ve el último sin quitar.
# tamanio(): Elementos totales.
# esta_vacia(): Indica si está vacío.
# limpiar(): Borra todos los elementos.
# como_lista(): Devuelve los elementos como lista.
