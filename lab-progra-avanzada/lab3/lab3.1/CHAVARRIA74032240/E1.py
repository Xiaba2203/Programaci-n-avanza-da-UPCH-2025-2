def caracteres_unicos(strings):  # Función que recibe varias palabras
    for palabra in strings:  # Itera cada palabra recibida
        unicos = list(set(palabra))  # Saca letras repetidas de palabra
        print(f"String: {palabra} → Caracteres únicos: {unicos}")  # Muestra palabra y letras únicas

# Ejemplo:


caracteres = []
while len(caracteres) < 3:  # Pide tres palabras
    entrada = input("Introduce una palabra: ").strip()
    if entrada:  # Asegura que no esté vacía
        caracteres.append(entrada)
caracteres_unicos(caracteres)  # Prueba función con tres palabras
