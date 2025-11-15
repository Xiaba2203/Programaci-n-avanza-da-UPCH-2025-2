def buscar_min(lista):
    # asume lista no vacía
    pos_min = 0        # posición mínima
    for i in range(1, len(lista)):  # recorre lista
        if lista[i] < lista[pos_min]:  # compara valor
            pos_min = i
    return pos_min      # devuelve posición mínima

if __name__ == "__main__":
    # ejemplo rápido
    datos = [5, 2, 9, 1, 7]
    print(buscar_min(datos))  # muestra 3
