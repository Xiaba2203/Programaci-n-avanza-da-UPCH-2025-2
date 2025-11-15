import random  # usa funciones aleatorias
import json  # lee y escribe JSON DNI 74032240

class Profesor:  # clase base profesor
    """Clase base para profesores de la facultad."""  # descripción breve
    
    def __init__(self, num_id, nombre, edad, departamento):
        self.num_id = num_id  # id del profesor
        self.nombre = nombre  # nombre profesor
        self.edad = edad  # edad actual
        self.departamento = departamento  # departamento asignado
        self.cargo = None  # cargo actual
        self.anio_inicio_cargo = None  # año inicio cargo
    
    def cumplir_anio(self):
        # incrementar edad del profesor
        self.edad += 1  # suma un año
    
    def debe_cesar(self):
        # verifica si debe cesar por edad
        return self.edad >= 70  # cesa si >=70
    
    def asignar_cargo(self, cargo, anio):
        # asignar cargo directivo al profesor
        self.cargo = cargo  # asigna cargo
        self.anio_inicio_cargo = anio  # guarda año inicio
    
    def liberar_cargo(self):
        # quitar cargo al profesor
        self.cargo = None  # quita cargo
        self.anio_inicio_cargo = None  # borra año inicio
    
    def cargo_termino(self, anio_actual):
        # verificar si cargo terminó 3 años
        if self.cargo and self.anio_inicio_cargo:
            return (anio_actual - self.anio_inicio_cargo) >= 3  # cargo dura tres años
        return False  # no cumple condición
    
    def __str__(self):
        cargo_str = f" [{self.cargo}]" if self.cargo else ""  # muestra cargo si existe
        return f"{self.num_id} - {self.nombre} ({self.edad} años){cargo_str}"  # texto simple


class ProfesorNombrado(Profesor):  # profesor con nombramiento
    """Profesor nombrado con categoría."""  # breve
    
    def __init__(self, num_id, nombre, edad, departamento, categoria):
        super().__init__(num_id, nombre, edad, departamento)
        self.categoria = categoria  # categoría nombrado
        self.tipo = "Nombrado"  # tipo etiqueta
    
    def puede_ser_jefe_dpto(self):
        # asociado o principal
        return self.categoria in ["Asociado", "Principal"]  # candidatos jefe
    
    def puede_ser_vicedecano(self):
        # asociado o principal
        return self.categoria in ["Asociado", "Principal"]  # candidatos vicedecano
    
    def puede_ser_decano(self):
        # solo principal
        return self.categoria == "Principal"  # solo principal


class ProfesorContratado(Profesor):  # profesor contratado por horas
    """Profesor contratado por horas."""  # breve
    
    def __init__(self, num_id, nombre, edad, departamento, horas, anios_servicio=0):
        super().__init__(num_id, nombre, edad, departamento)
        self.horas = horas  # horas contratadas
        self.anios_servicio = anios_servicio  # años de servicio
        self.tipo = "Contratado"  # tipo etiqueta
    
    def incrementar_servicio(self):
        # sumar un año de servicio
        self.anios_servicio += 1  # aumenta servicio
    
    def puede_ser_nombrado(self):
        # 5 años o más de servicio
        return self.anios_servicio >= 5  # elegible si >=5


class Departamento:  # representa un departamento
    """Representa un departamento académico."""  # breve
    
    def __init__(self, nombre):
        self.nombre = nombre  # nombre depto
        self.profesores = []  # lista profesores
        self.jefe = None  # jefe actual
    
    def agregar_profesor(self, profesor):
        self.profesores.append(profesor)  # añade profesor lista
    
    def quitar_profesor(self, profesor):
        if profesor in self.profesores:
            self.profesores.remove(profesor)  # eliminar si existe
    
    def get_nombrados(self):
        # profesores nombrados del departamento
        return [p for p in self.profesores if isinstance(p, ProfesorNombrado)]  # lista nombrados
    
    def get_contratados(self):
        # profesores contratados del departamento
        return [p for p in self.profesores if isinstance(p, ProfesorContratado)]  # lista contratados
    
    def elegir_jefe(self, anio):
        # elegir jefe entre nombrados elegibles
        candidatos = [p for p in self.get_nombrados() 
                     if p.puede_ser_jefe_dpto() and not p.cargo]  # filtra candidatos
        if candidatos:
            self.jefe = random.choice(candidatos)  # asigna aleatoriamente
            self.jefe.asignar_cargo("Jefe Dpto", anio)  # marca inicio cargo


