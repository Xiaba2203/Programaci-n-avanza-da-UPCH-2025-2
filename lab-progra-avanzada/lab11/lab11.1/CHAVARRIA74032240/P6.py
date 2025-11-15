def buscar_binario_rec(dato, lista):
    # envoltura recursiva
    def _buscar(izq, der):
        if izq > der: return -1
        medio = (izq + der)//2
        if lista[medio] == dato: return medio
        if dato < lista[medio]: return _buscar(izq, medio - 1)
        return _buscar(medio + 1, der)
    return _buscar(0, len(lista) - 1)

if __name__ == "__main__":
    nums = list(range(1000))
    print(buscar_binario_rec(500, nums))  # muestra 500
