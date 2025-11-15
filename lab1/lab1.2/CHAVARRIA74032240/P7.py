archivo = "alumnos2025.txt"
cadena = input("Ingrese el string a eliminar: ")

with open(archivo,"r") as f:
    lineas = f.readlines()

with open(archivo,"w") as f:
    for l in lineas:
        nueva = l.replace(cadena,"").strip()
        if nueva:  # si no quedó vacío
            f.write(nueva+"\n")

print("Archivo actualizado sin líneas vacías.")
