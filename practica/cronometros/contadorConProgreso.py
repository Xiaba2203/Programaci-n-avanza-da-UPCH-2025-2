import tkinter as tk

# Crear ventana - MODIFICAR: título
root = tk.Tk()
root.title("Temporizador con Mensajes")

# Crear canvas - MODIFICAR: ancho, alto, color fondo
canvas = tk.Canvas(root, width=600, height=400, bg="white")
canvas.pack()

# Variables globales
tiempo_total = 12  # tiempo total en segundos - MODIFICAR: duración total
tiempo_actual = 0
corriendo = False

# Texto del tiempo - MODIFICAR: posición, font, fill
texto_tiempo_id = canvas.create_text(300, 120, text="0 s",
                                     font=("Arial", 50, "bold"), fill="black")

# Texto del mensaje de progreso - MODIFICAR: posición, font, fill
texto_mensaje_id = canvas.create_text(300, 220, text="",
                                      font=("Arial", 30, "bold"), fill="blue")

# Barra de progreso visual - MODIFICAR: posición y tamaño
barra_x, barra_y = 50, 300
barra_ancho, barra_alto = 500, 40
canvas.create_rectangle(barra_x, barra_y, barra_x + barra_ancho, barra_y + barra_alto,
                        outline="black", width=2)
barra_id = canvas.create_rectangle(barra_x, barra_y, barra_x, barra_y + barra_alto,
                                   fill="dodgerblue", outline="")

# Función que actualiza el temporizador
def actualizar_tiempo():
    global tiempo_actual, corriendo
    
    if corriendo and tiempo_actual < tiempo_total:
        # Incrementar tiempo - MODIFICAR: +1 para cada segundo
        tiempo_actual += 1
        
        # Actualizar texto del tiempo
        canvas.itemconfig(texto_tiempo_id, text=f"{tiempo_actual} s")
        
        # Calcular porcentaje de progreso
        porcentaje = tiempo_actual / tiempo_total
        
        # Actualizar barra de progreso
        nuevo_ancho = barra_ancho * porcentaje
        canvas.coords(barra_id, barra_x, barra_y, barra_x + nuevo_ancho, barra_y + barra_alto)
        
        # Determinar mensaje según el progreso - MODIFICAR: umbrales y mensajes
        if tiempo_actual == 1:
            canvas.itemconfig(texto_mensaje_id, text="🚀 INICIO", fill="green")
        elif tiempo_actual == tiempo_total // 2:  # mitad del tiempo
            canvas.itemconfig(texto_mensaje_id, text="⏱️ MITAD", fill="orange")
        elif tiempo_actual == tiempo_total:  # final del tiempo
            canvas.itemconfig(texto_mensaje_id, text="🏁 FIN", fill="red")
            corriendo = False
            parpadear_mensaje()
        
        # Cambiar color de barra según progreso - MODIFICAR: colores y umbrales
        if porcentaje < 0.33:
            canvas.itemconfig(barra_id, fill="green")
        elif porcentaje < 0.66:
            canvas.itemconfig(barra_id, fill="yellow")
        else:
            canvas.itemconfig(barra_id, fill="orange")
        
        # Llamar cada 1000ms (1 segundo) - MODIFICAR: velocidad
        root.after(1000, actualizar_tiempo)

# Función para hacer parpadear el mensaje final
def parpadear_mensaje():
    if tiempo_actual >= tiempo_total:
        color_actual = canvas.itemcget(texto_mensaje_id, "fill")
        nuevo_color = "white" if color_actual == "red" else "red"
        canvas.itemconfig(texto_mensaje_id, fill=nuevo_color)
        root.after(500, parpadear_mensaje)

# Función para iniciar
def iniciar():
    global corriendo
    if not corriendo and tiempo_actual < tiempo_total:
        corriendo = True
        actualizar_tiempo()

# Función para pausar
def pausar():
    global corriendo
    corriendo = False

# Función para reiniciar
def reiniciar():
    global tiempo_actual, corriendo
    corriendo = False
    tiempo_actual = 0
    canvas.itemconfig(texto_tiempo_id, text="0 s", fill="black")
    canvas.itemconfig(texto_mensaje_id, text="", fill="blue")
    canvas.coords(barra_id, barra_x, barra_y, barra_x, barra_y + barra_alto)
    canvas.itemconfig(barra_id, fill="dodgerblue")

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

# Etiqueta informativa - MODIFICAR: texto
label_info = tk.Label(root, text=f"Duración total: {tiempo_total} segundos",
                      font=("Arial", 10), fg="gray")
label_info.pack()

# Iniciar ventana
root.mainloop()