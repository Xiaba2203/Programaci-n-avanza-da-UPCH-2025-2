def normalizar_frase(frase):
    reemplazos = {  # mapeo de caracteres
        "á":"a","é":"e","í":"i","ó":"o","ú":"u",
        "Á":"A","É":"E","Í":"I","Ó":"O","Ú":"U",
        "ñ":"n","Ñ":"N","ü":"u","Ü":"U"
    }
    salida = ""  # acumulador
    for c in frase:  # recorrer cada letra
        salida += reemplazos.get(c, c)  # reemplazar si está en el diccionario
    return salida

frase = input("Ingrese una frase: ")
print("La frase modificada:", normalizar_frase(frase))
