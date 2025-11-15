from P3 import Escuela

# 3 pruebas
esc = Escuela()
# 3.a agregar
esc.agregar("Marta", 3)
esc.agregar("Pedro", 2)
esc.agregar("Carmen", 2)
esc.agregar("Juan", 1)
esc.agregar("Susana", 1)
# 3.b mostrar grado 2
print("Grado 2:", esc.mostrar_grado(2))
# 3.c mostrar todos
esc.mostrar_todos()
