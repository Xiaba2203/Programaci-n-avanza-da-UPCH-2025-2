"""
═══════════════════════════════════════════════════════════════════════
    GUÍA POO EXPLICADA CON MANZANITAS 🍎
    TODO LO QUE NECESITAS SABER PARA TU EXAMEN
═══════════════════════════════════════════════════════════════════════
"""

# ═══════════════════════════════════════════════════════════════════════
# 1. CLASE BÁSICA - TU PRIMER MOLDE 🏗️
# ═══════════════════════════════════════════════════════════════════════

"""
🍎 PIENSA ASÍ: Una clase es como un MOLDE de galletas.
   El molde define la FORMA, pero no es la galleta en sí.
"""

class Perro:
    # __init__ es el CONSTRUCTOR (se ejecuta cuando creas un perro)
    # self = "yo mismo" (el perro que estás creando)
    
    def __init__(self, nombre, edad, raza):
        """
        🍎 Esto es como LLENAR EL MOLDE con ingredientes específicos
        """
        self.nombre = nombre    # Cada perro tiene SU nombre
        self.edad = edad        # Cada perro tiene SU edad
        self.raza = raza        # Cada perro tiene SU raza
    
    def ladrar(self):
        """
        🍎 Los métodos son ACCIONES que puede hacer el objeto
        """
        return f"{self.nombre} dice: ¡Guau guau!"
    
    def cumplir_anios(self):
        """
        🍎 Los métodos pueden MODIFICAR los atributos
        """
        self.edad += 1
        return f"{self.nombre} ahora tiene {self.edad} años"
    
    def describir(self):
        return f"{self.nombre} es un {self.raza} de {self.edad} años"

# ═══ CÓMO USAR ═══
# Crear objetos (galletas con el molde):
firulais = Perro("Firulais", 3, "Labrador")
rocky = Perro("Rocky", 5, "Pastor Alemán")

# Usar sus métodos:
print(firulais.ladrar())           # Firulais dice: ¡Guau guau!
print(firulais.describir())        # Firulais es un Labrador de 3 años
firulais.cumplir_anios()           # Firulais cumple años
print(firulais.edad)               # Ahora muestra 4


# ═══════════════════════════════════════════════════════════════════════
# 2. ENCAPSULAMIENTO - PROTEGER TUS DATOS 🔒
# ═══════════════════════════════════════════════════════════════════════

"""
🍎 PIENSA ASÍ: Tu billetera está en tu bolsillo (privada).
   Nadie puede agarrar tu dinero directamente, pero TÚ puedes dárselo.
"""

class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.__saldo = saldo_inicial  # __ = PRIVADO (nadie puede tocarlo directo)
    
    # GETTER - para VER el saldo (como PEDIR permiso)
    def ver_saldo(self):
        return f"Saldo de {self.titular}: ${self.__saldo}"
    
    # SETTER - para MODIFICAR el saldo de forma CONTROLADA
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            return f"Depositado: ${cantidad}. Nuevo saldo: ${self.__saldo}"
        return "La cantidad debe ser positiva"
    
    def retirar(self, cantidad):
        if cantidad > self.__saldo:
            return "¡Saldo insuficiente!"
        self.__saldo -= cantidad
        return f"Retirado: ${cantidad}. Saldo restante: ${self.__saldo}"

# ═══ CÓMO USAR ═══
cuenta = CuentaBancaria("Juan", 1000)
print(cuenta.ver_saldo())          # Saldo de Juan: $1000
print(cuenta.depositar(500))       # Depositado: $500. Nuevo saldo: $1500
print(cuenta.retirar(200))         # Retirado: $200. Saldo restante: $1300

# ❌ NO PUEDES: print(cuenta.__saldo)  <- Esto da ERROR (es privado)
# ✅ SÍ PUEDES: print(cuenta.ver_saldo())  <- Así es correcto


# ═══════════════════════════════════════════════════════════════════════
# 3. HERENCIA - HEREDAR CARACTERÍSTICAS 👨‍👦
# ═══════════════════════════════════════════════════════════════════════

"""
🍎 PIENSA ASÍ: Tú HEREDAS características de tus padres (ojos, estatura),
   pero TAMBIÉN tienes cosas propias (tu personalidad, gustos).
"""

class Animal:
    """CLASE PADRE (la base)"""
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def hacer_sonido(self):
        return "Algún sonido..."
    
    def dormir(self):
        return f"{self.nombre} está durmiendo 😴"

