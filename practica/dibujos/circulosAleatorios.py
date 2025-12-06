import tkinter as tk
import random

# Crear ventana - MODIFICAR: título
root = tk.Tk()
root.title("10 Círculos Aleatorios")

# Crear canvas - MODIFICAR: ancho, alto, color fondo
canvas = tk.Canvas(root, width=600, height=600, bg="white")
canvas.pack()

# Lista de colores posibles - MODIFICAR: agregar o quitar colores
colores = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "cyan", "magenta", "lime"]

# Dibujar 10 círculos - MODIFICAR: range(10) para más o menos círculos
for i in range(10):
    # Posición aleatoria X - MODIFICAR: 50 y 550 son los límites (mínimo y máximo)
    x = random.randint(50, 550)
    
    # Posición aleatoria Y - MODIFICAR: 50 y 550 son los límites
    y = random.randint(50, 550)
    
    # Radio aleatorio - MODIFICAR: 10 y 50 son tamaño mínimo y máximo
    radio = random.randint(10, 50)
    
    # Elegir color aleatorio de la lista - MODIFICAR: usar random.choice(colores)
    color = random.choice(colores)
    
    # Dibujar círculo - MODIFICAR: outline (color borde), width (grosor)
    canvas.create_oval(x - radio, y - radio, x + radio, y + radio,
                       fill=color, outline="black", width=2)
    
    # Opcional: agregar número en el centro - MODIFICAR: font y fill
    canvas.create_text(x, y, text=str(i+1), font=("Arial", 12, "bold"), fill="white")

# Iniciar ventana
root.mainloop()