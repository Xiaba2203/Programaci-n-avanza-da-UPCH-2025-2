"""
╔════════════════════════════════════════════════════════════════════════════╗
║                    GUÍA DEFINITIVA DE TKINTER                              ║
║                    Todo lo que necesitas en un solo archivo                ║
╚════════════════════════════════════════════════════════════════════════════╝

ÍNDICE:
1. CONCEPTOS BÁSICOS      5. ANIMACIONES           9. COLISIONES
2. DIBUJAR FIGURAS        6. WIDGETS              10. DRAG & DROP  
3. EVENTOS MOUSE          7. MODIFICAR OBJETOS    11. POO
4. EVENTOS TECLADO        8. LAYOUTS              12. TIPS

═══════════════════════════════════════════════════════════════════════════
1. CONCEPTOS BÁSICOS
═══════════════════════════════════════════════════════════════════════════

ESTRUCTURA MÍNIMA:
"""
import tkinter as tk
import math, random

# Plantilla base (copia esto para empezar cualquier programa)
def plantilla_base():
    ventana = tk.Tk()
    ventana.title("Mi Programa")
    ventana.geometry("800x600")
    
    canvas = tk.Canvas(ventana, width=800, height=600, bg="white")
    canvas.pack()
    
    # Tu código aquí
    
    ventana.mainloop()  # SIEMPRE al final

"""
COORDENADAS:
(0,0) está arriba a la izquierda
X aumenta hacia la DERECHA →
Y aumenta hacia ABAJO ↓

GUARDAR REFERENCIAS:
id_circulo = canvas.create_oval(...)  # Guarda el ID para modificarlo después
canvas.itemconfig(id_circulo, fill="red")  # Cambia propiedades
canvas.coords(id_circulo, x1, y1, x2, y2)  # Cambia posición
canvas.delete(id_circulo)  # Borra el objeto

═══════════════════════════════════════════════════════════════════════════
2. DIBUJAR FIGURAS
═══════════════════════════════════════════════════════════════════════════
"""

# RECTÁNGULO: (x1,y1) esquina superior izq, (x2,y2) esquina inferior der
rect = canvas.create_rectangle(50, 50, 150, 150, 
                               fill="red",          # Color relleno
                               outline="black",     # Color borde
                               width=3)             # Grosor borde

# CÍRCULO/ÓVALO: Para círculo perfecto → ancho = alto
circulo = canvas.create_oval(200, 50, 300, 150,    # 100x100 = círculo
                            fill="blue", outline="black", width=2)

# LÍNEA: Múltiples puntos para líneas conectadas
linea = canvas.create_line(50, 200, 150, 250, 250, 200,
                          fill="green", width=3,
                          smooth=True,              # Suavizar curvas
                          arrow=tk.LAST)            # Flecha: FIRST, LAST, BOTH

# POLÍGONO: Conecta puntos automáticamente
triangulo = canvas.create_polygon(100, 300, 150, 400, 50, 400,
                                 fill="yellow", outline="black", width=2)

# Estrella (matemática)
estrella_x, estrella_y, radio_ext, radio_int = 400, 350, 50, 20
puntos = []
for i in range(10):
    angulo = math.radians(36 * i - 90)
    radio = radio_ext if i % 2 == 0 else radio_int
    puntos.extend([estrella_x + radio * math.cos(angulo),
                   estrella_y + radio * math.sin(angulo)])
estrella = canvas.create_polygon(*puntos, fill="gold", outline="orange", width=2)

# TEXTO: (x,y) = centro por defecto
texto = canvas.create_text(400, 500, text="¡Hola Tkinter!",
                          font=("Arial", 24, "bold"),
                          fill="purple",
                          anchor=tk.CENTER)  # CENTER, W, E, N, S, NW, NE, SW, SE

# ARCO: start=ángulo inicial (0°=derecha), extent=amplitud
arco = canvas.create_arc(550, 300, 650, 400,
                        start=45, extent=270,
                        fill="pink", outline="black", width=2,
                        style=tk.PIESLICE)  # PIESLICE, CHORD, ARC

