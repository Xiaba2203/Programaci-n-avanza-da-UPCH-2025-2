import tkinter as tk
from tkinter import messagebox

# ==================== CLASE FIGURA ====================
class Figura:
    """Clase base para todas las figuras"""
    def __init__(self, canvas, x1, y1, x2, y2, color, relleno):
        self.canvas = canvas
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color
        self.relleno = relleno
        self.id = None
        self.seleccionado = False
    
    def dibujar(self):
        """Debe ser sobreescrito por cada tipo de figura"""
        pass
    
    def seleccionar(self):
        """Marca la figura como seleccionada"""
        self.seleccionado = True
        self.canvas.itemconfig(self.id, width=4)
    
    def deseleccionar(self):
        """Desmarca la figura"""
        self.seleccionado = False
        self.canvas.itemconfig(self.id, width=2)
    
    def mover(self, dx, dy):
        """Mueve la figura"""
        self.canvas.move(self.id, dx, dy)
        self.x1 += dx
        self.y1 += dy
        self.x2 += dx
        self.y2 += dy
    
    def cambiar_tamaño(self, factor):
        """Cambia el tamaño de la figura"""
        centro_x = (self.x1 + self.x2) / 2
        centro_y = (self.y1 + self.y2) / 2
        ancho = (self.x2 - self.x1) * factor
        alto = (self.y2 - self.y1) * factor
        
        self.x1 = centro_x - ancho / 2
        self.y1 = centro_y - alto / 2
        self.x2 = centro_x + ancho / 2
        self.y2 = centro_y + alto / 2
        
        self.canvas.coords(self.id, self.x1, self.y1, self.x2, self.y2)
    
    def contiene_punto(self, x, y):
        """Verifica si un punto está dentro de la figura"""
        return self.x1 <= x <= self.x2 and self.y1 <= y <= self.y2
    
    def borrar(self):
        """Elimina la figura del canvas"""
        self.canvas.delete(self.id)

# ==================== CIRCULO ====================
class Circulo(Figura):
    """Círculo u óvalo"""
    def dibujar(self):
        if self.relleno:
            self.id = self.canvas.create_oval(self.x1, self.y1, self.x2, self.y2, 
                                             fill=self.color, outline="black", width=2)
        else:
            self.id = self.canvas.create_oval(self.x1, self.y1, self.x2, self.y2, 
                                             outline=self.color, width=2, fill="")
        return self.id

# ==================== RECTANGULO ====================
class Rectangulo(Figura):
    """Rectángulo o cuadrado"""
    def dibujar(self):
        if self.relleno:
            self.id = self.canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, 
                                                   fill=self.color, outline="black", width=2)
        else:
            self.id = self.canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, 
                                                   outline=self.color, width=2, fill="")
        return self.id

# ==================== LINEA ====================
class Linea(Figura):
    """Línea simple"""
    def dibujar(self):
        self.id = self.canvas.create_line(self.x1, self.y1, self.x2, self.y2, 
                                         fill=self.color, width=3)
        return self.id

