import numpy as np  # usamos numpy

N = 5  # tamaño de la matriz
A = np.random.randint(-30, 31, (N, N))  # matriz aleatoria entre -30 y 30
print("Matriz A:\n", A)  # muestra matriz

print("Filas desplazadas:\n", np.roll(A, 1, axis=1))  # mueve a la derecha
print("Filas ordenadas desc:\n", np.sort(A)[:, ::-1])  # ordena filas desc
print("Columnas ordenadas desc:\n", np.sort(A, axis=0)[::-1])  # columnas desc
print("Suma positivos:", A[A > 0].sum())  # suma solo positivos
print("Suma filas pares col impares:", A[::2, 1::2].sum())  # pares/impares
print("Negativos en 0:\n", np.where(A < 0, 0, A))  # cambia negativos por 0
print("Entre -10 y 10 es 0, resto 9:\n", np.where((-10 <= A) & (A <= 10), 0, 9))  # filtro