"""
OPCIONES COMUNES PARA TODAS LAS FIGURAS:
fill=""           → Sin relleno (solo borde)
outline=""        → Sin borde
dash=(5, 2)       → Línea punteada (5px línea, 2px espacio)
tags="nombre"     → Etiqueta para identificar/agrupar objetos
state=tk.HIDDEN   → Objeto invisible (NORMAL para mostrarlo)

═══════════════════════════════════════════════════════════════════════════
3. EVENTOS DEL MOUSE
═══════════════════════════════════════════════════════════════════════════

EVENTOS DISPONIBLES:
<Button-1>          → Click izquierdo
<Button-3>          → Click derecho
<Double-Button-1>   → Doble click
<B1-Motion>         → Arrastrar (botón izq presionado)
<ButtonRelease-1>   → Soltar botón
<Motion>            → Mover mouse (sin click)
<Enter>             → Mouse entra en objeto
<Leave>             → Mouse sale de objeto
<MouseWheel>        → Rueda del mouse

PROPIEDADES DEL EVENTO:
evento.x, evento.y  → Coordenadas del mouse
"""

# Ejemplo: Dibujar con el mouse
x_ant, y_ant = None, None

def click(evento):
    # Crear punto donde hiciste click
    canvas.create_oval(evento.x-5, evento.y-5, evento.x+5, evento.y+5, fill="black")
    print(f"Click en ({evento.x}, {evento.y})")

def arrastrar(evento):
    global x_ant, y_ant
    if x_ant and y_ant:
        canvas.create_line(x_ant, y_ant, evento.x, evento.y,
                         fill="blue", width=3, capstyle=tk.ROUND)
    x_ant, y_ant = evento.x, evento.y

def soltar(evento):
    global x_ant, y_ant
    x_ant, y_ant = None, None

# Vincular eventos al CANVAS (eventos globales)
canvas.bind("<Button-1>", click)
canvas.bind("<B1-Motion>", arrastrar)
canvas.bind("<ButtonRelease-1>", soltar)

# Vincular eventos a OBJETOS ESPECÍFICOS (por tag)
canvas.tag_bind("miObjeto", "<Button-1>", lambda e: print("¡Clickeaste el objeto!"))

"""
ENCONTRAR OBJETOS:
canvas.find_closest(x, y)           → Objeto más cercano a (x,y)
canvas.find_overlapping(x1,y1,x2,y2)→ Objetos en área rectangular
canvas.find_withtag("tag")          → Objetos con cierta etiqueta

═══════════════════════════════════════════════════════════════════════════
4. EVENTOS DEL TECLADO
═══════════════════════════════════════════════════════════════════════════

EVENTOS:
<Key>               → Cualquier tecla
<KeyPress-a>        → Tecla 'a' presionada
<KeyRelease-a>      → Tecla 'a' soltada

TECLAS ESPECIALES:
"Up", "Down", "Left", "Right"  → Flechas
"space"                        → Barra espaciadora
"Return"                       → Enter
"Escape"                       → Escape
"Shift_L", "Control_L"         → Modificadores
"a", "b", "1", "2"             → Letras y números

PROPIEDADES:
evento.keysym       → Nombre de la tecla ("Up", "a", "space")
evento.char         → Carácter de la tecla ("a", "1", "")
"""

# Ejemplo: Mover cuadrado con flechas
jugador = canvas.create_rectangle(375, 275, 425, 325, fill="cyan")

def tecla_presionada(evento):
    velocidad = 10
    
    if evento.keysym == "Up":
        canvas.move(jugador, 0, -velocidad)
    elif evento.keysym == "Down":
        canvas.move(jugador, 0, velocidad)
    elif evento.keysym == "Left":
        canvas.move(jugador, -velocidad, 0)
    elif evento.keysym == "Right":
        canvas.move(jugador, velocidad, 0)
    elif evento.keysym == "space":
        color = random.choice(["red", "blue", "green", "yellow"])
        canvas.itemconfig(jugador, fill=color)
    elif evento.char == "r":  # Tecla 'r'
        canvas.coords(jugador, 375, 275, 425, 325)  # Resetear posición

# Vincular a la VENTANA (no al canvas)
ventana.bind("<Key>", tecla_presionada)

"""
MÚLTIPLES TECLAS A LA VEZ:
Usa un set para detectar varias teclas simultáneas
"""
teclas = set()

def presionar(e):
    teclas.add(e.keysym)

def soltar_tecla(e):
    teclas.discard(e.keysym)

def actualizar():
    if "Up" in teclas:
        canvas.move(jugador, 0, -5)
    if "Right" in teclas:
        canvas.move(jugador, 5, 0)
    ventana.after(20, actualizar)  # Repetir cada 20ms