# ==================== APLICACION DIBUJAR ====================
class AplicacionDibujar:
    """Aplicación completa para dibujar figuras"""
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Dibujar Figuras - POO")
        
        # Variables
        self.figura_actual = "circulo"
        self.color_actual = "blue"
        self.relleno_activo = tk.BooleanVar(value=True)
        self.figuras = []
        self.figura_seleccionada = None
        
        # Variables para dibujar
        self.x_inicio = None
        self.y_inicio = None
        self.figura_temporal = None
        
        # Variables para drag & drop
        self.arrastrando = False
        self.offset_x = 0
        self.offset_y = 0
        
        # Crear interfaz
        self._crear_menu()
        self._crear_canvas()
        self._crear_controles()
        self._vincular_eventos()
    
    def _crear_menu(self):
        """Crea el menú superior"""
        menubar = tk.Menu(self.ventana)
        self.ventana.config(menu=menubar)
        
        # Menú Archivo
        menu_archivo = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Archivo", menu=menu_archivo)
        menu_archivo.add_command(label="Limpiar todo", command=self.limpiar_todo)
        menu_archivo.add_separator()
        menu_archivo.add_command(label="Salir", command=self.ventana.quit)
        
        # Menú Editar
        menu_editar = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Editar", menu=menu_editar)
        menu_editar.add_command(label="Borrar seleccionada", command=self.borrar_seleccionada)
    
    def _crear_canvas(self):
        """Crea el canvas"""
        self.canvas = tk.Canvas(self.ventana, width=800, height=500, bg="white")
        self.canvas.pack(pady=10)
    
    def _crear_controles(self):
        """Crea los controles"""
        frame = tk.Frame(self.ventana)
        frame.pack()
        
        # Frame para elegir figura
        frame_figura = tk.LabelFrame(frame, text="Figura", padx=10, pady=5)
        frame_figura.grid(row=0, column=0, padx=5)
        
        tk.Button(frame_figura, text="Círculo", width=10, 
                 command=lambda: self.cambiar_figura("circulo")).pack(side=tk.LEFT, padx=2)
        tk.Button(frame_figura, text="Rectángulo", width=10, 
                 command=lambda: self.cambiar_figura("rectangulo")).pack(side=tk.LEFT, padx=2)
        tk.Button(frame_figura, text="Línea", width=10, 
                 command=lambda: self.cambiar_figura("linea")).pack(side=tk.LEFT, padx=2)
        
        # Frame para elegir color
        frame_color = tk.LabelFrame(frame, text="Color", padx=10, pady=5)
        frame_color.grid(row=0, column=1, padx=5)
        
        colores = [("Rojo", "red"), ("Azul", "blue"), ("Verde", "green"), 
                  ("Amarillo", "yellow"), ("Púrpura", "purple"), ("Negro", "black")]
        
        for texto, color in colores:
            tk.Button(frame_color, text=texto, bg=color, fg="white" if color != "yellow" else "black",
                     width=8, command=lambda c=color: self.cambiar_color(c)).pack(side=tk.LEFT, padx=2)
        
        # Frame para opciones
        frame_opciones = tk.LabelFrame(frame, text="Opciones", padx=10, pady=5)
        frame_opciones.grid(row=0, column=2, padx=5)
        
        tk.Checkbutton(frame_opciones, text="Relleno", variable=self.relleno_activo).pack()
        tk.Button(frame_opciones, text="Borrar seleccionada", 
                 command=self.borrar_seleccionada).pack(pady=2)
        tk.Button(frame_opciones, text="Agrandar", 
                 command=lambda: self.cambiar_tamaño_seleccionada(1.2)).pack(pady=2)
        tk.Button(frame_opciones, text="Achicar", 
                 command=lambda: self.cambiar_tamaño_seleccionada(0.8)).pack(pady=2)
        
        # Etiqueta de estado
        self.etiqueta_estado = tk.Label(self.ventana, text="Modo: Círculo | Color: Azul", 
                                       font=("Arial", 12))
        self.etiqueta_estado.pack()
    
    def _vincular_eventos(self):
        """Vincula eventos del mouse"""
        self.canvas.bind("<Button-1>", self.mouse_presionado)
        self.canvas.bind("<B1-Motion>", self.mouse_arrastrado)
        self.canvas.bind("<ButtonRelease-1>", self.mouse_soltado)
    
    def cambiar_figura(self, figura):
        """Cambia el tipo de figura a dibujar"""
        self.figura_actual = figura
        self.actualizar_estado()
    
    def cambiar_color(self, color):
        """Cambia el color actual"""
        self.color_actual = color
        self.actualizar_estado()
    
    def actualizar_estado(self):
        """Actualiza la etiqueta de estado"""
        self.etiqueta_estado.config(
            text=f"Modo: {self.figura_actual.capitalize()} | Color: {self.color_actual}"
        )
    
    def mouse_presionado(self, evento):
        """Cuando se presiona el mouse"""
        # Verificar si hay una figura en esa posición (para seleccionar/arrastrar)
        figura_clickeada = None
        for figura in reversed(self.figuras):  # Revisar de arriba hacia abajo
            if figura.contiene_punto(evento.x, evento.y):
                figura_clickeada = figura
                break
        
        if figura_clickeada:
            # Modo seleccionar y arrastrar
            self.deseleccionar_todas()
            figura_clickeada.seleccionar()
            self.figura_seleccionada = figura_clickeada
            self.arrastrando = True
            self.offset_x = evento.x - figura_clickeada.x1
            self.offset_y = evento.y - figura_clickeada.y1
        else:
            # Modo dibujar nueva figura
            self.x_inicio = evento.x
            self.y_inicio = evento.y
            self.arrastrando = False
    
    def mouse_arrastrado(self, evento):
        """Cuando se arrastra el mouse"""
        if self.arrastrando and self.figura_seleccionada:
            # Arrastrar figura seleccionada
            nueva_x = evento.x - self.offset_x
            nueva_y = evento.y - self.offset_y
            dx = nueva_x - self.figura_seleccionada.x1
            dy = nueva_y - self.figura_seleccionada.y1
            self.figura_seleccionada.mover(dx, dy)
        
        elif self.x_inicio is not None:
            # Dibujar figura temporal
            if self.figura_temporal:
                self.canvas.delete(self.figura_temporal)
            
            if self.figura_actual == "circulo":
                self.figura_temporal = self.canvas.create_oval(
                    self.x_inicio, self.y_inicio, evento.x, evento.y,
                    outline=self.color_actual, width=2, dash=(5, 5))
            elif self.figura_actual == "rectangulo":
                self.figura_temporal = self.canvas.create_rectangle(
                    self.x_inicio, self.y_inicio, evento.x, evento.y,
                    outline=self.color_actual, width=2, dash=(5, 5))
            elif self.figura_actual == "linea":
                self.figura_temporal = self.canvas.create_line(
                    self.x_inicio, self.y_inicio, evento.x, evento.y,
                    fill=self.color_actual, width=2, dash=(5, 5))
    
    def mouse_soltado(self, evento):
        """Cuando se suelta el mouse"""
        if not self.arrastrando and self.x_inicio is not None:
            # Crear figura definitiva
            if self.figura_temporal:
                self.canvas.delete(self.figura_temporal)
                self.figura_temporal = None
            
            if self.figura_actual == "circulo":
                fig = Circulo(self.canvas, self.x_inicio, self.y_inicio, 
                             evento.x, evento.y, self.color_actual, self.relleno_activo.get())
            elif self.figura_actual == "rectangulo":
                fig = Rectangulo(self.canvas, self.x_inicio, self.y_inicio, 
                                evento.x, evento.y, self.color_actual, self.relleno_activo.get())
            elif self.figura_actual == "linea":
                fig = Linea(self.canvas, self.x_inicio, self.y_inicio, 
                           evento.x, evento.y, self.color_actual, False)
            
            fig.dibujar()
            self.figuras.append(fig)
        
        # Resetear variables
        self.x_inicio = None
        self.y_inicio = None
        self.arrastrando = False
    
    def deseleccionar_todas(self):
        """Deselecciona todas las figuras"""
        for figura in self.figuras:
            figura.deseleccionar()
        self.figura_seleccionada = None
    
    def borrar_seleccionada(self):
        """Borra la figura seleccionada"""
        if self.figura_seleccionada:
            self.figura_seleccionada.borrar()
            self.figuras.remove(self.figura_seleccionada)
            self.figura_seleccionada = None
        else:
            messagebox.showinfo("Info", "No hay figura seleccionada")
    
    def cambiar_tamaño_seleccionada(self, factor):
        """Cambia el tamaño de la figura seleccionada"""
        if self.figura_seleccionada:
            self.figura_seleccionada.cambiar_tamaño(factor)
        else:
            messagebox.showinfo("Info", "No hay figura seleccionada")
    
    def limpiar_todo(self):
        """Limpia todas las figuras"""
        for figura in self.figuras:
            figura.borrar()
        self.figuras.clear()
        self.figura_seleccionada = None
    
    def ejecutar(self):
        """Ejecuta la aplicación"""
        self.ventana.mainloop()

# ==================== EJECUTAR ====================
if __name__ == "__main__":
    app = AplicacionDibujar()
    app.ejecutar()

# ==================== CÓMO USAR ====================
# 1. Elige la figura con los botones (Círculo, Rectángulo, Línea)
# 2. Elige el color
# 3. Marca/desmarca "Relleno" si quieres figura con relleno
# 4. Click y arrastra en el canvas para dibujar
# 5. Click en una figura para seleccionarla (borde más grueso)
# 6. Arrastra una figura seleccionada para moverla
# 7. Usa "Agrandar" y "Achicar" para cambiar tamaño
# 8. Usa "Borrar seleccionada" para eliminar
#
# PARA TU EXAMEN:
# - Esta clase tiene TODO lo que puede pedir tu profesor
# - Puedes agregar más figuras heredando de Figura
# - Puedes agregar más colores en la lista
# - El drag & drop ya está implementado