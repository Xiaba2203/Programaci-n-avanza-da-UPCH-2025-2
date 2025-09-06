import numpy as np  # usamos numpy

# Pedimos tamaño del vector
N = int(input("Ingrese cantidad de elementos N: "))

# Creamos vector A con enteros aleatorios [10,99]
A = np.random.randint(10, 100, N)

print("Vector A:", A)  # mostramos A original

# a) Solo impares de A
impares = A[A % 2 != 0]  # filtramos impares
print("a) Impares:", impares)

# b) Reemplazar impares con -1
b = np.where(A % 2 != 0, -1, A)  # cambio
print("b) Impares=-1:", b)

# c) Invertir vector
c = A[::-1]  # volteamos
print("c) Invertido:", c)

# d) Negar elementos 30-60
d = np.where((A >= 30) & (A <= 60), -A, A)  # negamos
print("d) Rango negado:", d)

# e) Ordenar descendente
e = np.sort(A)[::-1]  # descendente
print("e) Orden descendente:", e)
