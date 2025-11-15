# trazas por pasada de tres métodos
lista_inicial = [44, 88, 55, 99, 66, 33, 22, 88, 77]

def traza_seleccion(lista):
    L = lista.copy()
    pasos = []
    n = len(L)
    for i in range(n - 1):
        menor = i
        for j in range(i + 1, n):
            if L[j] < L[menor]:
                menor = j
        L[i], L[menor] = L[menor], L[i]
        pasos.append(L.copy())
    return pasos

def traza_burbuja(lista):
    L = lista.copy()
    pasos = []
    n = len(L)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]
        pasos.append(L.copy())
    return pasos

def traza_insercion(lista):
    L = lista.copy()
    pasos = []
    for i in range(1, len(L)):
        v = L[i]
        j = i - 1
        while j >= 0 and L[j] > v:
            L[j + 1] = L[j]
            j -= 1
        L[j + 1] = v
        pasos.append(L.copy())
    return pasos

if __name__ == "__main__":
    print("Original:", lista_inicial)
    print("\nSelección primera pasada:", traza_seleccion(lista_inicial)[0])
    print("Burbuja primera pasada:", traza_burbuja(lista_inicial)[0])
    print("Inserción primera pasada:", traza_insercion(lista_inicial)[0])
