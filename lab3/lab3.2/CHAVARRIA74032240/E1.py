# a) Diccionario de gerencias
gerencias = {
    101:"RRHH",           # clave 101 es RRHH
    102:"FINANZA",        # clave 102 es FINANZA
    103:"CONTABILIDAD",   # clave 103 es CONTABILIDAD
    104:"VENTAS",         # clave 104 es VENTAS
    105:"INGENIERIA",     # clave 105 es INGENIERIA
    106:"SOPORTE"         # clave 106 es SOPORTE
}

# b) Diccionario de empleados
empleados = {
    1000: {"Nombre":"Juan", "Fing":"10-10-17", "Dept":103},   # empleado 1000 datos
    1001: {"Nombre":"Mary", "Fing":"01-11-88", "Dept":101},   # empleado 1001 datos
    1002: {"Nombre":"Luis", "Fing":"05-03-20", "Dept":104}    # empleado 1002 datos
}

# c) Imprimir bases de datos
print("Base de Datos de Gerencias:")      # muestra texto gerencias
for k,v in gerencias.items():             # recorre gerencias
    print(k, v)                           # imprime clave y valor

print("\nBase de Datos de Empleados:")    # muestra texto empleados
for id, datos in empleados.items():       # recorre empleados
    print("Persona ID:", id)              # imprime id persona
    for clave, valor in datos.items():    # recorre datos persona
        print(clave+":", valor)           # imprime dato y valor
    print()                               # salto de línea

# d) Empleados con id impar
print("IDs impares:")                     # muestra texto ids impares
for id in empleados:                      # recorre ids empleados
    if id % 2 == 1:                       # si id es impar
        print(id, empleados[id]["Nombre"])# imprime id y nombre

# e) Agregar nuevo empleado
empleados[1003] = {"Nombre":"Carlos", "Fing":"12-06-22", "Dept":106} # añade empleado 1003

# f) Modificar nombre sin update
empleados[1001]["Nombre"] = "Maria"       # cambia nombre Mary a Maria

# g) Borrar dept del nuevo empleado
del empleados[1003]["Dept"]               # elimina dept de empleado 1003

# h) Eliminar al empleado agregado
del empleados[1003]                       # borra empleado 1003