ventana.bind("<KeyPress>", presionar)
ventana.bind("<KeyRelease>", soltar_tecla)
actualizar()

"""
═══════════════════════════════════════════════════════════════════════════
5. ANIMACIONES
═══════════════════════════════════════════════════════════════════════════

MÉTODO PRINCIPAL: ventana.after(milisegundos, funcion)
Ejecuta una función después de X milisegundos
Para loop continuo: llamar after() dentro de la misma función
"""

# Ejemplo 1: Movimiento horizontal con rebote
pelota = canvas.create_oval(0, 50, 40, 90, fill="red")
velocidad = 5

def mover():
    global velocidad
    canvas.move(pelota, velocidad, 0)
    coords = canvas.coords(pelota)  # [x1, y1, x2, y2]
    
    # Rebotar en los bordes
    if coords[2] >= 800 or coords[0] <= 0:
        velocidad = -velocidad
    
    ventana.after(20, mover)  # Repetir cada 20ms (50 FPS)

mover()  # Iniciar animación

# Ejemplo 2: Movimiento circular
pelota2 = canvas.create_oval(0, 0, 30, 30, fill="blue")
angulo = 0

def circular():
    global angulo
    centro_x, centro_y, radio = 400, 300, 100
    
    x = centro_x + radio * math.cos(math.radians(angulo))
    y = centro_y + radio * math.sin(math.radians(angulo))
    
    canvas.coords(pelota2, x-15, y-15, x+15, y+15)
    angulo += 2
    
    ventana.after(20, circular)

circular()

# Ejemplo 3: Cambio de color periódico
cuadrado = canvas.create_rectangle(50, 400, 150, 500, fill="purple")
colores = ["red", "blue", "green", "yellow", "orange"]
indice = 0

def cambiar_color():
    global indice
    canvas.itemconfig(cuadrado, fill=colores[indice])
    indice = (indice + 1) % len(colores)
    ventana.after(500, cambiar_color)  # Cada 500ms

cambiar_color()

# Ejemplo 4: Pulsar (crecer y encoger)
circulo = canvas.create_oval(0, 0, 50, 50, fill="pink")
tamaño, creciendo = 25, True

def pulsar():
    global tamaño, creciendo
    
    if creciendo:
        tamaño += 2
        if tamaño >= 50: creciendo = False
    else:
        tamaño -= 2
        if tamaño <= 10: creciendo = True
    
    centro_x, centro_y = 600, 450
    canvas.coords(circulo, 
                 centro_x-tamaño, centro_y-tamaño,
                 centro_x+tamaño, centro_y+tamaño)
    
    ventana.after(30, pulsar)

pulsar()

"""
TIPS ANIMACIONES:
- 20ms = ~50 FPS (suave)
- 16ms = ~60 FPS (muy suave)
- 100ms = 10 FPS (lento, para efectos)
- Usa 'global' o 'nonlocal' para modificar variables fuera de la función
- Guarda el ID: timer_id = ventana.after(...) para poder cancelar con ventana.after_cancel(timer_id)

═══════════════════════════════════════════════════════════════════════════
6. WIDGETS (Controles de Interfaz)
═══════════════════════════════════════════════════════════════════════════
"""

# BUTTON - Botón
def mi_funcion():
    print("¡Botón presionado!")

boton = tk.Button(ventana, text="Presióname", command=mi_funcion,
                 bg="lightblue", fg="darkblue",
                 font=("Arial", 14), width=15, height=2)
boton.pack(pady=10)

# ENTRY - Campo de texto
entry = tk.Entry(ventana, width=30, font=("Arial", 12))
entry.pack(pady=5)
entry.insert(0, "Texto inicial")  # Insertar texto
texto = entry.get()                # Obtener texto
entry.delete(0, tk.END)            # Borrar todo

# LABEL - Etiqueta de texto
label = tk.Label(ventana, text="Soy una etiqueta", 
                font=("Arial", 12), bg="yellow")
label.pack()
label.config(text="Texto cambiado")  # Cambiar texto

# RADIOBUTTON - Selección única
opcion = tk.StringVar(value="opcion1")
tk.Radiobutton(ventana, text="Opción 1", variable=opcion, value="opcion1").pack()
tk.Radiobutton(ventana, text="Opción 2", variable=opcion, value="opcion2").pack()
seleccionada = opcion.get()  # Obtener opción seleccionada

