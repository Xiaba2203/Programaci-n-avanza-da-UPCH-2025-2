import tkinter as tk

ventana = tk.Tk()
ventana.title("Círculo Rebotando")

canvas = tk.Canvas(ventana, width=600, height=400, bg="lightblue")
canvas.pack()

# Crear círculo
circulo = canvas.create_oval(280, 180, 320, 220, fill="red", outline="black", width=2)

# Velocidades
velocidad_x = 5
velocidad_y = 3

def animar():
    global velocidad_x, velocidad_y
    
    # Obtener posición actual
    coords = canvas.coords(circulo)
    x1, y1, x2, y2 = coords
    
    # Mover círculo
    canvas.move(circulo, velocidad_x, velocidad_y)
    
    # Detectar colisión con bordes y rebotar
    if x2 + velocidad_x >= 600 or x1 + velocidad_x <= 0:
        velocidad_x = -velocidad_x
    
    if y2 + velocidad_y >= 400 or y1 + velocidad_y <= 0:
        velocidad_y = -velocidad_y
    
    # Repetir animación cada 20ms
    ventana.after(20, animar)

# Iniciar animación
animar()

ventana.mainloop()

# CÓMO MODIFICAR:
# - Cambia velocidad_x y velocidad_y para más rápido/lento
# - Cambia 20 en after() para velocidad de actualización
# - Cambia fill="red" para otro color