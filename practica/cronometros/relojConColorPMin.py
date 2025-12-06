import tkinter as tk
import time

# Crear ventana - MODIFICAR: título
root = tk.Tk()
root.title("Reloj Digital Colorido")

# Crear canvas - MODIFICAR: ancho, alto, color fondo
canvas = tk.Canvas(root, width=600, height=300, bg="black")
canvas.pack()

# Lista de colores para cada minuto - MODIFICAR: agregar o cambiar colores
colores = [
    "red", "orange", "yellow", "lime", "green", "cyan",
    "blue", "purple", "magenta", "pink", "white", "gold"
]

# Variable para recordar el último minuto
ultimo_minuto = -1

# Texto del reloj - MODIFICAR: posición, font
texto_reloj_id = canvas.create_text(300, 120, text="00:00:00",
                                    font=("Digital-7", 80, "bold"), fill="lime")
# Si no tienes Digital-7, usa: font=("Courier", 80, "bold")

# Texto de la fecha - MODIFICAR: posición, font, fill
texto_fecha_id = canvas.create_text(300, 200, text="",
                                    font=("Arial", 16), fill="gray")

# Función que actualiza el reloj
def actualizar_reloj():
    global ultimo_minuto
    
    # Obtener hora actual del sistema
    hora_actual = time.strftime("%H:%M:%S")  # formato HH:MM:SS
    fecha_actual = time.strftime("%d/%m/%Y")  # formato DD/MM/YYYY
    
    # Obtener minuto actual (0-59)
    minuto_actual = int(time.strftime("%M"))
    
    # Actualizar texto del reloj
    canvas.itemconfig(texto_reloj_id, text=hora_actual)
    canvas.itemconfig(texto_fecha_id, text=fecha_actual)
    
    # Si cambió el minuto, cambiar el color - MODIFICAR: lógica del cambio
    if minuto_actual != ultimo_minuto:
        ultimo_minuto = minuto_actual
        
        # Elegir color según el minuto (módulo para ciclar la lista)
        # MODIFICAR: índice para otra forma de elegir color
        indice_color = minuto_actual % len(colores)
        color_nuevo = colores[indice_color]
        
        # Cambiar color del reloj - MODIFICAR: aplicar a otros elementos
        canvas.itemconfig(texto_reloj_id, fill=color_nuevo)
        
        # Efecto de transición (parpadeo rápido) - MODIFICAR: efecto
        def efecto_cambio(veces=3):
            if veces > 0:
                canvas.itemconfig(texto_reloj_id, fill="white")
                root.after(100, lambda: canvas.itemconfig(texto_reloj_id, fill=color_nuevo))
                root.after(200, lambda: efecto_cambio(veces - 1))
        
        efecto_cambio()
    
    # Actualizar cada 100ms para mayor precisión - MODIFICAR: frecuencia
    root.after(100, actualizar_reloj)

# Etiqueta informativa - MODIFICAR: texto, font, colores
label_info = tk.Label(root, text="El color cambia cada minuto",
                      font=("Arial", 12), fg="white", bg="black")
label_info.pack(pady=10)

# Mostrar el minuto actual y su color - MODIFICAR: formato
def mostrar_info_color():
    minuto = int(time.strftime("%M"))
    indice = minuto % len(colores)
    color = colores[indice]
    label_color_info.config(text=f"Minuto actual: {minuto} | Color: {color.upper()}")
    root.after(1000, mostrar_info_color)

label_color_info = tk.Label(root, text="", font=("Arial", 10), fg="gray", bg="black")
label_color_info.pack()

mostrar_info_color()

# Tabla de colores (referencia visual) - MODIFICAR: mostrar u ocultar
frame_colores = tk.Frame(root, bg="black")
frame_colores.pack(pady=10)

tk.Label(frame_colores, text="Paleta de colores:", font=("Arial", 10),
         fg="white", bg="black").pack()

# Mostrar los primeros 12 colores como referencia
frame_muestras = tk.Frame(frame_colores, bg="black")
frame_muestras.pack()

for i, color in enumerate(colores[:12]):
    # Crear un pequeño canvas para cada color - MODIFICAR: tamaño
    mini_canvas = tk.Canvas(frame_muestras, width=30, height=20, bg=color,
                           highlightthickness=1, highlightbackground="white")
    mini_canvas.grid(row=0, column=i, padx=2)
    # Etiqueta con el número - MODIFICAR: font
    tk.Label(frame_muestras, text=str(i), font=("Arial", 7),
             fg="white", bg="black").grid(row=1, column=i)

# Iniciar actualización del reloj
actualizar_reloj()

# Iniciar ventana
root.mainloop()