# CHECKBUTTON - Selección múltiple
check1 = tk.BooleanVar()
check2 = tk.BooleanVar()
tk.Checkbutton(ventana, text="Opción A", variable=check1).pack()
tk.Checkbutton(ventana, text="Opción B", variable=check2).pack()
if check1.get():
    print("Opción A está marcada")

# SCALE - Deslizador
def cambio_valor(valor):
    print(f"Valor: {valor}")

scale = tk.Scale(ventana, from_=0, to=100, orient=tk.HORIZONTAL,
                command=cambio_valor, length=300)
scale.pack()
scale.set(50)  # Establecer valor inicial
valor_actual = scale.get()  # Obtener valor

# LISTBOX - Lista de opciones
listbox = tk.Listbox(ventana, height=5)
listbox.pack()
for item in ["Item 1", "Item 2", "Item 3"]:
    listbox.insert(tk.END, item)
seleccion = listbox.curselection()  # Índice seleccionado
if seleccion:
    item = listbox.get(seleccion[0])

# TEXT - Campo de texto multilínea
text_widget = tk.Text(ventana, width=40, height=5, font=("Arial", 10))
text_widget.pack()
text_widget.insert(tk.END, "Texto multilínea\nLínea 2")
contenido = text_widget.get("1.0", tk.END)  # Obtener todo el texto

# FRAME - Contenedor para agrupar widgets
frame = tk.Frame(ventana, bg="lightgray", bd=2, relief=tk.RAISED)
frame.pack(padx=10, pady=10)
tk.Label(frame, text="Dentro del frame").pack()
tk.Button(frame, text="Botón").pack()

"""
═══════════════════════════════════════════════════════════════════════════
7. MODIFICAR OBJETOS DINÁMICAMENTE
═══════════════════════════════════════════════════════════════════════════
"""

obj = canvas.create_rectangle(100, 100, 200, 200, fill="red", tags="mi_rect")

# Cambiar propiedades
canvas.itemconfig(obj, fill="blue")              # Cambiar color
canvas.itemconfig(obj, outline="black", width=5) # Cambiar borde

# Cambiar posición
canvas.coords(obj, 300, 300, 400, 400)  # Nueva posición absoluta

# Mover relativamente
canvas.move(obj, 10, -5)  # Mover 10px derecha, 5px arriba

# Cambiar visibilidad
canvas.itemconfig(obj, state=tk.HIDDEN)  # Ocultar
canvas.itemconfig(obj, state=tk.NORMAL)  # Mostrar

# Rotar (no hay función directa, hay que recrear)
# Elevar/bajar nivel (orden de dibujo)
canvas.tag_raise(obj)   # Traer al frente
canvas.tag_lower(obj)   # Enviar atrás

# Obtener propiedades actuales
color_actual = canvas.itemcget(obj, "fill")
coords_actuales = canvas.coords(obj)  # [x1, y1, x2, y2]

"""
═══════════════════════════════════════════════════════════════════════════
8. LAYOUTS - POSICIONAR WIDGETS
═══════════════════════════════════════════════════════════════════════════

3 MÉTODOS PRINCIPALES:
"""

# 1. PACK - Apila widgets (más simple)
tk.Button(ventana, text="Arriba").pack(side=tk.TOP)
tk.Button(ventana, text="Abajo").pack(side=tk.BOTTOM)
tk.Button(ventana, text="Izquierda").pack(side=tk.LEFT)
tk.Button(ventana, text="Derecha").pack(side=tk.RIGHT)
tk.Button(ventana, text="Centrado").pack(pady=10, padx=20, fill=tk.X)

# 2. GRID - Sistema de cuadrícula (más control)
tk.Label(ventana, text="Nombre:").grid(row=0, column=0, sticky=tk.W)
tk.Entry(ventana).grid(row=0, column=1, padx=5)
tk.Label(ventana, text="Email:").grid(row=1, column=0, sticky=tk.W)
tk.Entry(ventana).grid(row=1, column=1, padx=5)
tk.Button(ventana, text="Enviar").grid(row=2, column=0, columnspan=2, pady=10)

# 3. PLACE - Posición absoluta (más preciso)
tk.Button(ventana, text="Aquí").place(x=100, y=50)
tk.Label(ventana, text="Allá").place(x=300, y=200, width=100, height=30)

