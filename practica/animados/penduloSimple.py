import tkinter as tk
import math

ventana = tk.Tk()
ventana.title("Péndulo Simple")

canvas = tk.Canvas(ventana, width=600, height=400, bg="white")
canvas.pack()

# Punto de pivote
pivote_x = 300
pivote_y = 50

# Dibujar pivote
canvas.create_oval(pivote_x-5, pivote_y-5, pivote_x+5, pivote_y+5, fill="black")

# Crear cuerda y bola
cuerda = canvas.create_line(pivote_x, pivote_y, pivote_x, pivote_y+200, width=3, fill="black")
bola = canvas.create_oval(pivote_x-20, pivote_y+180, pivote_x+20, pivote_y+220, fill="blue", outline="black", width=2)

# Variables del péndulo
angulo = -45  # Ángulo inicial en grados
velocidad_angular = 0
longitud = 200

def animar_pendulo():
    global angulo, velocidad_angular
    
    # Convertir a radianes
    rad = math.radians(angulo)
    
    # Calcular posición de la bola
    bola_x = pivote_x + longitud * math.sin(rad)
    bola_y = pivote_y + longitud * math.cos(rad)
    
    # Actualizar cuerda
    canvas.coords(cuerda, pivote_x, pivote_y, bola_x, bola_y)
    
    # Actualizar bola
    canvas.coords(bola, bola_x-20, bola_y-20, bola_x+20, bola_y+20)
    
    # Simular oscilación simple
    velocidad_angular += -0.3 * math.sin(rad)
    angulo += velocidad_angular
    velocidad_angular *= 0.999  # Amortiguamiento muy leve
    
    # Repetir cada 20ms
    ventana.after(20, animar_pendulo)

# Iniciar animación
animar_pendulo()

ventana.mainloop()

# CÓMO MODIFICAR:
# - Cambia angulo inicial para posición diferente
# - Cambia longitud para péndulo más largo/corto
# - Cambia 0.999 para más/menos amortiguamiento
# - Cambia fill="blue" para otro color de bola