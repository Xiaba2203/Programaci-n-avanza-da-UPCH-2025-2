import numpy as np  # usamos numpy

estudiantes = np.array(["Sue", "Paul", "Steven", "Nancy"])  # nombres
cursos = np.array(["Programming", "Chemistry", "Biology"])  # cursos

notas = np.array([  # matriz de notas
    [17, 15, 16],
    [14, 18, 15],
    [16, 14, 18],
    [15, 17, 14]
])

print("Promedio general:", notas.mean())  # promedio total

for i, nombre in enumerate(estudiantes):  # recorre estudiantes
    idx = notas[i].argmax()  # mayor nota
    print(nombre, "mejor nota:", notas[i][idx], "en", cursos[idx])  # muestra mejor

promedios_cursos = notas.mean(axis=0)  # promedio por curso
print("Promedio cursos:", promedios_cursos)  # muestra promedios
print("Curso mayor promedio:", cursos[promedios_cursos.argmax()])  # mayor curso

for i, nombre in enumerate(estudiantes):  # recorre estudiantes
    print(nombre, "promedio:", notas[i].mean())  # promedio de cada uno

promedios_est = notas.mean(axis=1)  # promedios alumnos
idx_max = promedios_est.argmax()  # mejor alumno
print("Mejor alumno:", estudiantes[idx_max], "con", promedios_est[idx_max])  # muestra
