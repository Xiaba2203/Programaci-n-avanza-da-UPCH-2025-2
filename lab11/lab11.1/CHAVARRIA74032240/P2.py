def buscar_mientras(dato, lista):
    # busca usando mientras
    i = 0               # índice inicial
    while i < len(lista):
        if lista[i] == dato:  # compara elemento
            return i
        i += 1
    return -1           # no encontrado

def buscar_para(dato, lista):
    # busca usando para
    for i, valor in enumerate(lista):
        if valor == dato:  # compara elemento
            return i
    return -1           # no encontrado

if __name__ == "__main__":
    # prueba rápida
    datos = [3, 7, 2, 9, 10]
    print(buscar_mientras(9, datos))  # muestra 3
    print(buscar_para(9, datos))      # muestra 3
