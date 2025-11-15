import os

def factorial(n): # Calcula factorial de n
    if n == 0 or n == 1: # Si n es 0 o 1
        return 1 # Retorna 1
    else: # Si no
        return n * factorial(n - 1) # Llama recursivo

def fibonacci(n): # Calcula n-ésimo Fibonacci
    if n <= 0: # Si n <= 0
        return 0 # Retorna 0
    elif n == 1: # Si n es 1
        return 1 # Retorna 1
    else: # Si no
        return fibonacci(n - 1) + fibonacci(n - 2) # Suma dos anteriores

def imprimir_recursivo(n): # Imprime n hasta 0
    print(n, end=' ') # Imprime n
    if n > 0: # Si n > 0
        imprimir_recursivo(n - 1) # Llama recursivo

def suma_recursiva(n): # Suma de n a 1
    if n == 1: # Si n es 1
        return 1 # Retorna 1
    else: # Si no
        return n + suma_recursiva(n - 1) # Suma y llama recursivo

def matriz_aplanada(matriz): # Aplana matriz recursivo
    if not matriz: # Si matriz vacía
        return [] # Retorna lista vacía
    return list(matriz[0]) + matriz_aplanada(matriz[1:]) # Une fila y recursivo

def tamano(path): # Calcula tamaño de archivo/carpeta
    if os.path.isfile(path): # Si es archivo
        return os.path.getsize(path) # Retorna tamaño
    total = 0 # Inicializa total
    for entry in os.listdir(path): # Por cada entrada
        entry_path = os.path.join(path, entry) # Ruta completa
        total += tamano(entry_path) # Suma tamaño recursivo
    return total # Retorna total

def sucesion_ulam(n): # Genera sucesión de Ulam
    if n < 1:
        raise ValueError("El número debe ser un entero positivo mayor que 0")
    print(n, end=' ') # Imprime n
    if n == 1: # Si n es 1
        return 1 # Retorna 1
    elif n % 2 == 0: # Si n es par
        return n + sucesion_ulam(n // 2) # Suma y llama recursivo
    else: # Si n es impar
        return n + sucesion_ulam(3 * n + 1) # Suma y llama recursivo


# Pruebas de las funciones
if __name__ == "__main__":
    matriz = [
        [5, 8, 15],
        [3, 0, 9],
        [11, 48, 22]
    ]

    print("Factorial de 5:", factorial(5))
    print("Fibonacci de 10:", fibonacci(10))
    print("Imprimir recursivo desde 5:")
    imprimir_recursivo(5)
    print("Suma recursiva de 5 a 1:", suma_recursiva(5))
    print("Matriz aplanada:", matriz_aplanada(matriz))
    print("Tamaño de carpeta actual:", tamano("."))
    n = input("Ingrese un número para la sucesión de Ulam: ")
    sucesion_ulam(int(n))