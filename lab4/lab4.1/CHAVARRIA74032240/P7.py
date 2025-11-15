import numpy as np  # usamos numpy

N, M = 5, 5  # tamaño matriz
A = np.arange(N*M).reshape(N, M)  # matriz base
print("Matriz original:\n", A)  # muestra matriz

i = 2  # columna a borrar

B = [fila.tolist() for fila in A]  # copia
if 0 <= i < M:  # valida
    for fila in B:  # recorre filas
        del fila[i]  # borra columna
print("Columna borrada con del:\n", B)  # muestra lista

C = [fila[:i] + fila[i+1:] for fila in A.tolist()]  # slicing
print("Columna borrada con slicing:\n", C)  # muestra lista

D = []  # lista nueva
for fila in zip(*A):  # transpuesta con zip
    D.append(list(fila))  # agrega filas
if 0 <= i < len(D):  # valida
    del D[i]  # borra columna
print("Columna borrada con zip:\n", list(zip(*D)))  # lista resultante

if 0 <= i < A.shape[1]:  # valida
    print("Columna borrada con numpy:\n", np.delete(A, i, axis=1))  # delete