"""
NO MEZCLES PACK Y GRID EN EL MISMO CONTENEDOR (usa Frames para separar)

═══════════════════════════════════════════════════════════════════════════
9. COLISIONES - DETECTAR CONTACTO ENTRE OBJETOS
═══════════════════════════════════════════════════════════════════════════
"""

obj1 = canvas.create_rectangle(100, 100, 150, 150, fill="red")
obj2 = canvas.create_rectangle(200, 200, 250, 250, fill="blue")

def hay_colision(id1, id2):
    """Detecta si dos objetos se tocan"""
    x1_1, y1_1, x2_1, y2_1 = canvas.coords(id1)
    x1_2, y1_2, x2_2, y2_2 = canvas.coords(id2)
    
    # Detectar superposición de rectángulos
    if (x1_1 < x2_2 and x2_1 > x1_2 and y1_1 < y2_2 and y2_1 > y1_2):
        return True
    return False

# Usar en animación
def actualizar():
    canvas.move(obj1, 2, 0)
    if hay_colision(obj1, obj2):
        canvas.itemconfig(obj1, fill="green")  # Cambiar color al tocar
    ventana.after(20, actualizar)

# Método alternativo: find_overlapping
def colision_en_punto(x, y):
    """Detecta objetos en un punto específico"""
    objetos = canvas.find_overlapping(x-1, y-1, x+1, y+1)
    return len(objetos) > 0

"""
═══════════════════════════════════════════════════════════════════════════
10. DRAG & DROP - ARRASTRAR Y SOLTAR
═══════════════════════════════════════════════════════════════════════════
"""

# Sistema completo de drag & drop
objeto_seleccionado = None
offset_x, offset_y = 0, 0

def iniciar_drag(evento):
    global objeto_seleccionado, offset_x, offset_y
    # Encontrar objeto bajo el mouse
    objetos = canvas.find_overlapping(evento.x-5, evento.y-5, evento.x+5, evento.y+5)
    if objetos:
        objeto_seleccionado = objetos[-1]  # Último = el de arriba
        coords = canvas.coords(objeto_seleccionado)
        offset_x = evento.x - coords[0]
        offset_y = evento.y - coords[1]

def arrastrar_objeto(evento):
    global objeto_seleccionado
    if objeto_seleccionado:
        # Mover objeto siguiendo el mouse
        coords = canvas.coords(objeto_seleccionado)
        ancho = coords[2] - coords[0]
        alto = coords[3] - coords[1]
        canvas.coords(objeto_seleccionado,
                     evento.x - offset_x,
                     evento.y - offset_y,
                     evento.x - offset_x + ancho,
                     evento.y - offset_y + alto)

def soltar_objeto(evento):
    global objeto_seleccionado
    objeto_seleccionado = None

canvas.bind("<Button-1>", iniciar_drag)
canvas.bind("<B1-Motion>", arrastrar_objeto)
canvas.bind("<ButtonRelease-1>", soltar_objeto)

"""
═══════════════════════════════════════════════════════════════════════════
11. POO - PROGRAMACIÓN ORIENTADA A OBJETOS
═══════════════════════════════════════════════════════════════════════════
"""

# Clase base para objetos en canvas
class ObjetoCanvas:
    def __init__(self, canvas, x, y, ancho, alto, color):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto
        self.color = color
        self.id = self.canvas.create_rectangle(x, y, x+ancho, y+alto, fill=color)
        self.vx = 0
        self.vy = 0
    
    def mover(self):
        self.canvas.move(self.id, self.vx, self.vy)
        coords = self.canvas.coords(self.id)
        self.x, self.y = coords[0], coords[1]
    
    def cambiar_color(self, nuevo_color):
        self.color = nuevo_color
        self.canvas.itemconfig(self.id, fill=nuevo_color)
    
    def colisiona_con(self, otro):
        x1, y1, x2, y2 = self.canvas.coords(self.id)
        ox1, oy1, ox2, oy2 = self.canvas.coords(otro.id)
        return (x1 < ox2 and x2 > ox1 and y1 < oy2 and y2 > oy1)

