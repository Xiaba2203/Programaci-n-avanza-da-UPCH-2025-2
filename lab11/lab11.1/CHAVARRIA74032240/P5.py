import time

def buscar_para(dato, lista):
    # búsqueda con para
    for i, v in enumerate(lista):
        if v == dato: return i
    return -1

def buscar_binario(dato, lista):
    # búsqueda binaria
    izq, der = 0, len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if lista[medio] == dato: return medio
        if dato < lista[medio]: der = medio - 1
        else: izq = medio + 1
    return -1

def medir_tiempos(lista, dato):
    # mide duración de cada método
    t0 = time.perf_counter()
    r1 = buscar_para(dato, lista)
    t1 = time.perf_counter()
    r2 = buscar_binario(dato, lista)
    t2 = time.perf_counter()
    try:
        t3 = time.perf_counter()
        r3 = lista.index(dato)
        t4 = time.perf_counter()
    except ValueError:
        r3, t4 = -1, time.perf_counter()
    return {
        'para': (r1, t1-t0),
        'binario': (r2, t2-t1),
        'index': (r3, t4-t3)
    }

if __name__ == "__main__":
    n = 200000
    nums = list(range(n))
    for d in (10, n//2, n-10):
        print("dato", d, medir_tiempos(nums, d))
