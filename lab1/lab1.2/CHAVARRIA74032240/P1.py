# a) Nombres con más de 6 notas
with open("datos_estudiante.txt","r") as f:  # abrir archivo
    lineas = f.readlines()  # guardar todas las líneas

print("Estudiantes con más de 6 notas:")
for linea in lineas:
    partes = linea.split()  # separar por espacio
    nombre = partes[0]  # primer elemento es el nombre
    notas = partes[1:]  # el resto son notas
    if len(notas) > 6:  # si tiene más de 6 notas
        print(nombre)

# b) Imprimir nombre del archivo
with open("datos_estudiante.txt","r") as f:
    print("El nombre del archivo es:", f.name)

# c) Imprimir todo el contenido
print("Contenido del archivo:")
for linea in lineas:
    print(linea.strip())  # imprimir cada línea sin saltos de línea
