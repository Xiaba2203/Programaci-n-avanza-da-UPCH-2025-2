import tkinter as tk
import math

# Crear ventana - MODIFICAR: título
root = tk.Tk()
root.title("Estrella de 5 Puntas")

# Crear canvas - MODIFICAR: ancho, alto, color fondo
canvas = tk.Canvas(root, width=600, height=600, bg="navy")
canvas.pack()

# Centro de la estrella - MODIFICAR: para mover la estrella
cx = 300
cy = 300

# Radio exterior (puntas) - MODIFICAR: tamaño de las puntas
radio_exterior = 200

# Radio interior (valles entre puntas) - MODIFICAR: profundidad de los valles
radio_interior = 80

# Número de puntas - MODIFICAR: 5 para estrella normal, 6 para estrella de David, etc.
num_puntas = 6

# Lista para guardar los puntos de la estrella
puntos = []

# Calcular los puntos alternando entre radio exterior e interior
for i in range(num_puntas * 2):  # multiplicamos por 2 porque alternamos punta-valle
    # Calcular ángulo (empezamos desde arriba: -90 grados)
    angulo = (360 / (num_puntas * 2)) * i - 90
    angulo_rad = math.radians(angulo)
    
    # Alternar entre radio exterior (puntas) y radio interior (valles)
    if i % 2 == 0:
        radio = radio_exterior  # punto de punta
    else:
        radio = radio_interior  # punto de valle
    
    # Calcular posición del punto
    x = cx + radio * math.cos(angulo_rad)
    y = cy + radio * math.sin(angulo_rad)
    
    # Agregar a la lista
    puntos.append(x)
    puntos.append(y)

# Dibujar la estrella - MODIFICAR: fill (color), outline (borde), width
canvas.create_polygon(puntos, fill="yellow", outline="gold", width=3)

# Dibujar líneas desde el centro a cada punta - MODIFICAR: fill, width, dash
for i in range(0, len(puntos), 4):  # cada 4 porque son 2 puntos (x,y) por punta
    x = puntos[i]
    y = puntos[i + 1]
    # Línea del centro a la punta - MODIFICAR: fill, width
    canvas.create_line(cx, cy, x, y, fill="orange", width=2, dash=(5, 3))

# Círculo en el centro - MODIFICAR: tamaño y fill
canvas.create_oval(cx - 15, cy - 15, cx + 15, cy + 15,
                   fill="white", outline="yellow", width=2)

# Marcar cada punta con un círculo - MODIFICAR: tamaño y fill
for i in range(0, len(puntos), 4):  # solo las puntas (radio exterior)
    x = puntos[i]
    y = puntos[i + 1]
    canvas.create_oval(x - 10, y - 10, x + 10, y + 10,
                       fill="red", outline="white", width=2)

# Círculos brillantes en los valles - MODIFICAR: tamaño y fill
for i in range(2, len(puntos), 4):  # solo los valles (radio interior)
    x = puntos[i]
    y = puntos[i + 1]
    canvas.create_oval(x - 8, y - 8, x + 8, y + 8,
                       fill="lightblue", outline="white", width=1)

# Texto decorativo - MODIFICAR: texto, font, fill
canvas.create_text(cx, cy + radio_exterior + 40,
                   text=f" Estrella de {num_puntas} Puntas ",
                   font=("Arial", 18, "bold"), fill="white")

# Iniciar ventana
root.mainloop()