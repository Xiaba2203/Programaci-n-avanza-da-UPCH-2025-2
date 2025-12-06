import tkinter as tk
import random

# ==================== CLASE OBJETO INTERACTIVO ====================
class ObjetoInteractivo:
    """Objeto que responde a diferentes eventos del mouse"""
    def __init__(self, canvas, x, y, tamaño=50):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.tamaño = tamaño
        
        # Colores
        self.color_normal = "blue"
        self.color_hover = "lightblue"
        self.color_click = "red"
        self.color_derecho = "green"
        
        # Crear objeto
        self.id = canvas.create_rectangle(
            x, y, x+tamaño, y+tamaño,
            fill=self.color_normal, outline="black", width=2
        )
        
        # Estado
        self.eliminado = False
        
        # Vincular eventos
        self._vincular_eventos()
    
    def _vincular_eventos(self):
        """Vincula todos los eventos del mouse"""
        # Mouse over (hover)
        self.canvas.tag_bind(self.id, "<Enter>", self.mouse_entra)
        self.canvas.tag_bind(self.id, "<Leave>", self.mouse_sale)
        
        # Click izquierdo
        self.canvas.tag_bind(self.id, "<Button-1>", self.click_izquierdo)
        
        # Click derecho
        self.canvas.tag_bind(self.id, "<Button-3>", self.click_derecho)
        
        # Doble click
        self.canvas.tag_bind(self.id, "<Double-Button-1>", self.doble_click)
    
    def mouse_entra(self, evento):
        """Cuando el mouse entra al objeto (hover)"""
        if not self.eliminado:
            self.canvas.itemconfig(self.id, fill=self.color_hover)
    
    def mouse_sale(self, evento):
        """Cuando el mouse sale del objeto"""
        if not self.eliminado:
            self.canvas.itemconfig(self.id, fill=self.color_normal)
    
    def click_izquierdo(self, evento):
        """Click izquierdo - cambiar color"""
        if not self.eliminado:
            self.color_normal = self.color_click
            self.canvas.itemconfig(self.id, fill=self.color_click)
    
    def click_derecho(self, evento):
        """Click derecho - otro color"""
        if not self.eliminado:
            self.color_normal = self.color_derecho
            self.canvas.itemconfig(self.id, fill=self.color_derecho)
    
    def doble_click(self, evento):
        """Doble click - borrar"""
        if not self.eliminado:
            self.canvas.delete(self.id)
            self.eliminado = True

# ==================== CLASE CIRCULO INTERACTIVO ====================
class CirculoInteractivo(ObjetoInteractivo):
    """Círculo con eventos de mouse"""
    def __init__(self, canvas, x, y, radio=30):
        self.radio = radio
        self.canvas = canvas
        self.x = x
        self.y = y
        self.tamaño = radio * 2
        
        # Colores
        self.color_normal = "purple"
        self.color_hover = "pink"
        self.color_click = "orange"
        self.color_derecho = "yellow"
        
        # Crear círculo
        self.id = canvas.create_oval(
            x-radio, y-radio, x+radio, y+radio,
            fill=self.color_normal, outline="black", width=2
        )
        
        self.eliminado = False
        self._vincular_eventos()

# ==================== CLASE OBJETO CON CICLO DE COLORES ====================
class ObjetoConCiclo:
    """Objeto que cicla entre varios colores con cada click"""
    def __init__(self, canvas, x, y, tamaño=60):
        self.canvas = canvas
        self.colores = ["red", "orange", "yellow", "green", "blue", "purple"]
        self.indice_color = 0
        
        # Crear objeto
        self.id = canvas.create_oval(
            x, y, x+tamaño, y+tamaño,
            fill=self.colores[0], outline="black", width=3
        )
        
        # Vincular click
        self.canvas.tag_bind(self.id, "<Button-1>", self.siguiente_color)
    
    def siguiente_color(self, evento):
        """Cambia al siguiente color en el ciclo"""
        self.indice_color = (self.indice_color + 1) % len(self.colores)
        self.canvas.itemconfig(self.id, fill=self.colores[self.indice_color])

# ==================== CLASE OBJETO ALEATORIO ====================
class ObjetoAleatorio:
    """Objeto que cambia a color aleatorio con click"""
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        
        # Crear objeto
        self.id = canvas.create_rectangle(
            x, y, x+70, y+70,
            fill="gray", outline="black", width=2
        )
        
        # Vincular eventos
        self.canvas.tag_bind(self.id, "<Button-1>", self.color_aleatorio)
        self.canvas.tag_bind(self.id, "<Button-3>", self.tamaño_aleatorio)
    
    def color_aleatorio(self, evento):
        """Genera un color aleatorio"""
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = f'#{r:02x}{g:02x}{b:02x}'
        self.canvas.itemconfig(self.id, fill=color)
    
    def tamaño_aleatorio(self, evento):
        """Cambia el tamaño aleatoriamente"""
        coords = self.canvas.coords(self.id)
        centro_x = (coords[0] + coords[2]) / 2
        centro_y = (coords[1] + coords[3]) / 2
        nuevo_tamaño = random.randint(30, 100)
        
        self.canvas.coords(self.id,
                          centro_x - nuevo_tamaño/2,
                          centro_y - nuevo_tamaño/2,
                          centro_x + nuevo_tamaño/2,
                          centro_y + nuevo_tamaño/2)

