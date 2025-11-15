def encriptar(texto, llave):
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # letras ordenadas
    mapa = {a: b for a, b in zip(alfabeto, llave)}  # correspondencia

    resultado = ""  # acumulador
    for c in texto.upper():  # recorrer el texto en mayúscula
        if c in mapa:  # si está en el alfabeto
            resultado += mapa[c]  # sustituir
        else:
            resultado += c  # dejar igual si no es letra
    return resultado

alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
llave = "JVKMLONIBHDCR EFZUPYGXASQWT".replace(" ", "")  # llave dada
mensaje = input("Ingrese un mensaje: ")
print("Mensaje encriptado:", encriptar(mensaje, llave))
