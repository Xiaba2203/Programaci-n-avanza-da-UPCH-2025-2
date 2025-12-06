import tkinter as tk

# Crear ventana - MODIFICAR: título
root = tk.Tk()
root.title("Corazón")

# Crear canvas - MODIFICAR: ancho, alto, color fondo
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

# Centro del corazón - MODIFICAR: para mover todo el corazón
cx = 200
cy = 150

# Tamaño del corazón - MODIFICAR: este número para hacerlo más grande o pequeño
escala = 80

# Corazón dibujado con polígono (muchos puntos que forman curvas)
# MODIFICAR: estos puntos para cambiar la forma. Cada par es x,y
puntos = [
    cx, cy + escala * 0.3,  # punto inferior (punta del corazón)
    cx - escala * 0.5, cy - escala * 0.1,  # izquierda medio
    cx - escala * 0.5, cy - escala * 0.5,  # izquierda arriba
    cx - escala * 0.2, cy - escala * 0.7,  # curva izquierda superior
    cx, cy - escala * 0.6,  # centro superior
    cx + escala * 0.2, cy - escala * 0.7,  # curva derecha superior
    cx + escala * 0.5, cy - escala * 0.5,  # derecha arriba
    cx + escala * 0.5, cy - escala * 0.1,  # derecha medio
]

# Dibujar el corazón - MODIFICAR: fill (color), outline (borde), width (grosor borde)
canvas.create_polygon(puntos, fill="red", outline="darkred", width=3, smooth=True)
# smooth=True suaviza las líneas para que parezcan curvas

# Agregar brillo (óvalo blanco semitransparente simulado) - MODIFICAR: posición y tamaño
canvas.create_oval(cx - 25, cy - 50, cx + 10, cy - 20, fill="pink", outline="")

# Texto opcional - MODIFICAR: texto, posición, font (fuente), fill (color)
canvas.create_text(cx, cy + escala + 30, text="❤", font=("Arial", 40), fill="red")

# Iniciar ventana
root.mainloop()