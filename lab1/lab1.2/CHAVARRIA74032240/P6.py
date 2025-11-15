nombre = input("Ingrese nombre del nuevo alumno: ")
notas = input("Ingrese notas separadas por espacio: ")

with open("datos_estudiante.txt","a") as f:
    f.write(nombre + " " + notas + "\n")

print("Alumno agregado al archivo.")
