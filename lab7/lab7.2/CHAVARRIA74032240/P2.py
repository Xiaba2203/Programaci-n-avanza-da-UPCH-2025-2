# Clase base para objetos geometricos
class GeometricObject:
    def __init__(self, color="verde", filled=True):
        # guardar color recibido
        self.color = color
        # guardar relleno recibido
        self.filled = filled

    def __str__(self):
        # mostrar color y relleno
        return f"Color: {self.color}, Relleno: {self.filled}"


# Clase Circulo 
class Circulo(GeometricObject):
    def __init__(self, radio):
        # llamar constructor padre
        super().__init__()
        # guardar radio
        self.radio = radio

    def imprimirCirculo(self):
        # imprimir info del padre
        print(super().__str__())
        # imprimir radio
        print(f"Radio: {self.radio}")

    def __str__(self):
        # mostrar info heredada + radio
        return f"{super().__str__()}, Radio: {self.radio}"


# Clase Rectangulo
class Rectangulo(GeometricObject):
    def __init__(self, ancho, alto):
        # llamar constructor padre
        super().__init__()
        # guardar ancho
        self.ancho = ancho
        # guardar alto
        self.alto = alto

    def __str__(self):
        # mostrar info heredada + dimensiones
        return f"{super().__str__()}, Ancho: {self.ancho}, Alto: {self.alto}"
