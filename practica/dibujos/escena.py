import tkinter as tk

# Crear ventana - MODIFICAR: título
root = tk.Tk()
root.title("Escena Natural")

# Crear canvas - MODIFICAR: ancho, alto, color fondo (cielo)
canvas = tk.Canvas(root, width=700, height=500, bg="skyblue")
canvas.pack()

# ===== SOL ===== MODIFICAR: posición y tamaño
sol_x = 600
sol_y = 80
sol_radio = 50

# Dibujar sol (círculo) - MODIFICAR: fill (color), outline (borde)
canvas.create_oval(sol_x - sol_radio, sol_y - sol_radio,
                   sol_x + sol_radio, sol_y + sol_radio,
                   fill="yellow", outline="orange", width=3)

# Rayos del sol (líneas) - MODIFICAR: cantidad, longitud, fill, width
import math
num_rayos = 12  # MODIFICAR: cantidad de rayos
longitud_rayo = 30  # MODIFICAR: longitud de cada rayo

for i in range(num_rayos):
    # Calcular ángulo de cada rayo
    angulo = (360 / num_rayos) * i
    angulo_rad = math.radians(angulo)
    
    # Punto inicial (borde del sol)
    x1 = sol_x + (sol_radio + 5) * math.cos(angulo_rad)
    y1 = sol_y + (sol_radio + 5) * math.sin(angulo_rad)
    
    # Punto final (fuera del sol)
    x2 = sol_x + (sol_radio + longitud_rayo) * math.cos(angulo_rad)
    y2 = sol_y + (sol_radio + longitud_rayo) * math.sin(angulo_rad)
    
    # Dibujar rayo - MODIFICAR: fill (color), width (grosor)
    canvas.create_line(x1, y1, x2, y2, fill="yellow", width=3)

# ===== NUBE 1 ===== MODIFICAR: posición
nube1_x = 150
nube1_y = 100

# Nube hecha con 5 círculos superpuestos - MODIFICAR: tamaños y fill
canvas.create_oval(nube1_x, nube1_y, nube1_x + 60, nube1_y + 40, fill="white", outline="lightgray")
canvas.create_oval(nube1_x + 30, nube1_y - 10, nube1_x + 80, nube1_y + 30, fill="white", outline="lightgray")
canvas.create_oval(nube1_x + 50, nube1_y, nube1_x + 100, nube1_y + 40, fill="white", outline="lightgray")
canvas.create_oval(nube1_x + 20, nube1_y + 10, nube1_x + 70, nube1_y + 45, fill="white", outline="lightgray")
canvas.create_oval(nube1_x + 40, nube1_y + 5, nube1_x + 85, nube1_y + 40, fill="white", outline="lightgray")

# ===== NUBE 2 ===== MODIFICAR: posición
nube2_x = 400
nube2_y = 120

# Segunda nube más pequeña - MODIFICAR: tamaños y fill
canvas.create_oval(nube2_x, nube2_y, nube2_x + 50, nube2_y + 35, fill="white", outline="lightgray")
canvas.create_oval(nube2_x + 25, nube2_y - 8, nube2_x + 70, nube2_y + 25, fill="white", outline="lightgray")
canvas.create_oval(nube2_x + 40, nube2_y, nube2_x + 85, nube2_y + 35, fill="white", outline="lightgray")

# ===== MONTAÑAS AL FONDO ===== MODIFICAR: puntos y fill
# Montaña izquierda
canvas.create_polygon(50, 350, 150, 250, 250, 350, fill="gray", outline="darkgray", width=2)
# Montaña derecha
canvas.create_polygon(200, 350, 320, 220, 440, 350, fill="darkgray", outline="gray", width=2)

# ===== PASTO ===== MODIFICAR: altura y fill
canvas.create_rectangle(0, 350, 700, 500, fill="green", outline="")

# Decoración del pasto (líneas verticales) - MODIFICAR: cantidad, fill, width
for x in range(0, 700, 15):  # MODIFICAR: 15 es la separación entre líneas
    # Altura aleatoria de cada línea de pasto
    import random
    altura = random.randint(10, 25)
    # Dibujar línea de pasto - MODIFICAR: fill (color), width (grosor)
    canvas.create_line(x, 350, x, 350 - altura, fill="darkgreen", width=2)

# ===== FLORES DECORATIVAS ===== MODIFICAR: cantidad y posiciones
# Flor 1 (roja)
canvas.create_oval(100, 380, 115, 395, fill="red", outline="darkred")
canvas.create_line(107, 395, 107, 410, fill="green", width=2)

# Flor 2 (amarilla)
canvas.create_oval(200, 370, 215, 385, fill="yellow", outline="orange")
canvas.create_line(207, 385, 207, 400, fill="green", width=2)

# Flor 3 (azul)
canvas.create_oval(320, 385, 335, 400, fill="blue", outline="darkblue")
canvas.create_line(327, 400, 327, 415, fill="green", width=2)

# Iniciar ventana
root.mainloop()