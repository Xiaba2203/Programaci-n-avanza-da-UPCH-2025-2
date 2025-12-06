import tkinter as tk

ventana = tk.Tk()
ventana.title("Punto en Zigzag")

canvas = tk.Canvas(ventana, width=600, height=400, bg="white")
canvas.pack()

# Crear punto
punto = canvas.create_oval(0, 0, 20, 20, fill="red", outline="black", width=2)

# Variables
x = 0
y = 200
velocidad_x = 3
velocidad_y = 5
bajando = True

def mover_zigzag():
    global x, y, bajando
    
    # Mover horizontalmente
    x += velocidad_x
    
    # Mover verticalmente en zigzag
    if bajando:
        y += velocidad_y
        if y >= 380:
            bajando = False
    else:
        y -= velocidad_y
        if y <= 20:
            bajando = True
    
    # Actualizar posición
    canvas.coords(punto, x, y, x+20, y+20)
    
    # Reiniciar si sale del canvas
    if x > 600:
        x = -20
    
    # Repetir cada 30ms
    ventana.after(30, mover_zigzag)

# Iniciar animación
mover_zigzag()

ventana.mainloop()

# CÓMO MODIFICAR:
# - Cambia velocidad_x y velocidad_y para diferente zigzag
# - Cambia 380 y 20 para límites verticales
# - Cambia fill="red" para otro color