class Gato(Animal):  # Gato HEREDA de Animal
    """CLASE HIJA"""
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)  # Llamar al constructor del PADRE
        self.color = color  # Característica PROPIA del gato
    
    # OVERRIDE - Reescribir un método heredado
    def hacer_sonido(self):
        return f"{self.nombre} dice: ¡Miau miau!"
    
    # Método NUEVO (solo los gatos lo tienen)
    def ronronear(self):
        return f"{self.nombre} está ronroneando 😸"

class Pajaro(Animal):
    def hacer_sonido(self):
        return f"{self.nombre} dice: ¡Pío pío!"
    
    def volar(self):
        return f"{self.nombre} está volando 🦅"

# ═══ CÓMO USAR ═══
michi = Gato("Michi", 2, "naranja")
print(michi.hacer_sonido())        # Michi dice: ¡Miau miau!
print(michi.dormir())              # Michi está durmiendo 😴 (heredado)
print(michi.ronronear())           # Michi está ronroneando 😸 (propio)

piolín = Pajaro("Piolín", 1)
print(piolín.hacer_sonido())       # Piolín dice: ¡Pío pío!
print(piolín.volar())              # Piolín está volando 🦅


# ═══════════════════════════════════════════════════════════════════════
# 4. POLIMORFISMO - MISMA ACCIÓN, DIFERENTE FORMA 🎭
# ═══════════════════════════════════════════════════════════════════════

"""
🍎 PIENSA ASÍ: Todos los vehículos "avanzan", pero:
   - Un auto avanza rodando
   - Un barco avanza navegando
   - Un avión avanza volando
   Misma ACCIÓN (avanzar), diferentes FORMAS de hacerlo.
"""

class Vehiculo:
    def __init__(self, marca):
        self.marca = marca
    
    def avanzar(self):
        return "El vehículo avanza"

class Auto(Vehiculo):
    def avanzar(self):
        return f"{self.marca} avanza rodando 🚗"

class Barco(Vehiculo):
    def avanzar(self):
        return f"{self.marca} avanza navegando ⛵"

class Avion(Vehiculo):
    def avanzar(self):
        return f"{self.marca} avanza volando ✈️"

# ═══ CÓMO USAR - AQUÍ VES EL POLIMORFISMO ═══
vehiculos = [
    Auto("Toyota"),
    Barco("Yamaha"),
    Avion("Boeing")
]

# Mismo método, diferentes resultados:
for v in vehiculos:
    print(v.avanzar())
# Toyota avanza rodando 🚗
# Yamaha avanza navegando ⛵
# Boeing avanza volando ✈️


# ═══════════════════════════════════════════════════════════════════════
# 5. CLASE ABSTRACTA - EL CONTRATO 📜
# ═══════════════════════════════════════════════════════════════════════

"""
🍎 PIENSA ASÍ: Es como un CONTRATO que dice:
   "Si quieres ser una Figura, DEBES tener área y perímetro"
   No puedes crear una "Figura" genérica, debe ser específica (círculo, cuadrado...)
"""

from abc import ABC, abstractmethod

class Figura(ABC):  # ABC = Abstract Base Class
    """No puedes crear objetos de esta clase directamente"""
    
    @abstractmethod
    def calcular_area(self):
        """OBLIGA a las clases hijas a implementar esto"""
        pass
    
    @abstractmethod
    def calcular_perimetro(self):
        pass

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado
    
    def calcular_area(self):
        return self.lado ** 2
    
    def calcular_perimetro(self):
        return 4 * self.lado

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    
    def calcular_area(self):
        return 3.1416 * (self.radio ** 2)
    
    def calcular_perimetro(self):
        return 2 * 3.1416 * self.radio

# ═══ CÓMO USAR ═══
cuadrado = Cuadrado(5)
circulo = Circulo(3)

print(f"Área del cuadrado: {cuadrado.calcular_area()}")      # 25
print(f"Perímetro del círculo: {circulo.calcular_perimetro():.2f}")  # 18.85

# ❌ NO PUEDES: figura = Figura()  <- Esto da ERROR


# ═══════════════════════════════════════════════════════════════════════
# 6. COMPOSICIÓN - OBJETOS DENTRO DE OBJETOS 📦
# ═══════════════════════════════════════════════════════════════════════

"""
🍎 PIENSA ASÍ: Una computadora TIENE un procesador, memoria, disco.
   No ES un procesador, lo CONTIENE.
"""

class Procesador:
    def __init__(self, marca, velocidad):
        self.marca = marca
        self.velocidad = velocidad
    
    def procesar(self):
        return f"Procesando a {self.velocidad} GHz"