class Facultad:  # gestión de la facultad
    """Gestión de la facultad universitaria."""  # breve
    
    def __init__(self):
        self.departamentos = {}  # dicc departamentos
        self.vicedecano = None  # vicedecano actual
        self.decano = None  # decano actual
        self.profesores_cesantes = []  # lista cesantes
        self.historico = []  # historial anual
    
    def agregar_departamento(self, nombre):
        # crear nuevo departamento
        self.departamentos[nombre] = Departamento(nombre)  # añade depto
    
    def agregar_profesor(self, profesor):
        # agregar profesor a su departamento
        if profesor.departamento in self.departamentos:
            self.departamentos[profesor.departamento].agregar_profesor(profesor)  # agrega si existe
    
    def todos_nombrados(self):
        # todos los profesores nombrados
        nombrados = []
        for dept in self.departamentos.values():
            nombrados.extend(dept.get_nombrados())  # extiende lista
        return nombrados  # devuelve lista
    
    def todos_contratados(self):
        # todos los profesores contratados
        contratados = []
        for dept in self.departamentos.values():
            contratados.extend(dept.get_contratados())  # extiende lista
        return contratados  # devuelve lista
    
    def elegir_vicedecano(self, anio):
        # elegir vicedecano entre nombrados elegibles
        candidatos = [p for p in self.todos_nombrados() 
                     if p.puede_ser_vicedecano() and not p.cargo]  # filtra candidatos
        if candidatos:
            self.vicedecano = random.choice(candidatos)  # asigna aleatoriamente
            self.vicedecano.asignar_cargo("Vicedecano", anio)  # marca inicio cargo
    
    def elegir_decano(self, anio):
        # elegir decano entre principales sin cargo
        candidatos = [p for p in self.todos_nombrados() 
                     if p.puede_ser_decano() and not p.cargo]  # filtra candidatos
        if candidatos:
            self.decano = random.choice(candidatos)  # asigna aleatoriamente
            self.decano.asignar_cargo("Decano", anio)  # marca inicio cargo
    
    def verificar_cargos_terminados(self, anio):
        # verificar si hay cargos que terminan
        for dept in self.departamentos.values():
            if dept.jefe and dept.jefe.cargo_termino(anio):
                dept.jefe.liberar_cargo()  # libera cargo
                dept.jefe = None  # borra jefe
        
        if self.vicedecano and self.vicedecano.cargo_termino(anio):
            self.vicedecano.liberar_cargo()  # libera vicedecano
            self.vicedecano = None  # borra vicedecano
        
        if self.decano and self.decano.cargo_termino(anio):
            self.decano.liberar_cargo()  # libera decano
            self.decano = None  # borra decano
    
    def procesar_ceses(self):
        # procesar profesores que deben cesar
        cesados = []
        for dept in self.departamentos.values():
            for prof in dept.profesores[:]:
                if prof.debe_cesar():
                    if prof.cargo:
                        prof.liberar_cargo()  # libera su cargo
                        if prof == dept.jefe:
                            dept.jefe = None  # borra jefe si es el
                        if prof == self.vicedecano:
                            self.vicedecano = None  # borra vicedecano si es el
                        if prof == self.decano:
                            self.decano = None  # borra decano si es el
                    dept.quitar_profesor(prof)  # quita del depto
                    self.profesores_cesantes.append(prof)  # añade cesante
                    cesados.append(prof)  # registra cesado
        return cesados  # devuelve lista cesados
    
    def procesar_contratados(self):
        # renovar o promover contratados
        promovidos = []
        for dept in self.departamentos.values():
            for prof in dept.get_contratados()[:]:
                prof.incrementar_servicio()  # suma servicio
                if prof.puede_ser_nombrado():
                    if random.random() < 0.5:  # 50% promoción
                        nuevo = ProfesorNombrado(prof.num_id, prof.nombre, 
                                                prof.edad, prof.departamento, 
                                                "Auxiliar")  # crea nombrado auxiliar
                        dept.quitar_profesor(prof)  # quita contratado
                        dept.agregar_profesor(nuevo)  # agrega nombrado nuevo
                        promovidos.append(nuevo)  # registra promovido
        return promovidos  # devuelve promovidos
    
    def avanzar_anio(self, anio):
        # procesar un año académico
        for dept in self.departamentos.values():
            for prof in dept.profesores:
                prof.cumplir_anio()  # todos envejecen un año
    
    def guardar_estado(self, anio):
        # guardar estado del año
        estado = {
            'anio': anio,  # año registrado
            'departamentos': {},  # detalle por depto
            'vicedecano': self.vicedecano.nombre if self.vicedecano else None,  # nombre vicedecano
            'decano': self.decano.nombre if self.decano else None  # nombre decano
        }
        
        for nombre, dept in self.departamentos.items():
            estado['departamentos'][nombre] = {
                'jefe': dept.jefe.nombre if dept.jefe else None,  # jefe nombre
                'nombrados': [(p.num_id, p.nombre, p.categoria, p.edad) 
                             for p in dept.get_nombrados()],  # lista nombrados
                'contratados': [(p.num_id, p.nombre, p.horas, p.edad) 
                               for p in dept.get_contratados()]  # lista contratados
            }
        
        self.historico.append(estado)  # guarda en histórico
    
    def get_estado_anio(self, anio):
        # obtener estado de un año
        for estado in self.historico:
            if estado['anio'] == anio:
                return estado  # devuelve estado encontrado
        return None  # no encontrado