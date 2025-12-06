import tkinter as tk

ventana = tk.Tk()
ventana.title("Figura Creciendo y Encogiendo")

canvas = tk.Canvas(ventana, width=600, height=400, bg="lightblue")
canvas.pack()

# Centro
centro_x = 300
centro_y = 200

# Crear círculo
circulo = canvas.create_oval(centro_x-50, centro_y-50, centro_x+50, centro_y+50, 
                            fill="purple", outline="black", width=2)

# Variables
radio = 50
creciendo = True
velocidad = 2

def animar_tamaño():
    global radio, creciendo
    
    # Cambiar tamaño
    if creciendo:
        radio += velocidad
        if radio >= 100:
            creciendo = False
    else:
        radio -= velocidad
        if radio <= 20:
            creciendo = True
    
    # Actualizar círculo
    canvas.coords(circulo, centro_x-radio, centro_y-radio, 
                 centro_x+radio, centro_y+radio)
    
    # Repetir cada 30ms
    ventana.after(30, animar_tamaño)

# Iniciar animación
animar_tamaño()

ventana.mainloop()

# CÓMO MODIFICAR:
# - Cambia velocidad = 2 para más rápido/lento
# - Cambia 100 y 20 para tamaños máximo/mínimo
# - Cambia fill="purple" para otro color
# - Usa create_rectangle para cuadrado que crece