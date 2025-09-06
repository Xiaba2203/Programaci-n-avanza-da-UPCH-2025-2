import E1 #importo el diccionario de E1

empleados = E1.empleados # guardo empleados de E1

# a) Orden descendente por nombre
print("Orden descendente por nombre:") # muestro mensaje
for id, datos in sorted(empleados.items(), key=lambda x: x[1]["Nombre"], reverse=True):
    print(id, datos) # imprimo id y datos ordenados

# b) Empleados de Finanzas
print("\nEmpleados de Finanzas:")
for id, datos in empleados.items():
    print(f"ID: {id}, Nombre: {datos['Nombre']}, Departamento: {datos['Dept']}")

# c) Cambiar nombre con update
empleados[1002].update({"Nombre":"Luisito"}) # cambio nombre del empleado 1002
print("\nEmpleado 1002 actualizado:")
print(f"ID: 1002, Nombre: {empleados[1002]['Nombre']}, Departamento: {empleados[1002]['Dept']}")
