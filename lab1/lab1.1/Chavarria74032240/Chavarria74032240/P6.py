def normalizar_frase_manual(frase):
    mapeo = {  # cambios
        "á":"a","é":"e","í":"i","ó":"o","ú":"u",
        "Á":"A","É":"E","Í":"I","Ó":"O","Ú":"U",
        "ñ":"n","Ñ":"N","ü":"u","Ü":"U"
    }
    salida = ""  # acumulador
    for letra in frase:  # recorrer
        if letra in mapeo:
            salida += mapeo[letra]
        else:
            salida += letra
    return salida

print(normalizar_frase_manual("En España no hay pingüinos, en Bélgica tampoco"))
