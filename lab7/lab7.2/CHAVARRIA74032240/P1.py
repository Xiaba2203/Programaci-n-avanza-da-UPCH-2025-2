# Clase base para multimedia
class Multimedia:
    def __init__(self, titulo, autor, formato, duracion):
        # guardar atributos recibidos
        self.titulo = titulo
        self.autor = autor
        self.formato = formato
        self.duracion = duracion

    def get_titulo(self):
        # devolver titulo
        return self.titulo

    def get_autor(self):
        # devolver autor
        return self.autor

    def get_formato(self):
        # devolver formato
        return self.formato

    def get_duracion(self):
        # devolver duracion
        return self.duracion

    def __str__(self):
        # mostrar toda la info
        return f"Título: {self.titulo}, Autor: {self.autor}, Formato: {self.formato}, Duración: {self.duracion}"

    def equals(self, other):
        # comparar titulo y autor
        if not isinstance(other, Multimedia):
            return False
        return self.titulo == other.titulo and self.autor == other.autor


# Clase Pelicula 
class Pelicula(Multimedia):
    def __init__(self, titulo, autor, formato, duracion, actor_principal=None, actriz_principal=None):
        # llamar constructor de Multimedia
        super().__init__(titulo, autor, formato, duracion)
        # al menos un actor o actriz
        if actor_principal is None and actriz_principal is None:
            raise ValueError("Debe existir un actor o actriz")
        # guardar actores
        self.actor_principal = actor_principal
        self.actriz_principal = actriz_principal

    def get_actor_principal(self):
        # devolver actor principal
        return self.actor_principal

    def get_actriz_principal(self):
        # devolver actriz principal
        return self.actriz_principal

    def __str__(self):
        # mostrar info heredada + actores
        base = super().__str__()
        return f"{base}, Actor Principal: {self.actor_principal}, Actriz Principal: {self.actriz_principal}"


# Clase ListaMultimedia
class ListaMultimedia:
    def __init__(self, max_size):
        # tamaño maximo de la lista
        self.max_size = max_size
        # lista vacia
        self.lista = []
        # contador de objetos
        self.count = 0

    def size(self):
        # devolver cuantos objetos hay
        return self.count

    def add(self, m: Multimedia):
        # agregar objeto si hay espacio
        if self.count < self.max_size:
            self.lista.append(m)
            self.count += 1
            return True
        return False

    def get(self, posicion):
        # devolver objeto en posicion
        if 0 <= posicion < self.count:
            return self.lista[posicion]
        return None

    def indexOf(self, m: Multimedia):
        # buscar objeto en la lista
        for i, obj in enumerate(self.lista):
            if obj.equals(m):
                return i
        return -1

    def __str__(self):
        # mostrar todos los objetos
        return "\n".join(str(obj) for obj in self.lista)
