import tkinter as tk

# Crear ventana - MODIFICAR: título
root = tk.Tk()
root.title("Stickman")

# Crear canvas - MODIFICAR: ancho, alto, color fondo
canvas = tk.Canvas(root, width=400, height=500, bg="white")
canvas.pack()

# Posición central del stickman - MODIFICAR: estos valores para mover todo el personaje
centro_x = 200
centro_y = 150

# Cabeza (círculo) - MODIFICAR: radio (tamaño), fill (color), outline (borde)
radio_cabeza = 30
canvas.create_oval(centro_x - radio_cabeza, centro_y - radio_cabeza,
                   centro_x + radio_cabeza, centro_y + radio_cabeza,
                   fill="peachpuff", outline="black", width=2)

# Ojos (dos círculos pequeños) - MODIFICAR: posición relativa y fill
canvas.create_oval(centro_x - 12, centro_y - 10, centro_x - 5, centro_y - 3, fill="black")  # ojo izquierdo
canvas.create_oval(centro_x + 5, centro_y - 10, centro_x + 12, centro_y - 3, fill="black")  # ojo derecho

# Boca (arco/línea curva aproximada con línea recta) - MODIFICAR: posición y forma
canvas.create_arc(centro_x - 15, centro_y, centro_x + 15, centro_y + 20,
                  start=0, extent=-180, style="arc", outline="black", width=2)
# start=0, extent=-180 hace una sonrisa. Para triste: start=180, extent=-180

# Cuerpo (línea vertical) - MODIFICAR: longitud (y2), fill (color), width (grosor)
canvas.create_line(centro_x, centro_y + radio_cabeza,
                   centro_x, centro_y + radio_cabeza + 100,
                   fill="black", width=3)

# Brazo izquierdo (línea diagonal) - MODIFICAR: ángulo y longitud, fill, width
canvas.create_line(centro_x, centro_y + radio_cabeza + 20,
                   centro_x - 50, centro_y + radio_cabeza + 60,
                   fill="black", width=3)

# Brazo derecho (línea diagonal) - MODIFICAR: ángulo y longitud, fill, width
canvas.create_line(centro_x, centro_y + radio_cabeza + 20,
                   centro_x + 50, centro_y + radio_cabeza + 60,
                   fill="black", width=3)

# Pierna izquierda (línea diagonal) - MODIFICAR: ángulo y longitud, fill, width
canvas.create_line(centro_x, centro_y + radio_cabeza + 100,
                   centro_x - 40, centro_y + radio_cabeza + 180,
                   fill="black", width=3)

# Pierna derecha (línea diagonal) - MODIFICAR: ángulo y longitud, fill, width
canvas.create_line(centro_x, centro_y + radio_cabeza + 100,
                   centro_x + 40, centro_y + radio_cabeza + 180,
                   fill="black", width=3)

# Manos (círculos pequeños) - MODIFICAR: tamaño y fill
canvas.create_oval(centro_x - 55, centro_y + radio_cabeza + 55,
                   centro_x - 45, centro_y + radio_cabeza + 65,
                   fill="peachpuff", outline="black")  # mano izquierda

canvas.create_oval(centro_x + 45, centro_y + radio_cabeza + 55,
                   centro_x + 55, centro_y + radio_cabeza + 65,
                   fill="peachpuff", outline="black")  # mano derecha

# Pies (óvalos) - MODIFICAR: tamaño y fill
canvas.create_oval(centro_x - 50, centro_y + radio_cabeza + 180,
                   centro_x - 30, centro_y + radio_cabeza + 195,
                   fill="black", outline="black")  # pie izquierdo

canvas.create_oval(centro_x + 30, centro_y + radio_cabeza + 180,
                   centro_x + 50, centro_y + radio_cabeza + 195,
                   fill="black", outline="black")  # pie derecho

# Iniciar ventana
root.mainloop()