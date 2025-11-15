"""
═══════════════════════════════════════════════════════════════════════
    🎯 100 CLASES Y CONCEPTOS PARA TU EXAMEN DE POO 🎯
    Con detalles de: Herencia, Composición, Para qué sirve, etc.
═══════════════════════════════════════════════════════════════════════
"""

# ════════════════════════════════════════════════════════════════════
# 🧬 SECCIÓN 1: BIOINFORMÁTICA (20 clases)
# ════════════════════════════════════════════════════════════════════

# ──────────────────────────────────────────────────────────────────
# 1. SecuenciaADN
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene (clase base)
📌 COMPOSICIÓN: No
📌 SIRVE PARA: Representar y manipular secuencias de ADN
📌 PROBLEMAS: Validar secuencias, calcular GC%, buscar motivos, complemento
"""
class SecuenciaADN:
    def __init__(self, secuencia):
        self.secuencia = secuencia.upper()
        self._validar()
    
    def _validar(self):
        validos = set('ATGC')
        if not all(n in validos for n in self.secuencia):
            raise ValueError("Secuencia inválida")
    
    def complemento(self):
        comp = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
        return ''.join(comp[n] for n in self.secuencia)
    
    def gc_porcentaje(self):
        gc = self.secuencia.count('G') + self.secuencia.count('C')
        return (gc / len(self.secuencia)) * 100
    
    def transcribir(self):
        return self.secuencia.replace('T', 'U')

# ──────────────────────────────────────────────────────────────────
# 2. SecuenciaARN
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene
📌 COMPOSICIÓN: No
📌 SIRVE PARA: Trabajar con ARN (tiene U en vez de T)
📌 PROBLEMAS: Traducir a proteínas, buscar codones
"""
class SecuenciaARN:
    def __init__(self, secuencia):
        self.secuencia = secuencia.upper()
    
    def traducir_a_proteina(self):
        codones = {
            'AUG': 'M', 'UUU': 'F', 'UUC': 'F', 'UAA': '*',
            'UAG': '*', 'UGA': '*', 'GCU': 'A', 'GCC': 'A'
        }
        proteina = []
        for i in range(0, len(self.secuencia) - 2, 3):
            codon = self.secuencia[i:i+3]
            aa = codones.get(codon, 'X')
            if aa == '*':
                break
            proteina.append(aa)
        return ''.join(proteina)

# ──────────────────────────────────────────────────────────────────
# 3. Proteina
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene
📌 COMPOSICIÓN: No
📌 SIRVE PARA: Representar secuencias de aminoácidos
📌 PROBLEMAS: Calcular peso molecular, contar aminoácidos, plegamiento
"""
class Proteina:
    PESOS_MOLECULARES = {
        'A': 89, 'R': 174, 'N': 132, 'D': 133, 'C': 121,
        'E': 147, 'Q': 146, 'G': 75, 'H': 155, 'I': 131
    }
    
    def __init__(self, secuencia):
        self.secuencia = secuencia.upper()
    
    def peso_molecular(self):
        return sum(self.PESOS_MOLECULARES.get(aa, 0) for aa in self.secuencia)
    
    def contar_aminoacidos(self):
        from collections import Counter
        return Counter(self.secuencia)

# ──────────────────────────────────────────────────────────────────
# 4. Gen
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: Hereda de SecuenciaADN
📌 COMPOSICIÓN: Tiene regiones (promotor, exones, intrones)
📌 SIRVE PARA: Representar genes completos con sus partes
📌 PROBLEMAS: Expresión génica, mutaciones, splicing
"""
class Gen(SecuenciaADN):
    def __init__(self, secuencia, nombre, organismo):
        super().__init__(secuencia)
        self.nombre = nombre
        self.organismo = organismo
        self.exones = []
        self.intrones = []
    
    def agregar_exon(self, inicio, fin):
        self.exones.append((inicio, fin))
    
    def obtener_arn_maduro(self):
        # Empalmar solo los exones
        arn_maduro = ''
        for inicio, fin in self.exones:
            arn_maduro += self.secuencia[inicio:fin]
        return arn_maduro.replace('T', 'U')

# ──────────────────────────────────────────────────────────────────
# 5. Cromosoma
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene
📌 COMPOSICIÓN: SÍ - contiene múltiples Genes
📌 SIRVE PARA: Representar cromosomas completos
📌 PROBLEMAS: Organizar genes, buscar genes por nombre, calcular tamaño
"""
class Cromosoma:
    def __init__(self, numero, longitud):
        self.numero = numero
        self.longitud = longitud
        self.genes = []  # Composición: tiene genes
    
    def agregar_gen(self, gen):
        self.genes.append(gen)
    
    def buscar_gen(self, nombre):
        for gen in self.genes:
            if gen.nombre == nombre:
                return gen
        return None
    
    def contar_genes(self):
        return len(self.genes)

# ──────────────────────────────────────────────────────────────────
# 6. Genoma
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene
📌 COMPOSICIÓN: SÍ - contiene múltiples Cromosomas
📌 SIRVE PARA: Representar genoma completo de un organismo
📌 PROBLEMAS: Análisis genómico, buscar genes, contar cromosomas
"""
class Genoma:
    def __init__(self, especie):
        self.especie = especie
        self.cromosomas = []  # Composición: tiene cromosomas
    
    def agregar_cromosoma(self, cromosoma):
        self.cromosomas.append(cromosoma)
    
    def total_genes(self):
        return sum(c.contar_genes() for c in self.cromosomas)

# ──────────────────────────────────────────────────────────────────
# 7. Mutacion
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene
📌 COMPOSICIÓN: No
📌 SIRVE PARA: Representar mutaciones en secuencias
📌 PROBLEMAS: Aplicar mutaciones, simular evolución, detectar mutaciones
"""
class Mutacion:
    def __init__(self, tipo, posicion, nucleotido_original, nucleotido_nuevo):
        self.tipo = tipo  # 'sustitucion', 'insercion', 'delecion'
        self.posicion = posicion
        self.nucleotido_original = nucleotido_original
        self.nucleotido_nuevo = nucleotido_nuevo
    
    def aplicar(self, secuencia):
        seq_lista = list(secuencia)
        if self.tipo == 'sustitucion':
            seq_lista[self.posicion] = self.nucleotido_nuevo
        elif self.tipo == 'insercion':
            seq_lista.insert(self.posicion, self.nucleotido_nuevo)
        elif self.tipo == 'delecion':
            del seq_lista[self.posicion]
        return ''.join(seq_lista)

# ──────────────────────────────────────────────────────────────────
# 8. Alineador
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene
📌 COMPOSICIÓN: No (usa métodos estáticos)
📌 SIRVE PARA: Comparar y alinear secuencias
📌 PROBLEMAS: Calcular similitud, distancia de Hamming, encontrar matches
"""
class Alineador:
    @staticmethod
    def distancia_hamming(seq1, seq2):
        if len(seq1) != len(seq2):
            raise ValueError("Secuencias deben tener igual longitud")
        return sum(c1 != c2 for c1, c2 in zip(seq1, seq2))
    
    @staticmethod
    def similitud_porcentaje(seq1, seq2):
        min_len = min(len(seq1), len(seq2))
        coincidencias = sum(c1 == c2 for c1, c2 in zip(seq1[:min_len], seq2[:min_len]))
        return (coincidencias / min_len) * 100

# ──────────────────────────────────────────────────────────────────
# 9. BuscadorMotivos
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene
📌 COMPOSICIÓN: No
📌 SIRVE PARA: Buscar patrones específicos en secuencias
📌 PROBLEMAS: Encontrar sitios de restricción, motivos funcionales
"""
class BuscadorMotivos:
    def __init__(self, secuencia):
        self.secuencia = secuencia
    
    def buscar(self, motivo):
        posiciones = []
        for i in range(len(self.secuencia) - len(motivo) + 1):
            if self.secuencia[i:i+len(motivo)] == motivo:
                posiciones.append(i)
        return posiciones
    
    def buscar_todos(self, motivos):
        resultados = {}
        for motivo in motivos:
            resultados[motivo] = self.buscar(motivo)
        return resultados

# ──────────────────────────────────────────────────────────────────
# 10. EnzimaRestriccion
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene
📌 COMPOSICIÓN: No
📌 SIRVE PARA: Simular corte de ADN con enzimas de restricción
📌 PROBLEMAS: Clonación, mapeo de restricción, RFLP
"""
class EnzimaRestriccion:
    def __init__(self, nombre, sitio_reconocimiento):
        self.nombre = nombre
        self.sitio = sitio_reconocimiento
    
    def cortar(self, secuencia_adn):
        fragmentos = []
        inicio = 0
        while True:
            pos = secuencia_adn.find(self.sitio, inicio)
            if pos == -1:
                fragmentos.append(secuencia_adn[inicio:])
                break
            fragmentos.append(secuencia_adn[inicio:pos])
            inicio = pos + len(self.sitio)
        return fragmentos

# ──────────────────────────────────────────────────────────────────
# 11. Plasmido
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: Hereda de SecuenciaADN
📌 COMPOSICIÓN: Contiene genes y marcadores
📌 SIRVE PARA: Clonación molecular, ingeniería genética
📌 PROBLEMAS: Insertar genes, verificar construcciones
"""
class Plasmido(SecuenciaADN):
    def __init__(self, secuencia, nombre):
        super().__init__(secuencia)
        self.nombre = nombre
        self.circular = True
        self.genes_insertados = []
    
    def insertar_gen(self, gen, posicion):
        nueva_seq = self.secuencia[:posicion] + gen + self.secuencia[posicion:]
        self.secuencia = nueva_seq
        self.genes_insertados.append(gen)

# ──────────────────────────────────────────────────────────────────
# 12. Celula
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene
📌 COMPOSICIÓN: SÍ - contiene Genoma, Proteinas, etc.
📌 SIRVE PARA: Simular células completas
📌 PROBLEMAS: Expresión génica, metabolismo, división
"""
class Celula:
    def __init__(self, tipo):
        self.tipo = tipo
        self.genoma = None  # Composición
        self.proteinas = []  # Composición
        self.energia = 100
    
    def expresar_gen(self, gen):
        arn = gen.transcribir()
        # Simplificado: crear proteína
        self.proteinas.append(arn)
        self.energia -= 5

# ──────────────────────────────────────────────────────────────────
# 13. Organismo
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene
📌 COMPOSICIÓN: SÍ - contiene Genoma y Celulas
📌 SIRVE PARA: Representar organismos completos
📌 PROBLEMAS: Evolución, reproducción, heredabilidad
"""
class Organismo:
    def __init__(self, especie, nombre):
        self.especie = especie
        self.nombre = nombre
        self.genoma = None
        self.edad = 0
    
    def reproducir(self, pareja):
        # Simplificado: combinar genomas
        hijo = Organismo(self.especie, f"Hijo de {self.nombre}")
        return hijo

# ──────────────────────────────────────────────────────────────────
# 14. Poblacion
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene
📌 COMPOSICIÓN: SÍ - contiene múltiples Organismos
📌 SIRVE PARA: Estudios de genética de poblaciones
📌 PROBLEMAS: Frecuencias alélicas, deriva génica, selección
"""
class Poblacion:
    def __init__(self, especie):
        self.especie = especie
        self.individuos = []
    
    def agregar_individuo(self, organismo):
        self.individuos.append(organismo)
    
    def tamanio(self):
        return len(self.individuos)
    
    def calcular_frecuencias_alelicas(self):
        # Simplificado
        return {"A": 0.6, "a": 0.4}

# ──────────────────────────────────────────────────────────────────
# 15. Filogenia
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene
📌 COMPOSICIÓN: Contiene nodos (especies)
📌 SIRVE PARA: Construir árboles filogenéticos
📌 PROBLEMAS: Evolución, taxonomía, relaciones evolutivas
"""
class Filogenia:
    def __init__(self):
        self.nodos = []
        self.relaciones = {}
    
    def agregar_especie(self, especie, ancestro=None):
        self.nodos.append(especie)
        if ancestro:
            self.relaciones[especie] = ancestro
    
    def obtener_ancestro(self, especie):
        return self.relaciones.get(especie)

# ──────────────────────────────────────────────────────────────────
# 16. Codon
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene
📌 COMPOSICIÓN: No
📌 SIRVE PARA: Representar codones individuales
📌 PROBLEMAS: Traducción, uso de codones, optimización
"""
class Codon:
    TABLA_GENETICA = {
        'AUG': 'M', 'UUU': 'F', 'UUC': 'F', 'UAA': '*'
    }
    
    def __init__(self, triplete):
        if len(triplete) != 3:
            raise ValueError("Un codón debe tener 3 nucleótidos")
        self.triplete = triplete.upper()
    
    def traducir(self):
        return self.TABLA_GENETICA.get(self.triplete, 'X')
    
    def es_inicio(self):
        return self.triplete == 'AUG'
    
    def es_parada(self):
        return self.triplete in ['UAA', 'UAG', 'UGA']