class Computadora:
    def __init__(self, marca):
        self.marca = marca
        # La computadora TIENE un procesador (composición)
        self.procesador = Procesador("Intel", 3.5)
        self.encendida = False
    
    def encender(self):
        self.encendida = True
        return f"{self.marca} encendida. {self.procesador.procesar()}"

# ═══ CÓMO USAR ═══
mi_pc = Computadora("Dell")
print(mi_pc.encender())  # Dell encendida. Procesando a 3.5 GHz


# ═══════════════════════════════════════════════════════════════════════
# 7. LISTAS DE OBJETOS - GESTIONAR COLECCIONES 📚
# ═══════════════════════════════════════════════════════════════════════

"""
🍎 PIENSA ASÍ: Un salón de clases tiene MUCHOS estudiantes.
   Necesitas poder agregarlos, buscarlos, sacar promedios, etc.
"""

class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.notas = []
    
    def agregar_nota(self, nota):
        self.notas.append(nota)
    
    def promedio(self):
        if not self.notas:
            return 0
        return sum(self.notas) / len(self.notas)

class Salon:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = []  # Lista para guardar estudiantes
    
    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
        return f"{estudiante.nombre} agregado al salón"
    
    def buscar_estudiante(self, nombre):
        for est in self.estudiantes:
            if est.nombre == nombre:
                return est
        return None
    
    def promedio_salon(self):
        promedios = [e.promedio() for e in self.estudiantes]
        if not promedios:
            return 0
        return sum(promedios) / len(promedios)
    
    def listar_estudiantes(self):
        return [e.nombre for e in self.estudiantes]

# ═══ CÓMO USAR ═══
salon = Salon("Biología 101")

# Agregar estudiantes
ana = Estudiante("Ana", 20)
ana.agregar_nota(85)
ana.agregar_nota(90)

luis = Estudiante("Luis", 21)
luis.agregar_nota(75)
luis.agregar_nota(80)

salon.agregar_estudiante(ana)
salon.agregar_estudiante(luis)

# Buscar
print(salon.buscar_estudiante("Ana").promedio())  # 87.5

# Listar todos
print(salon.listar_estudiantes())  # ['Ana', 'Luis']

# Promedio general
print(f"Promedio del salón: {salon.promedio_salon()}")  # 82.5


# ═══════════════════════════════════════════════════════════════════════
# 8. BIOINFORMÁTICA - SECUENCIAS DE ADN 🧬
# ═══════════════════════════════════════════════════════════════════════

"""
🍎 PIENSA ASÍ: El ADN es como un libro escrito con solo 4 letras: A, T, G, C
   Necesitas poder leerlo, traducirlo, buscar palabras específicas, etc.
"""

class SecuenciaADN:
    """Para trabajar con cadenas de ADN"""
    
    def __init__(self, secuencia):
        self.secuencia = secuencia.upper()
        self._validar()
    
    def _validar(self):
        """Verificar que solo tenga A, T, G, C"""
        validos = set('ATGC')
        if not all(letra in validos for letra in self.secuencia):
            raise ValueError("❌ ERROR: Solo se permiten A, T, G, C")
    
    def complemento(self):
        """
        🍎 La hebra complementaria:
           A ↔ T
           G ↔ C
        """
        complementos = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
        return ''.join(complementos[n] for n in self.secuencia)
    
    def reverso_complemento(self):
        """
        🍎 Complemento al revés (hebra antisentido)
           ATGC → complemento: TACG → reverso: GCTA
        """
        return self.complemento()[::-1]
    
    def transcribir_a_arn(self):
        """
        🍎 Convertir ADN a ARN (cambiar T por U)
           ADN: ATGC → ARN: AUGC
        """
        return self.secuencia.replace('T', 'U')
    
    def contenido_gc(self):
        """
        🍎 Porcentaje de G y C (importante en biología)
           Más GC = enlaces más fuertes
        """
        gc = self.secuencia.count('G') + self.secuencia.count('C')
        return (gc / len(self.secuencia)) * 100
    
    def buscar_motivo(self, motivo):
        """
        🍎 Encontrar un patrón específico en la secuencia
           Como buscar una palabra en un libro
        """
        posiciones = []
        motivo = motivo.upper()
        for i in range(len(self.secuencia) - len(motivo) + 1):
            if self.secuencia[i:i+len(motivo)] == motivo:
                posiciones.append(i)
        return posiciones
    
    def contar_nucleotidos(self):
        """🍎 Contar cuántas veces aparece cada letra"""
        return {
            'A': self.secuencia.count('A'),
            'T': self.secuencia.count('T'),
            'G': self.secuencia.count('G'),
            'C': self.secuencia.count('C')
        }
    
    def __len__(self):
        return len(self.secuencia)
    
    def __str__(self):
        return f"ADN: {self.secuencia} | Longitud: {len(self)} | GC: {self.contenido_gc():.1f}%"

