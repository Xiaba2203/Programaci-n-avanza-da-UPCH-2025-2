from P1 import Empleado, Empresa
empleados = [
    Empleado("Juan", "Perez", 5000, 5, 10, 1990, 1, 1, 2020),
    Empleado("Ana", "Lopez", 12000, 3, 15, 1985, 6, 20, 2010),
    Empleado("Luis", "Garcia", 8000, 7, 25, 2000, 8, 5, 2023),
]

empresa = Empresa(empleados)

print("Suma sueldos:", empresa.suma_sueldos())
print("Menor sueldo:", empresa.empleado_menor_sueldo().nombre)
print("Mayor sueldo:", empresa.empleado_mayor_sueldo().nombre)
print("Promedio sueldos:", empresa.promedio_sueldos())
print("Menores de 30:", len(empresa.menores_de(30)))
print("Mayores de 55:", len(empresa.mayores_de(55)))
print("Entre 25 y 70:", len(empresa.entre_edades(25, 70)))
print("Menores 35 con sueldo >10000:", len(empresa.menores_con_sueldo(35, 10000)))
print("Promedio edad:", empresa.promedio_edad())
print("Mayor edad:", empresa.empleado_mayor_edad().nombre)
print("Menor edad:", empresa.empleado_menor_edad().nombre)
