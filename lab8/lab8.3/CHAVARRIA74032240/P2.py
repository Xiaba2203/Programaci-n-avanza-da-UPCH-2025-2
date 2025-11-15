def f(n):
    if n > 0:
        print(n)
        f(n - 2)
        f(n - 3)
        print(n)

if __name__ == "__main__":
    print("Salida de f(6):")
    f(6)
