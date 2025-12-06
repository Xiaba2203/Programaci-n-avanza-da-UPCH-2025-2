import tkinter as tk
import math

# Crear ventana - MODIFICAR: título
root = tk.Tk()
root.title("Polígono Regular")

# Crear canvas - MODIFICAR: ancho, alto, color fondo
canvas = tk.Canvas(root, width=600, height=600, bg="white")
canvas.pack()

# Centro del polígono - MODIFICAR: para mover el polígono
cx = 300
cy = 300

# Radio (distancia del centro a cada vértice) - MODIFICAR: tamaño del polígono
radio = 200

# NÚMERO DE LADOS - MODIFICAR: 3=triángulo, 4=cuadrado, 5=pentágono, 6=hexágono, etc.
n_lados = 9

# Lista para guardar los puntos del polígono
puntos = []

# Calcular cada vértice del polígono
for i in range(n_lados):
    # Ángulo de cada vértice (dividimos 360 grados entre n lados)
    # -90 es para que empiece desde arriba
    angulo = math.radians((360 / n_lados) * i - 90)
    
    # Calcular posición x,y del vértice
    x = cx + radio * math.cos(angulo)
    y = cy + radio * math.sin(angulo)
    
    # Agregar punto a la lista
    puntos.append(x)
    puntos.append(y)

# Dibujar el polígono - MODIFICAR: fill (color relleno), outline (borde), width
canvas.create_polygon(puntos, fill="lightgreen", outline="darkgreen", width=3)

# Marcar el centro con un círculo - MODIFICAR: radio y fill
canvas.create_oval(cx - 5, cy - 5, cx + 5, cy + 5, fill="red", outline="darkred", width=2)

# Dibujar líneas desde el centro a cada vértice - MODIFICAR: fill y width
for i in range(0, len(puntos), 2):  # recorre de 2 en 2 (x,y)
    x = puntos[i]
    y = puntos[i + 1]
    # Línea desde centro al vértice - MODIFICAR: fill (color), width, dash (punteado)
    canvas.create_line(cx, cy, x, y, fill="blue", width=1, dash=(5, 3))

# Marcar cada vértice con un círculo - MODIFICAR: tamaño y fill
for i in range(0, len(puntos), 2):
    x = puntos[i]
    y = puntos[i + 1]
    # Círculo en el vértice - MODIFICAR: radio y fill
    canvas.create_oval(x - 8, y - 8, x + 8, y + 8, fill="yellow", outline="orange", width=2)
    # Número del vértice - MODIFICAR: font y fill
    canvas.create_text(x, y, text=str(i // 2 + 1), font=("Arial", 10, "bold"), fill="black")

# Texto indicando cantidad de lados - MODIFICAR: texto, posición, font
canvas.create_text(cx, cy + radio + 40,
                   text=f"Polígono de {n_lados} lados",
                   font=("Arial", 16, "bold"), fill="black")

# Iniciar ventana
root.mainloop()