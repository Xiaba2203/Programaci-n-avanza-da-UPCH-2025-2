# Código original con error
# class A:
#     def __init__(self, i = 0):
#         # guardar i
#         self.i = i
#
# class B(A):
#     def __init__(self, j = 0):
#         # solo guarda j, no inicializa i
#         self.j = j
#
# def main():
#     b = B()
#     print(b.i)  # error: i no existe
#     print(b.j)
#
# main()

# Código corregido
# Clase A
class A:
    def __init__(self, i = 0):
        # guardar i
        self.i = i

# Clase B que hereda de A
class B(A):
    def __init__(self, j = 0):
        # llamar al constructor de A
        super().__init__()
        # guardar j
        self.j = j

# función principal
def main():
    # crear objeto B
    b = B()
    # imprimir atributo i
    print(b.i)
    # imprimir atributo j
    print(b.j)

# ejecutar main
main()

# Salida esperada
# 0
# 0
