lista = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]  # lista inicial
valor = int(input("Ingrese un valor: "))            # pide valor

# a) Reemplazar último elemento con valor ingresado
lista_a = [tupla[:-1] + (valor,) for tupla in lista]
print("Lista a:", lista_a)

# b) Nueva lista con suma de cada tupla
lista_b = [sum(tupla) for tupla in lista]
print("Lista b:", lista_b)

# c) Nueva lista quitando último valor
lista_c = [tupla[:-1] for tupla in lista]
print("Lista c:", lista_c)
