def collatz_sequence(n):
    """Devuelve la lista de la sucesión de Collatz (Ulam) comenzando en n hasta 1."""
    if n <= 0:
        raise ValueError("n debe ser entero positivo")
    if n == 1:
        return [1]
    if n % 2 == 0:
        return [n] + collatz_sequence(n // 2)
    else:
        return [n] + collatz_sequence(3 * n + 1)

if __name__ == "__main__":
    n = 26
    seq = collatz_sequence(n)
    print("Sucesión de Ulam para", n, "=>", seq)
    print("Suma de la sucesión:", sum(seq))
