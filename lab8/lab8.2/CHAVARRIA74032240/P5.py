import time

problemSize = 10000
print(f"{'Problem Size':12}{'Seconds':>16}")

for count in range(5):
    start = time.time()
    work = 1
    for j in range(problemSize):
        for k in range(problemSize):
            work += 1
            work -= 1
    elapsed = time.time() - start
    print(f"{problemSize:12}{elapsed:16.3f}")
    problemSize *= 2
