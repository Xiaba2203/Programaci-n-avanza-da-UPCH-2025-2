import numpy as np  # usamos numpy

N = 6  # tamaño de la matriz
A = np.zeros((N, N), dtype=int)  # matriz llena de ceros

for i in range(N):  # recorre filas
    for j in range(N):  # recorre columnas
        A[i][j] = i*10 + j  # formula para llenar

print("Matriz A:\n", A)  # muestra matriz

print("Segunda columna:", A[:, 1])  # todas filas, columna 1
print("Segunda fila:", A[1, :])  # fila 1, todas columnas
print("Mitad superior diagonal principal:\n", A[0:3, 0:3])  # parte superior
print("Mitad inferior diagonal secundaria:\n", A[3:6, 0:3])  # parte inferior
print("Columnas invertidas:\n", A[:, ::-1])  # invierte columnas
print("Matriz sin bordes:\n", A[1:-1, 1:-1])  # quita contorno
