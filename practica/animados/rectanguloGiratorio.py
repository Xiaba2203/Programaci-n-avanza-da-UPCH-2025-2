import tkinter as tk
import math

ventana = tk.Tk()
ventana.title("Rectángulo Girando")

canvas = tk.Canvas(ventana, width=600, height=400, bg="white")
canvas.pack()

# Centro del rectángulo
centro_x = 300
centro_y = 200

# Dimensiones del rectángulo
ancho = 100
alto = 40

# Ángulo inicial
angulo = 0

# Crear rectángulo usando polígono (para poder rotarlo)
rectangulo = canvas.create_polygon(0, 0, 0, 0, 0, 0, 0, 0, fill="blue", outline="black", width=2)

def rotar_rectangulo():
    global angulo
    
    # Incrementar ángulo
    angulo += 3
    
    # Calcular los 4 puntos del rectángulo rotado
    rad = math.radians(angulo)
    cos_a = math.cos(rad)
    sin_a = math.sin(rad)
    
    # Puntos del rectángulo antes de rotar (centrado en origen)
    puntos = [
        (-ancho/2, -alto/2),
        (ancho/2, -alto/2),
        (ancho/2, alto/2),
        (-ancho/2, alto/2)
    ]
    
    # Rotar y trasladar al centro
    puntos_rotados = []
    for px, py in puntos:
        x_rot = px * cos_a - py * sin_a + centro_x
        y_rot = px * sin_a + py * cos_a + centro_y
        puntos_rotados.extend([x_rot, y_rot])
    
    # Actualizar polígono
    canvas.coords(rectangulo, *puntos_rotados)
    
    # Repetir cada 30ms
    ventana.after(30, rotar_rectangulo)

# Iniciar animación
rotar_rectangulo()

ventana.mainloop()

# CÓMO MODIFICAR:
# - Cambia angulo += 3 para girar más rápido/lento
# - Cambia ancho y alto para rectángulo diferente
# - Cambia fill="blue" para otro color
# - Cambia 30 en after() para velocidad diferente