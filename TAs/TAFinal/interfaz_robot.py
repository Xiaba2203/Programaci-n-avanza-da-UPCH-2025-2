#importo las librerias necesarias y mi libreria de robot
import tkinter as tk 
from tkinter import messagebox  
from robot import Robot  

#creo el interfaz
class InterfazRobot:
    
    def __init__(self): 
        #creo la ventana principal
        self.ventana = tk.Tk() 
        self.ventana.title("Simulador de Robot") 
        self.ventana.geometry("580x650") 
        
        self.robot = None  #se incia sin robot
        self.escala = 20  #le pongo 20 pixeles por casilla
        
        #establezco los limites del canvas
        self.ancho_canvas = 400
        self.alto_canvas = 400
        self.centro_x = self.ancho_canvas // 2
        self.centro_y = self.alto_canvas // 2 
        
        self.instrucciones_cola = []
        self.esta_animando = False
        self.id_triangulo = None 
        self.ids_lineas = [] 
        self.direccion_actual = "norte"
        self.botones_dir = {}
        
        #ejecución
        self.crear_interfaz() 
        self.dibujar_cuadricula() 
    
    #método para crear los widgets
    def crear_interfaz(self):
        #Frame superior
        frame_sup = tk.Frame(self.ventana, bg="lightgray", pady=8) 
        frame_sup.pack(fill=tk.X) 
        
        tk.Label(frame_sup, text="Posicion Inicial:", bg="lightgreen", font=("Arial", 10, "bold")).pack()
        
        frame_pos = tk.Frame(frame_sup, bg="lightgray")  #frame para "x" e "y"
        frame_pos.pack(pady=3) 
        
        #etiquetas y entradas para "x" e "y"
        tk.Label(frame_pos, text="X:", bg="lightgray").pack(side=tk.LEFT, padx=3) 
        self.entrada_x = tk.Entry(frame_pos, width=6) 
        self.entrada_x.pack(side=tk.LEFT, padx=3)
        self.entrada_x.insert(0, "0")
        
        tk.Label(frame_pos, text="Y:", bg="lightgray").pack(side=tk.LEFT, padx=3) 
        self.entrada_y = tk.Entry(frame_pos, width=6)  
        self.entrada_y.pack(side=tk.LEFT, padx=3)
        self.entrada_y.insert(0, "0")
        
        tk.Label(frame_sup, text="Direccion:", bg="lightgray", font=("Arial", 10, "bold")).pack(pady=(5,3))
        
        frame_dir = tk.Frame(frame_sup, bg="lightgray")  #frame para los botones de dirección
        frame_dir.pack()
        
        #creo los 4 botones de dirección
        for dir_nombre in ["norte", "sur", "este", "oeste"]:
            #defino a norte como inicial
            if dir_nombre == "norte":
                color_inicial = "lightblue"
                relieve_inicial = tk.SUNKEN
            else:
                color_inicial = "SystemButtonFace"
                relieve_inicial = tk.RAISED
            
            btn = tk.Button(
                frame_dir, 
                text=dir_nombre.capitalize(), 
                width=8, 
                bg=color_inicial, 
                relief=relieve_inicial, 
                command=lambda d=dir_nombre: self.seleccionar_direccion(d)
            )
            btn.pack(side=tk.LEFT, padx=2)
            self.botones_dir[dir_nombre] = btn
        
        tk.Button(frame_sup, text="Crear Robot", bg="green", fg="white", width=12, command=self.crear_robot).pack(pady=5)
        
        #Frame de instrucciones
        frame_inst = tk.Frame(self.ventana, bg="lightblue", pady=8)
        frame_inst.pack(fill=tk.X)
        
        tk.Label(frame_inst, text="Instrucciones (R, L, A):", bg="lightblue").pack()
        self.entrada_inst = tk.Entry(frame_inst, width=35)
        self.entrada_inst.pack(pady=3)
        
        frame_botones = tk.Frame(frame_inst, bg="lightblue")  #frame para ejecutar y limpiar
        frame_botones.pack()
        
        tk.Button(frame_botones, text="Ejecutar", width=10, bg="blue", fg="white", command=self.ejecutar_instrucciones).pack(side=tk.LEFT, padx=3)
        tk.Button(frame_botones, text="Limpiar", width=10, bg="orange", command=self.limpiar_todo).pack(side=tk.LEFT, padx=3)
        
        #creo el canvas donde voy a dibujar
        self.canvas = tk.Canvas(
            self.ventana, 
            width=self.ancho_canvas, 
            height=self.alto_canvas, 
            bg="white", 
            highlightthickness=1, 
            highlightbackground="black"
        )
        self.canvas.pack(pady=8)
        
        #Frame inferior para mostrar la posición
        frame_inf = tk.Frame(self.ventana, bg="lightgreen", pady=6)
        frame_inf.pack(fill=tk.X)
        self.etiqueta_estado = tk.Label(
            frame_inf, 
            text="Posicion: -- | Direccion: --", 
            bg="lightgreen", 
            font=("Arial", 9)
        )
        self.etiqueta_estado.pack()
    
    #método para seleccionar dirección inicial
    def seleccionar_direccion(self, direccion):
        self.direccion_actual = direccion
        
        #actualizo todos los botones
        for nombre, boton in self.botones_dir.items():
            if nombre == direccion:
                boton.config(bg="lightblue", relief=tk.SUNKEN)
            else:
                boton.config(bg="SystemButtonFace", relief=tk.RAISED)
    
    #método que dibuja la cuadrícula
    def dibujar_cuadricula(self):
        for i in range(-10, 11):
            x = self.centro_x + (i * self.escala)
            self.canvas.create_line(x, 0, x, self.alto_canvas, fill="lightgray")
            
            y = self.centro_y - (i * self.escala)
            self.canvas.create_line(0, y, self.ancho_canvas, y, fill="lightgray")
        
        #dibujo los ejes principales más gruesos
        self.canvas.create_line(self.centro_x, 0, self.centro_x, self.alto_canvas, fill="gray", width=2)
        self.canvas.create_line(0, self.centro_y, self.ancho_canvas, self.centro_y, fill="gray", width=2)
    
    #convierte coordenadas del robot a coordenadas del canvas
    def convertir_coordenadas(self, x_robot, y_robot):
        x_canvas = self.centro_x + (x_robot * self.escala)
        y_canvas = self.centro_y - (y_robot * self.escala)  #invertido porque en canvas Y crece hacia abajo
        return x_canvas, y_canvas
    
    #calcula los puntos del triángulo según la dirección
    def obtener_puntos_triangulo(self, x_canvas, y_canvas, direccion):
        tam = 10
        
        if direccion == "norte":
            return [
                x_canvas, y_canvas - tam, 
                x_canvas - tam//2, y_canvas + tam//2, 
                x_canvas + tam//2, y_canvas + tam//2
            ]
        elif direccion == "sur":
            return [
                x_canvas, y_canvas + tam, 
                x_canvas - tam//2, y_canvas - tam//2, 
                x_canvas + tam//2, y_canvas - tam//2
            ]
        elif direccion == "este":
            return [
                x_canvas + tam, y_canvas, 
                x_canvas - tam//2, y_canvas - tam//2, 
                x_canvas - tam//2, y_canvas + tam//2
            ]
        else:  #oeste
            return [
                x_canvas - tam, y_canvas, 
                x_canvas + tam//2, y_canvas - tam//2, 
                x_canvas + tam//2, y_canvas + tam//2
            ]
    
    #dibuja el robot en el canvas
    def dibujar_robot(self):
        if self.id_triangulo:
            self.canvas.delete(self.id_triangulo)  #borro el triángulo anterior
        
        x, y = self.robot.obtener_posicion()
        direccion = self.robot.obtener_direccion()
        x_canvas, y_canvas = self.convertir_coordenadas(x, y)
        puntos = self.obtener_puntos_triangulo(x_canvas, y_canvas, direccion)
        
        self.id_triangulo = self.canvas.create_polygon(puntos, fill="red", outline="black", width=2)
    
    #dibuja una línea entre dos puntos
    def dibujar_linea(self, x1, y1, x2, y2):
        x1_c, y1_c = self.convertir_coordenadas(x1, y1)
        x2_c, y2_c = self.convertir_coordenadas(x2, y2)
        linea = self.canvas.create_line(x1_c, y1_c, x2_c, y2_c, fill="blue", width=2) #creo una linea azul que indica su recorrido
        self.ids_lineas.append(linea)
    
    #actualiza el texto de estado
    def actualizar_estado(self):
        if self.robot:
            x, y = self.robot.obtener_posicion()
            dir = self.robot.obtener_direccion()
            self.etiqueta_estado.config(text=f"Posicion: ({x}, {y}) | Direccion: {dir}")
    
    #crea el robot con la posición y dirección inicial
    def crear_robot(self):
        try:
            x = int(self.entrada_x.get())
            y = int(self.entrada_y.get())
            self.robot = Robot(x, y, self.direccion_actual)
            
            #limpio el canvas y redibujo todo
            self.canvas.delete("all")
            self.dibujar_cuadricula()
            self.dibujar_robot()
            self.actualizar_estado()
            self.entrada_inst.delete(0, tk.END)
            self.ids_lineas = []
            
            messagebox.showinfo("Exito", f"Robot creado en ({x}, {y})")
        except ValueError:
            messagebox.showerror("Error", "X e Y deben ser numeros")
    
    #verifica que el robot no se salga del área
    def validar_limites(self, instrucciones):
        robot_temp = Robot(self.robot.x, self.robot.y, self.robot.direccion)
        x_min, x_max = -8, 8
        y_min, y_max = -8, 8
        
        #simulo todas las instrucciones
        for char in instrucciones:
            if char == 'R':
                robot_temp.girar_derecha()
            elif char == 'L':
                robot_temp.girar_izquierda()
            elif char == 'A':
                robot_temp.avanzar()
            
            x, y = robot_temp.obtener_posicion()
            if x < x_min or x > x_max or y < y_min or y > y_max:
                return False
        
        return True
    
    #ejecuta las instrucciones ingresadas
    def ejecutar_instrucciones(self):
        if not self.robot:
            messagebox.showwarning("Advertencia", "Primero crea un robot") #si no hay robot creado
            return
        
        if self.esta_animando:
            return
        
        cadena = self.entrada_inst.get().upper().strip()
        if not cadena:
            messagebox.showwarning("Advertencia", "Ingresa instrucciones") #si no hay instrucciones
            return
        
        #valido que solo tenga R, L, A
        for char in cadena:
            if char not in ['R', 'L', 'A']:
                messagebox.showerror("Error", f"Caracter invalido: {char}") #si hay caracteres invalidos
                return
        
        #valido que no se salga de los límites
        if not self.validar_limites(cadena):
            messagebox.showerror("Fuera de limites", "El robot saldria del area.\nIngresa nuevas instrucciones.")
            self.entrada_inst.delete(0, tk.END)
            return
        
        #inicio la animación
        self.instrucciones_cola = list(cadena)
        self.esta_animando = True
        self.animar_paso()
    
    #anima cada paso de las instrucciones
    def animar_paso(self):
        if not self.instrucciones_cola:
            self.esta_animando = False
            self.actualizar_estado()
            messagebox.showinfo("Completado", "Instrucciones ejecutadas")
            return
        
        inst = self.instrucciones_cola.pop(0)
        x_ant, y_ant = self.robot.obtener_posicion()
        
        if inst == 'R':
            self.robot.girar_derecha()
        elif inst == 'L':
            self.robot.girar_izquierda()
        elif inst == 'A':
            self.robot.avanzar()
            x_nueva, y_nueva = self.robot.obtener_posicion()
            self.dibujar_linea(x_ant, y_ant, x_nueva, y_nueva)
        
        self.dibujar_robot()
        self.actualizar_estado()
        self.ventana.after(500, self.animar_paso)  #espero medio segundo y sigo
    
    #limpia todo y reinicia el robot
    def limpiar_todo(self):
        if self.robot:
            x = int(self.entrada_x.get())
            y = int(self.entrada_y.get())
            self.robot.reiniciar(x, y, self.direccion_actual)
            
            self.canvas.delete("all")
            self.dibujar_cuadricula()
            self.dibujar_robot()
            self.actualizar_estado()
            self.entrada_inst.delete(0, tk.END)
            self.ids_lineas = []
    
    #inicia la aplicación
    def iniciar(self):
        self.ventana.mainloop()