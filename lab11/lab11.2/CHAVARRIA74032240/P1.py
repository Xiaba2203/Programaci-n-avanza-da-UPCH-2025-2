# ordenamiento por selección
def ordenar_seleccion(lista):
    # recorre toda la lista
    n = len(lista)
    for i in range(n - 1):
        # asumimos este como mínimo
        menor = i
        for j in range(i + 1, n):
            # si hay valor menor, guardamos
            if lista[j] < lista[menor]:
                menor = j
        # intercambiamos posiciones
        if menor != i:
            lista[i], lista[menor] = lista[menor], lista[i]
    return lista  # devuelve lista ordenada

if __name__ == "__main__":
    datos = [5, 2, 9, 1, 7]
    print(ordenar_seleccion(datos))  # prueba simple
