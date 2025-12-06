import tkinter as tk
import math

# ==================== CLASE BASE ANIMACION ====================
class Animacion:
    """Clase base para todas las animaciones"""
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.activo = True
    
    def animar(self):
        """Método que debe ser sobreescrito por cada animación"""
        pass
    
    def detener(self):
        """Detiene la animación"""
        self.activo = False

# ==================== MOVIMIENTO CIRCULAR ====================
class MovimientoCircular(Animacion):
    """Objeto que se mueve en círculo"""
    def __init__(self, canvas, centro_x, centro_y, radio=100, velocidad=2):
        super().__init__(canvas, centro_x, centro_y)
        self.radio = radio
        self.angulo = 0
        self.velocidad = velocidad
        # Crear objeto
        self.objeto = canvas.create_oval(0, 0, 20, 20, fill="red")
    
    def animar(self):
        if not self.activo:
            return
        
        # Calcular nueva posición
        rad = math.radians(self.angulo)
        x = self.x + self.radio * math.cos(rad)
        y = self.y + self.radio * math.sin(rad)
        
        # Actualizar objeto
        self.canvas.coords(self.objeto, x-10, y-10, x+10, y+10)
        
        # Incrementar ángulo
        self.angulo += self.velocidad
        if self.angulo >= 360:
            self.angulo = 0
        
        # Continuar animación
        self.canvas.after(20, self.animar)

# ==================== PENDULO ====================
class Pendulo(Animacion):
    """Péndulo oscilante"""
    def __init__(self, canvas, pivote_x, pivote_y, longitud=200, angulo_inicial=45):
        super().__init__(canvas, pivote_x, pivote_y)
        self.longitud = longitud
        self.angulo = angulo_inicial
        self.velocidad_angular = 0
        
        # Crear cuerda y bola
        self.cuerda = canvas.create_line(pivote_x, pivote_y, pivote_x, pivote_y+longitud, width=2)
        self.bola = canvas.create_oval(0, 0, 20, 20, fill="blue")
    
    def animar(self):
        if not self.activo:
            return
        
        # Física del péndulo
        rad = math.radians(self.angulo)
        bola_x = self.x + self.longitud * math.sin(rad)
        bola_y = self.y + self.longitud * math.cos(rad)
        
        # Actualizar cuerda y bola
        self.canvas.coords(self.cuerda, self.x, self.y, bola_x, bola_y)
        self.canvas.coords(self.bola, bola_x-10, bola_y-10, bola_x+10, bola_y+10)
        
        # Física
        self.velocidad_angular += -0.3 * math.sin(rad)
        self.angulo += self.velocidad_angular
        self.velocidad_angular *= 0.999  # Amortiguamiento
        
        # Continuar
        self.canvas.after(20, self.animar)

# ==================== MOVIMIENTO LINEAL ====================
class MovimientoLineal(Animacion):
    """Objeto que se mueve en línea recta"""
    def __init__(self, canvas, x, y, velocidad_x=3, velocidad_y=0):
        super().__init__(canvas, x, y)
        self.velocidad_x = velocidad_x
        self.velocidad_y = velocidad_y
        self.objeto = canvas.create_rectangle(x, y, x+30, y+30, fill="green")
    
    def animar(self):
        if not self.activo:
            return
        
        # Mover objeto
        self.canvas.move(self.objeto, self.velocidad_x, self.velocidad_y)
        
        # Obtener posición actual
        coords = self.canvas.coords(self.objeto)
        
        # Reiniciar si sale del canvas
        if coords[0] > 600:
            self.canvas.coords(self.objeto, -30, coords[1], 0, coords[3])
        
        self.canvas.after(20, self.animar)

# ==================== REBOTE ====================
class Rebote(Animacion):
    """Objeto que rebota en los bordes"""
    def __init__(self, canvas, x, y, velocidad_x=5, velocidad_y=3):
        super().__init__(canvas, x, y)
        self.velocidad_x = velocidad_x
        self.velocidad_y = velocidad_y
        self.objeto = canvas.create_oval(x, y, x+30, y+30, fill="purple")
    
    def animar(self):
        if not self.activo:
            return
        
        # Mover
        self.canvas.move(self.objeto, self.velocidad_x, self.velocidad_y)
        
        # Obtener posición
        coords = self.canvas.coords(self.objeto)
        
        # Rebotar en bordes
        if coords[2] >= 600 or coords[0] <= 0:
            self.velocidad_x = -self.velocidad_x
        if coords[3] >= 400 or coords[1] <= 0:
            self.velocidad_y = -self.velocidad_y
        
        self.canvas.after(20, self.animar)

