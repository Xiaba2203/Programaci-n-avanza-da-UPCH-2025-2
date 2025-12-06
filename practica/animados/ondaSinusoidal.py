import tkinter as tk
import math

ventana = tk.Tk()
ventana.title("Onda Sinusoidal")

canvas = tk.Canvas(ventana, width=600, height=400, bg="black")
canvas.pack()

# Línea del centro
canvas.create_line(0, 200, 600, 200, fill="gray", dash=(5, 5))

# Variables para la onda
desplazamiento = 0

def dibujar_onda():
    global desplazamiento
    
    # Limpiar canvas (excepto línea central)
    canvas.delete("onda")
    
    # Dibujar onda
    puntos = []
    for x in range(0, 601, 2):
        y = 200 + 80 * math.sin((x + desplazamiento) * 0.02)
        puntos.extend([x, y])
    
    canvas.create_line(puntos, fill="cyan", width=3, smooth=True, tags="onda")
    
    # Incrementar desplazamiento
    desplazamiento += 5
    
    # Repetir cada 30ms
    ventana.after(30, dibujar_onda)

# Iniciar animación
dibujar_onda()

ventana.mainloop()

# CÓMO MODIFICAR:
# - Cambia 80 para amplitud (altura de onda)
# - Cambia 0.02 para frecuencia (más ondas)
# - Cambia desplazamiento += 5 para velocidad
# - Cambia fill="cyan" para otro color