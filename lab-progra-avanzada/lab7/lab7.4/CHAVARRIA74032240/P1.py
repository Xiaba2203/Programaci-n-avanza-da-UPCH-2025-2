class Persona:
    def __init__(self, nombre, codigo):
        # Inicializa nombre y código
        self.nombre = nombre
        self.codigo = codigo

    def mostrar(self):
        # Retorna texto con nombre y código
        return f"{self.nombre} ({self.codigo})"


class Estudiante(Persona):
    def __init__(self, nombre, codigo, carrera, promedio, becario=False):
        # Llama al constructor de Persona
        super().__init__(nombre, codigo)
        # Atributos propios de Estudiante
        self.carrera = carrera
        self.promedio = promedio
        self.becario = becario

    def tipo(self):
        # Retorna tipo genérico
        return "Estudiante"


class Pregrado(Estudiante):
    def tipo(self):
        # Cambia comportamiento (polimorfismo)
        return "Pregrado"


class Postgrado(Estudiante):
    def tipo(self):
        # Retorna tipo postgrado
        return "Postgrado"


class Visitante(Pregrado):
    def tipo(self):
        # Es subtipo de pregrado
        return "Visitante"


class Carrera:
    def __init__(self, nombre):
        # Inicializa nombre y lista vacía
        self.nombre = nombre
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        # Agrega estudiante a la lista
        self.estudiantes.append(estudiante)