# ──────────────────────────────────────────────────────────────────
# 17. MarcoLectura
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene
📌 COMPOSICIÓN: Contiene múltiples Codones
📌 SIRVE PARA: Identificar regiones codificantes
📌 PROBLEMAS: Predicción de genes, búsqueda de ORFs
"""
class MarcoLectura:
    def __init__(self, secuencia_arn, inicio=0):
        self.secuencia = secuencia_arn
        self.inicio = inicio
        self.codones = []
        self._generar_codones()
    
    def _generar_codones(self):
        for i in range(self.inicio, len(self.secuencia) - 2, 3):
            triplete = self.secuencia[i:i+3]
            self.codones.append(Codon(triplete))
    
    def buscar_orf(self):
        # Buscar marco de lectura abierto
        en_orf = False
        orf_actual = []
        orfs = []
        
        for codon in self.codones:
            if codon.es_inicio():
                en_orf = True
                orf_actual = [codon]
            elif en_orf:
                orf_actual.append(codon)
                if codon.es_parada():
                    orfs.append(orf_actual)
                    en_orf = False
                    orf_actual = []
        
        return orfs

# ──────────────────────────────────────────────────────────────────
# 18. SecuenciadorADN
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene
📌 COMPOSICIÓN: No
📌 SIRVE PARA: Simular secuenciación de ADN
📌 PROBLEMAS: Ensamblar lecturas, control de calidad
"""
class SecuenciadorADN:
    def __init__(self, tecnologia):
        self.tecnologia = tecnologia  # 'Sanger', 'Illumina', etc.
        self.precision = 0.99
    
    def secuenciar(self, muestra_adn):
        # Simula generar lecturas con posibles errores
        lecturas = []
        for i in range(0, len(muestra_adn), 100):
            lectura = muestra_adn[i:i+100]
            # Simular error aleatorio
            import random
            if random.random() > self.precision:
                lectura = self._introducir_error(lectura)
            lecturas.append(lectura)
        return lecturas
    
    def _introducir_error(self, lectura):
        import random
        pos = random.randint(0, len(lectura)-1)
        nucleotidos = ['A', 'T', 'G', 'C']
        lectura_lista = list(lectura)
        lectura_lista[pos] = random.choice(nucleotidos)
        return ''.join(lectura_lista)

# ──────────────────────────────────────────────────────────────────
# 19. AleleGenetico
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene
📌 COMPOSICIÓN: No
📌 SIRVE PARA: Representar variantes alélicas
📌 PROBLEMAS: Genética mendeliana, heredabilidad
"""
class AleleGenetico:
    def __init__(self, nombre, dominancia, fenotipo):
        self.nombre = nombre  # 'A' o 'a'
        self.dominancia = dominancia  # 'dominante', 'recesivo', 'codominante'
        self.fenotipo = fenotipo  # "ojos azules", "pelo rojo", etc.
    
    def es_dominante(self):
        return self.dominancia == 'dominante'

# ──────────────────────────────────────────────────────────────────
# 20. Genotipo
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene
📌 COMPOSICIÓN: SÍ - contiene dos Aleles
📌 SIRVE PARA: Representar combinación de alelos
📌 PROBLEMAS: Predecir fenotipos, cruces genéticos
"""
class Genotipo:
    def __init__(self, alelo1, alelo2):
        self.alelo1 = alelo1
        self.alelo2 = alelo2
    
    def es_homocigoto(self):
        return self.alelo1.nombre == self.alelo2.nombre
    
    def es_heterocigoto(self):
        return not self.es_homocigoto()
    
    def determinar_fenotipo(self):
        if self.alelo1.es_dominante():
            return self.alelo1.fenotipo
        elif self.alelo2.es_dominante():
            return self.alelo2.fenotipo
        else:
            return self.alelo1.fenotipo  # Ambos recesivos


# ════════════════════════════════════════════════════════════════════
# 🎓 SECCIÓN 2: UNIVERSIDAD Y EDUCACIÓN (15 clases)
# ════════════════════════════════════════════════════════════════════

# ──────────────────────────────────────────────────────────────────
# 21. Persona (CLASE BASE)
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene (es la BASE)
📌 COMPOSICIÓN: No
📌 SIRVE PARA: Base para Estudiante, Profesor, etc.
📌 PROBLEMAS: Gestión de personas, datos comunes
"""
class Persona:
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
    
    def presentarse(self):
        return f"Hola, soy {self.nombre}"
    
    def es_mayor_edad(self):
        return self.edad >= 18

# ──────────────────────────────────────────────────────────────────
# 22. Estudiante
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: SÍ - hereda de Persona
📌 COMPOSICIÓN: Contiene Notas, Cursos
📌 SIRVE PARA: Representar estudiantes
📌 PROBLEMAS: Calcular promedios, gestionar inscripciones
"""
class Estudiante(Persona):
    def __init__(self, nombre, edad, dni, codigo):
        super().__init__(nombre, edad, dni)
        self.codigo = codigo
        self.notas = []
        self.cursos_inscritos = []
    
    def agregar_nota(self, nota):
        self.notas.append(nota)
    
    def promedio(self):
        if not self.notas:
            return 0
        return sum(self.notas) / len(self.notas)
    
    def inscribir_curso(self, curso):
        self.cursos_inscritos.append(curso)

# ──────────────────────────────────────────────────────────────────
# 23. Profesor
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: SÍ - hereda de Persona
📌 COMPOSICIÓN: Tiene Cursos que dicta
📌 SIRVE PARA: Representar profesores
📌 PROBLEMAS: Asignar cursos, calificar estudiantes
"""
class Profesor(Persona):
    def __init__(self, nombre, edad, dni, especialidad):
        super().__init__(nombre, edad, dni)
        self.especialidad = especialidad
        self.cursos_dictados = []
        self.salario = 0
    
    def asignar_curso(self, curso):
        self.cursos_dictados.append(curso)
    
    def calificar_estudiante(self, estudiante, nota):
        estudiante.agregar_nota(nota)

# ──────────────────────────────────────────────────────────────────
# 24. Curso
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene
📌 COMPOSICIÓN: Tiene Profesor y lista de Estudiantes
📌 SIRVE PARA: Representar cursos/asignaturas
📌 PROBLEMAS: Gestionar matriculación, horarios, notas
"""
class Curso:
    def __init__(self, codigo, nombre, creditos):
        self.codigo = codigo
        self.nombre = nombre
        self.creditos = creditos
        self.profesor = None
        self.estudiantes = []
        self.horario = []
    
    def asignar_profesor(self, profesor):
        self.profesor = profesor
    
    def matricular_estudiante(self, estudiante):
        if len(self.estudiantes) < 30:  # Límite
            self.estudiantes.append(estudiante)
            return True
        return False
    
    def promedio_curso(self):
        promedios = [e.promedio() for e in self.estudiantes]
        if not promedios:
            return 0
        return sum(promedios) / len(promedios)

# ──────────────────────────────────────────────────────────────────
# 25. Nota
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene
📌 COMPOSICIÓN: Relaciona Estudiante + Curso
📌 SIRVE PARA: Registrar calificaciones específicas
📌 PROBLEMAS: Historial académico, promedios ponderados
"""
class Nota:
    def __init__(self, estudiante, curso, valor, fecha):
        self.estudiante = estudiante
        self.curso = curso
        self.valor = valor  # 0-20
        self.fecha = fecha
    
    def aprobo(self):
        return self.valor >= 11
    
    def letra_calificacion(self):
        if self.valor >= 18:
            return 'A'
        elif self.valor >= 15:
            return 'B'
        elif self.valor >= 11:
            return 'C'
        else:
            return 'F'

# ──────────────────────────────────────────────────────────────────
# 26. Aula
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene
📌 COMPOSICIÓN: No
📌 SIRVE PARA: Representar espacios físicos
📌 PROBLEMAS: Reservas, capacidad, horarios
"""
class Aula:
    def __init__(self, numero, capacidad, tipo):
        self.numero = numero
        self.capacidad = capacidad
        self.tipo = tipo  # 'laboratorio', 'teoria', 'computo'
        self.disponible = True
    
    def reservar(self):
        if self.disponible:
            self.disponible = False
            return True
        return False
    
    def liberar(self):
        self.disponible = True

# ──────────────────────────────────────────────────────────────────
# 27. Horario
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene
📌 COMPOSICIÓN: Relaciona Curso + Aula + tiempo
📌 SIRVE PARA: Programación de clases
📌 PROBLEMAS: Evitar cruces de horarios, optimización
"""
class Horario:
    def __init__(self, dia, hora_inicio, hora_fin):
        self.dia = dia  # 'Lunes', 'Martes', etc.
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.curso = None
        self.aula = None
    
    def duracion_horas(self):
        return self.hora_fin - self.hora_inicio
    
    def se_cruza_con(self, otro_horario):
        if self.dia != otro_horario.dia:
            return False
        return not (self.hora_fin <= otro_horario.hora_inicio or 
                   self.hora_inicio >= otro_horario.hora_fin)

# ──────────────────────────────────────────────────────────────────
# 28. Carrera
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene
📌 COMPOSICIÓN: SÍ - contiene lista de Cursos
📌 SIRVE PARA: Programas académicos completos
📌 PROBLEMAS: Mallas curriculares, requisitos, duración
"""
class Carrera:
    def __init__(self, nombre, duracion_semestres):
        self.nombre = nombre
        self.duracion_semestres = duracion_semestres
        self.cursos_obligatorios = []
        self.cursos_electivos = []
        self.estudiantes_matriculados = []
    
    def agregar_curso_obligatorio(self, curso):
        self.cursos_obligatorios.append(curso)
    
    def total_creditos(self):
        return sum(c.creditos for c in self.cursos_obligatorios)
    
    def puede_graduarse(self, estudiante):
        # Verificar si completó todos los cursos
        cursos_estudiante = set(c.codigo for c in estudiante.cursos_inscritos)
        cursos_requeridos = set(c.codigo for c in self.cursos_obligatorios)
        return cursos_requeridos.issubset(cursos_estudiante)

