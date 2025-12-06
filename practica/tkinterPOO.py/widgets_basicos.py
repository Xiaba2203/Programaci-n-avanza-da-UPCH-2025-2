import tkinter as tk
from tkinter import messagebox, Menu

# ==================== EJEMPLO 1: BOTONES ====================
class EjemploBotones:
    """Ejemplos de diferentes tipos de botones"""
    def __init__(self, ventana):
        frame = tk.LabelFrame(ventana, text="BOTONES", padx=10, pady=10)
        frame.pack(padx=10, pady=5, fill=tk.BOTH)
        
        # Botón simple
        tk.Button(frame, text="Botón Simple", 
                 command=self.accion_simple).pack(pady=2)
        
        # Botón con color
        tk.Button(frame, text="Botón con Color", bg="lightblue", fg="darkblue",
                 command=lambda: messagebox.showinfo("Info", "Botón con color")).pack(pady=2)
        
        # Botón deshabilitado
        boton_des = tk.Button(frame, text="Botón Deshabilitado", state=tk.DISABLED)
        boton_des.pack(pady=2)
        
        # Botón que se deshabilita
        self.boton_toggle = tk.Button(frame, text="Click para deshabilitar", 
                                     command=self.toggle_boton)
        self.boton_toggle.pack(pady=2)
        
        # Botón con imagen (simulado con emoji)
        tk.Button(frame, text="🎨 Botón con Emoji", 
                 command=lambda: print("Botón con emoji")).pack(pady=2)
    
    def accion_simple(self):
        print("¡Botón presionado!")
        messagebox.showinfo("Acción", "¡Botón presionado!")
    
    def toggle_boton(self):
        if self.boton_toggle["state"] == tk.NORMAL:
            self.boton_toggle.config(state=tk.DISABLED, text="Deshabilitado")
        else:
            self.boton_toggle.config(state=tk.NORMAL, text="Click para deshabilitar")

# ==================== EJEMPLO 2: ENTRY ====================
class EjemploEntry:
    """Ejemplos de campos de texto (Entry)"""
    def __init__(self, ventana):
        frame = tk.LabelFrame(ventana, text="ENTRY (Campos de Texto)", padx=10, pady=10)
        frame.pack(padx=10, pady=5, fill=tk.BOTH)
        
        # Entry simple
        tk.Label(frame, text="Nombre:").grid(row=0, column=0, sticky=tk.W)
        self.entry_nombre = tk.Entry(frame, width=20)
        self.entry_nombre.grid(row=0, column=1, padx=5, pady=2)
        
        # Entry con valor por defecto
        tk.Label(frame, text="Email:").grid(row=1, column=0, sticky=tk.W)
        self.entry_email = tk.Entry(frame, width=20)
        self.entry_email.insert(0, "ejemplo@correo.com")
        self.entry_email.grid(row=1, column=1, padx=5, pady=2)
        
        # Entry de contraseña
        tk.Label(frame, text="Password:").grid(row=2, column=0, sticky=tk.W)
        self.entry_pass = tk.Entry(frame, width=20, show="*")
        self.entry_pass.grid(row=2, column=1, padx=5, pady=2)
        
        # Entry de solo lectura
        tk.Label(frame, text="Solo lectura:").grid(row=3, column=0, sticky=tk.W)
        entry_readonly = tk.Entry(frame, width=20, state="readonly")
        entry_readonly.grid(row=3, column=1, padx=5, pady=2)
        entry_readonly.config(state=tk.NORMAL)
        entry_readonly.insert(0, "No editable")
        entry_readonly.config(state="readonly")
        
        # Botón para obtener valores
        tk.Button(frame, text="Obtener Valores", 
                 command=self.obtener_valores).grid(row=4, column=0, columnspan=2, pady=5)
    
    def obtener_valores(self):
        nombre = self.entry_nombre.get()
        email = self.entry_email.get()
        password = self.entry_pass.get()
        
        mensaje = f"Nombre: {nombre}\nEmail: {email}\nPassword: {'*' * len(password)}"
        messagebox.showinfo("Valores", mensaje)

# ==================== EJEMPLO 3: RADIOBUTTON ====================
class EjemploRadiobutton:
    """Ejemplos de botones de radio (opción única)"""
    def __init__(self, ventana):
        frame = tk.LabelFrame(ventana, text="RADIOBUTTON (Opción Única)", padx=10, pady=10)
        frame.pack(padx=10, pady=5, fill=tk.BOTH)
        
        # Variable para guardar selección
        self.opcion = tk.StringVar(value="python")
        
        tk.Label(frame, text="Lenguaje favorito:").pack(anchor=tk.W)
        
        # Crear radiobuttons
        lenguajes = [("Python", "python"), ("JavaScript", "js"), 
                    ("Java", "java"), ("C++", "cpp")]
        
        for texto, valor in lenguajes:
            tk.Radiobutton(frame, text=texto, variable=self.opcion, 
                          value=valor, command=self.mostrar_seleccion).pack(anchor=tk.W)
        
        self.label_seleccion = tk.Label(frame, text="Seleccionado: python", fg="blue")
        self.label_seleccion.pack(pady=5)
    
    def mostrar_seleccion(self):
        self.label_seleccion.config(text=f"Seleccionado: {self.opcion.get()}")

