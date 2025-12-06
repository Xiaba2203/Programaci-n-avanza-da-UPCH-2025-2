import tkinter as tk

# Crear ventana - MODIFICAR: título
root = tk.Tk()
root.title("Círculos Concéntricos")

# Crear canvas - MODIFICAR: ancho, alto, color fondo
canvas = tk.Canvas(root, width=600, height=600, bg="white")
canvas.pack()

# Centro de los círculos - MODIFICAR: para mover todo el patrón
cx = 300
cy = 300

# Radio inicial (el más grande) - MODIFICAR: este número
radio_inicial = 250

# Cantidad de círculos - MODIFICAR: este número para más o menos círculos
num_circulos = 10

# Diferencia de radio entre cada círculo - MODIFICAR: este número
diferencia = radio_inicial // num_circulos

# Lista de colores - MODIFICAR: agregar o cambiar colores
colores = ["red", "orange", "yellow", "green", "cyan", "blue", "purple", "pink", "magenta", "lime"]

# Dibujar círculos desde el más grande al más pequeño
for i in range(num_circulos):
    # Calcular radio del círculo actual
    radio = radio_inicial - (i * diferencia)
    
    # Elegir color (cicla la lista si hay más círculos que colores)
    color = colores[i % len(colores)]
    
    # Dibujar círculo - MODIFICAR: outline (color borde), width (grosor)
    canvas.create_oval(cx - radio, cy - radio, cx + radio, cy + radio,
                       fill=color, outline="black", width=2)

# Círculo central (punto) - MODIFICAR: tamaño y fill
canvas.create_oval(cx - 10, cy - 10, cx + 10, cy + 10,
                   fill="black", outline="white", width=2)

# Texto decorativo - MODIFICAR: texto, font, fill
canvas.create_text(cx, cy + radio_inicial + 30,
                   text="Círculos Concéntricos",
                   font=("Arial", 16, "bold"), fill="black")

# Iniciar ventana
root.mainloop()