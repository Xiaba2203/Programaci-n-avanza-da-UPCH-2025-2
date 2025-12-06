import tkinter as tk
import math

# Crear ventana - MODIFICAR: título
root = tk.Tk()
root.title("Cronómetro con Control de Animación")

# Crear canvas - MODIFICAR: ancho, alto, color fondo
canvas = tk.Canvas(root, width=600, height=500, bg="white")
canvas.pack()

# Variables globales del cronómetro
segundos = 0
corriendo_crono = False

# Variables de la animación
animacion_activa = True
angulo_pelota = 0

# ===== CRONÓMETRO (parte superior) =====
# Texto del cronómetro - MODIFICAR: posición, font, fill
texto_crono_id = canvas.create_text(350, 60, text="00:00",
                                    font=("Arial", 50, "bold"), fill="darkblue")

canvas.create_text(350, 20, text="CRONÓMETRO",
                   font=("Arial", 16, "bold"), fill="black")

# ===== ANIMACIÓN (círculo que gira) =====
# Centro y radio de la órbita - MODIFICAR: posición y tamaño
centro_x, centro_y = 350, 350
radio_orbita = 150

# Crear pelota que gira - MODIFICAR: tamaño y color
pelota_id = canvas.create_oval(0, 0, 30, 30, fill="red", outline="black", width=2)

# Círculo de la órbita (guía visual) - MODIFICAR: color
canvas.create_oval(centro_x - radio_orbita, centro_y - radio_orbita,
                   centro_x + radio_orbita, centro_y + radio_orbita,
                   outline="lightgray", width=2, dash=(5, 3))

# Texto de estado de animación - MODIFICAR: posición, font
texto_anim_id = canvas.create_text(350, 520, text="Animación: ACTIVA",
                                   font=("Arial", 14, "bold"), fill="green")

# Función que actualiza el cronómetro
def actualizar_cronometro():
    global segundos, corriendo_crono, animacion_activa
    
    if corriendo_crono:
        # Incrementar segundos - MODIFICAR: velocidad
        segundos += 1
        
        # Formatear como MM:SS - MODIFICAR: formato
        minutos = segundos // 60
        segs = segundos % 60
        texto = f"{minutos:02d}:{segs:02d}"
        canvas.itemconfig(texto_crono_id, text=texto)
        
        # Detener animación al llegar a cierto tiempo - MODIFICAR: umbral
        if segundos >= 10 and animacion_activa:
            animacion_activa = False
            canvas.itemconfig(texto_anim_id, text="Animación: DETENIDA", fill="red")
            # Efecto visual
            canvas.itemconfig(texto_crono_id, fill="red")
        
        # Llamar cada 1000ms - MODIFICAR: velocidad
        root.after(1000, actualizar_cronometro)

# Función que anima la pelota
def animar_pelota():
    global angulo_pelota, animacion_activa, corriendo_crono

    # Solo animar si el cronómetro está corriendo o la animación está activa manualmente
    if corriendo_crono or animacion_activa:
        if animacion_activa:
            # Incrementar ángulo - MODIFICAR: velocidad de rotación
            angulo_pelota += 2  # grados por frame

            # Calcular nueva posición en círculo
            angulo_rad = math.radians(angulo_pelota)
            x = centro_x + radio_orbita * math.cos(angulo_rad)
            y = centro_y + radio_orbita * math.sin(angulo_rad)

            # Mover la pelota - MODIFICAR: tamaño (15 es el radio)
            canvas.coords(pelota_id, x - 15, y - 15, x + 15, y + 15)

            # Cambiar color según posición - MODIFICAR: colores
            if angulo_pelota % 360 < 90:
                canvas.itemconfig(pelota_id, fill="red")
            elif angulo_pelota % 360 < 180:
                canvas.itemconfig(pelota_id, fill="blue")
            elif angulo_pelota % 360 < 270:
                canvas.itemconfig(pelota_id, fill="green")
            else:
                canvas.itemconfig(pelota_id, fill="yellow")
    # Llamar cada 20ms (50 FPS) - MODIFICAR: velocidad de animación
    root.after(20, animar_pelota)

# Funciones de control del cronómetro
def iniciar_crono():
    global corriendo_crono
    if not corriendo_crono:
        corriendo_crono = True
        actualizar_cronometro()

def pausar_crono():
    global corriendo_crono
    corriendo_crono = False

def reiniciar_crono():
    global segundos, corriendo_crono, animacion_activa
    corriendo_crono = False
    segundos = 0
    animacion_activa = True
    canvas.itemconfig(texto_crono_id, text="00:00", fill="darkblue")
    canvas.itemconfig(texto_anim_id, text="Animación: ACTIVA", fill="green")

# Función para toggle manual de animación
def toggle_animacion():
    global animacion_activa
    animacion_activa = not animacion_activa
    if animacion_activa:
        canvas.itemconfig(texto_anim_id, text="Animación: ACTIVA", fill="green")
    else:
        canvas.itemconfig(texto_anim_id, text="Animación: DETENIDA", fill="red")

# Frame para botones del cronómetro - MODIFICAR: bg
frame_crono = tk.Frame(root, bg="white")
frame_crono.pack(pady=10)

tk.Label(frame_crono, text="Control Cronómetro:", font=("Arial", 11, "bold"),
         bg="white").grid(row=0, column=0, columnspan=3, pady=5)

# Botones del cronómetro - MODIFICAR: texto, colores
boton_iniciar = tk.Button(frame_crono, text="▶ Iniciar", command=iniciar_crono,
                          font=("Arial", 11, "bold"), bg="green", fg="white", width=10)
boton_iniciar.grid(row=1, column=0, padx=5)

boton_pausar = tk.Button(frame_crono, text="⏸ Pausar", command=pausar_crono,
                         font=("Arial", 11, "bold"), bg="orange", fg="white", width=10)
boton_pausar.grid(row=1, column=1, padx=5)

boton_reiniciar = tk.Button(frame_crono, text="⏹ Reiniciar", command=reiniciar_crono,
                            font=("Arial", 11, "bold"), bg="red", fg="white", width=10)
boton_reiniciar.grid(row=1, column=2, padx=5)

# Botón para control manual de animación - MODIFICAR: texto, color
boton_toggle_anim = tk.Button(root, text="🔄 Activar/Desactivar Animación", 
                              command=toggle_animacion,
                              font=("Arial", 12, "bold"), bg="purple", fg="white",
                              width=30)
boton_toggle_anim.pack(pady=10)

# Etiqueta informativa - MODIFICAR: texto
label_info = tk.Label(root, text="La animación se detiene automáticamente a los 10 segundos",
                      font=("Arial", 10), fg="gray")
label_info.pack()

# Iniciar la animación
animar_pelota()

# Llamar al cronómetro para que esté listo para iniciar con el botón
actualizar_cronometro()

# Iniciar ventana
root.mainloop()