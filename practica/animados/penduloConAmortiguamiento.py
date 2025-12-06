import tkinter as tk
import math

ventana = tk.Tk()
ventana.title("Péndulo con Amortiguamiento")

canvas = tk.Canvas(ventana, width=600, height=400, bg="lightyellow")
canvas.pack()

# Punto de pivote
pivote_x = 300
pivote_y = 50

# Dibujar soporte
canvas.create_rectangle(280, 40, 320, 50, fill="brown", outline="black", width=2)
canvas.create_oval(pivote_x-8, pivote_y-8, pivote_x+8, pivote_y+8, fill="gray", outline="black", width=2)

# Crear cuerda y bola
cuerda = canvas.create_line(pivote_x, pivote_y, pivote_x, pivote_y+250, width=2, fill="black")
bola = canvas.create_oval(pivote_x-25, pivote_y+225, pivote_x+25, pivote_y+275, fill="red", outline="black", width=3)

# Etiqueta
etiqueta = tk.Label(ventana, text="Observa cómo se detiene lentamente", font=("Arial", 12))
etiqueta.pack()

# Variables del péndulo
angulo = 60  # Ángulo inicial más grande
velocidad_angular = 0
longitud = 250

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
    canvas.coords(bola, bola_x-25, bola_y-25, bola_x+25, bola_y+25)
    
    # Física del péndulo con amortiguamiento
    aceleracion = -0.2 * math.sin(rad)
    velocidad_angular += aceleracion
    velocidad_angular *= 0.995  # Amortiguamiento más notable
    angulo += velocidad_angular
    
    # Mostrar ángulo actual
    etiqueta.config(text=f"Ángulo: {abs(angulo):.1f}° | Velocidad: {abs(velocidad_angular):.2f}")
    
    # Repetir cada 20ms
    ventana.after(20, animar_pendulo)

# Iniciar animación
animar_pendulo()

ventana.mainloop()

# CÓMO MODIFICAR:
# - Cambia 0.995 para más amortiguamiento (0.99) o menos (0.998)
# - Cambia angulo = 60 para arranque diferente
# - Cambia longitud para péndulo diferente
# - Cambia fill="red" para otro color