import numpy as np  # usamos numpy

# Pedimos cantidad de puntos
N = int(input("Ingrese N puntos: "))

# Creamos coordenadas X e Y en rango [-50,50]
X = np.random.randint(-50, 51, N)
Y = np.random.randint(-50, 51, N)

print("X:", X)
print("Y:", Y)

# a) Radio menor círculo centrado en origen
dist_origen = np.sqrt(X**2 + Y**2)  # distancia origen
radio = np.max(dist_origen)  # máximo
print("a) Radio menor círculo:", radio)

# b) Punto más alejado del eje Y
alejado_Y = np.argmax(np.abs(X))  # mayor |X|
print("b) Punto más alejado de Y:", (X[alejado_Y], Y[alejado_Y]))

# c) Distancia mayor entre dos puntos
distancias = np.sqrt((X[:,None]-X)**2 + (Y[:,None]-Y)**2)  # matriz dist
max_dist = np.max(distancias)  # distancia mayor
indices = np.where(distancias == max_dist)  # puntos que cumplen
puntos = list(zip(X[indices[0]], Y[indices[0]], X[indices[1]], Y[indices[1]]))
print("c) Distancia mayor:", max_dist)
print("c) Pares de puntos:", puntos)

# d) Distancia del origen a recta entre puntos lejanos
x1, y1 = X[indices[0][0]], Y[indices[0][0]]
x2, y2 = X[indices[1][0]], Y[indices[1][0]]
dist_recta = abs((y2-y1)*0 - (x2-x1)*0 + (x2*y1 - y2*x1)) / np.sqrt((y2-y1)**2 + (x2-x1)**2)
print("d) Distancia del origen a recta:", dist_recta)
