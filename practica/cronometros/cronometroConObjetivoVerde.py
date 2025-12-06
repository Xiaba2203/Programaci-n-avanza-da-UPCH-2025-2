import tkinter as tk

# Crear ventana - MODIFICAR: título
root = tk.Tk()
root.title("Cronómetro con Objetivo")

# Crear canvas - MODIFICAR: ancho, alto, color fondo
canvas = tk.Canvas(root, width=500, height=450, bg="white")
canvas.pack()

# Variables globales
segundos = 0
corriendo = False
objetivo = 10  # tiempo objetivo en segundos - MODIFICAR: meta a alcanzar
objetivo_alcanzado = False

# Texto del cronómetro - MODIFICAR: posición, font, fill
texto_id = canvas.create_text(250, 120, text="0 s",
                              font=("Arial", 60, "bold"), fill="black")

# Texto del objetivo - MODIFICAR: posición, font, fill
texto_objetivo_id = canvas.create_text(250, 200, text=f"Objetivo: {objetivo} s",
                                       font=("Arial", 20), fill="gray")

# Indicador visual del objetivo (círculo) - MODIFICAR: posición y tamaño
indicador_id = canvas.create_oval(210, 250, 290, 330, fill="red", outline="darkred", width=3)
texto_indicador_id = canvas.create_text(250, 290, text="NO", 
                                        font=("Arial", 30, "bold"), fill="white")

# Función que actualiza el cronómetro
def actualizar_cronometro():
    global segundos, corriendo, objetivo_alcanzado
    
    if corriendo:
        # Incrementar segundos - MODIFICAR: +1 para cada segundo
        segundos += 1
        
        # Actualizar texto
        canvas.itemconfig(texto_id, text=f"{segundos} s")
        
        # Verificar si alcanzó el objetivo - MODIFICAR: condición
        if segundos >= objetivo and not objetivo_alcanzado:
            objetivo_alcanzado = True
            # Cambiar a verde - MODIFICAR: colores
            canvas.itemconfig(indicador_id, fill="green", outline="darkgreen")
            canvas.itemconfig(texto_indicador_id, text="SÍ", fill="white")
            canvas.itemconfig(texto_id, fill="green")
            # Efecto de celebración
            celebrar()
        
        # Llamar cada 1000ms (1 segundo) - MODIFICAR: velocidad
        root.after(1000, actualizar_cronometro)

# Función de celebración (parpadeo y mensaje) - MODIFICAR: efecto
def celebrar():
    # Mostrar mensaje temporal
    mensaje_id = canvas.create_text(250, 360, text="🎉 ¡Objetivo alcanzado! 🎉",
                                    font=("Arial", 16, "bold"), fill="green")
    # Hacer parpadear el indicador
    def parpadear(veces=6):
        if veces > 0:
            color_actual = canvas.itemcget(indicador_id, "fill")
            nuevo_color = "lightgreen" if color_actual == "green" else "green"
            canvas.itemconfig(indicador_id, fill=nuevo_color)
            root.after(200, lambda: parpadear(veces - 1))
    parpadear()

# Función para iniciar
def iniciar():
    global corriendo
    if not corriendo:
        corriendo = True
        actualizar_cronometro()

# Función para pausar
def pausar():
    global corriendo
    corriendo = False

# Función para reiniciar
def reiniciar():
    global segundos, corriendo, objetivo_alcanzado
    corriendo = False
    segundos = 0
    objetivo_alcanzado = False
    canvas.itemconfig(texto_id, text="0 s", fill="black")
    canvas.itemconfig(indicador_id, fill="red", outline="darkred")
    canvas.itemconfig(texto_indicador_id, text="NO", fill="white")
    # Limpiar mensajes de celebración
    canvas.delete("mensaje")

# Frame para botones - MODIFICAR: bg
frame_botones = tk.Frame(root, bg="white")
frame_botones.pack(pady=15)

# Botones - MODIFICAR: texto, colores, font
boton_iniciar = tk.Button(frame_botones, text="▶ Iniciar", command=iniciar,
                          font=("Arial", 12, "bold"), bg="green", fg="white", width=10)
boton_iniciar.grid(row=0, column=0, padx=5)

boton_pausar = tk.Button(frame_botones, text="⏸ Pausar", command=pausar,
                         font=("Arial", 12, "bold"), bg="orange", fg="white", width=10)
boton_pausar.grid(row=0, column=1, padx=5)

boton_reiniciar = tk.Button(frame_botones, text="⏹ Reiniciar", command=reiniciar,
                            font=("Arial", 12, "bold"), bg="red", fg="white", width=10)
boton_reiniciar.grid(row=0, column=2, padx=5)

# Frame para cambiar objetivo - MODIFICAR: opciones
frame_objetivo = tk.Frame(root, bg="white")
frame_objetivo.pack(pady=10)

tk.Label(frame_objetivo, text="Cambiar objetivo:", font=("Arial", 10)).pack(side=tk.LEFT, padx=5)

def cambiar_objetivo(nuevo):
    global objetivo, objetivo_alcanzado
    if not corriendo:  # solo se puede cambiar si no está corriendo
        objetivo = nuevo
        canvas.itemconfig(texto_objetivo_id, text=f"Objetivo: {objetivo} s")
        objetivo_alcanzado = False

# Botones de objetivos predefinidos - MODIFICAR: valores
tk.Button(frame_objetivo, text="5s", command=lambda: cambiar_objetivo(5),
          font=("Arial", 9), bg="lightblue").pack(side=tk.LEFT, padx=2)
tk.Button(frame_objetivo, text="10s", command=lambda: cambiar_objetivo(10),
          font=("Arial", 9), bg="lightgreen").pack(side=tk.LEFT, padx=2)
tk.Button(frame_objetivo, text="20s", command=lambda: cambiar_objetivo(20),
          font=("Arial", 9), bg="lightcoral").pack(side=tk.LEFT, padx=2)
tk.Button(frame_objetivo, text="30s", command=lambda: cambiar_objetivo(30),
          font=("Arial", 9), bg="lightyellow").pack(side=tk.LEFT, padx=2)

# Iniciar ventana
root.mainloop()