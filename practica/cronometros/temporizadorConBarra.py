import tkinter as tk

# Crear ventana - MODIFICAR: título
root = tk.Tk()
root.title("Temporizador con Barra")

# Crear canvas - MODIFICAR: ancho, alto, color fondo
canvas = tk.Canvas(root, width=600, height=400, bg="white")
canvas.pack()

# Variables globales
tiempo_total = 20  # tiempo total en segundos - MODIFICAR: duración del temporizador
tiempo_restante = tiempo_total
corriendo = False

# Dimensiones de la barra - MODIFICAR: tamaño y posición
barra_x = 50
barra_y = 200
barra_ancho = 500
barra_alto = 50

# Dibujar borde de la barra - MODIFICAR: outline (color borde), width
canvas.create_rectangle(barra_x, barra_y, barra_x + barra_ancho, barra_y + barra_alto,
                        outline="black", width=3)

# Dibujar barra de progreso (se irá achicando) - MODIFICAR: fill (color)
barra_id = canvas.create_rectangle(barra_x, barra_y, barra_x + barra_ancho, barra_y + barra_alto,
                                   fill="green", outline="")

# Texto del tiempo restante - MODIFICAR: posición, font, fill
texto_id = canvas.create_text(300, 120, text=f"{tiempo_restante} s",
                              font=("Arial", 50, "bold"), fill="black")

# Etiqueta superior - MODIFICAR: texto, posición, font
canvas.create_text(300, 50, text="Temporizador Regresivo",
                   font=("Arial", 20, "bold"), fill="darkblue")

# Función que actualiza el temporizador
def actualizar_temporizador():
    global tiempo_restante, corriendo
    
    if corriendo and tiempo_restante > 0:
        # Decrementar tiempo - MODIFICAR: -1 para cada segundo
        tiempo_restante -= 1
        
        # Actualizar texto
        canvas.itemconfig(texto_id, text=f"{tiempo_restante} s")
        
        # Calcular porcentaje restante
        porcentaje = tiempo_restante / tiempo_total
        
        # Calcular nuevo ancho de la barra
        nuevo_ancho = barra_ancho * porcentaje
        
        # Actualizar barra - MODIFICAR: coordenadas
        canvas.coords(barra_id, barra_x, barra_y, 
                     barra_x + nuevo_ancho, barra_y + barra_alto)
        
        # Cambiar color según tiempo restante - MODIFICAR: umbrales y colores
        if tiempo_restante <= 3:
            canvas.itemconfig(barra_id, fill="red")  # rojo cuando quedan 3 o menos
        elif tiempo_restante <= 6:
            canvas.itemconfig(barra_id, fill="orange")  # naranja en la mitad
        else:
            canvas.itemconfig(barra_id, fill="green")  # verde al inicio
        
        # Llamar cada 1000ms (1 segundo) - MODIFICAR: velocidad
        root.after(1000, actualizar_temporizador)
    
    elif tiempo_restante <= 0:
        # Cuando llega a 0
        corriendo = False
        canvas.itemconfig(texto_id, text="¡TIEMPO!", fill="red")
        # Opcional: hacer parpadear
        parpadear_final()

# Función para parpadear al terminar - MODIFICAR: colores y velocidad
def parpadear_final():
    color_actual = canvas.itemcget(texto_id, "fill")
    nuevo_color = "black" if color_actual == "red" else "red"
    canvas.itemconfig(texto_id, fill=nuevo_color)
    if tiempo_restante <= 0:
        root.after(500, parpadear_final)  # parpadear cada 500ms

# Función para iniciar
def iniciar():
    global corriendo
    if not corriendo and tiempo_restante > 0:
        corriendo = True
        actualizar_temporizador()

# Función para pausar
def pausar():
    global corriendo
    corriendo = False

# Función para reiniciar
def reiniciar():
    global tiempo_restante, corriendo
    corriendo = False
    tiempo_restante = tiempo_total
    canvas.itemconfig(texto_id, text=f"{tiempo_restante} s", fill="black")
    canvas.coords(barra_id, barra_x, barra_y, barra_x + barra_ancho, barra_y + barra_alto)
    canvas.itemconfig(barra_id, fill="green")

# Frame para botones - MODIFICAR: bg
frame_botones = tk.Frame(root, bg="white")
frame_botones.pack(pady=20)

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

# Iniciar ventana
root.mainloop()