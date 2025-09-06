
with open("archivo.txt", "r") as f:
    datos = [list(map(int, fila.strip().split(','))) for fila in f]

A, B, C = datos[0], datos[1], datos[2]

neg = [x for x in B if x < 0]
no_neg = [x for x in B if x >= 0]
B_mod = neg + no_neg

with open("archivo.txt", "w") as f:
    f.write(','.join(map(str, A)) + '\n')
    f.write(','.join(map(str, B_mod)) + '\n')
    f.write(','.join(map(str, C)) + '\n')

print("Archivo modificado:")
with open("archivo.txt", "r") as f:
    for fila in f:  
        print(fila.strip())