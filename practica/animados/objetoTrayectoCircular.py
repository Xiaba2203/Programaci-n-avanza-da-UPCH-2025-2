import tkinter as tk
import math

ventana = tk.Tk()
ventana.title("Trayectoria Circular")

canvas = tk.Canvas(ventana, width=600, height=400, bg="black")
canvas.pack()

# Centro del círculo
centro_x = 300
centro_y = 200

# Dibujar círculo guía
canvas.create_oval(centro_x-150, centro_y-150, centro_x+150, centro_y+150, 
                  outline="gray", width=2, dash=(5, 5))

# Punto central
canvas.create_oval(centro_x-5, centro_y-5, centro_x+5, centro_y+5, fill="white")

# Crear objeto que se mueve
objeto = canvas.create_oval(0, 0, 30, 30, fill="cyan", outline="white", width=2)

# Variables
angulo = 0
radio = 150

def mover_circular():
    global angulo
    
    # Convertir a radianes
    rad = math.radians(angulo)
    
    # Calcular posición
    x = centro_x + radio * math.cos(rad)
    y = centro_y + radio * math.sin(rad)
    
    # Actualizar objeto
    canvas.coords(objeto, x-15, y-15, x+15, y+15)
    
    # Incrementar ángulo
    angulo += 2
    if angulo >= 360:
        angulo = 0
    
    # Repetir cada 20ms
    ventana.after(20, mover_circular)

# Iniciar animación
mover_circular()

ventana.mainloop()

# CÓMO MODIFICAR:
# - Cambia angulo += 2 para velocidad diferente
# - Cambia radio = 150 para círculo más grande/pequeño
# - Cambia fill="cyan" para otro color
# - Cambia el tamaño del objeto (30, 30)