# Clase específica: Pelota con rebote
class Pelota(ObjetoCanvas):
    def __init__(self, canvas, x, y, radio, color):
        self.radio = radio
        self.id = canvas.create_oval(x-radio, y-radio, x+radio, y+radio, fill=color)
        self.canvas = canvas
        self.vx = random.randint(-5, 5)
        self.vy = random.randint(-5, 5)
    
    def actualizar(self):
        self.canvas.move(self.id, self.vx, self.vy)
        coords = self.canvas.coords(self.id)
        
        # Rebotar en bordes
        if coords[2] >= 800 or coords[0] <= 0:
            self.vx = -self.vx
        if coords[3] >= 600 or coords[1] <= 0:
            self.vy = -self.vy

# Uso:
pelota1 = Pelota(canvas, 400, 300, 20, "red")
pelota2 = Pelota(canvas, 200, 150, 15, "blue")

def loop_juego():
    pelota1.actualizar()
    pelota2.actualizar()
    ventana.after(20, loop_juego)

loop_juego()

"""
═══════════════════════════════════════════════════════════════════════════
12. MENÚS Y DIÁLOGOS
═══════════════════════════════════════════════════════════════════════════
"""

# BARRA DE MENÚS
menubar = tk.Menu(ventana)
ventana.config(menu=menubar)

# Menú Archivo
menu_archivo = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Archivo", menu=menu_archivo)
menu_archivo.add_command(label="Nuevo", command=lambda: print("Nuevo"))
menu_archivo.add_command(label="Abrir", command=lambda: print("Abrir"))
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=ventana.quit)

# Menú Editar
menu_editar = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Editar", menu=menu_editar)
menu_editar.add_command(label="Copiar", command=lambda: print("Copiar"))
menu_editar.add_command(label="Pegar", command=lambda: print("Pegar"))

# VENTANAS DE DIÁLOGO
def mostrar_dialogos():
    # Mensaje simple
    messagebox.showinfo("Título", "Este es un mensaje informativo")
    
    # Advertencia
    messagebox.showwarning("Cuidado", "Esto es una advertencia")
    
    # Error
    messagebox.showerror("Error", "Ocurrió un error")
    
    # Pregunta Sí/No
    respuesta = messagebox.askyesno("Pregunta", "¿Estás seguro?")
    if respuesta:
        print("Usuario dijo SÍ")
    
    # Pregunta OK/Cancelar
    respuesta = messagebox.askokcancel("Confirmar", "¿Continuar?")
    
    # Elegir color
    color = colorchooser.askcolor(title="Elige un color")
    if color[1]:  # color[1] es el código hexadecimal
        print(f"Color elegido: {color[1]}")
    
    # Abrir archivo
    archivo = filedialog.askopenfilename(
        title="Selecciona un archivo",
        filetypes=[("Archivos de texto", "*.txt"), ("Todos", "*.*")]
    )
    if archivo:
        print(f"Archivo seleccionado: {archivo}")
    
    # Guardar archivo
    archivo = filedialog.asksaveasfilename(defaultextension=".txt")
    
    # Entrada de texto simple
    respuesta = simpledialog.askstring("Input", "Escribe tu nombre:")
    print(f"Nombre: {respuesta}")

tk.Button(ventana, text="Mostrar Diálogos", command=mostrar_dialogos).pack()

"""
═══════════════════════════════════════════════════════════════════════════
13. TIPS Y TRUCOS
═══════════════════════════════════════════════════════════════════════════

🎯 MEJORES PRÁCTICAS:

1. ORGANIZAR CÓDIGO:
   - Usa funciones para cada funcionalidad
   - Usa clases para objetos complejos
   - Separa lógica del juego de la interfaz

2. RENDIMIENTO:
   - No crees objetos innecesarios en loops
   - Borra objetos que ya no usas: canvas.delete(id)
   - Usa tags para manipular grupos: canvas.delete("enemigos")

3. COLORES:
   - Nombres: "red", "blue", "lightgreen"
   - Hexadecimal: "#FF0000", "#00FF00"
   - RGB: No directo, convertir a hex: f"#{r:02x}{g:02x}{b:02x}"

4. FUENTES:
   - ("Arial", 12)          → Normal
   - ("Arial", 12, "bold")  → Negrita
   - ("Arial", 12, "italic")→ Cursiva

5. TAGS (Etiquetas):
   canvas.create_rectangle(..., tags="enemigo")
   canvas.create_rectangle(..., tags=("enemigo", "rojo"))
   canvas.itemconfig("enemigo", fill="blue")  # Cambiar todos
   canvas.delete("enemigo")                   #