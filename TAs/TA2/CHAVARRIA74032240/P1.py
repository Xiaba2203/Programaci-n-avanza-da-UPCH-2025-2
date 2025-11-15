import random  # DNI 74032240

class Pelicula:  # película con datos básicos
    """Representa una película con sus datos básicos."""
    
    def __init__(self, titulo, duracion, edad_minima, director):  # crea instancia película
        self.titulo = titulo  # guarda título
        self.duracion = duracion  # guarda duración en minutos
        self.edad_minima = edad_minima  # edad mínima permitida
        self.director = director  # guarda nombre del director
    
    def __str__(self):  # representación en texto
        return f"{self.titulo} ({self.duracion} min, +{self.edad_minima})"  # texto compacto


class Espectador:  # persona que va al cine
    """Representa un espectador del cine."""
    
    def __init__(self, nombre, edad, dinero):  # crea espectador
        self.nombre = nombre  # nombre del espectador
        self.edad = edad  # edad en años
        self.dinero = dinero  # dinero disponible
    
    def __str__(self):  # representación en texto
        return f"{self.nombre} ({self.edad} años, S/.{self.dinero})"  # texto compacto


class Asiento:  # asiento individual
    """Representa un asiento individual en la sala."""
    
    def __init__(self, fila, columna):  # crea asiento
        self.fila = fila  # número de fila
        self.columna = columna  # letra de columna
        self.ocupado = False  # libre por defecto
        self.espectador = None  # sin espectador
    
    def get_etiqueta(self):  # etiqueta tipo "5C"
        # generar etiqueta tipo "5C"
        return f"{self.fila}{self.columna}"  # devuelve etiqueta
    
    def ocupar(self, espectador):  # asigna espectador
        # asignar espectador al asiento
        self.ocupado = True  # marca como ocupado
        self.espectador = espectador  # guarda espectador
    
    def esta_libre(self):  # comprueba si está libre
        return not self.ocupado  # True si no ocupado


class Sala:  # sala de cine con asientos
    """Representa una sala de cine con asientos."""
    
    def __init__(self, numero, filas, columnas, pelicula, precio):  # crea sala
        self.numero = numero  # número de sala
        self.filas = filas  # cantidad de filas
        self.columnas = columnas  # cantidad de columnas
        self.pelicula = pelicula  # película en exhibición
        self.precio = precio  # precio del ticket
        self.asientos = []  # matriz de asientos
        self.espectadores_admitidos = []  # lista admitidos
        self.recaudacion = 0  # dinero recaudado
        
        # crear matriz de asientos
        letras = 'ABCDEFGHI'  # letras para columnas
        for f in range(filas, 0, -1):  # recorre filas de atrás adelante
            fila_asientos = []  # lista temporal fila
            for c in range(columnas):  # recorre columnas
                asiento = Asiento(f, letras[c])  # crea asiento
                fila_asientos.append(asiento)  # añade asiento
            self.asientos.append(fila_asientos)  # añade fila completa
    
    def buscar_asiento_libre(self):  # busca primer asiento libre
        # buscar primer asiento disponible
        for fila in self.asientos:  # para cada fila
            for asiento in fila:  # para cada asiento
                if asiento.esta_libre():  # si está libre
                    return asiento  # devuelve asiento libre
        return None  # no hay asientos libres
    
    def sentar_espectador(self, espectador):  # intenta sentar persona
        # verificar edad mínima
        if espectador.edad < self.pelicula.edad_minima:  # edad insuficiente
            return False  # no admitir
        
        # verificar dinero suficiente
        if espectador.dinero < self.precio:  # dinero insuficiente
            return False  # no admitir
        
        # buscar asiento libre
        asiento = self.buscar_asiento_libre()  # obtiene asiento libre
        if asiento is None:  # no hay asiento
            return False  # no admitir
        
        # sentar espectador
        asiento.ocupar(espectador)  # ocupa el asiento
        self.espectadores_admitidos.append(espectador)  # añade a lista
        self.recaudacion += self.precio  # suma al total
        return True  # ingreso exitoso
    
    def get_asientos_vacios(self):  # lista etiquetas vacías
        # obtener lista de asientos vacíos
        vacios = []  # inicia lista vacíos
        for fila in self.asientos:  # recorre filas
            for asiento in fila:  # recorre asientos
                if asiento.esta_libre():  # si está libre
                    vacios.append(asiento.get_etiqueta())  # añade etiqueta
        return vacios  # devuelve lista vacíos
    
    def get_menores_edad(self):  # espectadores menores de 18
        # obtener espectadores menores de 18
        return [e for e in self.espectadores_admitidos if e.edad < 18]  # filtra menores
    
    def get_espectador_menor(self):  # espectador más joven
        # espectador con menor edad
        if not self.espectadores_admitidos:  # sin espectadores
            return None  # devuelve None
        return min(self.espectadores_admitidos, key=lambda e: e.edad)  # menor por edad
    
    def get_espectador_mayor(self):  # espectador más viejo
        # espectador con mayor edad
        if not self.espectadores_admitidos:  # sin espectadores
            return None  # devuelve None
        return max(self.espectadores_admitidos, key=lambda e: e.edad)  # mayor por edad
    
    def contar_filas_llenas(self):  # contar filas completas
        # contar filas completamente ocupadas
        count = 0  # contador
        for fila in self.asientos:  # recorre filas
            if all(not a.esta_libre() for a in fila):  # si toda fila ocupada
                count += 1  # incrementa contador
        return count  # retorna número filas llenas