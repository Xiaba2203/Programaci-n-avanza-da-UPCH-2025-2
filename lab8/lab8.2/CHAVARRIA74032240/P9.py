problemSize = 1000
print(f"{'Problem Size':12}{'Iteraciones':>16}")

for count in range(5):
    work = 0
    for j in range(problemSize):
        for k in range(problemSize):
            work += 1
    print(f"{problemSize:12}{work:16}")
    problemSize *= 2