# ──────────────────────────────────────────────────────────────────
# 29. Facultad
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene
📌 COMPOSICIÓN: SÍ - contiene Carreras y Profesores
📌 SIRVE PARA: Organización administrativa universitaria
📌 PROBLEMAS: Gestión de recursos, presupuesto
"""
class Facultad:
    def __init__(self, nombre, decano):
        self.nombre = nombre
        self.decano = decano
        self.carreras = []
        self.profesores = []
        self.presupuesto = 0
    
    def agregar_carrera(self, carrera):
        self.carreras.append(carrera)
    
    def contratar_profesor(self, profesor):
        self.profesores.append(profesor)
    
    def total_estudiantes(self):
        return sum(len(c.estudiantes_matriculados) for c in self.carreras)

# ──────────────────────────────────────────────────────────────────
# 30. Universidad
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene
📌 COMPOSICIÓN: SÍ - contiene Facultades
📌 SIRVE PARA: Institución completa
📌 PROBLEMAS: Gestión global, estadísticas, reportes
"""
class Universidad:
    def __init__(self, nombre, ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.facultades = []
        self.rector = None
    
    def agregar_facultad(self, facultad):
        self.facultades.append(facultad)
    
    def total_estudiantes_universidad(self):
        return sum(f.total_estudiantes() for f in self.facultades)

# ──────────────────────────────────────────────────────────────────
# 31. Biblioteca
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene
📌 COMPOSICIÓN: SÍ - contiene Libros
📌 SIRVE PARA: Sistema de biblioteca universitaria
📌 PROBLEMAS: Préstamos, devoluciones, multas
"""
class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []
        self.prestamos_activos = []
    
    def agregar_libro(self, libro):
        self.libros.append(libro)
    
    def buscar_libro(self, titulo):
        for libro in self.libros:
            if titulo.lower() in libro.titulo.lower():
                return libro
        return None
    
    def prestar_libro(self, libro, estudiante):
        if libro.disponible:
            prestamo = Prestamo(libro, estudiante)
            self.prestamos_activos.append(prestamo)
            libro.disponible = False
            return prestamo
        return None

# ──────────────────────────────────────────────────────────────────
# 32. Libro
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene
📌 COMPOSICIÓN: No
📌 SIRVE PARA: Representar libros
📌 PROBLEMAS: Catalogación, búsqueda
"""
class Libro:
    def __init__(self, titulo, autor, isbn, anio):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.anio = anio
        self.disponible = True
        self.veces_prestado = 0
    
    def __str__(self):
        return f"{self.titulo} - {self.autor} ({self.anio})"

# ──────────────────────────────────────────────────────────────────
# 33. Prestamo
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene
📌 COMPOSICIÓN: Relaciona Libro + Estudiante
📌 SIRVE PARA: Registrar préstamos
📌 PROBLEMAS: Controlar devoluciones, calcular multas
"""
class Prestamo:
    def __init__(self, libro, estudiante):
        self.libro = libro
        self.estudiante = estudiante
        from datetime import datetime, timedelta
        self.fecha_prestamo = datetime.now()
        self.fecha_devolucion = self.fecha_prestamo + timedelta(days=14)
        self.devuelto = False
    
    def calcular_multa(self):
        if self.devuelto:
            return 0
        from datetime import datetime
        dias_atraso = (datetime.now() - self.fecha_devolucion).days
        if dias_atraso > 0:
            return dias_atraso * 0.5  # 0.5 soles por día
        return 0

# ──────────────────────────────────────────────────────────────────
# 34. Examen
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene
📌 COMPOSICIÓN: Relaciona Curso + Preguntas
📌 SIRVE PARA: Evaluaciones
📌 PROBLEMAS: Calificar automáticamente, estadísticas
"""
class Examen:
    def __init__(self, curso, tipo, fecha):
        self.curso = curso
        self.tipo = tipo  # 'parcial', 'final', 'practica'
        self.fecha = fecha
        self.preguntas = []
        self.puntaje_total = 0
    
    def agregar_pregunta(self, pregunta, puntaje):
        self.preguntas.append((pregunta, puntaje))
        self.puntaje_total += puntaje
    
    def calificar(self, respuestas):
        puntaje_obtenido = 0
        for i, (pregunta, puntaje) in enumerate(self.preguntas):
            if i < len(respuestas) and respuestas[i] == pregunta.respuesta_correcta:
                puntaje_obtenido += puntaje
        return (puntaje_obtenido / self.puntaje_total) * 20

# ──────────────────────────────────────────────────────────────────
# 35. Pregunta
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene
📌 COMPOSICIÓN: No
📌 SIRVE PARA: Preguntas de exámenes
📌 PROBLEMAS: Bancos de preguntas, tipos de pregunta
"""
class Pregunta:
    def __init__(self, enunciado, opciones, respuesta_correcta):
        self.enunciado = enunciado
        self.opciones = opciones  # Lista ['A', 'B', 'C', 'D']
        self.respuesta_correcta = respuesta_correcta
        self.dificultad = 'media'
    
    def validar_respuesta(self, respuesta):
        return respuesta == self.respuesta_correcta


# ════════════════════════════════════════════════════════════════════
# 🏦 SECCIÓN 3: SISTEMA BANCARIO (10 clases)
# ════════════════════════════════════════════════════════════════════

# ──────────────────────────────────────────────────────────────────
# 36. CuentaBancaria (CLASE BASE)
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene (es BASE)
📌 COMPOSICIÓN: Tiene Transacciones
📌 SIRVE PARA: Base para diferentes tipos de cuenta
📌 PROBLEMAS: Depósitos, retiros, transferencias
"""
class CuentaBancaria:
    def __init__(self, numero_cuenta, titular, saldo_inicial=0):
        self.numero_cuenta = numero_cuenta
        self.titular = titular
        self._saldo = saldo_inicial  # Privado
        self.transacciones = []
        self.activa = True
    
    def depositar(self, monto):
        if monto > 0:
            self._saldo += monto
            self._registrar_transaccion('deposito', monto)
            return True
        return False
    
    def retirar(self, monto):
        if monto > 0 and monto <= self._saldo:
            self._saldo -= monto
            self._registrar_transaccion('retiro', monto)
            return True
        return False
    
    def ver_saldo(self):
        return self._saldo
    
    def _registrar_transaccion(self, tipo, monto):
        from datetime import datetime
        trans = {'tipo': tipo, 'monto': monto, 'fecha': datetime.now()}
        self.transacciones.append(trans)

# ──────────────────────────────────────────────────────────────────
# 37. CuentaAhorro
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: SÍ - hereda de CuentaBancaria
📌 COMPOSICIÓN: No adicional
📌 SIRVE PARA: Cuentas de ahorro con intereses
📌 PROBLEMAS: Calcular intereses, límite de retiros
"""
class CuentaAhorro(CuentaBancaria):
    def __init__(self, numero_cuenta, titular, saldo_inicial=0, tasa_interes=0.02):
        super().__init__(numero_cuenta, titular, saldo_inicial)
        self.tasa_interes = tasa_interes
        self.retiros_mes = 0
        self.limite_retiros = 3
    
    def retirar(self, monto):
        if self.retiros_mes >= self.limite_retiros:
            return False
        if super().retirar(monto):
            self.retiros_mes += 1
            return True
        return False
    
    def aplicar_interes(self):
        interes = self._saldo * self.tasa_interes
        self.depositar(interes)
        return interes

# ──────────────────────────────────────────────────────────────────
# 38. CuentaCorriente
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: SÍ - hereda de CuentaBancaria
📌 COMPOSICIÓN: Tiene Cheques
📌 SIRVE PARA: Cuentas corrientes con sobregiro
📌 PROBLEMAS: Cheques, sobregiros, mantenimiento
"""
class CuentaCorriente(CuentaBancaria):
    def __init__(self, numero_cuenta, titular, saldo_inicial=0):
        super().__init__(numero_cuenta, titular, saldo_inicial)
        self.limite_sobregiro = 500
        self.costo_mantenimiento = 10
        self.cheques = []
    
    def retirar(self, monto):
        if monto <= self._saldo + self.limite_sobregiro:
            self._saldo -= monto
            self._registrar_transaccion('retiro', monto)
            return True
        return False
    
    def emitir_cheque(self, beneficiario, monto):
        cheque = Cheque(self, beneficiario, monto)
        self.cheques.append(cheque)
        return cheque

# ──────────────────────────────────────────────────────────────────
# 39. Cheque
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene
📌 COMPOSICIÓN: Relacionado con CuentaCorriente
📌 SIRVE PARA: Pagos con cheque
📌 PROBLEMAS: Cobrar cheques, verificar fondos
"""
class Cheque:
    contador = 1
    
    def __init__(self, cuenta_origen, beneficiario, monto):
        self.numero = Cheque.contador
        Cheque.contador += 1
        self.cuenta_origen = cuenta_origen
        self.beneficiario = beneficiario
        self.monto = monto
        self.cobrado = False
    
    def cobrar(self):
        if not self.cobrado and self.cuenta_origen.retirar(self.monto):
            self.cobrado = True
            return True
        return False

# ──────────────────────────────────────────────────────────────────
# 40. TarjetaCredito
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene
📌 COMPOSICIÓN: Relacionada con Cliente
📌 SIRVE PARA: Línea de crédito
📌 PROBLEMAS: Compras a crédito, intereses, pagos
"""
class TarjetaCredito:
    def __init__(self, numero, titular, limite_credito):
        self.numero = numero
        self.titular = titular
        self.limite_credito = limite_credito
        self.saldo_usado = 0
        self.tasa_interes_mensual = 0.03
        self.compras = []
    
    def comprar(self, monto, descripcion):
        if self.saldo_usado + monto <= self.limite_credito:
            self.saldo_usado += monto
            self.compras.append({'monto': monto, 'descripcion': descripcion})
            return True
        return False
    
    def pagar(self, monto):
        self.saldo_usado = max(0, self.saldo_usado - monto)
    
    def credito_disponible(self):
        return self.limite_credito - self.saldo_usado
    
    def calcular_pago_minimo(self):
        return self.saldo_usado * 0.05  # 5% del saldo

# ──────────────────────────────────────────────────────────────────
# 41. Prestamo
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene
📌 COMPOSICIÓN: Tiene Cuotas
📌 SIRVE PARA: Préstamos bancarios
📌 PROBLEMAS: Amortización, intereses, cuotas
"""
class Prestamo:
    def __init__(self, monto, tasa_interes_anual, plazo_meses, cliente):
        self.monto = monto
        self.tasa_interes_anual = tasa_interes_anual
        self.plazo_meses = plazo_meses
        self.cliente = cliente
        self.cuotas = []
        self.saldo_pendiente = monto
        self._generar_cuotas()
    
    def _generar_cuotas(self):
        tasa_mensual = self.tasa_interes_anual / 12 / 100
        cuota_mensual = self.monto * (tasa_mensual * (1 + tasa_mensual)**self.plazo_meses) / \
                        ((1 + tasa_mensual)**self.plazo_meses - 1)
        
        for i in range(self.plazo_meses):
            self.cuotas.append(Cuota(i+1, cuota_mensual))
    
    def pagar_cuota(self, numero_cuota):
        if numero_cuota <= len(self.cuotas):
            cuota = self.cuotas[numero_cuota - 1]
            if not cuota.pagada:
                cuota.pagar()
                self.saldo_pendiente -= cuota.monto
                return True
        return False

# ──────────────────────────────────────────────────────────────────
# 42. Cuota
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene
📌 COMPOSICIÓN: No
📌 SIRVE PARA: Representar cuota de préstamo
📌 PROBLEMAS: Control de pagos, mora
"""
class Cuota:
    def __init__(self, numero, monto):
        self.numero = numero
        self.monto = monto
        self.pagada = False
        from datetime import datetime, timedelta
        self.fecha_vencimiento = datetime.now() + timedelta(days=30*numero)
    
    def pagar(self):
        self.pagada = True
        from datetime import datetime
        self.fecha_pago = datetime.now()
    
    def esta_vencida(self):
        from datetime import datetime
        return datetime.now() > self.fecha_vencimiento and not self.pagada

# ──────────────────────────────────────────────────────────────────
# 43. Cliente
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: Hereda de Persona
📌 COMPOSICIÓN: SÍ - tiene Cuentas, Tarjetas, Prestamos
📌 SIRVE PARA: Cliente bancario completo
📌 PROBLEMAS: Gestión de productos bancarios
"""
class Cliente(Persona):
    def __init__(self, nombre, edad, dni):
        super().__init__(nombre, edad, dni)
        self.cuentas = []
        self.tarjetas = []
        self.prestamos = []
        self.puntaje_crediticio = 700
    
    def agregar_cuenta(self, cuenta):
        self.cuentas.append(cuenta)
    
    def patrimonio_total(self):
        return sum(c.ver_saldo() for c in self.cuentas)
    
    def deuda_total(self):
        deuda = sum(t.saldo_usado for t in self.tarjetas)
        deuda += sum(p.saldo_pendiente for p in self.prestamos)
        return deuda

# ──────────────────────────────────────────────────────────────────
# 44. Banco
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene
📌 COMPOSICIÓN: SÍ - tiene Clientes, Cuentas, Sucursales
📌 SIRVE PARA: Sistema bancario completo
📌 PROBLEMAS: Gestión global, reportes, sucursales
"""
class Banco:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo
        self.clientes = []
        self.cuentas = []
        self.sucursales = []
    
    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)
    
    def buscar_cuenta(self, numero_cuenta):
        for cuenta in self.cuentas:
            if cuenta.numero_cuenta == numero_cuenta:
                return cuenta
        return None
    
    def transferencia(self, cuenta_origen, cuenta_destino, monto):
        if cuenta_origen.retirar(monto):
            cuenta_destino.depositar(monto)
            return True
        return False

# ──────────────────────────────────────────────────────────────────
# 45. Cajero
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene
📌 COMPOSICIÓN: No
📌 SIRVE PARA: Cajeros automáticos
📌 PROBLEMAS: Retiros, consultas, límites diarios
"""
class Cajero:
    def __init__(self, id_cajero, ubicacion):
        self.id_cajero = id_cajero
        self.ubicacion = ubicacion
        self.efectivo_disponible = 50000
        self.operativo = True
        self.transacciones_dia = []
    
    def retirar_efectivo(self, cuenta, monto):
        if not self.operativo or monto > self.efectivo_disponible:
            return False
        if cuenta.retirar(monto):
            self.efectivo_disponible -= monto
            self.transacciones_dia.append({'tipo': 'retiro', 'monto': monto})
            return True
        return False
    
    def consultar_saldo(self, cuenta):
        return cuenta.ver_saldo()


# ════════════════════════════════════════════════════════════════════
# 🚗 SECCIÓN 4: VEHÍCULOS Y TRANSPORTE (10 clases)
# ════════════════════════════════════════════════════════════════════

# ──────────────────────────────────────────────────────────────────
# 46. Vehiculo (CLASE BASE)
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene (es BASE)
📌 COMPOSICIÓN: Tiene Motor
📌 SIRVE PARA: Base para todos los vehículos
📌 PROBLEMAS: Características comunes, polimorfismo
"""
class Vehiculo:
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.kilometraje = 0
        self.encendido = False
    
    def encender(self):
        self.encendido = True
        return "Vehículo encendido"
    
    def apagar(self):
        self.encendido = False
        return "Vehículo apagado"
    
    def avanzar(self, km):
        if self.encendido:
            self.kilometraje += km
            return f"Avanzó {km} km"
        return "Debe encender el vehículo"

