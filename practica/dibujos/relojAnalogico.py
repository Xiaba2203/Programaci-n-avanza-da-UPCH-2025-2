import tkinter as tk
import math

# Crear ventana - MODIFICAR: título entre comillas
root = tk.Tk()
root.title("Reloj Analógico")

# Crear canvas - MODIFICAR: width (ancho), height (alto), bg (color fondo)
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

# Centro del reloj - MODIFICAR: estos números para mover el reloj
cx = 200  # posición X del centro
cy = 200  # posición Y del centro

# Radio del reloj - MODIFICAR: este número para hacerlo más grande o pequeño
radio = 150

# Dibujar círculo exterior del reloj - MODIFICAR: outline (color borde), width (grosor)
canvas.create_oval(cx-radio, cy-radio, cx+radio, cy+radio, outline="black", width=3)

# Dibujar las 12 marcas de las horas
for i in range(12):
    # Calcular ángulo - cada hora son 30 grados (360/12)
    # -90 es para que empiece desde arriba (las 12)
    angulo = math.radians(i * 30 - 90)
    
    # Punto interno de la marca (más cerca del centro)
    x1 = cx + (radio - 15) * math.cos(angulo)  # MODIFICAR: -15 para marcas más largas o cortas
    y1 = cy + (radio - 15) * math.sin(angulo)
    
    # Punto externo de la marca (en el borde)
    x2 = cx + radio * math.cos(angulo)
    y2 = cy + radio * math.sin(angulo)
    
    # Dibujar línea de marca - MODIFICAR: fill (color), width (grosor)
    canvas.create_line(x1, y1, x2, y2, fill="black", width=2)

# Manecilla de HORA - apunta a las 3 - MODIFICAR: longitud y ángulo
angulo_hora = math.radians(0)  # MODIFICAR: 0=3hr, 90=6hr, 180=9hr, 270=12hr
longitud_hora = radio * 0.5  # MODIFICAR: 0.5 para más corta, 0.7 para más larga
x_hora = cx + longitud_hora * math.cos(angulo_hora)
y_hora = cy + longitud_hora * math.sin(angulo_hora)
canvas.create_line(cx, cy, x_hora, y_hora, fill="black", width=6)  # MODIFICAR: width (grosor)

# Manecilla de MINUTOS - apunta a las 12 - MODIFICAR: longitud y ángulo
angulo_minuto = math.radians(-90)  # MODIFICAR: -90=12, 0=3, 90=6, 180=9
longitud_minuto = radio * 0.7  # MODIFICAR: 0.7 para más corta, 0.9 para más larga
x_minuto = cx + longitud_minuto * math.cos(angulo_minuto)
y_minuto = cy + longitud_minuto * math.sin(angulo_minuto)
canvas.create_line(cx, cy, x_minuto, y_minuto, fill="blue", width=4)  # MODIFICAR: fill (color)

# Manecilla de SEGUNDOS - apunta a las 6 - MODIFICAR: longitud y ángulo
angulo_segundo = math.radians(90)  # MODIFICAR: igual que las otras
longitud_segundo = radio * 0.8
x_segundo = cx + longitud_segundo * math.cos(angulo_segundo)
y_segundo = cy + longitud_segundo * math.sin(angulo_segundo)
canvas.create_line(cx, cy, x_segundo, y_segundo, fill="red", width=2)  # MODIFICAR: fill (color)

# Círculo central decorativo - MODIFICAR: radio (tamaño), fill (color)
canvas.create_oval(cx-10, cy-10, cx+10, cy+10, fill="black")

# Iniciar ventana
root.mainloop()