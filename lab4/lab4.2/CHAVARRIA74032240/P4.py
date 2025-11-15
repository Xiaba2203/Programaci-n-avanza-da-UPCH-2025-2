import numpy as np  # importar numpy

# matriz de coeficientes
A = np.array([
    [2, -6, 12, 16],
    [1, -2, 6, 6],
    [-1, -3, 3, -7],
    [0, 3, 4, -6]
])

# vector de resultados
b = np.array([70, 64, -30, -26])

# a) usando inv() y dot()
A_inv = np.linalg.inv(A)  # inversa
x1 = np.dot(A_inv, b)  # multiplicar
print("Solución con inv:", x1)

# b) usando solve()
x2 = np.linalg.solve(A, b)  # resolver directo
print("Solución con solve:", x2)