# ──────────────────────────────────────────────────────────────────
# 47. Auto
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: SÍ - hereda de Vehiculo
📌 COMPOSICIÓN: Tiene Motor
📌 SIRVE PARA: Autos específicos
📌 PROBLEMAS: Características de autos
"""
class Auto(Vehiculo):
    def __init__(self, marca, modelo, anio, num_puertas):
        super().__init__(marca, modelo, anio)
        self.num_puertas = num_puertas
        self.tipo_combustible = 'gasolina'
        self.capacidad_tanque = 50
        self.combustible_actual = 50
    
    def consumir_combustible(self, km):
        consumo = km * 0.1  # 0.1 litros por km
        if self.combustible_actual >= consumo:
            self.combustible_actual -= consumo
            return True
        return False

# ──────────────────────────────────────────────────────────────────
# 48. Moto
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: SÍ - hereda de Vehiculo
📌 COMPOSICIÓN: No adicional
📌 SIRVE PARA: Motocicletas
📌 PROBLEMAS: Características específicas de motos
"""
class Moto(Vehiculo):
    def __init__(self, marca, modelo, anio, cilindrada):
        super().__init__(marca, modelo, anio)
        self.cilindrada = cilindrada
        self.tipo = '2 ruedas'
    
    def hacer_caballito(self):
        return "¡Haciendo caballito!"

# ──────────────────────────────────────────────────────────────────
# 49. Camion
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: SÍ - hereda de Vehiculo
📌 COMPOSICIÓN: Tiene carga
📌 SIRVE PARA: Vehículos de carga
📌 PROBLEMAS: Gestión de carga, peso
"""
class Camion(Vehiculo):
    def __init__(self, marca, modelo, anio, capacidad_carga):
        super().__init__(marca, modelo, anio)
        self.capacidad_carga = capacidad_carga  # en toneladas
        self.carga_actual = 0
    
    def cargar(self, peso):
        if self.carga_actual + peso <= self.capacidad_carga:
            self.carga_actual += peso
            return True
        return False
    
    def descargar(self, peso):
        if peso <= self.carga_actual:
            self.carga_actual -= peso
            return True
        return False

# ──────────────────────────────────────────────────────────────────
# 50. Motor
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene
📌 COMPOSICIÓN: Es PARTE de Vehiculo
📌 SIRVE PARA: Representar motor del vehículo
📌 PROBLEMAS: Potencia, eficiencia, mantenimiento
"""
class Motor:
    def __init__(self, tipo, potencia, cilindros):
        self.tipo = tipo  # 'gasolina', 'diesel', 'electrico'
        self.potencia = potencia  # en HP
        self.cilindros = cilindros
        self.temperatura = 20
        self.encendido = False
    
    def encender(self):
        self.encendido = True
        self.temperatura = 90
    
    def apagar(self):
        self.encendido = False
        self.temperatura = 20

# ──────────────────────────────────────────────────────────────────
# 51. GPS
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene
📌 COMPOSICIÓN: Agregación con Vehiculo
📌 SIRVE PARA: Sistema de navegación
📌 PROBLEMAS: Rutas, ubicación, distancias
"""
class GPS:
    def __init__(self):
        self.ubicacion_actual = (0, 0)
        self.destino = None
        self.historial_ubicaciones = []
    
    def actualizar_ubicacion(self, lat, lon):
        self.ubicacion_actual = (lat, lon)
        self.historial_ubicaciones.append((lat, lon))
    
    def calcular_distancia(self, destino):
        # Fórmula simplificada
        import math
        lat1, lon1 = self.ubicacion_actual
        lat2, lon2 = destino
        return math.sqrt((lat2-lat1)**2 + (lon2-lon1)**2)
    
    def establecer_destino(self, lat, lon):
        self.destino = (lat, lon)

# ──────────────────────────────────────────────────────────────────
# 52. Estacionamiento
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene
📌 COMPOSICIÓN: Tiene Espacios
📌 SIRVE PARA: Gestión de estacionamientos
📌 PROBLEMAS: Disponibilidad, tarifas, tickets
"""
class Estacionamiento:
    def __init__(self, nombre, capacidad):
        self.nombre = nombre
        self.capacidad = capacidad
        self.espacios = [None] * capacidad  # None = disponible
        self.tarifa_hora = 3.0
    
    def ingresar_vehiculo(self, vehiculo):
        for i in range(self.capacidad):
            if self.espacios[i] is None:
                self.espacios[i] = vehiculo
                from datetime import datetime
                return Ticket(i, vehiculo, datetime.now())
        return None  # Estacionamiento lleno
    
    def sacar_vehiculo(self, numero_espacio):
        if 0 <= numero_espacio < self.capacidad:
            vehiculo = self.espacios[numero_espacio]
            self.espacios[numero_espacio] = None
            return vehiculo
        return None
    
    def espacios_disponibles(self):
        return sum(1 for e in self.espacios if e is None)

# ──────────────────────────────────────────────────────────────────
# 53. Ticket (COMPLETADA)
# ──────────────────────────────────────────────────────────────────
class Ticket:
    contador = 1
    
    def __init__(self, espacio, vehiculo, hora_entrada):
        self.numero = Ticket.contador
        Ticket.contador += 1
        self.espacio = espacio
        self.vehiculo = vehiculo
        self.hora_entrada = hora_entrada
        self.hora_salida = None
    
    def registrar_salida(self):
        from datetime import datetime
        self.hora_salida = datetime.now()
    
    def calcular_tiempo(self):
        if self.hora_salida:
            delta = self.hora_salida - self.hora_entrada
            return delta.total_seconds() / 3600  # horas
        return 0
    
    def calcular_monto(self, tarifa_hora):
        horas = self.calcular_tiempo()
        return horas * tarifa_hora

# ──────────────────────────────────────────────────────────────────
# 54. Taller
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene
📌 COMPOSICIÓN: SÍ - tiene Mecanicos y servicios
📌 SIRVE PARA: Mantenimiento de vehículos
📌 PROBLEMAS: Reparaciones, presupuestos, turnos
"""
class Taller:
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad
        self.mecanicos = []
        self.vehiculos_en_servicio = []
        self.servicios_disponibles = {}
    
    def agregar_mecanico(self, mecanico):
        self.mecanicos.append(mecanico)
    
    def recibir_vehiculo(self, vehiculo, servicio):
        if servicio in self.servicios_disponibles:
            self.vehiculos_en_servicio.append({
                'vehiculo': vehiculo,
                'servicio': servicio,
                'estado': 'en espera'
            })
            return True
        return False
    
    def calcular_presupuesto(self, servicio):
        return self.servicios_disponibles.get(servicio, 0)

# ──────────────────────────────────────────────────────────────────
# 55. Mecanico
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: Hereda de Persona
📌 COMPOSICIÓN: No adicional
📌 SIRVE PARA: Personal del taller
📌 PROBLEMAS: Asignar trabajos, especialidades
"""
class Mecanico(Persona):
    def __init__(self, nombre, edad, dni, especialidad):
        super().__init__(nombre, edad, dni)
        self.especialidad = especialidad
        self.vehiculos_reparados = 0
        self.calificacion = 5.0
    
    def reparar_vehiculo(self, vehiculo, problema):
        self.vehiculos_reparados += 1
        return f"Reparando {problema} en {vehiculo.marca} {vehiculo.modelo}"


# ════════════════════════════════════════════════════════════════════
# 🏥 SECCIÓN 5: SISTEMA DE SALUD (12 clases)
# ════════════════════════════════════════════════════════════════════

# ──────────────────────────────────────────────────────────────────
# 56. Paciente
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: Hereda de Persona
📌 COMPOSICIÓN: Tiene HistoriaClinica, Citas
📌 SIRVE PARA: Representar pacientes
📌 PROBLEMAS: Historial médico, citas, alergias
"""
class Paciente(Persona):
    def __init__(self, nombre, edad, dni, grupo_sanguineo):
        super().__init__(nombre, edad, dni)
        self.grupo_sanguineo = grupo_sanguineo
        self.alergias = []
        self.citas = []
        self.historia_clinica = None
    
    def agregar_alergia(self, alergia):
        self.alergias.append(alergia)
    
    def agendar_cita(self, cita):
        self.citas.append(cita)

# ──────────────────────────────────────────────────────────────────
# 57. Doctor
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: Hereda de Persona
📌 COMPOSICIÓN: Tiene Consultorio, Especialidad
📌 SIRVE PARA: Representar doctores
📌 PROBLEMAS: Atender pacientes, prescribir, horarios
"""
class Doctor(Persona):
    def __init__(self, nombre, edad, dni, especialidad, numero_colegiatura):
        super().__init__(nombre, edad, dni)
        self.especialidad = especialidad
        self.numero_colegiatura = numero_colegiatura
        self.pacientes = []
        self.horario_atencion = {}
    
    def atender_paciente(self, paciente, diagnostico):
        consulta = Consulta(self, paciente, diagnostico)
        return consulta
    
    def prescribir_receta(self, paciente, medicamentos):
        return Receta(self, paciente, medicamentos)

# ──────────────────────────────────────────────────────────────────
# 58. Enfermero
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: Hereda de Persona
📌 COMPOSICIÓN: No adicional
📌 SIRVE PARA: Personal de enfermería
📌 PROBLEMAS: Toma de signos vitales, asistencia
"""
class Enfermero(Persona):
    def __init__(self, nombre, edad, dni, turno):
        super().__init__(nombre, edad, dni)
        self.turno = turno  # 'mañana', 'tarde', 'noche'
        self.area_asignada = None
    
    def tomar_signos_vitales(self, paciente):
        signos = {
            'presion': '120/80',
            'temperatura': 36.5,
            'pulso': 70
        }
        return signos
    
    def administrar_medicamento(self, paciente, medicamento):
        return f"Administrando {medicamento} a {paciente.nombre}"

# ──────────────────────────────────────────────────────────────────
# 59. Consulta
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene
📌 COMPOSICIÓN: Relaciona Doctor + Paciente
📌 SIRVE PARA: Registro de consultas médicas
📌 PROBLEMAS: Diagnósticos, seguimiento
"""
class Consulta:
    def __init__(self, doctor, paciente, motivo):
        self.doctor = doctor
        self.paciente = paciente
        self.motivo = motivo
        from datetime import datetime
        self.fecha = datetime.now()
        self.diagnostico = None
        self.tratamiento = None
    
    def agregar_diagnostico(self, diagnostico):
        self.diagnostico = diagnostico
    
    def agregar_tratamiento(self, tratamiento):
        self.tratamiento = tratamiento

