import random
import statistics

def experimento(inicial):
    resultados = []
    for _ in range(100):
        monto = inicial
        for _ in range(100):
            apuesta = monto * 0.7
            if random.random() < 0.7:  # 60% de probabilidad de ganar
                factor = random.uniform(1.55, 1.80)
                monto += apuesta * (factor - 1)
            else:
                monto -= apuesta
            if monto <= 0:
                monto = 0
                break
        resultados.append(monto)
    return resultados

inicial = float(input("Ingrese el monto inicial: "))

# Ejecutar el experimento 100 veces y guardar los resultados de cada ejecución
todos_los_resultados = []
for _ in range(100):
    resultados = experimento(inicial)
    todos_los_resultados.append(resultados)

# Calcular estadísticas para cada ejecución y mostrar los resultados
for i, resultados in enumerate(todos_los_resultados, 1):
    print(f"\nEjecución {i}:")
    print(f"Monto inicial: {inicial}")
    print(f"Monto final promedio: {sum(resultados)/len(resultados):.2f}")
    print(f"Media: {statistics.mean(resultados):.2f}")
    print(f"Resultado mínimo: {min(resultados):.2f}")
    print(f"Resultado máximo: {max(resultados):.2f}")
print(f"Resultado máximo: {max(resultados):.2f}")