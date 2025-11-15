def leer_alumnos(nombre_archivo):
    with open(nombre_archivo, "r") as f:  # abrir archivo para leer
        next(f)  # saltar encabezado
        alumnos = [line.strip().split(",") for line in f]  # dividir cada línea en lista

        # convertir a lista de diccionarios
        lista_de_diccionarios = [
            {"nombre": alumno[0], 
             "edad": int(alumno[1]), 
             "semestre": alumno[2], 
             "nota": float(alumno[3])}
            for alumno in alumnos
        ]
    return lista_de_diccionarios


# a) y b)
alumnos = leer_alumnos("alumnos.csv")  # leer archivo y guardar lista

print("Lista de alumnos:")
for a in alumnos:  # recorrer lista de diccionarios
    print(a)       # mostrar cada alumno
print()

# c) Alumno de mayor edad
mayor_edad = max(alumnos, key=lambda x: x["edad"])  # busca diccionario con mayor edad
print("Alumno de mayor edad:")
print(mayor_edad)
print()

# d) Promedio de notas de los alumnos de 20 años
notas_20 = [a["nota"] for a in alumnos if a["edad"] == 20]  # lista de notas de edad=20

if notas_20:  # si hay alumnos de 20 años
    promedio = sum(notas_20) / len(notas_20)
    print("Promedio de notas de alumnos de 20 años:", promedio)
else:
    print("No hay alumnos de 20 años")
