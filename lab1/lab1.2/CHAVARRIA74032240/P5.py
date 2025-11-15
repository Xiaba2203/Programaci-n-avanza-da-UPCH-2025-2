with open("datos_estudiante.txt","r") as f:
    lineas = f.readlines()

mayor = -1
mejor_alumno = ""

for linea in lineas:
    partes = linea.strip().split()
    nombre = partes[0]
    notas = [float(n) for n in partes[1:]]
    promedio = sum(notas)/len(notas)
    print(nombre, "promedio:", promedio)
    if max(notas) > mayor:
        mayor = max(notas)
        mejor_alumno = nombre

print("La mayor nota fue", mayor, "y la obtuvo", mejor_alumno)
