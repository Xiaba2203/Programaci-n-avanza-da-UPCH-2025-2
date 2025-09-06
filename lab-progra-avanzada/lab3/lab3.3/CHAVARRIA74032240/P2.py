import numpy as np  # usamos numpy

# Pedimos tamaños de los vectores
N = int(input("Ingrese N: "))
M = int(input("Ingrese M: "))

# Creamos vectores A y B con enteros aleatorios [1,50]
A = np.random.randint(1, 51, N)
B = np.random.randint(1, 51, M)

print("Vector A:", A)
print("Vector B:", B)

# a) Elementos comunes
comunes = np.intersect1d(A, B)  # comunes
print("a) Comunes:", comunes)

# b) Nuevo vector A sin elementos de B
sinB = np.setdiff1d(A, B)  # quitamos
print("b) A sin B:", sinB)

# c) Nuevo vector con +1 en posiciones pares
c = A.copy()  # copiamos para no dañar
c[::2] += 1  # sumamos en pares (0,2,4…)
print("c) A con +1 en pares:", c)

# d) Verificar igualdad A y B
iguales = np.array_equal(A, B)  # mismo tamaño y valores
print("d) ¿A y B iguales?:", iguales)

# e) Volver B inmutable
B.flags.writeable = False  # solo lectura
print("e) Vector B inmutable")

# f) Guardar y leer archivo .npz
np.savez("vectores.npz", A=A, B=B)  # guardamos
data = np.load("vectores.npz")  # leemos
print("f) A cargado:", data["A"])
print("f) B cargado:", data["B"])
