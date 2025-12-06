import tkinter as tk
import math

ventana = tk.Tk()
ventana.title("Polígono Deformándose")

canvas = tk.Canvas(ventana, width=600, height=400, bg="lightblue")
canvas.pack()

# Centro
centro_x = 300
centro_y = 200

# Crear polígono
poligono = canvas.create_polygon(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                fill="purple", outline="black", width=3)

# Variables
tiempo = 0
num_lados = 6

def deformar_poligono():
    global tiempo
    
    puntos = []
    
    for i in range(num_lados):
        angulo = (2 * math.pi * i / num_lados)
        
        # Radio variable que cambia con el tiempo
        radio = 100 + 30 * math.sin(tiempo + i)
        
        x = centro_x + radio * math.cos(angulo)
        y = centro_y + radio * math.sin(angulo)
        
        puntos.extend([x, y])
    
    # Actualizar polígono
    canvas.coords(poligono, *puntos)
    
    # Incrementar tiempo
    tiempo += 0.1
    
    # Repetir cada 30ms
    ventana.after(30, deformar_poligono)

# Iniciar animación
deformar_poligono()

ventana.mainloop()

# CÓMO MODIFICAR:
# - Cambia num_lados para más/menos lados
# - Cambia 30 en math.sin para más/menos deformación
# - Cambia tiempo += 0.1 para velocidad diferente
# - Cambia fill="purple" para otro color