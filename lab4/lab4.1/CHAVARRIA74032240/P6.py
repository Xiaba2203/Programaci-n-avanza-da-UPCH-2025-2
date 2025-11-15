import numpy as np  # usamos numpy

N, M = 5, 5  # tamaño matriz
A = np.arange(N*M).reshape(N, M)  # matriz base
print("Matriz original:\n", A)  # muestra matriz

i = 2  # fila a borrar

B = A.tolist()  # convierte a lista
if 0 <= i < len(B):  # valida
    del B[i]  # borra con del
print("Borrado con del:\n", B)  # muestra lista sin fila

if 0 <= i < A.shape[0]:  # valida
    print("Borrado con slicing:\n", A[np.arange(N) != i])  # slicing

C = []  # lista vacía
for idx, fila in enumerate(A):  # recorre filas
    if idx != i:  # si no es la fila
        C.append(fila.tolist())  # agrega fila
print("Borrado con bucles:\n", C)  # muestra lista

if 0 <= i < A.shape[0]:  # valida
    print("Borrado con numpy:\n", np.delete(A, i, axis=0))  # delete
