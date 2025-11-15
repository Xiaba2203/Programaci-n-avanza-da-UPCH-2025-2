import time

problemSize = 10000000
print(f"{'Problem Size':12}{'Seconds':>16}")

for count in range(5):
    start = time.time()
    work = 1
    for x in range(problemSize):
        work += 1  # Se eliminó una operación del algoritmo
    elapsed = time.time() - start
    print(f"{problemSize:12}{elapsed:16.3f}")
    problemSize *= 2
