def fun9(n):
    m = 0
    i = n
    while i > 0:
        j = 0
        while j < i:
            m += 1
            j += 1
        i //= 2
    return m
# O(n)

def fun10(n):
    m = 0
    i = 0
    while i < n:
        j = i
        while j > 0:
            m += 1
            j -= 1
        i += 1
    return m
# O(n²)

def fun12(n):
    m = 0
    i = 0
    while i < n:
        j = 0
        while j < n:
            m += 1
            j += 1
        i += 1
    return m
# O(n²)

if __name__ == "__main__":
    n = 16
    print("fun9(", n, ") =", fun9(n))
    print("fun10(", n, ") =", fun10(n))
    print("fun12(", n, ") =", fun12(n))