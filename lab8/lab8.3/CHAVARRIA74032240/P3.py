# (a) rfunc1: no tiene caso base -> recursión infinita
def rfunc1(n):
    return n + rfunc1(n - 1)

# (b) rfunc2: tiene caso base, pero la llamada recursiva se aleja del caso base (n+1)
def rfunc2(n):
    if n == 0:
        return 1
    return n + rfunc2(n + 1)

if __name__ == "__main__":
    rfunc1(5)
    rfunc2(5)
    # No se logra ejecutar debido a la recursión infinita en ambas funciones.
