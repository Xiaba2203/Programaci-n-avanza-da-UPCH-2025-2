def pareja(machos, hembras):  # Función para emparejar listas
    pares = set()  # Creo conjunto para parejas
    while machos and hembras:   # Mientras ambos tengan elementos
        m = machos.pop()  # Saco un macho del conjunto
        h = hembras.pop()  # Saco una hembra del conjunto
        pares.add((m, h))  # Agrego la pareja al conjunto
    return pares  # Devuelvo el conjunto de parejas

# Programa principal
n = int(input("Ingrese el tamaño de las listas: "))  # Pido tamaño de las listas

machos = [input(f"Ingrese macho {i+1}: ") for i in range(n)]  # Pido nombres de machos
hembras = [input(f"Ingrese hembra {i+1}: ") for i in range(n)]  # Pido nombres de hembras

set_machos = set(machos)  # Convierto machos a conjunto
set_hembras = set(hembras)  # Convierto hembras a conjunto

if len(set_machos) == len(set_hembras):  # Verifico si conjuntos son iguales
    print("Parejas formadas:", pareja(set_machos, set_hembras))  # Muestro parejas formadas
else:
    print("Los conjuntos no son del mismo tamaño")  # Aviso si tamaños no coinciden
