import random

m = int(input("Ingrese tamaño de listas: "))
A = []  
for i in range(m):
    A.append(int(input(f"Número {i+1} para A: ")))  # llenar A

B = [random.randint(-30, 30) for _ in range(m)]  # aleatorios
print("Lista A:", A)
print("Lista B:", B)

with open("archivo.txt", "w") as f:  
    f.write(','.join(map(str, A)) + '\n')  # guardar A
    f.write(','.join(map(str, B)) + '\n')  # guardar B

print("Archivo con A y B:")  
with open("archivo.txt", "r") as f:  
    for fila in f:  
        print(fila.strip())  # mostrar archivo

C = [A[i] + B[i] for i in range(m)]  # suma elemento a elemento
print("Lista C:", C)

with open("archivo.txt", "a") as f:  
    f.write(','.join(map(str, C)) + '\n')  # agregar C
