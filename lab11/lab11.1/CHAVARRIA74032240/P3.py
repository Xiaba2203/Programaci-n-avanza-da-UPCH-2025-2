def buscar_binario(dato, lista):
    # búsqueda binaria iterativa
    izq, der = 0, len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if lista[medio] == dato: return medio
        if dato < lista[medio]: der = medio - 1
        else: izq = medio + 1
    return -1            # no encontrado

def buscar_binario_rec(dato, lista, izq=0, der=None):
    # búsqueda binaria recursiva
    if der is None: der = len(lista) - 1
    if izq > der: return -1
    medio = (izq + der) // 2
    if lista[medio] == dato: return medio
    if dato < lista[medio]: return buscar_binario_rec(dato, lista, izq, medio - 1)
    return buscar_binario_rec(dato, lista, medio + 1, der)

if __name__ == "__main__":
    nums = [10, 20, 30, 40, 50]
    print(buscar_binario(30, nums))      # muestra 2
    print(buscar_binario_rec(30, nums))  # muestra 2