# ═══ CÓMO USAR ═══
adn = SecuenciaADN("ATGCGATCGATCG")

print(adn)                              # ADN: ATGCGATCGATCG | Longitud: 13 | GC: 53.8%
print(f"Complemento: {adn.complemento()}")  # TACGCTAGCTAGC
print(f"ARN: {adn.transcribir_a_arn()}")   # AUGCGAUCGAUCG

# Buscar un patrón
posiciones = adn.buscar_motivo("ATC")
print(f"El motivo ATC está en las posiciones: {posiciones}")  # [5, 9]

# Contar nucleótidos
conteo = adn.contar_nucleotidos()
print(f"Conteo: {conteo}")  # {'A': 4, 'T': 3, 'G': 4, 'C': 2}


# ═══════════════════════════════════════════════════════════════════════
# 9. BIOINFORMÁTICA - TRADUCCIÓN A PROTEÍNAS 🧬→🧪
# ═══════════════════════════════════════════════════════════════════════

"""
🍎 PIENSA ASÍ: El ARN se lee en grupos de 3 letras (codones).
   Cada codón es como una "palabra" que representa un aminoácido.
"""

class Traductor:
    """Traduce ARN a secuencia de aminoácidos"""
    
    # Tabla genética (codón → aminoácido)
    CODIGO_GENETICO = {
        'AUG': 'M', 'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
        'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
        'UAU': 'Y', 'UAC': 'Y', 'UAA': '*', 'UAG': '*', 'UGA': '*',
        'UGU': 'C', 'UGC': 'C', 'UGG': 'W',
        'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
        'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
        'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
        'AUU': 'I', 'AUC': 'I', 'AUA': 'I',
        'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
        'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
        'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
        'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
        'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
        'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
        'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
    }
    
    @classmethod
    def traducir(cls, secuencia_arn):
        """
        🍎 Lee el ARN de 3 en 3 y traduce a aminoácidos
           AUGCCCUAA → AUG=M, CCC=P, UAA=* (stop)
        """
        proteina = []
        
        # Leer de 3 en 3 (codones)
        for i in range(0, len(secuencia_arn) - 2, 3):
            codon = secuencia_arn[i:i+3]
            aminoacido = cls.CODIGO_GENETICO.get(codon, 'X')
            
            if aminoacido == '*':  # Codón de parada
                break
            
            proteina.append(aminoacido)
        
        return ''.join(proteina)
    
    @classmethod
    def traducir_desde_adn(cls, adn):
        """🍎 Atajo: ADN → ARN → Proteína"""
        sec_adn = SecuenciaADN(adn)
        arn = sec_adn.transcribir_a_arn()
        return cls.traducir(arn)

# ═══ CÓMO USAR ═══
# Desde ARN
arn = "AUGUUUGGCUAA"
proteina = Traductor.traducir(arn)
print(f"ARN: {arn}")
print(f"Proteína: {proteina}")  # MFG (Metionina-Fenilalanina-Glicina)

# Desde ADN directamente
adn = "ATGTTTGGCTAA"
proteina2 = Traductor.traducir_desde_adn(adn)
print(f"Desde ADN {adn}: {proteina2}")


# ═══════════════════════════════════════════════════════════════════════
# 10. COMPARAR SECUENCIAS - ALINEAMIENTO 📊
# ═══════════════════════════════════════════════════════════════════════

"""
🍎 PIENSA ASÍ: Quieres saber qué tan parecidas son dos secuencias.
   Como comparar dos frases para ver cuántas letras coinciden.
"""

class Comparador:
    
    @staticmethod
    def distancia_hamming(seq1, seq2):
        """
        🍎 Cuenta cuántas posiciones son DIFERENTES
           ATGC vs ATGG → 1 diferencia (C vs G en posición 3)
        """
        if len(seq1) != len(seq2):
            raise ValueError("❌ Las secuencias deben tener la misma longitud")
        
        diferencias = sum(c1 != c2 for c1, c2 in zip(seq1, seq2))
        return diferencias
    
    @staticmethod
    def similitud_porcentaje(seq1, seq2):
        """
        🍎 Calcula el % de letras que coinciden
           ATGC vs ATGC → 100%
           ATGC vs ATGA → 75%
        """
        # Ajustar a la longitud más corta
        min_len = min(len(seq1), len(seq2))
        seq1, seq2 = seq1[:min_len], seq2[:min_len]
        
        coincidencias = sum(c1 == c2 for c1, c2 in zip(seq1, seq2))
        return (coincidencias / min_len) * 100
    
    @staticmethod
    def encontrar_subsecuencia_comun(seq1, seq2):
        """
        🍎 Encuentra la subsecuencia común más larga
           ATGCGAT y GCGATC → GCGAT
        """
        m, n = len(seq1), len(seq2)
        mejor = ""
        
        for i in range(m):
            for j in range(i+1, m+1):
                subsec = seq1[i:j]
                if subsec in seq2 and len(subsec) > len(mejor):
                    mejor = subsec
        
        return mejor

