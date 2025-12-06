import tkinter as tk

ventana = tk.Tk()
ventana.title("Serpiente Animada")

canvas = tk.Canvas(ventana, width=600, height=400, bg="lightgreen")
canvas.pack()

# Posiciones de los segmentos
segmentos = []
num_segmentos = 10
tamaño_segmento = 20

# Crear segmentos
for i in range(num_segmentos):
    x = 100 - i * 25
    segmento = canvas.create_oval(x, 180, x+tamaño_segmento, 200, 
                                  fill="green", outline="darkgreen", width=2)
    segmentos.append([segmento, x, 190])

# Crear cabeza diferente
canvas.itemconfig(segmentos[0][0], fill="darkgreen")

# Dirección
direccion_x = 3
direccion_y = 0

def mover_serpiente():
    global direccion_x, direccion_y
    
    # Guardar posición anterior de la cabeza
    cabeza_x = segmentos[0][1]
    cabeza_y = segmentos[0][2]
    
    # Mover cabeza
    nueva_x = cabeza_x + direccion_x
    nueva_y = cabeza_y + direccion_y
    
    # Rebotar en bordes
    if nueva_x > 580 or nueva_x < 0:
        direccion_x = -direccion_x
    if nueva_y > 380 or nueva_y < 0:
        direccion_y = -direccion_y
    
    # Actualizar posición de la cabeza
    segmentos[0][1] = nueva_x
    segmentos[0][2] = nueva_y
    canvas.coords(segmentos[0][0], nueva_x, nueva_y, 
                 nueva_x+tamaño_segmento, nueva_y+tamaño_segmento)
    
    # Mover cada segmento a la posición del segmento anterior
    for i in range(num_segmentos-1, 0, -1):
        segmentos[i][1] = segmentos[i-1][1]
        segmentos[i][2] = segmentos[i-1][2]
        canvas.coords(segmentos[i][0], segmentos[i][1], segmentos[i][2],
                     segmentos[i][1]+tamaño_segmento, segmentos[i][2]+tamaño_segmento)
    
    # Repetir cada 50ms
    ventana.after(50, mover_serpiente)

# Cambiar dirección con teclas
def cambiar_direccion(evento):
    global direccion_x, direccion_y
    if evento.keysym == "Right" and direccion_x == 0:
        direccion_x = 3
        direccion_y = 0
    elif evento.keysym == "Left" and direccion_x == 0:
        direccion_x = -3
        direccion_y = 0
    elif evento.keysym == "Up" and direccion_y == 0:
        direccion_x = 0
        direccion_y = -3
    elif evento.keysym == "Down" and direccion_y == 0:
        direccion_x = 0
        direccion_y = 3

ventana.bind("<Key>", cambiar_direccion)

# Iniciar animación
mover_serpiente()

ventana.mainloop()

# CÓMO MODIFICAR:
# - Cambia num_segmentos para serpiente más larga/corta
# - Cambia 3 en direccion_x para velocidad diferente
# - Cambia fill="green" para otro color
# - Cambia 50 en after() para velocidad de animación