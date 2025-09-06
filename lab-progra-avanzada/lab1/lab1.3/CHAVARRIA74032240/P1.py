A = []  # lista vacía
N = int(input("Ingrese cantidad de números: "))
for i in range(N):  
    try:
        num = int(input(f"Número {i+1}: "))
        A.append(num)  # agregando con append
    except ValueError:  # verifica que el valor ingresado sea un número
        print("Por favor ingrese un número válido.")
        break
print("Lista A:", A)

B = [None] * N  # lista con None
for i in range(N):
    num = int(input(f"Número {i+1} para B: "))  
    B[i] = num  # colocando en índice
print("Lista B:", B)

pos_max = A.index(max(A))  # posición max
pos_min = A.index(min(A))  # posición min
ini = min(pos_max, pos_min)  
fin = max(pos_max, pos_min)  
C = A[ini:fin+1]  # elementos entre min y max
print("Lista C:", C)

prom = sum(B) / len(B)  # promedio
print("Promedio de B:", prom)
D = [x for x in B if x > prom]  # mayores al promedio
print("Lista D:", D)