# ──────────────────────────────────────────────────────────────────
# 60. Receta
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene
📌 COMPOSICIÓN: Contiene Medicamentos
📌 SIRVE PARA: Prescripción médica
📌 PROBLEMAS: Validar recetas, control de medicamentos
"""
class Receta:
    contador = 1
    
    def __init__(self, doctor, paciente, medicamentos):
        self.numero = Receta.contador
        Receta.contador += 1
        self.doctor = doctor
        self.paciente = paciente
        self.medicamentos = medicamentos  # Lista de dict
        from datetime import datetime, timedelta
        self.fecha_emision = datetime.now()
        self.fecha_vencimiento = self.fecha_emision + timedelta(days=30)
        self.dispensada = False
    
    def esta_vigente(self):
        from datetime import datetime
        return datetime.now() <= self.fecha_vencimiento
    
    def dispensar(self):
        if self.esta_vigente() and not self.dispensada:
            self.dispensada = True
            return True
        return False

# ──────────────────────────────────────────────────────────────────
# 61. Medicamento
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene
📌 COMPOSICIÓN: No
📌 SIRVE PARA: Representar medicamentos
📌 PROBLEMAS: Stock, precios, prescripción
"""
class Medicamento:
    def __init__(self, nombre, principio_activo, concentracion):
        self.nombre = nombre
        self.principio_activo = principio_activo
        self.concentracion = concentracion
        self.requiere_receta = False
        self.precio = 0
        self.stock = 0
    
    def esta_disponible(self):
        return self.stock > 0
    
    def vender(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            return True
        return False

# ──────────────────────────────────────────────────────────────────
# 62. Cita
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene
📌 COMPOSICIÓN: Relaciona Paciente + Doctor
📌 SIRVE PARA: Agendar citas médicas
📌 PROBLEMAS: Gestión de agenda, cancelaciones
"""
class Cita:
    def __init__(self, paciente, doctor, fecha_hora, motivo):
        self.paciente = paciente
        self.doctor = doctor
        self.fecha_hora = fecha_hora
        self.motivo = motivo
        self.estado = 'programada'  # 'programada', 'completada', 'cancelada'
    
    def confirmar(self):
        self.estado = 'confirmada'
    
    def cancelar(self):
        self.estado = 'cancelada'
    
    def completar(self):
        self.estado = 'completada'

# ──────────────────────────────────────────────────────────────────
# 63. HistoriaClinica
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene
📌 COMPOSICIÓN: SÍ - contiene Consultas, Examenes
📌 SIRVE PARA: Registro completo del paciente
📌 PROBLEMAS: Historial médico, seguimiento
"""
class HistoriaClinica:
    def __init__(self, paciente):
        self.paciente = paciente
        self.consultas = []
        self.examenes = []
        self.cirugias = []
        self.vacunas = []
    
    def agregar_consulta(self, consulta):
        self.consultas.append(consulta)
    
    def agregar_examen(self, examen):
        self.examenes.append(examen)
    
    def obtener_ultimo_diagnostico(self):
        if self.consultas:
            return self.consultas[-1].diagnostico
        return None

# ──────────────────────────────────────────────────────────────────
# 64. Examen
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene
📌 COMPOSICIÓN: Relaciona Paciente
📌 SIRVE PARA: Exámenes médicos/laboratorio
📌 PROBLEMAS: Resultados, análisis
"""
class Examen:
    def __init__(self, tipo, paciente):
        self.tipo = tipo  # 'sangre', 'orina', 'rayos x', etc.
        self.paciente = paciente
        from datetime import datetime
        self.fecha_solicitud = datetime.now()
        self.fecha_resultado = None
        self.resultados = {}
        self.estado = 'pendiente'
    
    def agregar_resultado(self, parametro, valor):
        self.resultados[parametro] = valor
    
    def completar(self):
        from datetime import datetime
        self.fecha_resultado = datetime.now()
        self.estado = 'completado'

# ──────────────────────────────────────────────────────────────────
# 65. Hospital
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene
📌 COMPOSICIÓN: SÍ - tiene Doctores, Pacientes, Areas
📌 SIRVE PARA: Sistema hospitalario completo
📌 PROBLEMAS: Gestión integral, emergencias
"""
class Hospital:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.doctores = []
        self.pacientes = []
        self.camas_disponibles = 100
        self.emergencias = []
    
    def contratar_doctor(self, doctor):
        self.doctores.append(doctor)
    
    def registrar_paciente(self, paciente):
        self.pacientes.append(paciente)
    
    def buscar_doctor_especialidad(self, especialidad):
        return [d for d in self.doctores if d.especialidad == especialidad]

# ──────────────────────────────────────────────────────────────────
# 66. Ambulancia
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: Hereda de Vehiculo
📌 COMPOSICIÓN: Tiene Paramedico
📌 SIRVE PARA: Transporte de emergencia
📌 PROBLEMAS: Atención pre-hospitalaria
"""
class Ambulancia(Vehiculo):
    def __init__(self, marca, modelo, anio, placa):
        super().__init__(marca, modelo, anio)
        self.placa = placa
        self.disponible = True
        self.equipamiento = ['desfibrilador', 'oxigeno', 'camilla']
    
    def atender_emergencia(self, ubicacion):
        if self.disponible:
            self.disponible = False
            return f"Ambulancia en camino a {ubicacion}"
        return "Ambulancia no disponible"
    
    def finalizar_servicio(self):
        self.disponible = True

# ──────────────────────────────────────────────────────────────────
# 67. Farmacia
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene
📌 COMPOSICIÓN: SÍ - tiene Medicamentos
📌 SIRVE PARA: Gestión de farmacia
📌 PROBLEMAS: Inventario, ventas, recetas
"""
class Farmacia:
    def __init__(self, nombre):
        self.nombre = nombre
        self.medicamentos = []
        self.ventas = []
    
    def agregar_medicamento(self, medicamento):
        self.medicamentos.append(medicamento)
    
    def buscar_medicamento(self, nombre):
        for med in self.medicamentos:
            if nombre.lower() in med.nombre.lower():
                return med
        return None
    
    def vender_con_receta(self, receta):
        if receta.esta_vigente() and not receta.dispensada:
            receta.dispensar()
            self.ventas.append({'receta': receta.numero, 'paciente': receta.paciente})
            return True
        return False


# ════════════════════════════════════════════════════════════════════
# 🍕 SECCIÓN 6: RESTAURANTE Y COMIDA (10 clases)
# ════════════════════════════════════════════════════════════════════

# ──────────────────────────────────────────────────────────────────
# 68. Restaurante
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene
📌 COMPOSICIÓN: SÍ - tiene Menu, Mesas, Personal
📌 SIRVE PARA: Sistema de restaurante
📌 PROBLEMAS: Gestión de pedidos, reservas
"""
class Restaurante:
    def __init__(self, nombre, capacidad):
        self.nombre = nombre
        self.capacidad = capacidad
        self.mesas = []
        self.menu = None
        self.pedidos = []
        self.empleados = []
    
    def agregar_mesa(self, mesa):
        self.mesas.append(mesa)
    
    def mesas_disponibles(self):
        return [m for m in self.mesas if m.disponible]
    
    def tomar_pedido(self, mesa, items):
        pedido = Pedido(mesa, items)
        self.pedidos.append(pedido)
        return pedido

# ──────────────────────────────────────────────────────────────────
# 69. Mesa
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene
📌 COMPOSICIÓN: No
📌 SIRVE PARA: Mesas del restaurante
📌 PROBLEMAS: Reservas, ocupación
"""
class Mesa:
    def __init__(self, numero, capacidad):
        self.numero = numero
        self.capacidad = capacidad
        self.disponible = True
        self.pedido_actual = None
    
    def ocupar(self):
        self.disponible = False
    
    def liberar(self):
        self.disponible = True
        self.pedido_actual = None

# ──────────────────────────────────────────────────────────────────
# 70. Menu
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene
📌 COMPOSICIÓN: SÍ - contiene Platos
📌 SIRVE PARA: Menú del restaurante
📌 PROBLEMAS: Gestión de platos, precios
"""
class Menu:
    def __init__(self, nombre):
        self.nombre = nombre
        self.platos = []
        self.bebidas = []
        self.postres = []
    
    def agregar_plato(self, plato):
        self.platos.append(plato)
    
    def buscar_plato(self, nombre):
        for plato in self.platos:
            if nombre.lower() in plato.nombre.lower():
                return plato
        return None
    
    def platos_por_categoria(self, categoria):
        return [p for p in self.platos if p.categoria == categoria]

# ──────────────────────────────────────────────────────────────────
# 71. Plato
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene
📌 COMPOSICIÓN: Contiene Ingredientes
📌 SIRVE PARA: Platos individuales
📌 PROBLEMAS: Recetas, precios, disponibilidad
"""
class Plato:
    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria  # 'entrada', 'principal', 'postre'
        self.ingredientes = []
        self.tiempo_preparacion = 0
        self.disponible = True
    
    def agregar_ingrediente(self, ingrediente):
        self.ingredientes.append(ingrediente)
    
    def calcular_costo(self):
        return sum(ing.precio for ing in self.ingredientes)

# ──────────────────────────────────────────────────────────────────
# 72. Ingrediente
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene
📌 COMPOSICIÓN: No
📌 SIRVE PARA: Ingredientes de platos
📌 PROBLEMAS: Inventario, costos
"""
class Ingrediente:
    def __init__(self, nombre, unidad, cantidad_stock):
        self.nombre = nombre
        self.unidad = unidad  # 'kg', 'litros', 'unidades'
        self.cantidad_stock = cantidad_stock
        self.precio = 0
        self.punto_reorden = 10
    
    def usar(self, cantidad):
        if cantidad <= self.cantidad_stock:
            self.cantidad_stock -= cantidad
            return True
        return False
    
    def necesita_reorden(self):
        return self.cantidad_stock <= self.punto_reorden

# ──────────────────────────────────────────────────────────────────
# 73. Pedido
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene
📌 COMPOSICIÓN: SÍ - contiene Platos
📌 SIRVE PARA: Pedidos de clientes
📌 PROBLEMAS: Facturación, estado del pedido
"""
class Pedido:
    contador = 1
    
    def __init__(self, mesa, items):
        self.numero = Pedido.contador
        Pedido.contador += 1
        self.mesa = mesa
        self.items = items  # Lista de platos
        from datetime import datetime
        self.hora_pedido = datetime.now()
        self.estado = 'recibido'  # 'recibido', 'preparando', 'servido', 'pagado'
    
    def calcular_total(self):
        return sum(item.precio for item in self.items)
    
    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado
    
    def agregar_item(self, plato):
        self.items.append(plato)

# ──────────────────────────────────────────────────────────────────
# 74. Chef
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: Hereda de Persona
📌 COMPOSICIÓN: No adicional
📌 SIRVE PARA: Personal de cocina
📌 PROBLEMAS: Preparar platos, gestionar cocina
"""
class Chef(Persona):
    def __init__(self, nombre, edad, dni, especialidad):
        super().__init__(nombre, edad, dni)
        self.especialidad = especialidad
        self.platos_preparados = 0
    
    def preparar_plato(self, plato):
        self.platos_preparados += 1
        return f"Preparando {plato.nombre}"
    
    def crear_plato_especial(self, nombre, ingredientes):
        return Plato(nombre, 0, 'especial')

# ──────────────────────────────────────────────────────────────────
# 75. Mesero
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: Hereda de Persona
📌 COMPOSICIÓN: Tiene Mesas asignadas
📌 SIRVE PARA: Personal de servicio
📌 PROBLEMAS: Atender mesas, tomar pedidos
"""
class Mesero(Persona):
    def __init__(self, nombre, edad, dni):
        super().__init__(nombre, edad, dni)
        self.mesas_asignadas = []
        self.propinas = 0
    
    def asignar_mesa(self, mesa):
        self.mesas_asignadas.append(mesa)
    
    def tomar_pedido(self, mesa, items):
        pedido = Pedido(mesa, items)
        return pedido
    
    def recibir_propina(self, monto):
        self.propinas += monto

# ──────────────────────────────────────────────────────────────────
# 76. Factura
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene
📌 COMPOSICIÓN: Relaciona Pedido
📌 SIRVE PARA: Facturación
📌 PROBLEMAS: Cálculo de impuestos, pagos
"""
class Factura:
    contador = 1
    
    def __init__(self, pedido, cliente):
        self.numero = Factura.contador
        Factura.contador += 1
        self.pedido = pedido
        self.cliente = cliente
        from datetime import datetime
        self.fecha = datetime.now()
        self.subtotal = pedido.calcular_total()
        self.igv = self.subtotal * 0.18
        self.total = self.subtotal + self.igv
        self.pagada = False
    
    def pagar(self, metodo):
        self.pagada = True
        self.metodo_pago = metodo
        return True

# ──────────────────────────────────────────────────────────────────
# 77. Reserva
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene
📌 COMPOSICIÓN: Relaciona Mesa + Cliente
📌 SIRVE PARA: Reservas de mesas
📌 PROBLEMAS: Gestión de reservas, cancelaciones
"""
class Reserva:
    def __init__(self, cliente, mesa, fecha_hora, num_personas):
        self.cliente = cliente
        self.mesa = mesa
        self.fecha_hora = fecha_hora
        self.num_personas = num_personas
        self.estado = 'confirmada'
    
    def cancelar(self):
        self.estado = 'cancelada'
        self.mesa.liberar()
    
    def confirmar_llegada(self):
        self.estado = 'activa'
        self.mesa.ocupar()


# ════════════════════════════════════════════════════════════════════
# 🏨 SECCIÓN 7: HOTEL (8 clases)
# ════════════════════════════════════════════════════════════════════

# ──────────────────────────────────────────────────────────────────
# 78. Hotel
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene
📌 COMPOSICIÓN: SÍ - tiene Habitaciones, Huespedes
📌 SIRVE PARA: Sistema hotelero
📌 PROBLEMAS: Reservas, check-in, servicios
"""
class Hotel:
    def __init__(self, nombre, estrellas):
        self.nombre = nombre
        self.estrellas = estrellas
        self.habitaciones = []
        self.huespedes = []
        self.reservas = []
    
    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)
    
    def buscar_habitacion_disponible(self, tipo):
        for hab in self.habitaciones:
            if hab.tipo == tipo and hab.disponible:
                return hab
        return None
    
    def hacer_reserva(self, huesped, habitacion, fecha_inicio, fecha_fin):
        if habitacion.disponible:
            reserva = ReservaHotel(huesped, habitacion, fecha_inicio, fecha_fin)
            self.reservas.append(reserva)
            habitacion.disponible = False
            return reserva
        return None

# ──────────────────────────────────────────────────────────────────
# 79. Habitacion
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene
📌 COMPOSICIÓN: No
📌 SIRVE PARA: Habitaciones del hotel
📌 PROBLEMAS: Disponibilidad, precios, tipos
"""
class Habitacion:
    def __init__(self, numero, tipo, capacidad, precio_noche):
        self.numero = numero
        self.tipo = tipo  # 'simple', 'doble', 'suite'
        self.capacidad = capacidad
        self.precio_noche = precio_noche
        self.disponible = True
        self.amenidades = []
    
    def ocupar(self):
        self.disponible = False
    
    def liberar(self):
        self.disponible = True
    
    def agregar_amenidad(self, amenidad):
        self.amenidades.append(amenidad)

# ──────────────────────────────────────────────────────────────────
# 80. Huesped
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: Hereda de Persona
📌 COMPOSICIÓN: No adicional
📌 SIRVE PARA: Clientes del hotel
📌 PROBLEMAS: Check-in, servicios, facturación
"""
class Huesped(Persona):
    def __init__(self, nombre, edad, dni, nacionalidad):
        super().__init__(nombre, edad, dni)
        self.nacionalidad = nacionalidad
        self.historial_estancias = []
    
    def hacer_checkin(self, habitacion):
        from datetime import datetime
        self.habitacion_actual = habitacion
        self.fecha_checkin = datetime.now()
    
    def hacer_checkout(self):
        from datetime import datetime
        self.fecha_checkout = datetime.now()
        self.habitacion_actual = None
# ──────────────────────────────────────────────────────────────────
# 81. ReservaHotel
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene
📌 COMPOSICIÓN: Relaciona Huesped + Habitacion
📌 SIRVE PARA: Gestionar reservas hoteleras
📌 PROBLEMAS: Calcular costos, cancelaciones, extensiones
"""
class ReservaHotel:
    contador = 1
    
    def __init__(self, huesped, habitacion, fecha_inicio, fecha_fin):
        self.numero = ReservaHotel.contador
        ReservaHotel.contador += 1
        self.huesped = huesped
        self.habitacion = habitacion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.estado = 'confirmada'
    
    def calcular_noches(self):
        delta = self.fecha_fin - self.fecha_inicio
        return delta.days
    
    def calcular_total(self):
        noches = self.calcular_noches()
        return noches * self.habitacion.precio_noche
    
    def cancelar(self):
        self.estado = 'cancelada'
        self.habitacion.liberar()

# ──────────────────────────────────────────────────────────────────
# 82. ServicioHotel
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene
📌 COMPOSICIÓN: No
📌 SIRVE PARA: Servicios adicionales del hotel
📌 PROBLEMAS: Room service, lavandería, spa
"""
class ServicioHotel:
    def __init__(self, nombre, precio, tipo):
        self.nombre = nombre
        self.precio = precio
        self.tipo = tipo  # 'limpieza', 'comida', 'spa', 'transporte'
        self.disponible = True
    
    def solicitar(self, habitacion):
        if self.disponible:
            return f"Servicio {self.nombre} solicitado para habitación {habitacion.numero}"
        return "Servicio no disponible"

# ──────────────────────────────────────────────────────────────────
# 83. Recepcionista
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: Hereda de Persona
📌 COMPOSICIÓN: No adicional
📌 SIRVE PARA: Personal de recepción
📌 PROBLEMAS: Check-in, check-out, atención al cliente
"""
class Recepcionista(Persona):
    def __init__(self, nombre, edad, dni, turno):
        super().__init__(nombre, edad, dni)
        self.turno = turno
        self.idiomas = []
    
    def realizar_checkin(self, huesped, habitacion):
        huesped.hacer_checkin(habitacion)
        habitacion.ocupar()
        return f"Check-in realizado para {huesped.nombre}"
    
    def realizar_checkout(self, huesped):
        huesped.hacer_checkout()
        if huesped.habitacion_actual:
            huesped.habitacion_actual.liberar()
        return "Check-out completado"


# ════════════════════════════════════════════════════════════════════
# 🧬 SECCIÓN 8: BIOINFORMÁTICA AVANZADA Y ANÁLISIS (12 clases)
# ════════════════════════════════════════════════════════════════════

# ──────────────────────────────────────────────────────────────────
# 84. MuestraBiologica
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene
📌 COMPOSICIÓN: Relaciona con Paciente
📌 SIRVE PARA: Representar muestras de laboratorio
📌 PROBLEMAS: Trazabilidad, almacenamiento, análisis
"""
class MuestraBiologica:
    contador = 1
    
    def __init__(self, tipo, paciente, fecha_recoleccion):
        self.id_muestra = f"MB-{MuestraBiologica.contador:05d}"
        MuestraBiologica.contador += 1
        self.tipo = tipo  # 'sangre', 'orina', 'tejido', 'saliva'
        self.paciente = paciente
        self.fecha_recoleccion = fecha_recoleccion
        self.volumen = 0
        self.temperatura_almacenamiento = -80
        self.analisis_realizados = []
    
    def agregar_analisis(self, analisis):
        self.analisis_realizados.append(analisis)
    
    def es_valida(self):
        from datetime import datetime, timedelta
        dias_transcurridos = (datetime.now() - self.fecha_recoleccion).days
        return dias_transcurridos <= 30

# ──────────────────────────────────────────────────────────────────
# 85. AnalizadorSecuencias
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene
📌 COMPOSICIÓN: Utiliza SecuenciaADN
📌 SIRVE PARA: Análisis bioinformático de secuencias
📌 PROBLEMAS: Alineamiento, homología, variantes
"""
class AnalizadorSecuencias:
    def __init__(self):
        self.secuencias_analizadas = []
        self.resultados = {}
    
    def calcular_homologia(self, seq1, seq2):
        """Calcula porcentaje de similitud entre secuencias"""
        min_len = min(len(seq1), len(seq2))
        matches = sum(1 for i in range(min_len) if seq1[i] == seq2[i])
        return (matches / min_len) * 100
    
    def detectar_snps(self, secuencia_referencia, secuencia_muestra):
        """Detecta polimorfismos de un solo nucleótido"""
        snps = []
        for i, (ref, muestra) in enumerate(zip(secuencia_referencia, secuencia_muestra)):
            if ref != muestra:
                snps.append({'posicion': i, 'referencia': ref, 'variante': muestra})
        return snps
    
    def buscar_marcos_abiertos(self, secuencia):
        """Busca ORFs (Open Reading Frames)"""
        orfs = []
        codones_inicio = ['ATG']
        codones_parada = ['TAA', 'TAG', 'TGA']
        
        for frame in range(3):
            for i in range(frame, len(secuencia) - 2, 3):
                codon = secuencia[i:i+3]
                if codon in codones_inicio:
                    inicio = i
                    for j in range(i+3, len(secuencia) - 2, 3):
                        codon_actual = secuencia[j:j+3]
                        if codon_actual in codones_parada:
                            orfs.append({'inicio': inicio, 'fin': j+3, 'frame': frame})
                            break
        return orfs

# ──────────────────────────────────────────────────────────────────
# 86. Microarray
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene
📌 COMPOSICIÓN: Contiene datos de expresión génica
📌 SIRVE PARA: Análisis de expresión génica masiva
📌 PROBLEMAS: Normalización, clustering, genes diferenciales
"""
class Microarray:
    def __init__(self, nombre_experimento):
        self.nombre = nombre_experimento
        self.genes = []
        self.expresion_datos = {}  # {gen: [valores]}
        self.muestras = []
    
    def agregar_muestra(self, muestra_id):
        self.muestras.append(muestra_id)
    
    def agregar_expresion(self, gen, valores):
        self.genes.append(gen)
        self.expresion_datos[gen] = valores
    
    def normalizar_datos(self):
        """Normalización simple por media"""
        datos_normalizados = {}
        for gen, valores in self.expresion_datos.items():
            media = sum(valores) / len(valores)
            valores_norm = [v / media if media != 0 else 0 for v in valores]
            datos_normalizados[gen] = valores_norm
        return datos_normalizados
    
    def genes_diferencialmente_expresados(self, umbral=2.0):
        """Encuentra genes con fold-change > umbral"""
        genes_diff = []
        for gen, valores in self.expresion_datos.items():
            if len(valores) >= 2:
                fold_change = max(valores) / min(valores) if min(valores) != 0 else 0
                if fold_change > umbral:
                    genes_diff.append({'gen': gen, 'fold_change': fold_change})
        return genes_diff

# ──────────────────────────────────────────────────────────────────
# 87. BasesDatosGenomicas
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene
📌 COMPOSICIÓN: Almacena Genes, Proteinas, Variantes
📌 SIRVE PARA: Repositorio de información genómica
📌 PROBLEMAS: Búsquedas, anotación, integración de datos
"""
class BasesDatosGenomicas:
    def __init__(self, nombre):
        self.nombre = nombre
        self.genes = {}
        self.proteinas = {}
        self.variantes = {}
        self.anotaciones = {}
    
    def registrar_gen(self, gen_id, gen):
        self.genes[gen_id] = gen
    
    def buscar_gen_por_nombre(self, nombre):
        for gen_id, gen in self.genes.items():
            if gen.nombre == nombre:
                return gen
        return None
    
    def agregar_anotacion(self, entidad_id, anotacion):
        if entidad_id not in self.anotaciones:
            self.anotaciones[entidad_id] = []
        self.anotaciones[entidad_id].append(anotacion)
    
    def estadisticas(self):
        return {
            'total_genes': len(self.genes),
            'total_proteinas': len(self.proteinas),
            'total_variantes': len(self.variantes)
        }

# ──────────────────────────────────────────────────────────────────
# 88. VarianteGenetica
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene
📌 COMPOSICIÓN: Relacionada con Gen
📌 SIRVE PARA: Representar variantes genéticas (SNPs, indels)
📌 PROBLEMAS: Patogenicidad, frecuencia alélica, asociación con enfermedades
"""
class VarianteGenetica:
    def __init__(self, cromosoma, posicion, referencia, alternativo):
        self.cromosoma = cromosoma
        self.posicion = posicion
        self.referencia = referencia
        self.alternativo = alternativo
        self.frecuencia_poblacional = 0.0
        self.prediccion_patogenicidad = None
        self.enfermedades_asociadas = []
    
    def es_snp(self):
        return len(self.referencia) == 1 and len(self.alternativo) == 1
    
    def es_indel(self):
        return len(self.referencia) != len(self.alternativo)
    
    def clasificar_patogenicidad(self):
        """Clasificación simplificada"""
        if self.frecuencia_poblacional > 0.05:
            return "Benigna"
        elif self.frecuencia_poblacional < 0.01:
            return "Probablemente patogénica"
        else:
            return "Significado incierto"

# ──────────────────────────────────────────────────────────────────
# 89. Pipeline
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene
📌 COMPOSICIÓN: Contiene pasos de análisis
📌 SIRVE PARA: Flujo de trabajo bioinformático
📌 PROBLEMAS: NGS, análisis de variantes, RNA-seq
"""
class Pipeline:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo  # 'WGS', 'WES', 'RNA-seq', 'ChIP-seq'
        self.pasos = []
        self.parametros = {}
        self.archivos_entrada = []
        self.archivos_salida = []
    
    def agregar_paso(self, paso, orden):
        self.pasos.append({'paso': paso, 'orden': orden, 'completado': False})
    
    def ejecutar(self):
        """Simulación de ejecución del pipeline"""
        resultados = []
        for paso in sorted(self.pasos, key=lambda x: x['orden']):
            resultado = self._ejecutar_paso(paso['paso'])
            resultados.append(resultado)
            paso['completado'] = True
        return resultados
    
    def _ejecutar_paso(self, paso):
        return f"Ejecutando: {paso}"
    
    def progreso(self):
        completados = sum(1 for p in self.pasos if p['completado'])
        return (completados / len(self.pasos)) * 100 if self.pasos else 0

# ──────────────────────────────────────────────────────────────────
# 90. ModeloPredictivo
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene
📌 COMPOSICIÓN: Tiene datos de entrenamiento
📌 SIRVE PARA: Machine Learning en bioinformática
📌 PROBLEMAS: Predicción de estructura, clasificación de enfermedades
"""
class ModeloPredictivo:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo  # 'clasificacion', 'regresion', 'clustering'
        self.datos_entrenamiento = []
        self.datos_prueba = []
        self.entrenado = False
        self.precision = 0.0
    
    def agregar_datos_entrenamiento(self, caracteristicas, etiqueta):
        self.datos_entrenamiento.append({'X': caracteristicas, 'y': etiqueta})
    
    def entrenar(self):
        """Simulación de entrenamiento"""
        if len(self.datos_entrenamiento) > 0:
            self.entrenado = True
            self.precision = 0.85  # Simulado
            return True
        return False
    
    def predecir(self, caracteristicas):
        if not self.entrenado:
            return None
        # Predicción simulada
        return "Clase A" if sum(caracteristicas) > 0 else "Clase B"
    
    def evaluar(self, datos_prueba):
        if not self.entrenado:
            return None
        correctos = 0
        for dato in datos_prueba:
            prediccion = self.predecir(dato['X'])
            if prediccion == dato['y']:
                correctos += 1
        return (correctos / len(datos_prueba)) * 100 if datos_prueba else 0

# ──────────────────────────────────────────────────────────────────
# 91. ExpresionGenica
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene
📌 COMPOSICIÓN: Relaciona Gen con niveles de expresión
📌 SIRVE PARA: Cuantificar expresión génica
📌 PROBLEMAS: RNA-seq, qPCR, análisis temporal
"""
class ExpresionGenica:
    def __init__(self, gen, condicion, nivel):
        self.gen = gen
        self.condicion = condicion  # 'control', 'tratamiento', 'enfermedad'
        self.nivel = nivel  # FPKM, TPM, o conteos
        self.unidad = 'TPM'
        self.tiempo = None
    
    def esta_sobre_expresado(self, umbral=10):
        return self.nivel > umbral
    
    def esta_sub_expresado(self, umbral=1):
        return self.nivel < umbral
    
    def fold_change(self, control_nivel):
        if control_nivel == 0:
            return float('inf')
        return self.nivel / control_nivel

# ──────────────────────────────────────────────────────────────────
# 92. RedGentica
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene
📌 COMPOSICIÓN: Contiene nodos (genes) y conexiones
📌 SIRVE PARA: Análisis de redes de interacción
📌 PROBLEMAS: PPI, redes metabólicas, co-expresión
"""
class RedGenetica:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo  # 'PPI', 'metabolica', 'regulatoria'
        self.nodos = []
        self.conexiones = []
    
    def agregar_nodo(self, gen):
        if gen not in self.nodos:
            self.nodos.append(gen)
    
    def agregar_conexion(self, gen1, gen2, peso=1.0):
        self.agregar_nodo(gen1)
        self.agregar_nodo(gen2)
        self.conexiones.append({'origen': gen1, 'destino': gen2, 'peso': peso})
    
    def grado_nodo(self, gen):
        """Número de conexiones de un gen"""
        grado = 0
        for conexion in self.conexiones:
            if conexion['origen'] == gen or conexion['destino'] == gen:
                grado += 1
        return grado
    
    def genes_hub(self, umbral=5):
        """Genes con muchas conexiones"""
        hubs = []
        for gen in self.nodos:
            if self.grado_nodo(gen) >= umbral:
                hubs.append(gen)
        return hubs

# ──────────────────────────────────────────────────────────────────
# 93. AnalizadorFilogenetico
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene
📌 COMPOSICIÓN: Usa SecuenciasADN
📌 SIRVE PARA: Análisis evolutivo y filogenético
📌 PROBLEMAS: Árboles filogenéticos, distancias evolutivas
"""
class AnalizadorFilogenetico:
    def __init__(self):
        self.secuencias = {}
        self.matriz_distancias = {}
    
    def agregar_secuencia(self, especie, secuencia):
        self.secuencias[especie] = secuencia
    
    def calcular_distancia_jukes_cantor(self, seq1, seq2):
        """Modelo de Jukes-Cantor para distancia evolutiva"""
        import math
        if len(seq1) != len(seq2):
            return None
        diferencias = sum(1 for a, b in zip(seq1, seq2) if a != b)
        p = diferencias / len(seq1)
        if p >= 0.75:
            return float('inf')
        distancia = -0.75 * math.log(1 - (4/3) * p)
        return distancia
    
    def construir_matriz_distancias(self):
        """Calcula distancias entre todas las especies"""
        especies = list(self.secuencias.keys())
        for i, esp1 in enumerate(especies):
            for esp2 in especies[i+1:]:
                dist = self.calcular_distancia_jukes_cantor(
                    self.secuencias[esp1], 
                    self.secuencias[esp2]
                )
                self.matriz_distancias[(esp1, esp2)] = dist
        return self.matriz_distancias

# ──────────────────────────────────────────────────────────────────
# 94. EstructuraProteina
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene
📌 COMPOSICIÓN: Contiene coordenadas atómicas
📌 SIRVE PARA: Representar estructura 3D de proteínas
📌 PROBLEMAS: Modelado, docking, predicción de función
"""
class EstructuraProteina:
    def __init__(self, proteina, pdb_id=None):
        self.proteina = proteina
        self.pdb_id = pdb_id
        self.atomos = []
        self.estructura_secundaria = {}
        self.dominios = []
    
    def agregar_atomo(self, tipo, x, y, z):
        self.atomos.append({'tipo': tipo, 'x': x, 'y': y, 'z': z})
    
    def calcular_centro_masa(self):
        if not self.atomos:
            return (0, 0, 0)
        x_prom = sum(a['x'] for a in self.atomos) / len(self.atomos)
        y_prom = sum(a['y'] for a in self.atomos) / len(self.atomos)
        z_prom = sum(a['z'] for a in self.atomos) / len(self.atomos)
        return (x_prom, y_prom, z_prom)
    
    def predecir_estructura_secundaria(self):
        """Predicción simplificada"""
        self.estructura_secundaria = {
            'helice_alfa': 0.4,
            'hoja_beta': 0.3,
            'bucles': 0.3
        }
        return self.estructura_secundaria

# ──────────────────────────────────────────────────────────────────
# 95. Metaboloma
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene
📌 COMPOSICIÓN: Contiene Metabolitos
📌 SIRVE PARA: Análisis metabolómico
📌 PROBLEMAS: Identificar biomarcadores, rutas metabólicas
"""
class Metaboloma:
    def __init__(self, muestra_id):
        self.muestra_id = muestra_id
        self.metabolitos = {}
        self.condicion = None
    
    def agregar_metabolito(self, nombre, concentracion):
        self.metabolitos[nombre] = concentracion
    
    def comparar_con(self, otro_metaboloma):
        """Compara perfiles metabólicos"""
        diferencias = {}
        for metabolito in self.metabolitos:
            if metabolito in otro_metaboloma.metabolitos:
                fold_change = self.metabolitos[metabolito] / otro_metaboloma.metabolitos[metabolito]
                if fold_change > 2 or fold_change < 0.5:
                    diferencias[metabolito] = fold_change
        return diferencias
    
    def biomarcadores_potenciales(self, umbral_fold_change=3.0):
        """Identifica metabolitos significativamente alterados"""
        # Simplificado: compara contra valores baseline
        biomarcadores = []
        for metabolito, conc in self.metabolitos.items():
            if conc > umbral_fold_change or conc < (1/umbral_fold_change):
                biomarcadores.append(metabolito)
        return biomarcadores


# ════════════════════════════════════════════════════════════════════
# 📊 SECCIÓN 9: ANÁLISIS DE DATOS BIOMÉDICOS (5 clases)
# ════════════════════════════════════════════════════════════════════

# ──────────────────────────────────────────────────────────────────
# 96. EstudioClinico
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene
📌 COMPOSICIÓN: Contiene Pacientes, datos clínicos
📌 SIRVE PARA: Gestionar estudios clínicos
📌 PROBLEMAS: Reclutamiento, seguimiento, análisis estadístico
"""
class EstudioClinico:
    def __init__(self, nombre, tipo, fase):
        self.nombre = nombre
        self.tipo = tipo  # 'observacional', 'intervencional'
        self.fase = fase  # I, II, III, IV
        self.participantes = []
        self.grupos = {'control': [], 'tratamiento': []}
        self.datos_recolectados = []
        self.estado = 'reclutando'
    
    def inscribir_participante(self, paciente, grupo):
        if grupo in self.grupos:
            self.grupos[grupo].append(paciente)
            self.participantes.append(paciente)
            return True
        return False
    
    def registrar_dato(self, paciente, variable, valor, tiempo):
        dato = {
            'paciente': paciente,
            'variable': variable,
            'valor': valor,
            'tiempo': tiempo
        }
        self.datos_recolectados.append(dato)
    
    def analizar_eficacia(self):
        """Análisis simplificado de eficacia"""
        if not self.datos_recolectados:
            return None
        
        mejoras_tratamiento = 0
        mejoras_control = 0
        
        for dato in self.datos_recolectados:
            if dato['paciente'] in self.grupos['tratamiento']:
                if dato['valor'] > 0:  # Simplificado: valor positivo = mejora
                    mejoras_tratamiento += 1
            elif dato['paciente'] in self.grupos['control']:
                if dato['valor'] > 0:
                    mejoras_control += 1
        
        n_trat = len(self.grupos['tratamiento'])
        n_ctrl = len(self.grupos['control'])
        
        tasa_trat = mejoras_tratamiento / n_trat if n_trat > 0 else 0
        tasa_ctrl = mejoras_control / n_ctrl if n_ctrl > 0 else 0
        
        return {
            'tasa_respuesta_tratamiento': tasa_trat,
            'tasa_respuesta_control': tasa_ctrl,
            'diferencia': tasa_trat - tasa_ctrl
        }

# ──────────────────────────────────────────────────────────────────
# 97. DatasetBiomedico
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene
📌 COMPOSICIÓN: Matriz de datos
📌 SIRVE PARA: Almacenar y procesar datos biomédicos
📌 PROBLEMAS: Limpieza, normalización, análisis exploratorio
"""
class DatasetBiomedico:
    def __init__(self, nombre):
        self.nombre = nombre
        self.datos = []
        self.columnas = []
        self.metadatos = {}
    
    def agregar_columna(self, nombre_columna):
        self.columnas.append(nombre_columna)
    
    def agregar_fila(self, valores):
        if len(valores) == len(self.columnas):
            self.datos.append(valores)
            return True
        return False
    
    def obtener_columna(self, nombre_columna):
        if nombre_columna not in self.columnas:
            return None
        indice = self.columnas.index(nombre_columna)
        return [fila[indice] for fila in self.datos]
    
    def estadisticas_descriptivas(self, nombre_columna):
        """Calcula estadísticas básicas"""
        valores = self.obtener_columna(nombre_columna)
        if not valores:
            return None
        
        valores_numericos = [v for v in valores if isinstance(v, (int, float))]
        if not valores_numericos:
            return None
        
        n = len(valores_numericos)
        promedio = sum(valores_numericos) / n
        valores_ordenados = sorted(valores_numericos)
        mediana = valores_ordenados[n//2] if n % 2 else (valores_ordenados[n//2-1] + valores_ordenados[n//2]) / 2
        
        varianza = sum((x - promedio)**2 for x in valores_numericos) / n
        desv_std = varianza ** 0.5
        
        return {
            'n': n,
            'promedio': promedio,
            'mediana': mediana,
            'desviacion_estandar': desv_std,
            'minimo': min(valores_numericos),
            'maximo': max(valores_numericos)
        }
    
    def valores_faltantes(self):
        """Detecta valores faltantes"""
        faltantes = {}
        for i, col in enumerate(self.columnas):
            nulos = sum(1 for fila in self.datos if fila[i] is None or fila[i] == '')
            faltantes[col] = nulos
        return faltantes

# ──────────────────────────────────────────────────────────────────
# 98. AnalizadorEstadistico
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene
📌 COMPOSICIÓN: Usa DatasetBiomedico
📌 SIRVE PARA: Análisis estadístico de datos biomédicos
📌 PROBLEMAS: Pruebas de hipótesis, correlaciones, regresión
"""
class AnalizadorEstadistico:
    def __init__(self):
        self.resultados = {}
    
    def prueba_t_student(self, grupo1, grupo2):
        """T-test simplificado"""
        import math
        
        n1, n2 = len(grupo1), len(grupo2)
        if n1 == 0 or n2 == 0:
            return None
        
        media1 = sum(grupo1) / n1
        media2 = sum(grupo2) / n2
        
        var1 = sum((x - media1)**2 for x in grupo1) / n1
        var2 = sum((x - media2)**2 for x in grupo2) / n2
        
        # Error estándar
        se = math.sqrt(var1/n1 + var2/n2)
        
        # Estadístico t
        t_stat = (media1 - media2) / se if se != 0 else 0
        
        # Grados de libertad (aproximación)
        df = n1 + n2 - 2
        
        return {
            't_estadistico': t_stat,
            'grados_libertad': df,
            'media_grupo1': media1,
            'media_grupo2': media2,
            'diferencia': media1 - media2
        }
    
    def correlacion_pearson(self, variable1, variable2):
        """Coeficiente de correlación de Pearson"""
        import math
        
        n = len(variable1)
        if n != len(variable2) or n == 0:
            return None
        
        media1 = sum(variable1) / n
        media2 = sum(variable2) / n
        
        numerador = sum((x - media1) * (y - media2) for x, y in zip(variable1, variable2))
        
        sum_sq1 = sum((x - media1)**2 for x in variable1)
        sum_sq2 = sum((y - media2)**2 for y in variable2)
        
        denominador = math.sqrt(sum_sq1 * sum_sq2)
        
        r = numerador / denominador if denominador != 0 else 0
        
        return {
            'r': r,
            'r_cuadrado': r**2,
            'interpretacion': self._interpretar_correlacion(r)
        }
    
    def _interpretar_correlacion(self, r):
        r_abs = abs(r)
        if r_abs >= 0.9:
            return "Muy fuerte"
        elif r_abs >= 0.7:
            return "Fuerte"
        elif r_abs >= 0.5:
            return "Moderada"
        elif r_abs >= 0.3:
            return "Débil"
        else:
            return "Muy débil"
    
    def chi_cuadrado(self, observados, esperados):
        """Prueba Chi-cuadrado"""
        if len(observados) != len(esperados):
            return None
        
        chi2 = sum((o - e)**2 / e for o, e in zip(observados, esperados) if e != 0)
        df = len(observados) - 1
        
        return {
            'chi_cuadrado': chi2,
            'grados_libertad': df
        }

# ──────────────────────────────────────────────────────────────────
# 99. VisualizadorDatos
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene
📌 COMPOSICIÓN: Usa DatasetBiomedico
📌 SIRVE PARA: Generar visualizaciones de datos
📌 PROBLEMAS: Gráficos, reportes, dashboards
"""
class VisualizadorDatos:
    def __init__(self):
        self.graficos_generados = []
    
    def crear_histograma(self, datos, titulo, bins=10):
        """Genera datos para histograma"""
        if not datos:
            return None
        
        minimo = min(datos)
        maximo = max(datos)
        rango = maximo - minimo
        ancho_bin = rango / bins if rango > 0 else 1
        
        frecuencias = [0] * bins
        for valor in datos:
            if valor == maximo:
                indice = bins - 1
            else:
                indice = int((valor - minimo) / ancho_bin)
                indice = min(indice, bins - 1)
            frecuencias[indice] += 1
        
        grafico = {
            'tipo': 'histograma',
            'titulo': titulo,
            'bins': bins,
            'frecuencias': frecuencias,
            'limites': [(minimo + i*ancho_bin, minimo + (i+1)*ancho_bin) for i in range(bins)]
        }
        
        self.graficos_generados.append(grafico)
        return grafico
    
    def crear_diagrama_caja(self, datos, titulo):
        """Genera datos para box plot"""
        if not datos:
            return None
        
        datos_ordenados = sorted(datos)
        n = len(datos_ordenados)
        
        q1 = datos_ordenados[n//4]
        mediana = datos_ordenados[n//2]
        q3 = datos_ordenados[3*n//4]
        iqr = q3 - q1
        
        # Límites para outliers
        limite_inferior = q1 - 1.5 * iqr
        limite_superior = q3 + 1.5 * iqr
        
        outliers = [x for x in datos if x < limite_inferior or x > limite_superior]
        
        grafico = {
            'tipo': 'boxplot',
            'titulo': titulo,
            'q1': q1,
            'mediana': mediana,
            'q3': q3,
            'minimo': min(datos),
            'maximo': max(datos),
            'outliers': outliers
        }
        
        self.graficos_generados.append(grafico)
        return grafico
    
    def crear_diagrama_dispersion(self, x_datos, y_datos, titulo):
        """Genera datos para scatter plot"""
        if len(x_datos) != len(y_datos):
            return None
        
        grafico = {
            'tipo': 'scatter',
            'titulo': titulo,
            'puntos': list(zip(x_datos, y_datos)),
            'n_puntos': len(x_datos)
        }
        
        self.graficos_generados.append(grafico)
        return grafico
    
    def generar_reporte(self):
        """Resume todos los gráficos generados"""
        return {
            'total_graficos': len(self.graficos_generados),
            'tipos': [g['tipo'] for g in self.graficos_generados],
            'graficos': self.graficos_generados
        }

# ──────────────────────────────────────────────────────────────────
# 100. SistemaBioinformatico
# ──────────────────────────────────────────────────────────────────
"""
📌 HERENCIA: No tiene
📌 COMPOSICIÓN: SÍ - integra TODAS las clases anteriores
📌 SIRVE PARA: Sistema completo de análisis bioinformático
📌 PROBLEMAS: Integración de datos, análisis multiómico, reportes
"""
class SistemaBioinformatico:
    def __init__(self, nombre_laboratorio):
        self.nombre_laboratorio = nombre_laboratorio
        self.base_datos = BasesDatosGenomicas(f"DB_{nombre_laboratorio}")
        self.muestras = []
        self.pacientes = []
        self.estudios = []
        self.pipelines = []
        self.resultados_analisis = {}
        self.usuarios = []
    
    def registrar_muestra(self, muestra):
        """Registra una nueva muestra biológica"""
        self.muestras.append(muestra)
        return muestra.id_muestra
    
    def analizar_muestra(self, muestra_id, tipo_analisis):
        """Ejecuta análisis sobre una muestra"""
        muestra = next((m for m in self.muestras if m.id_muestra == muestra_id), None)
        if not muestra:
            return None
        
        resultado = {
            'muestra_id': muestra_id,
            'tipo_analisis': tipo_analisis,
            'fecha': None,
            'resultados': {}
        }
        
        from datetime import datetime
        resultado['fecha'] = datetime.now()
        
        if tipo_analisis == 'secuenciacion':
            # Simulación de análisis de secuenciación
            resultado['resultados'] = {
                'lecturas_totales': 50000000,
                'calidad_promedio': 35,
                'variantes_detectadas': 150
            }
        elif tipo_analisis == 'expresion_genica':
            resultado['resultados'] = {
                'genes_detectados': 15000,
                'genes_expresados': 12000,
                'genes_diferenciales': 250
            }
        
        self.resultados_analisis[muestra_id] = resultado
        return resultado
    
    def crear_estudio_clinico(self, nombre, tipo, fase):
        """Crea un nuevo estudio clínico"""
        estudio = EstudioClinico(nombre, tipo, fase)
        self.estudios.append(estudio)
        return estudio
    
    def ejecutar_pipeline(self, pipeline):
        """Ejecuta un pipeline de análisis"""
        self.pipelines.append(pipeline)
        resultados = pipeline.ejecutar()
        return resultados
    
    def analisis_integrativo(self, paciente_id):
        """Análisis multiómico de un paciente"""
        paciente = next((p for p in self.pacientes if p.dni == paciente_id), None)
        if not paciente:
            return None
        
        # Buscar todas las muestras del paciente
        muestras_paciente = [m for m in self.muestras if m.paciente == paciente]
        
        analisis_integrativo = {
            'paciente': paciente.nombre,
            'total_muestras': len(muestras_paciente),
            'analisis_realizados': [],
            'hallazgos_principales': [],
            'recomendaciones': []
        }
        
        # Recopilar todos los análisis
        for muestra in muestras_paciente:
            if muestra.id_muestra in self.resultados_analisis:
                analisis_integrativo['analisis_realizados'].append(
                    self.resultados_analisis[muestra.id_muestra]
                )
        
        # Generar hallazgos (simplificado)
        if len(analisis_integrativo['analisis_realizados']) > 0:
            analisis_integrativo['hallazgos_principales'] = [
                "Variantes genéticas de interés detectadas",
                "Perfil de expresión génica característico",
                "Biomarcadores potenciales identificados"
            ]
            
            analisis_integrativo['recomendaciones'] = [
                "Realizar seguimiento con análisis funcional",
                "Validar hallazgos con métodos independientes",
                "Considerar asesoramiento genético"
            ]
        
        return analisis_integrativo
    
    def generar_reporte_completo(self):
        """Genera reporte general del sistema"""
        reporte = {
            'laboratorio': self.nombre_laboratorio,
            'estadisticas': {
                'total_muestras': len(self.muestras),
                'total_pacientes': len(self.pacientes),
                'total_estudios': len(self.estudios),
                'analisis_completados': len(self.resultados_analisis),
                'pipelines_ejecutados': len(self.pipelines)
            },
            'base_datos': self.base_datos.estadisticas(),
            'estado_general': 'Operativo'
        }
        
        return reporte
    
    def buscar_paciente_por_variante(self, cromosoma, posicion):
        """Búsqueda de pacientes con variante específica"""
        # Simplificado: buscaría en base de datos de variantes
        pacientes_con_variante = []
        
        for resultado in self.resultados_analisis.values():
            if 'variantes_detectadas' in resultado['resultados']:
                # Aquí iría la lógica de búsqueda real
                pacientes_con_variante.append(resultado['muestra_id'])
        
        return pacientes_con_variante
    
    def exportar_datos(self, formato='csv'):
        """Exporta datos del sistema"""
        exportacion = {
            'formato': formato,
            'fecha_exportacion': None,
            'archivos_generados': []
        }
        
        from datetime import datetime
        exportacion['fecha_exportacion'] = datetime.now()
        
        # Simula generación de archivos
        exportacion['archivos_generados'] = [
            f'muestras_{self.nombre_laboratorio}.{formato}',
            f'resultados_{self.nombre_laboratorio}.{formato}',
            f'estudios_{self.nombre_laboratorio}.{formato}'
        ]
        
        return exportacion


# ════════════════════════════════════════════════════════════════════
# 🎉 ¡COMPLETADO! 100 CLASES DE POO
# ════════════════════════════════════════════════════════════════════

"""
═══════════════════════════════════════════════════════════════════════
    ✅ RESUMEN FINAL DE LAS 100 CLASES
═══════════════════════════════════════════════════════════════════════

📊 DISTRIBUCIÓN POR SECCIONES:
- Bioinformática Básica (1-20): 20 clases
- Universidad y Educación (21-35): 15 clases
- Sistema Bancario (36-45): 10 clases
- Vehículos y Transporte (46-55): 10 clases
- Sistema de Salud (56-67): 12 clases
- Restaurante y Comida (68-77): 10 clases
- Hotel (78-83): 6 clases
- Bioinformática Avanzada (84-95): 12 clases
- Análisis de Datos Biomédicos (96-100): 5 clases

🎯 CONCEPTOS DE POO CUBIERTOS:
✓ Herencia simple y múltiple
✓ Composición y agregación
✓ Encapsulamiento (atributos privados)
✓ Polimorfismo
✓ Métodos estáticos y de clase
✓ Sobrecarga de métodos
✓ Relaciones entre clases (1:1, 1:N, N:M)

💡 APLICACIONES ESPECIALES PARA BIOMEDICINA:
- Análisis de secuencias (ADN, ARN, Proteínas)
- Genética de poblaciones
- Estudios clínicos
- Machine Learning en bioinformática
- Análisis metabolómico
- Redes de interacción génica
- Análisis filogenético
- Estructuras de proteínas
- Pipelines de análisis NGS
- Sistemas integrativos multiómicos

🚀 PROBLEMAS QUE PUEDES RESOLVER:
1. Alineamiento de secuencias
2. Predicción de genes
3. Análisis de expresión génica
4. Detección de variantes (SNPs, indels)
5. Estudios de asociación
6. Análisis estadístico de datos clínicos
7. Visualización de datos biomédicos
8. Gestión de biobancos
9. Análisis de redes biológicas
10. Modelado predictivo en medicina

═══════════════════════════════════════════════════════════════════════
    🎓 ¡BUENA SUERTE EN TU EXAMEN DE POO! 🎓
═══════════════════════════════════════════════════════════════════════
"""