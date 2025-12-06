import tkinter as tk
import math

# Crear ventana - MODIFICAR: título
root = tk.Tk()
root.title("Flor con Pétalos")

# Crear canvas - MODIFICAR: ancho, alto, color fondo
canvas = tk.Canvas(root, width=500, height=600, bg="lightgreen")
canvas.pack()

# Centro de la flor - MODIFICAR: para mover toda la flor
cx = 250
cy = 250

# Tallo (línea gruesa verde) - MODIFICAR: posición, color fill, width (grosor)
canvas.create_line(cx, cy + 50, cx, cy + 300, fill="green", width=8)

# Hoja izquierda (óvalo verde) - MODIFICAR: posición, tamaño y fill
canvas.create_oval(cx - 60, cy + 150, cx - 20, cy + 200, fill="darkgreen", outline="green", width=2)

# Hoja derecha (óvalo verde) - MODIFICAR: posición, tamaño y fill
canvas.create_oval(cx + 20, cy + 200, cx + 60, cy + 250, fill="darkgreen", outline="green", width=2)

# Dibujar 8 pétalos en círculo - MODIFICAR: range(8) para más o menos pétalos
num_petalos = 8
for i in range(num_petalos):
    # Calcular ángulo de cada pétalo - MODIFICAR: matemática del ángulo
    angulo = (360 / num_petalos) * i
    angulo_rad = math.radians(angulo)
    
    # Distancia del centro al pétalo - MODIFICAR: este número
    distancia = 60
    
    # Calcular posición del pétalo
    x_petalo = cx + distancia * math.cos(angulo_rad)
    y_petalo = cy + distancia * math.sin(angulo_rad)
    
    # Tamaño del pétalo (óvalo) - MODIFICAR: ancho y alto
    ancho = 40
    alto = 70
    
    # Dibujar pétalo (óvalo) - MODIFICAR: fill (color), outline (borde)
    canvas.create_oval(x_petalo - ancho/2, y_petalo - alto/2,
                       x_petalo + ancho/2, y_petalo + alto/2,
                       fill="pink", outline="hotpink", width=2)

# Centro de la flor (círculo amarillo) - MODIFICAR: radio y fill
radio_centro = 50
canvas.create_oval(cx - radio_centro, cy - radio_centro,
                   cx + radio_centro, cy + radio_centro,
                   fill="yellow", outline="orange", width=3)

# Puntos en el centro (círculos pequeños) - MODIFICAR: cantidad y distribución
import random
for _ in range(20):  # MODIFICAR: cantidad de puntos
    # Posición aleatoria dentro del centro
    px = cx + random.randint(-40, 40)
    py = cy + random.randint(-40, 40)
    # Dibujar punto pequeño - MODIFICAR: tamaño y fill
    canvas.create_oval(px - 2, py - 2, px + 2, py + 2, fill="brown", outline="")

# Pasto en la base - MODIFICAR: altura y fill
canvas.create_rectangle(0, cy + 300, 500, 600, fill="green", outline="")

# Iniciar ventana
root.mainloop()