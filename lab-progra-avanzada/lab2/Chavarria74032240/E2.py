frase = input("Ingrese una frase: ")  # pide frase
palabras = frase.split()              # divide en palabras

# Lista de tuplas (palabra, tamaño)
lista_tuplas = [(palabra, len(palabra)) for palabra in palabras]

# Palabra más larga
palabra_larga = max(lista_tuplas, key=lambda x: x[1])
print("\nLa palabra más larga es:", palabra_larga[0])

# Orden descendente por tamaño
lista_ordenada = sorted(lista_tuplas, key=lambda x: x[1], reverse=True)
print("\nLista ordenada:", lista_ordenada)

# Imprimir cada ítem
print("\nDetalles de cada palabra:")
for palabra, tamaño in lista_ordenada:
    print(f'La palabra "{palabra}" tiene {tamaño} caracteres')
