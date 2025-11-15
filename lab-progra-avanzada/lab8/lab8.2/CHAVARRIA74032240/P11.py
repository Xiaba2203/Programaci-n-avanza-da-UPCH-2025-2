problemSize = 1000000
contador = 0

while problemSize > 0:
    problemSize //= 2
    contador += 1

print("Número de iteraciones:", contador)