# ═══ CÓMO USAR ═══
seq1 = "ATGCGATCG"
seq2 = "ATGCGATAG"

# Distancia de Hamming
distancia = Comparador.distancia_hamming(seq1, seq2)
print(f"Diferencias entre secuencias: {distancia}")  # 1

# Similitud
similitud = Comparador.similitud_porcentaje(seq1, seq2)
print(f"Similitud: {similitud:.1f}%")  # 88.9%

# Subsecuencia común
seq3 = "GCGATCGATAA"
seq4 = "ATCGATCG"
comun = Comparador.encontrar_subsecuencia_comun(seq3, seq4)
print(f"Subsecuencia común más larga: {comun}")  # CGATCG


# ═══════════════════════════════════════════════════════════════════════
# 11. EXCEPCIONES - MANEJO DE ERRORES ⚠️
# ═══════════════════════════════════════════════════════════════════════

"""
🍎 PIENSA ASÍ: Las excepciones son como alarmas cuando algo sale mal.
   En lugar de que el programa explote, TÚ decides qué hacer.
"""

class ErrorSecuencia(Exception):
    """Excepción personalizada"""
    pass

def validar_secuencia(secuencia):
    """Ejemplo de manejo de errores"""
    try:
        adn = SecuenciaADN(secuencia)
        return f"✅ Secuencia válida: {adn}"
    except ValueError as e:
        return f"❌ Error: {e}"
    except Exception as e:
        return f"❌ Error inesperado: {e}"

# ═══ CÓMO USAR ═══
print(validar_secuencia("ATGC"))      # ✅ Secuencia válida
print(validar_secuencia("ATXC"))      # ❌ Error: Solo se permiten A, T, G, C


# ═══════════════════════════════════════════════════════════════════════
# 12. MÉTODOS ESTÁTICOS Y DE CLASE 🔧
# ═══════════════════════════════════════════════════════════════════════

"""
🍎 PIENSA ASÍ:
   - Método normal: Necesitas UN objeto específico (firulais.ladrar())
   - Método estático: NO necesitas objeto, es una herramienta general
   - Método de clase: Trabaja con la clase entera, no con un objeto
"""

class Utilidades:
    
    @staticmethod
    def es_palindromo(secuencia):
        """
        🍎 Método estático: Lo usas SIN crear un objeto
           Verificar si una secuencia es igual al revés
        """
        return secuencia == secuencia[::-1]
    
    @staticmethod
    def contar_caracteres(texto, caracter):
        """🍎 Otra herramienta útil"""
        return texto.count(caracter)

class SecuenciaConContador:
    contador_total = 0  # Variable de clase
    
    def __init__(self, secuencia):
        self.secuencia = secuencia
        SecuenciaConContador.contador_total += 1
    
    @classmethod
    def obtener_total(cls):
        """🍎 Método de clase: Accede a variables de clase"""
        return f"Total de secuencias creadas: {cls.contador_total}"
    
    @classmethod
    def crear_desde_archivo(cls, texto):
        """🍎 Constructor alternativo"""
        return cls(texto.strip().upper())

# ═══ CÓMO USAR ═══
# Método estático (SIN objeto)
print(Utilidades.es_palindromo("ATGCGTA"))  # False
print(Utilidades.es_palindromo("ATCGCTA"))  # False
print(Utilidades.contar_caracteres("ATGCGATCG", "G"))  # 3

# Método de clase
s1 = SecuenciaConContador("ATGC")
s2 = SecuenciaConContador("GCTA")
print(SecuenciaConContador.obtener_total())  # Total de secuencias creadas: 2


# ═══════════════════════════════════════════════════════════════════════
# 13. EJEMPLO COMPLETO - ANALIZADOR DE GENOMA 🧬🔬
# ═══════════════════════════════════════════════════════════════════════

"""
🍎 ESTO ES TODO JUNTO: Un programa real que use varios conceptos
"""