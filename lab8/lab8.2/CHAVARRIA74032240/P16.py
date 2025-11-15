def tiempo(f, n, N=1000, T_N=10):
    return T_N * (f(n) / f(N))

t_lineal = tiempo(lambda x: x, 100_000)
t_cubico = tiempo(lambda x: x**3, 100_000)

print("Lineal:", t_lineal, "s")
print("Cúbico:", t_cubico, "s")
