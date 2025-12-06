import tkinter as tk

# Crear ventana - MODIFICAR: título
root = tk.Tk()
root.title("Montaña")

# Crear canvas - MODIFICAR: ancho, alto, color fondo
canvas = tk.Canvas(root, width=600, height=500, bg="lightblue")
canvas.pack()

# Montaña grande (polígono con líneas escalonadas) - MODIFICAR: puntos para cambiar forma
puntos_montana = [
    # Base izquierda
    50, 450,
    # Subida escalonada izquierda
    100, 400,
    120, 410,
    150, 350,
    170, 360,
    200, 300,
    220, 310,
    250, 250,
    270, 260,
    # Pico
    300, 150,
    # Bajada escalonada derecha
    330, 260,
    350, 250,
    380, 300,
    400, 310,
    430, 350,
    450, 360,
    480, 400,
    500, 410,
    # Base derecha
    550, 450,
]

# Dibujar montaña - MODIFICAR: fill (color), outline (borde), width (grosor)
canvas.create_polygon(puntos_montana, fill="gray", outline="black", width=2)

# Nieve en el pico (polígono blanco) - MODIFICAR: puntos y fill
puntos_nieve = [
    270, 260,
    280, 230,
    290, 240,
    300, 150,
    310, 240,
    320, 230,
    330, 260,
    315, 270,
    300, 200,
    285, 270,
]
canvas.create_polygon(puntos_nieve, fill="white", outline="lightgray", width=1)

# Montaña pequeña atrás (a la izquierda) - MODIFICAR: puntos y fill
puntos_montana2 = [
    20, 450,
    80, 350,
    120, 330,
    180, 400,
    220, 450,
]
canvas.create_polygon(puntos_montana2, fill="darkgray", outline="black", width=2)

# Montaña pequeña atrás (a la derecha) - MODIFICAR: puntos y fill
puntos_montana3 = [
    380, 450,
    420, 400,
    460, 380,
    500, 360,
    540, 400,
    580, 450,
]
canvas.create_polygon(puntos_montana3, fill="darkgray", outline="black", width=2)

# Pasto en la base - MODIFICAR: altura y fill
canvas.create_rectangle(0, 450, 600, 500, fill="green", outline="")

# Sol - MODIFICAR: posición y fill
canvas.create_oval(480, 40, 560, 120, fill="yellow", outline="orange", width=2)

# Nubes (óvalos blancos) - MODIFICAR: posición y tamaño
# Nube 1
canvas.create_oval(100, 80, 150, 110, fill="white", outline="lightgray")
canvas.create_oval(130, 70, 180, 100, fill="white", outline="lightgray")
canvas.create_oval(160, 80, 210, 110, fill="white", outline="lightgray")

# Nube 2
canvas.create_oval(350, 100, 400, 130, fill="white", outline="lightgray")
canvas.create_oval(380, 90, 430, 120, fill="white", outline="lightgray")
canvas.create_oval(410, 100, 460, 130, fill="white", outline="lightgray")

# Iniciar ventana
root.mainloop()