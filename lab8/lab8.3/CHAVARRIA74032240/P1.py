def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def f1(n):
    print(n)
    if n > 0:
        f1(n - 1)

def f2(n):
    if n == 1:
        return 1
    else:
        return n + f2(n - 1)

if __name__ == "__main__":
    print("factorial(0) =", factorial(0))
    print("factorial(5) =", factorial(5))
    print("\n=== f1(3) output ===")
    f1(3)
    print("\n=== f2 tests ===")
    print("f2(1) =", f2(1))
    print("f2(5) =", f2(5))
