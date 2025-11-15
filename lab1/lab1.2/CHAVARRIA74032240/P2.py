with open("datos_estudiante.txt","r") as f:  # abrir archivo
    lineas = f.readlines()

for linea in lineas:
    partes = linea.split()  # separar
    nombre = partes[0]
    notas = [float(n) for n in partes[1:]]  # convertir a número
    promedio = sum(notas)/len(notas)  # calcular promedio
    print(nombre, "tiene promedio:", promedio)