# ==================== EJEMPLO 4: CHECKBUTTON ====================
class EjemploCheckbutton:
    """Ejemplos de checkboxes (múltiples opciones)"""
    def __init__(self, ventana):
        frame = tk.LabelFrame(ventana, text="CHECKBUTTON (Múltiples Opciones)", padx=10, pady=10)
        frame.pack(padx=10, pady=5, fill=tk.BOTH)
        
        tk.Label(frame, text="Selecciona tus hobbies:").pack(anchor=tk.W)
        
        # Variables para cada checkbox
        self.hobby_deportes = tk.BooleanVar()
        self.hobby_musica = tk.BooleanVar()
        self.hobby_lectura = tk.BooleanVar()
        self.hobby_videojuegos = tk.BooleanVar()
        
        # Crear checkbuttons
        tk.Checkbutton(frame, text="Deportes", variable=self.hobby_deportes).pack(anchor=tk.W)
        tk.Checkbutton(frame, text="Música", variable=self.hobby_musica).pack(anchor=tk.W)
        tk.Checkbutton(frame, text="Lectura", variable=self.hobby_lectura).pack(anchor=tk.W)
        tk.Checkbutton(frame, text="Videojuegos", variable=self.hobby_videojuegos).pack(anchor=tk.W)
        
        tk.Button(frame, text="Ver Selección", 
                 command=self.ver_hobbies).pack(pady=5)
    
    def ver_hobbies(self):
        hobbies = []
        if self.hobby_deportes.get(): hobbies.append("Deportes")
        if self.hobby_musica.get(): hobbies.append("Música")
        if self.hobby_lectura.get(): hobbies.append("Lectura")
        if self.hobby_videojuegos.get(): hobbies.append("Videojuegos")
        
        if hobbies:
            messagebox.showinfo("Hobbies", "Seleccionaste: " + ", ".join(hobbies))
        else:
            messagebox.showinfo("Hobbies", "No seleccionaste ningún hobby")

# ==================== EJEMPLO 5: SCALE ====================
class EjemploScale:
    """Ejemplos de controles deslizantes"""
    def __init__(self, ventana):
        frame = tk.LabelFrame(ventana, text="SCALE (Deslizadores)", padx=10, pady=10)
        frame.pack(padx=10, pady=5, fill=tk.BOTH)
        
        # Scale horizontal
        tk.Label(frame, text="Volumen:").pack(anchor=tk.W)
        self.scale_volumen = tk.Scale(frame, from_=0, to=100, orient=tk.HORIZONTAL,
                                     command=self.actualizar_volumen)
        self.scale_volumen.set(50)
        self.scale_volumen.pack(fill=tk.X)
        
        self.label_volumen = tk.Label(frame, text="Volumen: 50%")
        self.label_volumen.pack()
        
        # Scale vertical
        tk.Label(frame, text="Temperatura:").pack(anchor=tk.W, pady=(10,0))
        self.scale_temp = tk.Scale(frame, from_=0, to=100, orient=tk.VERTICAL,
                                  command=self.actualizar_temperatura)
        self.scale_temp.set(25)
        self.scale_temp.pack()
        
        self.label_temp = tk.Label(frame, text="Temperatura: 25°C")
        self.label_temp.pack()
    
    def actualizar_volumen(self, valor):
        self.label_volumen.config(text=f"Volumen: {valor}%")
    
    def actualizar_temperatura(self, valor):
        self.label_temp.config(text=f"Temperatura: {valor}°C")

# ==================== EJEMPLO 6: CANVAS ====================
class EjemploCanvas:
    """Ejemplos de dibujo en Canvas"""
    def __init__(self, ventana):
        frame = tk.LabelFrame(ventana, text="CANVAS (Área de Dibujo)", padx=10, pady=10)
        frame.pack(padx=10, pady=5, fill=tk.BOTH)
        
        # Canvas
        self.canvas = tk.Canvas(frame, width=300, height=200, bg="white")
        self.canvas.pack()
        
        # Dibujar figuras
        self.canvas.create_rectangle(20, 20, 80, 80, fill="red", outline="black")
        self.canvas.create_oval(100, 20, 160, 80, fill="blue", outline="black")
        self.canvas.create_line(180, 20, 280, 80, fill="green", width=3)
        self.canvas.create_polygon(50, 120, 100, 180, 0, 180, fill="yellow", outline="black")
        self.canvas.create_text(200, 150, text="¡Canvas!", font=("Arial", 16, "bold"))
        
        # Botones
        btn_frame = tk.Frame(frame)
        btn_frame.pack()
        tk.Button(btn_frame, text="Limpiar", command=self.limpiar).pack(side=tk.LEFT, padx=2)
        tk.Button(btn_frame, text="Dibujar Círculo", command=self.dibujar_circulo).pack(side=tk.LEFT, padx=2)
    
    def limpiar(self):
        self.canvas.delete("all")
    
    def dibujar_circulo(self):
        import random
        x = random.randint(30, 270)
        y = random.randint(30, 170)
        self.canvas.create_oval(x-20, y-20, x+20, y+20, fill="purple")

