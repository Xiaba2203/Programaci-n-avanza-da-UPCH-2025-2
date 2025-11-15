def trazar_binario(dato, lista):
    # muestra pasos del binario
    izq, der = 0, len(lista) - 1
    pasos = []            # guarda los pasos
    while izq <= der:
        medio = (izq + der) // 2
        pasos.append((izq, der, medio))
        if lista[medio] == dato: return pasos, medio
        if dato < lista[medio]: der = medio - 1
        else: izq = medio + 1
    return pasos, -1       # no encontrado

if __name__ == "__main__":
    nums = [20,44,48,55,62,66,74,88,93,99]
    a, r1 = trazar_binario(90, nums)
    print("Trazado 90:", a, "resultado", r1)
    b, r2 = trazar_binario(44, nums)
    print("Trazado 44:", b, "resultado", r2)
