#Utilizando POO para modelar un robot que se mueve en una cuadrícula 2D

class Robot:
    
    #Se incializa el robot en una posición y una dirección dada por el usuario
    def __init__(self, x, y, direccion):
        self.x = x
        self.y = y
        self.direccion = direccion
        self.historial = [(x, y)]
        self.direcciones = ["norte", "este", "sur", "oeste"]
    
    #Agregamos metodos para girar y mover al robot
    def girar_derecha(self):
        indice = self.direcciones.index(self.direccion)
        self.direccion = self.direcciones[(indice + 1) % 4]
    
    def girar_izquierda(self):
        indice = self.direcciones.index(self.direccion)
        self.direccion = self.direcciones[(indice - 1) % 4]
    
    def avanzar(self):
        if self.direccion == "norte":
            self.y += 1
        elif self.direccion == "sur":
            self.y -= 1
        elif self.direccion == "este":
            self.x += 1
        elif self.direccion == "oeste":
            self.x -= 1
        
        self.historial.append((self.x, self.y)) #Guardamos las posiciones en un historial
    
    #Uso una función para obtener la posición y dirección actual del robot
    def obtener_posicion(self):
        return (self.x, self.y)
    
    def obtener_direccion(self):
        return self.direccion
    
    def obtener_historial(self):
        return self.historial
    
    def reiniciar(self, x, y, direccion):
        self.x = x
        self.y = y
        self.direccion = direccion
        self.historial = [(x, y)]