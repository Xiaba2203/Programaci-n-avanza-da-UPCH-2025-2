import tkinter as tk

# Crear ventana - MODIFICAR: título entre comillas
root = tk.Tk()
root.title("Casa")

# Crear canvas - MODIFICAR: width (ancho), height (alto), bg (color fondo)
canvas = tk.Canvas(root, width=500, height=500, bg="lightblue")
canvas.pack()

# Base de la casa (rectángulo) - MODIFICAR: coordenadas x1,y1,x2,y2 y fill (color relleno)
canvas.create_rectangle(150, 250, 350, 400, fill="yellow", outline="black", width=2)
# x1,y1 = esquina superior izquierda
# x2,y2 = esquina inferior derecha

# Techo (triángulo usando polígono) - MODIFICAR: puntos y fill (color)
canvas.create_polygon(140, 250, 250, 150, 360, 250, fill="red", outline="black", width=2)
# Cada par de números es un punto: x,y
# Primer punto (140,250), segundo (250,150), tercero (360,250)

# Puerta - MODIFICAR: posición y color fill
canvas.create_rectangle(220, 320, 280, 400, fill="brown", outline="black", width=2)

# Manija de puerta (círculo pequeño) - MODIFICAR: posición y fill
canvas.create_oval(270, 360, 278, 368, fill="gold", outline="black")

# Ventana izquierda - MODIFICAR: posición y fill
canvas.create_rectangle(170, 280, 210, 320, fill="lightblue", outline="black", width=2)

# Cruz de ventana izquierda (dos líneas) - MODIFICAR: color fill
canvas.create_line(190, 280, 190, 320, fill="black", width=2)  # línea vertical
canvas.create_line(170, 300, 210, 300, fill="black", width=2)  # línea horizontal

# Ventana derecha - MODIFICAR: posición y fill
canvas.create_rectangle(290, 280, 330, 320, fill="lightblue", outline="black", width=2)

# Cruz de ventana derecha - MODIFICAR: color fill
canvas.create_line(310, 280, 310, 320, fill="black", width=2)  # línea vertical
canvas.create_line(290, 300, 330, 300, fill="black", width=2)  # línea horizontal

# Chimenea - MODIFICAR: posición y fill
canvas.create_rectangle(300, 180, 330, 250, fill="gray", outline="black", width=2)

# Humo de la chimenea (círculos) - MODIFICAR: posición, tamaño y fill
canvas.create_oval(305, 160, 325, 180, fill="lightgray", outline="gray")
canvas.create_oval(310, 140, 330, 160, fill="lightgray", outline="gray")
canvas.create_oval(315, 120, 335, 140, fill="lightgray", outline="gray")

# Pasto (rectángulo verde) - MODIFICAR: altura y color fill
canvas.create_rectangle(0, 400, 500, 500, fill="green", outline="")

# Camino a la puerta - MODIFICAR: puntos y fill
canvas.create_polygon(220, 400, 280, 400, 300, 500, 200, 500, fill="gray", outline="black")

# Sol - MODIFICAR: posición y fill
canvas.create_oval(400, 50, 450, 100, fill="yellow", outline="orange", width=2)

# Iniciar ventana
root.mainloop()