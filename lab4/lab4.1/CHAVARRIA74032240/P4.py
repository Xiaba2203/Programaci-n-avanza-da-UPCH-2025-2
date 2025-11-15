import numpy as np  # usamos numpy

N = 5  # tamaño de la matriz

print("Diagonal identidad:\n", np.identity(N, dtype=int))  # identidad
print("Diagonal de 3 en 3:\n", np.diag(np.arange(0, N*3, 3)))  # diagonal 3 en 3

M = np.zeros((N, N), dtype=int)  # matriz de ceros
M[0, :] = 1  # fila arriba en 1
M[-1, :] = 1  # fila abajo en 1
M[:, 0] = 1  # columna izquierda en 1
M[:, -1] = 1  # columna derecha en 1
print("Bordes en 1:\n", M)  # muestra resultado