# ==================== CAMBIO DE COLOR ====================
class CambioColor(Animacion):
    """Objeto que cambia de color automáticamente"""
    def __init__(self, canvas, x, y, colores=None):
        super().__init__(canvas, x, y)
        self.colores = colores or ["red", "blue", "green", "yellow", "purple", "orange"]
        self.indice = 0
        self.objeto = canvas.create_rectangle(x, y, x+80, y+80, fill=self.colores[0], outline="black", width=2)
    
    def animar(self):
        if not self.activo:
            return
        
        # Cambiar color
        self.indice = (self.indice + 1) % len(self.colores)
        self.canvas.itemconfig(self.objeto, fill=self.colores[self.indice])
        
        # Continuar cada 1 segundo
        self.canvas.after(1000, self.animar)

# ==================== TEMPORIZADOR ====================
class Temporizador:
    """Temporizador visual que cuenta hacia atrás"""
    def __init__(self, canvas, x, y, segundos=10):
        self.canvas = canvas
        self.segundos_restantes = segundos
        self.segundos_iniciales = segundos
        self.activo = True
        
        # Crear texto
        self.texto = canvas.create_text(x, y, text=f"{segundos}s", 
                                       font=("Arial", 30, "bold"), fill="red")
    
    def iniciar(self):
        self._contar()
    
    def _contar(self):
        if not self.activo or self.segundos_restantes <= 0:
            self.canvas.itemconfig(self.texto, text="¡Tiempo!", fill="green")
            return
        
        # Actualizar texto
        self.canvas.itemconfig(self.texto, text=f"{self.segundos_restantes}s")
        self.segundos_restantes -= 1
        
        # Continuar cada 1 segundo
        self.canvas.after(1000, self._contar)
    
    def reiniciar(self):
        self.segundos_restantes = self.segundos_iniciales
        self.activo = True
        self._contar()

# ==================== APLICACION PRINCIPAL ====================
class AplicacionAnimaciones:
    """Aplicación que muestra todas las animaciones"""
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Animaciones Base - POO")
        
        # Canvas
        self.canvas = tk.Canvas(self.ventana, width=600, height=400, bg="lightblue")
        self.canvas.pack()
        
        # Frame de botones
        frame = tk.Frame(self.ventana)
        frame.pack()
        
        # Botones para crear animaciones
        tk.Button(frame, text="Movimiento Circular", command=self.crear_circular).pack(side=tk.LEFT, padx=5)
        tk.Button(frame, text="Péndulo", command=self.crear_pendulo).pack(side=tk.LEFT, padx=5)
        tk.Button(frame, text="Lineal", command=self.crear_lineal).pack(side=tk.LEFT, padx=5)
        tk.Button(frame, text="Rebote", command=self.crear_rebote).pack(side=tk.LEFT, padx=5)
        tk.Button(frame, text="Cambio Color", command=self.crear_color).pack(side=tk.LEFT, padx=5)
        tk.Button(frame, text="Temporizador", command=self.crear_temporizador).pack(side=tk.LEFT, padx=5)
        
        self.animaciones = []
    
    def crear_circular(self):
        anim = MovimientoCircular(self.canvas, 150, 200)
        self.animaciones.append(anim)
        anim.animar()
    
    def crear_pendulo(self):
        anim = Pendulo(self.canvas, 300, 50)
        self.animaciones.append(anim)
        anim.animar()
    
    def crear_lineal(self):
        anim = MovimientoLineal(self.canvas, 0, 100)
        self.animaciones.append(anim)
        anim.animar()
    
    def crear_rebote(self):
        anim = Rebote(self.canvas, 300, 200)
        self.animaciones.append(anim)
        anim.animar()
    
    def crear_color(self):
        anim = CambioColor(self.canvas, 450, 150)
        self.animaciones.append(anim)
        anim.animar()
    
    def crear_temporizador(self):
        temp = Temporizador(self.canvas, 500, 50, segundos=5)
        temp.iniciar()
    
    def ejecutar(self):
        self.ventana.mainloop()

# ==================== EJECUTAR ====================
if __name__ == "__main__":
    app = AplicacionAnimaciones()
    app.ejecutar()

# ==================== CÓMO USAR ====================
# 1. Ejecuta el programa
# 2. Click en los botones para crear diferentes animaciones
# 3. Puedes crear múltiples animaciones al mismo tiempo
#
# PARA TU EXAMEN:
# - Usa MovimientoCircular para objetos en círculo
# - Usa Pendulo para péndulos
# - Usa Rebote para pelotas que rebotan
# - Usa CambioColor para cambios de color automáticos
# - Modifica velocidad, colores, tamaños en __init__