# ==================== EJEMPLO 7: MENU ====================
class EjemploMenu:
    """Ejemplos de menús"""
    def __init__(self, ventana):
        # Crear barra de menú
        menubar = Menu(ventana)
        ventana.config(menu=menubar)
        
        # Menú Archivo
        menu_archivo = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Archivo", menu=menu_archivo)
        menu_archivo.add_command(label="Nuevo", command=self.nuevo)
        menu_archivo.add_command(label="Abrir", command=self.abrir)
        menu_archivo.add_command(label="Guardar", command=self.guardar)
        menu_archivo.add_separator()
        menu_archivo.add_command(label="Salir", command=ventana.quit)
        
        # Menú Editar
        menu_editar = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Editar", menu=menu_editar)
        menu_editar.add_command(label="Copiar", command=lambda: print("Copiar"))
        menu_editar.add_command(label="Pegar", command=lambda: print("Pegar"))
        
        # Menú Ayuda
        menu_ayuda = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Ayuda", menu=menu_ayuda)
        menu_ayuda.add_command(label="Acerca de", command=self.acerca_de)
    
    def nuevo(self):
        messagebox.showinfo("Archivo", "Nuevo archivo")
    
    def abrir(self):
        messagebox.showinfo("Archivo", "Abrir archivo")
    
    def guardar(self):
        messagebox.showinfo("Archivo", "Guardar archivo")
    
    def acerca_de(self):
        messagebox.showinfo("Acerca de", "Widgets Básicos POO\nVersión 1.0")

# ==================== APLICACION PRINCIPAL ====================
class AplicacionWidgets:
    """Aplicación que muestra todos los widgets básicos"""
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Widgets Básicos - POO")
        self.ventana.geometry("900x800")
        
        # Crear notebook (pestañas) para organizar mejor
        from tkinter import ttk
        notebook = ttk.Notebook(self.ventana)
        notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Página 1: Botones y Entry
        pagina1 = tk.Frame(notebook)
        notebook.add(pagina1, text="Botones & Entry")
        EjemploBotones(pagina1)
        EjemploEntry(pagina1)
        
        # Página 2: Radio y Check
        pagina2 = tk.Frame(notebook)
        notebook.add(pagina2, text="Radio & Check")
        EjemploRadiobutton(pagina2)
        EjemploCheckbutton(pagina2)
        
        # Página 3: Scale y Canvas
        pagina3 = tk.Frame(notebook)
        notebook.add(pagina3, text="Scale & Canvas")
        EjemploScale(pagina3)
        EjemploCanvas(pagina3)
        
        # Menú (aplicado a la ventana principal)
        EjemploMenu(self.ventana)
    
    def ejecutar(self):
        self.ventana.mainloop()

# ==================== EJECUTAR ====================
if __name__ == "__main__":
    app = AplicacionWidgets()
    app.ejecutar()

# ==================== CÓMO USAR ====================
# Este archivo es una REFERENCIA completa de todos los widgets básicos
# Usa las pestañas para ver cada categoría de widgets
#
# PARA TU EXAMEN:
# - Copia el código del widget que necesites
# - Modifica los textos, colores, comandos según necesites
# - Todos los widgets están comentados
#
# WIDGETS INCLUIDOS:
# 1. Button - Botones normales, con color, deshabilitados
# 2. Entry - Campos de texto, password, solo lectura
# 3. Radiobutton - Selección única entre opciones
# 4. Checkbutton - Selección múltiple
# 5. Scale - Deslizadores horizontales y verticales
# 6. Canvas - Área de dibujo con figuras
# 7. Menu - Menús desplegables
#
# TIPS RÁPIDOS:
# - Button: command=función
# - Entry: .get() para obtener texto, .insert() para poner texto
# - Radiobutton: usa StringVar() o IntVar()
# - Checkbutton: usa BooleanVar()
# - Scale: command se ejecuta al mover, .get() obtiene valor
# - Canvas: create_oval, create_rectangle, create_line, create_text
# - Menu: add_cascade para submenús, add_command para opciones