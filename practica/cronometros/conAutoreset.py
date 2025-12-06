import tkinter as tk

# Crear ventana - MODIFICAR: título
root = tk.Tk()
root.title("Cronómetro Auto-Reset")

# Crear canvas - MODIFICAR: ancho, alto, color fondo
canvas = tk.Canvas(root, width=600, height=400, bg="lightgray")
canvas.pack()

# Variables globales
segundos = 0
corriendo = False
limite_reset = 15  # se resetea al llegar a este valor - MODIFICAR: umbral de reset

# Texto del cronómetro - MODIFICAR: posición, font, fill
texto_id = canvas.create_text(300, 120, text="0 s",
                              font=("Arial", 70, "bold"), fill="black")

# Etiqueta superior - MODIFICAR: texto, posición
canvas.create_text(300, 50, text="Cronómetro con Auto-Reset",
                   font=("Arial", 20, "bold"), fill="darkblue")

# Texto del límite - MODIFICAR: posición, font
texto_limite_id = canvas.create_text(300, 200, text=f"Se reinicia al llegar a {limite_reset} segundos",
                                     font=("Arial", 14), fill="red")

# Barra de progreso hacia el reset - MODIFICAR: posición y tamaño
barra_x, barra_y = 50, 250
barra_ancho, barra_alto = 500, 30
canvas.create_rectangle(barra_x, barra_y, barra_x + barra_ancho, barra_y + barra_alto,
                        outline="black", width=2)
barra_id = canvas.create_rectangle(barra_x, barra_y, barra_x, barra_y + barra_alto,
                                   fill="blue", outline="")

# Función que actualiza el cronómetro
def actualizar_cronometro():
    global segundos, corriendo
    
    if corriendo:
        # Incrementar segundos - MODIFICAR: velocidad
        segundos += 1
        
        # Actualizar texto
        canvas.itemconfig(texto_id, text=f"{segundos} s")
        
        # Calcular porcentaje hacia el límite
        porcentaje = segundos / limite_reset
        
        # Actualizar barra de progreso
        nuevo_ancho = barra_ancho * porcentaje
        canvas.coords(barra_id, barra_x, barra_y, barra_x + nuevo_ancho, barra_y + barra_alto)
        
        # Cambiar color según proximidad al límite - MODIFICAR: colores y umbrales
        if porcentaje < 0.33:
            canvas.itemconfig(barra_id, fill="green")
            canvas.itemconfig(texto_id, fill="green")
        elif porcentaje < 0.66:
            canvas.itemconfig(barra_id, fill="yellow")
            canvas.itemconfig(texto_id, fill="orange")
        else:
            canvas.itemconfig(barra_id, fill="red")
            canvas.itemconfig(texto_id, fill="red")
        
        # Verificar si llegó al límite - MODIFICAR: condición de reset
        if segundos >= limite_reset:
            # Auto-reset con efecto visual
            realizar_reset()
            return  # no continuar actualizando hasta que se reinicie
        
        # Llamar cada 1000ms (1 segundo) - MODIFICAR: velocidad
        root.after(1000, actualizar_cronometro)

# Función que realiza el reset automático - MODIFICAR: efectos
def realizar_reset():
    global segundos, corriendo
    
    # Mostrar mensaje de reset - MODIFICAR: texto y posición
    mensaje_id = canvas.create_text(300, 320, text="¡AUTO-RESET!",
                                    font=("Arial", 30, "bold"), fill="red", tags="mensaje")
    
    # Efecto de parpadeo - MODIFICAR: velocidad y veces
    def parpadear(veces=6):
        if veces > 0:
            color = canvas.itemcget(texto_id, "fill")
            nuevo_color = "white" if color == "red" else "red"
            canvas.itemconfig(texto_id, fill=nuevo_color)
            root.after(200, lambda: parpadear(veces - 1))
        else:
            # Después del parpadeo, reiniciar
            segundos = 0
            canvas.itemconfig(texto_id, text="0 s", fill="black")
            canvas.coords(barra_id, barra_x, barra_y, barra_x, barra_y + barra_alto)
            canvas.itemconfig(barra_id, fill="blue")
            canvas.delete("mensaje")
            # Continuar contando si estaba corriendo
            if corriendo:
                actualizar_cronometro()
    
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

# Función para reiniciar manual
def reiniciar_manual():
    global segundos, corriendo
    corriendo = False
    segundos = 0
    canvas.itemconfig(texto_id, text="0 s", fill="black")
    canvas.coords(barra_id, barra_x, barra_y, barra_x, barra_y + barra_alto)
    canvas.itemconfig(barra_id, fill="blue")
    canvas.delete("mensaje")

# Frame para botones - MODIFICAR: bg
frame_botones = tk.Frame(root, bg="lightgray")
frame_botones.pack(pady=15)

# Botones - MODIFICAR: texto, colores, font
boton_iniciar = tk.Button(frame_botones, text="▶ Iniciar", command=iniciar,
                          font=("Arial", 12, "bold"), bg="green", fg="white", width=12)
boton_iniciar.grid(row=0, column=0, padx=5)

boton_pausar = tk.Button(frame_botones, text="⏸ Pausar", command=pausar,
                         font=("Arial", 12, "bold"), bg="orange", fg="white", width=12)
boton_pausar.grid(row=0, column=1, padx=5)

boton_reiniciar = tk.Button(frame_botones, text="⏹ Reiniciar", command=reiniciar_manual,
                            font=("Arial", 12, "bold"), bg="red", fg="white", width=12)
boton_reiniciar.grid(row=0, column=2, padx=5)

# Frame para cambiar límite - MODIFICAR: opciones
frame_limite = tk.Frame(root, bg="lightgray")
frame_limite.pack(pady=10)

tk.Label(frame_limite, text="Cambiar límite de reset:", font=("Arial", 10),
         bg="lightgray").pack(side=tk.LEFT, padx=5)

def cambiar_limite(nuevo):
    global limite_reset, segundos
    if not corriendo:  # solo cambiar si no está corriendo
        limite_reset = nuevo
        canvas.itemconfig(texto_limite_id, text=f"Se reinicia al llegar a {limite_reset} segundos")
        if segundos >= limite_reset:
            segundos = 0
            canvas.itemconfig(texto_id, text="0 s")

# Botones de límites predefinidos - MODIFICAR: valores
for valor in [10, 15, 20, 30, 60]:
    tk.Button(frame_limite, text=f"{valor}s", command=lambda v=valor: cambiar_limite(v),
              font=("Arial", 9), bg="lightblue", width=5).pack(side=tk.LEFT, padx=2)

# Iniciar ventana
root.mainloop()