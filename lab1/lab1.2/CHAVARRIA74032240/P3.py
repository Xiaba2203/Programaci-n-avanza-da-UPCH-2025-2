archivo = input("Ingrese el nombre del archivo: ")
cadena = input("Ingrese el string a eliminar: ")

# b) Mostrar contenido inicial
with open(archivo,"r") as f:
    lineas = f.readlines()

print("Contenido inicial:")
for l in lineas:
    print(l.strip())

# c) Crear nuevo archivo sin la cadena
nuevo = archivo.replace(".txt","_new.txt")
with open(nuevo,"w") as f:
    for l in lineas:
        f.write(l.replace(cadena,""))

print("Se generó el archivo:", nuevo)

# d) Modificar archivo original
with open(archivo,"w") as f:
    for l in lineas:
        f.write(l.replace(cadena,""))

print("Contenido actualizado del archivo original:")
with open(archivo,"r") as f:
    for l in f:
        print(l.strip())
