import random  # para randint

def generar_adn_manual(n):
    if not (20 <= n <= 1000):  # validar
        return "¡ERROR!, el tamaño debe estar entre 20 y 1000"
    letras = "ACGT"  # posibles caracteres
    adn = ""  # acumulador
    for _ in range(n):  # repetir n veces
        i = random.randint(0, 3)  # escoger índice
        adn += letras[i]  # añadir letra
    return adn

print(generar_adn_manual(25))
