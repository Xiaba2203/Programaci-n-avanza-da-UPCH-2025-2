import numpy as np  # importar numpy

# a) pedir dimensiones N y M
N = int(input("Ingrese N: "))  # filas
M = int(input("Ingrese M: "))  # columnas

# b) crear matriz de ceros
A = np.zeros((N, M), dtype=int)  # matriz inicial vacía

# c) llenar matriz con datos ingresados
for i in range(N):  # recorrer filas
    for j in range(M):  # recorrer columnas
        valor = int(input(f"Ingrese valor A[{i},{j}]: "))  # pedir dato
        A[i, j] = valor  # guardar en matriz

# d) vector con suma de filas
suma_filas = A.sum(axis=1)  # sumar por filas
print("Suma de filas:", suma_filas)

# e) convertir matriz a lista anidada
lista_B = A.tolist()  # matriz a lista
print("Lista anidada:", lista_B)

# f) vector con máximos de columnas
max_cols = A.max(axis=0)  # máximo por columna
print("Máximos de columnas:", max_cols)
