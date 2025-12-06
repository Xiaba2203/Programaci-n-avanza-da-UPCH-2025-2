import tkinter as tk

# Crear ventana - MODIFICAR: título
root = tk.Tk()
root.title("Árbol")

# Crear canvas - MODIFICAR: ancho, alto, color fondo
canvas = tk.Canvas(root, width=500, height=600, bg="lightblue")
canvas.pack()

# Tronco del árbol (rectángulo) - MODIFICAR: posición, ancho, alto, fill (color)
canvas.create_rectangle(220, 300, 280, 500, fill="brown", outline="black", width=2)
# x1=220, y1=300 (esquina superior izquierda)
# x2=280, y2=500 (esquina inferior derecha)

# Copa del árbol - 3 círculos grandes - MODIFICAR: posiciones, tamaños y fill

# Círculo izquierdo - MODIFICAR: centro y radio
canvas.create_oval(150, 200, 280, 330, fill="green", outline="darkgreen", width=2)

# Círculo derecho - MODIFICAR: centro y radio
canvas.create_oval(220, 200, 350, 330, fill="green", outline="darkgreen", width=2)

# Círculo superior (encima de los otros) - MODIFICAR: centro y radio
canvas.create_oval(185, 150, 315, 280, fill="green", outline="darkgreen", width=2)

# Manzanas (círculos rojos pequeños) - MODIFICAR: posición y tamaño
canvas.create_oval(200, 220, 220, 240, fill="red", outline="darkred", width=1)
canvas.create_oval(270, 240, 290, 260, fill="red", outline="darkred", width=1)
canvas.create_oval(230, 190, 250, 210, fill="red", outline="darkred", width=1)
canvas.create_oval(250, 270, 270, 290, fill="red", outline="darkred", width=1)

# Pasto (rectángulo verde) - MODIFICAR: altura y fill
canvas.create_rectangle(0, 500, 500, 600, fill="green", outline="")

# Líneas en el tronco para textura - MODIFICAR: cantidad y posición
canvas.create_line(230, 320, 230, 490, fill="saddlebrown", width=2)
canvas.create_line(250, 310, 250, 495, fill="saddlebrown", width=2)
canvas.create_line(270, 325, 270, 485, fill="saddlebrown", width=2)

# Sol en la esquina - MODIFICAR: posición y fill
canvas.create_oval(400, 50, 470, 120, fill="yellow", outline="orange", width=2)

# Iniciar ventana
root.mainloop()