# ordenamiento burbuja mejorado
def burbuja_mejorada(lista):
    # tamaño lista
    n = len(lista)
    for i in range(n - 1):
        # bandera de orden
        ordenado = True
        for j in range(n - 1 - i):
            # si está desordenado, intercambia
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                ordenado = False
        # si no hubo cambios, termina
        if ordenado:
            break
    return lista

if __name__ == "__main__":
    datos = [3, 7, 2, 9, 10]
    print(burbuja_mejorada(datos))  # prueba rápida
