from P1 import Pregrado, Postgrado, Visitante, Carrera

# Crea carreras (objetos de tipo Carrera)
c1 = Carrera("Ingeniería Biomédica")
c2 = Carrera("Ciencias Ambientales")

# Crea estudiantes con distintos tipos
e1 = Pregrado("Ana Pérez", "A001", "Ingeniería Biomédica", 17.5, True)
e2 = Pregrado("Luis Gómez", "A002", "Ingeniería Biomédica", 15.8)
e3 = Visitante("Marta Ruiz", "A003", "Ciencias Ambientales", 16.9)
e4 = Postgrado("Carlos Díaz", "P001", "Ciencias Ambientales", 18.2, True)

# Asocia estudiantes con sus carreras (composición)
c1.agregar_estudiante(e1)
c1.agregar_estudiante(e2)
c2.agregar_estudiante(e3)
c2.agregar_estudiante(e4)

# Función: busca mejor estudiante de pregrado
def mejor_pregrado(carrera):
    # Filtra solo pregrados o visitantes
    pregrados = [e for e in carrera.estudiantes if e.tipo() in ["Pregrado", "Visitante"]]
    # Si no hay, devuelve None
    if not pregrados:
        return None
    # Retorna con mayor promedio
    return max(pregrados, key=lambda e: e.promedio)

# Función: cuenta estudiantes becarios
def contar_becarios(carrera):
    # Suma True (1) por cada becario
    return sum(e.becario for e in carrera.estudiantes)

# Función: lista visitantes de la carrera
def listar_visitantes(carrera):
    # Retorna nombres de tipo Visitante
    return [e.mostrar() for e in carrera.estudiantes if e.tipo() == "Visitante"]

# Recorre cada carrera y muestra resultados
for carrera in [c1, c2]:
    print(f"\nCarrera: {carrera.nombre}")
    print("Mejor pregrado:", mejor_pregrado(carrera).mostrar() if mejor_pregrado(carrera) else "Ninguno")
    print("Becarios:", contar_becarios(carrera))
    print("Visitantes:", listar_visitantes(carrera))
