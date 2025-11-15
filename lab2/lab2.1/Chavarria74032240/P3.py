def generar_matriz(n):
    A=[] # aca la matriz
    for i in range(n): # recorremos filas
        fila=[] # cada fila vacia
        for j in range(n): # recorremos columnas
            if j>=i: # si columna es mayor o igual a fila
                valor=j-i+1 # pongo ese valor
            else:
                valor=0 # si no, es cero
            fila.append(valor) # meto el numero en la fila
        A.append(fila) # meto la fila en la matriz
    return A

def imprimir_matriz(A, n):
    for i in range(n):
        for j in range(n):
            print(A[i][j], end=" ")
        print()

def main():
    n=int(input("Tamaño de la matriz n: ")) # pedimos n
    A=generar_matriz(n) # armamos la matriz
    imprimir_matriz(A) # la mostramos
def main():
    n = int(input("Tamaño de la matriz n: ")) # pedimos n
    A = generar_matriz(n) # armamos la matriz
    imprimir_matriz(A, n) # la mostramos

if __name__ == "__main__":
    main()