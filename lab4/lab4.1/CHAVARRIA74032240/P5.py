import numpy as np  # usamos numpy

N = 4  # tamaño de la matriz
A = np.arange(N*N).reshape(N, N)  # matriz base
x = np.array([9, 9, 9, 9])  # vector

print("Vector x:", x)  # muestra vector
print("Matriz original:\n", A)  # muestra matriz

B = A.copy()  # copia de A
B[1::2] = x  # cambia filas impares
print("Matriz resultante:\n", B)  # muestra resultado
