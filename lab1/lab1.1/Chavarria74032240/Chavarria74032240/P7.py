def frecuencia_caracteres(frase):
    freq = {}  # diccionario de conteo
    for c in frase:  # recorrer cada caracter
        freq[c] = freq.get(c, 0) + 1  # aumentar contador
    for char, count in freq.items():  # mostrar resultado
        print(f"'{char}': {count}")

frase = input("Ingrese una frase: ")
frecuencia_caracteres(frase)