# ==================== APLICACION PRINCIPAL ====================
class AplicacionColoresEventos:
    """Aplicación que demuestra todos los eventos de colores"""
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Colores y Eventos - POO")
        
        # Canvas
        self.canvas = tk.Canvas(self.ventana, width=800, height=600, bg="lightgray")
        self.canvas.pack()
        
        # Crear objetos de ejemplo
        self._crear_ejemplos()
        
        # Instrucciones
        self._crear_instrucciones()
    
    def _crear_ejemplos(self):
        """Crea objetos de ejemplo"""
        # Fila 1: Objetos con hover y clicks
        ObjetoInteractivo(self.canvas, 50, 50)
        ObjetoInteractivo(self.canvas, 150, 50)
        ObjetoInteractivo(self.canvas, 250, 50)
        
        # Fila 2: Círculos interactivos
        CirculoInteractivo(self.canvas, 100, 200)
        CirculoInteractivo(self.canvas, 200, 200)
        CirculoInteractivo(self.canvas, 300, 200)
        
        # Fila 3: Objetos con ciclo de colores
        ObjetoConCiclo(self.canvas, 50, 320)
        ObjetoConCiclo(self.canvas, 150, 320)
        ObjetoConCiclo(self.canvas, 250, 320)
        
        # Fila 4: Objetos aleatorios
        ObjetoAleatorio(self.canvas, 50, 450)
        ObjetoAleatorio(self.canvas, 150, 450)
        ObjetoAleatorio(self.canvas, 250, 450)
    
    def _crear_instrucciones(self):
        """Crea el panel de instrucciones"""
        frame_info = tk.Frame(self.ventana, bg="white", relief=tk.RAISED, bd=2)
        frame_info.place(x=420, y=50, width=350, height=500)
        
        tk.Label(frame_info, text="INSTRUCCIONES", font=("Arial", 16, "bold"),
                bg="white").pack(pady=10)
        
        instrucciones = [
            ("CUADRADOS AZULES (arriba):", "black"),
            ("• Hover: Cambia a celeste", "blue"),
            ("• Click izq: Cambia a rojo", "red"),
            ("• Click der: Cambia a verde", "green"),
            ("• Doble click: Borra", "darkred"),
            ("", "black"),
            ("CÍRCULOS MORADOS (medio):", "black"),
            ("• Mismo comportamiento", "purple"),
            ("", "black"),
            ("CÍRCULOS ARCOIRIS (abajo-izq):", "black"),
            ("• Click: Cicla entre colores", "orange"),
            ("", "black"),
            ("CUADRADOS GRISES (abajo):", "black"),
            ("• Click izq: Color aleatorio", "blue"),
            ("• Click der: Tamaño aleatorio", "green"),
        ]
        
        for texto, color in instrucciones:
            tk.Label(frame_info, text=texto, font=("Arial", 10),
                    fg=color, bg="white", anchor="w").pack(fill=tk.X, padx=10)
        
        # Botón para crear nuevo objeto
        tk.Button(frame_info, text="Crear Cuadrado Interactivo",
                 command=self.crear_nuevo_cuadrado, bg="lightblue").pack(pady=10)
        
        tk.Button(frame_info, text="Crear Círculo Interactivo",
                 command=self.crear_nuevo_circulo, bg="lightgreen").pack(pady=5)
    
    def crear_nuevo_cuadrado(self):
        """Crea un nuevo cuadrado en posición aleatoria"""
        x = random.randint(50, 350)
        y = random.randint(50, 500)
        ObjetoInteractivo(self.canvas, x, y)
    
    def crear_nuevo_circulo(self):
        """Crea un nuevo círculo en posición aleatoria"""
        x = random.randint(80, 370)
        y = random.randint(80, 520)
        CirculoInteractivo(self.canvas, x, y)
    
    def ejecutar(self):
        """Ejecuta la aplicación"""
        self.ventana.mainloop()

# ==================== EJECUTAR ====================
if __name__ == "__main__":
    app = AplicacionColoresEventos()
    app.ejecutar()

# ==================== CÓMO USAR ====================
# 1. Pasa el mouse sobre cualquier objeto (hover)
# 2. Click izquierdo para cambiar a un color
# 3. Click derecho para cambiar a otro color
# 4. Doble click para borrar el objeto
# 5. Usa los botones para crear más objetos
#
# PARA TU EXAMEN:
# - Esta clase tiene TODOS los eventos de mouse que pueden pedir
# - <Enter> = mouse entra (hover)
# - <Leave> = mouse sale
# - <Button-1> = click izquierdo
# - <Button-3> = click derecho
# - <Double-Button-1> = doble click
# - tag_bind() vincula eventos a objetos específicos
#
# MODIFICAR:
# - Cambia self.color_normal, self.color_hover, etc.
# - Agrega más colores en la lista de ObjetoConCiclo
# - Cambia tamaños en __init__
# - Puedes crear tu propia clase heredando de ObjetoInteractivo