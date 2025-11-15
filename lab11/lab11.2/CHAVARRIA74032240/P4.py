# cálculo de tiempos O(n^2)
def calcular_tiempos():
    n_base = 200       # tamaño base
    t_base = 3.1       # tiempo base ms
    # caso 1: 400
    n1 = 400
    t1 = t_base * (n1 / n_base) ** 2
    # caso 2: 40000
    n2 = 40000
    t2 = t_base * (n2 / n_base) ** 2
    return t1, t2

if __name__ == "__main__":
    t1, t2 = calcular_tiempos()
    print("400 elementos →", round(t1, 3), "ms")
    print("40000 elementos →", round(t2 / 1000, 3), "s")
