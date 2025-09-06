import numpy as np  # usamos numpy

# Pedimos tamaño del vector
N = int(input("Ingrese N: "))

# Creamos vector A con enteros entre -10 y 10
A = np.random.randint(-10, 11, N)
print("Vector A:", A)

# a) Desplazar dos posiciones a derecha
a = np.roll(A, 2)  # movemos 2
print("a) Desplazado 2 derecha:", a)

# b) Contar positivos, negativos y ceros
positivos = np.sum(A > 0)  # mayores 0
negativos = np.sum(A < 0)  # menores 0
ceros = np.sum(A == 0)  # iguales 0
print("b) Positivos:", positivos)
print("b) Negativos:", negativos)
print("b) Ceros:", ceros)

# c) Contar cuántos son iguales al máximo
max_val = np.max(A)  # mayor valor
cant_max = np.sum(A == max_val)  # cuántos son iguales
print("c) Máximo:", max_val, "Cantidad:", cant_max)
