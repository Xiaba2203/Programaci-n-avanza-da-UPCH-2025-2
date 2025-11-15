# Clase A
class A:
    def __init__(self, i = 0):
        # guardar i
        self.i = i

    def m1(self):
        # aumentar i en 1
        self.i += 1


# Clase B que hereda de A
class B(A):
    def __init__(self, j = 0):
        # inicializar i en 3 usando super
        super().__init__(3)
        # guardar j
        self.j = j

    def m1(self):
        # sobrescribir método m1, aumentar i en 1
        self.i += 1


# función principal
def main():
    # crear objeto B
    b = B()
    # llamar m1 de B
    b.m1()
    # imprimir i después de aumentar
    print(b.i)
    # imprimir j
    print(b.j)

# ejecutar main
main()

# Salida
# 4
# 0
