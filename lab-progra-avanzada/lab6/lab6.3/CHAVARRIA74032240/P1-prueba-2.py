from P1 import Empleado, Empresa
empleados = [
    Empleado("Juan", "Perez", 5000, 5, 10, 1990, 1, 1, 2020),
    Empleado("Ana", "Lopez", 12000, 3, 15, 1985, 6, 20, 2010),
    Empleado("Luis", "Garcia", 8000, 7, 25, 2000, 8, 5, 2023),
]

empresa = Empresa(empleados)
empresa.guardar("empleados.dat")  # guarda objetos
empleados_leidos = Empresa.leer("empleados.dat")  # lee objetos

# nueva empresa con los leídos
empresa2 = Empresa(empleados_leidos)

df = empresa2.a_dataframe()
print(df)

print("Suma sueldos:", df["Sueldo"].sum())
print("Promedio sueldos:", df["Sueldo"].mean())
print("Menor sueldo:", df.loc[df["Sueldo"].idxmin(), "Nombre"])
print("Mayor sueldo:", df.loc[df["Sueldo"].idxmax(), "Nombre"])
print("Menores 30:", len(df[df["Edad"] < 30]))
print("Mayores 55:", len(df[df["Edad"] > 55]))
print("Entre 25 y 70:", len(df[(df["Edad"] >= 25) & (df["Edad"] <= 70)]))
print("Menores 35 con sueldo >10000:",
      len(df[(df["Edad"] < 35) & (df["Sueldo"] > 10000)]))
print("Promedio edad:", df["Edad"].mean())
print("Mayor edad:", df.loc[df["Edad"].idxmax(), "Nombre"])
print("Menor edad:", df.loc[df["Edad"].idxmin(), "Nombre"])
