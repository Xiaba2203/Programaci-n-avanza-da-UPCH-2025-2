import tkinter as tk
import math

# Crear ventana - MODIFICAR: título
root = tk.Tk()
root.title("Rueda Dentada")

# Crear canvas - MODIFICAR: ancho, alto, color fondo
canvas = tk.Canvas(root, width=600, height=600, bg="lightgray")
canvas.pack()

# Centro de la rueda - MODIFICAR: para mover la rueda
cx = 300
cy = 300

# Radio interior de la rueda - MODIFICAR: tamaño del círculo central
radio_interior = 80

# Radio exterior de la rueda - MODIFICAR: tamaño total de la rueda
radio_exterior = 200

# Número de dientes - MODIFICAR: cantidad de dientes
num_dientes = 12

# Tamaño de cada diente - MODIFICAR: alto y ancho del diente
ancho_diente = 20
alto_diente = 30

# Dibujar círculo interior - MODIFICAR: fill (color), outline (borde), width
canvas.create_oval(cx - radio_interior, cy - radio_interior,
                   cx + radio_interior, cy + radio_interior,
                   fill="gray", outline="black", width=3)

# Dibujar círculo de base (donde se conectan los dientes) - MODIFICAR: fill y outline
canvas.create_oval(cx - radio_exterior, cy - radio_exterior,
                   cx + radio_exterior, cy + radio_exterior,
                   fill="darkgray", outline="black", width=2)

# Dibujar los dientes
for i in range(num_dientes):
    # Calcular ángulo de cada diente
    angulo = (360 / num_dientes) * i
    angulo_rad = math.radians(angulo)
    
    # Posición del centro del diente (en el radio exterior)
    x_centro = cx + radio_exterior * math.cos(angulo_rad)
    y_centro = cy + radio_exterior * math.sin(angulo_rad)
    
    # Calcular esquinas del rectángulo del diente
    # Los dientes apuntan hacia afuera
    x1 = x_centro + (radio_exterior * 0.2) * math.cos(angulo_rad) - ancho_diente/2 * math.sin(angulo_rad)
    y1 = y_centro + (radio_exterior * 0.2) * math.sin(angulo_rad) + ancho_diente/2 * math.cos(angulo_rad)
    
    x2 = x_centro + (radio_exterior * 0.2) * math.cos(angulo_rad) + ancho_diente/2 * math.sin(angulo_rad)
    y2 = y_centro + (radio_exterior * 0.2) * math.sin(angulo_rad) - ancho_diente/2 * math.cos(angulo_rad)
    
    x3 = x_centro - ancho_diente/2 * math.sin(angulo_rad)
    y3 = y_centro + ancho_diente/2 * math.cos(angulo_rad)
    
    x4 = x_centro + ancho_diente/2 * math.sin(angulo_rad)
    y4 = y_centro - ancho_diente/2 * math.cos(angulo_rad)
    
    # Dibujar diente como polígono - MODIFICAR: fill (color), outline, width
    canvas.create_polygon(x3, y3, x4, y4, x1, y1, x2, y2,
                         fill="silver", outline="black", width=2)

# Dibujar círculo central decorativo - MODIFICAR: tamaño y fill
canvas.create_oval(cx - 20, cy - 20, cx + 20, cy + 20,
                   fill="yellow", outline="black", width=2)

# Dibujar radios desde el centro - MODIFICAR: cantidad y estilo
for i in range(num_dientes):
    angulo = (360 / num_dientes) * i
    angulo_rad = math.radians(angulo)
    
    x_fin = cx + radio_interior * math.cos(angulo_rad)
    y_fin = cy + radio_interior * math.sin(angulo_rad)
    
    # Línea desde centro al borde interior - MODIFICAR: fill, width
    canvas.create_line(cx, cy, x_fin, y_fin, fill="black", width=2)

# Texto decorativo - MODIFICAR: texto, font, fill
canvas.create_text(cx, cy + radio_exterior + 50,
                   text=f"Rueda con {num_dientes} dientes",
                   font=("Arial", 14, "bold"), fill="black")

# Iniciar ventana
root.mainloop()