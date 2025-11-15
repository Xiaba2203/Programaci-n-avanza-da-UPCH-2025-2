import random  # Para números aleatorios

def duplicados(lista):
    # Devuelve elementos repetidos
    return {x for x in lista if lista.count(x) > 1}

N = int(input("Ingrese el valor de N: "))  # Tamaño de la lista
lista = [random.randint(0, 100) for _ in range(N)]  # Lista aleatoria
print("Lista generada:", lista)  # Muestra la lista
print("Valores duplicados:", duplicados(lista))  # Muestra duplicados
