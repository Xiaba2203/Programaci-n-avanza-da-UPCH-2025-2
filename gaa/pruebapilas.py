from pilas import Pila, Cola, Deque

# ------------------------------
#        PRUEBA DE PILA
# ------------------------------

print("=== PRUEBA PILA ===")
p = Pila()

p.apilar(10)
p.apilar(20)
p.apilar(30)

print("Pila actual:", p.como_lista())
print("Elemento arriba:", p.mirar())
print("Desapilando:", p.desapilar())
print("Pila final:", p.como_lista())
print("Tamaño final:", p.tamanio())
print()


# ------------------------------
#        PRUEBA DE COLA
# ------------------------------

print("=== PRUEBA COLA ===")
c = Cola()

c.encolar("A")
c.encolar("B")
c.encolar("C")

print("Cola actual:", c.como_lista())
print("Primero en la cola:", c.mirar())
print("Desencolando:", c.desencolar())
print("Cola final:", c.como_lista())
print("Tamaño final:", c.tamanio())
print()


# ------------------------------
#        PRUEBA DE DEQUE
# ------------------------------

print("=== PRUEBA DEQUE ===")
d = Deque()

d.encolar_atras(1)
d.encolar_atras(2)
d.encolar_adelante(0)
d.encolar_atras(3)

print("Deque actual:", d.como_lista())
print("Adelante:", d.mirar_adelante())
print("Atrás:", d.mirar_atras())
print("Desencolando adelante:", d.desencolar_adelante())
print("Desencolando atrás:", d.desencolar_atras())
print("Deque final:", d.como_lista())
print("Tamaño final:", d.tamanio())
