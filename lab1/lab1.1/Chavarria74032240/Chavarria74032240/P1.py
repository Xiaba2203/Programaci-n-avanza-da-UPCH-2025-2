import random  # para usar números aleatorios

def generar_adn(n):
    if not (20 <= n <= 1000):  # validar rango
        return "¡ERROR!, el tamaño debe estar entre 20 y 1000"
    letras = "ACGT"  # símbolos válidos
    return "".join(random.choice(letras) for _ in range(n))  # formar la cadena

n = int(input("Ingrese la longitud de la cadena [20, 1000]: "))
print("La cadena ADN es:", generar_adn(n))
