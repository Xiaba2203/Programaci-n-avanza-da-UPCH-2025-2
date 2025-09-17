# a) Listas de 26 elementos
num = list(range(1, 27))   # lista 1 al 26
alpha = [chr(i) for i in range(97, 123)]  # letras a-z
ascii_vals = list(range(97, 123))         # valores ASCII

# b) Generar lista de tuplas
lista_tuplas = list(zip(num, alpha, ascii_vals))
print("Lista de tuplas:", lista_tuplas)

# c) Volver a listas originales
num2, alpha2, ascii2 = zip(*lista_tuplas)
print("\nListas originales:")
print("num:", list(num2))
print("alpha:", list(alpha2))
print("ascii:", list(ascii2))
