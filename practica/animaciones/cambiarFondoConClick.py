import tkinter as tk

ventana = tk.Tk()
ventana.title("Cambiar Color de Fondo")

canvas = tk.Canvas(ventana, width=600, height=400, bg="white")
canvas.pack()

colores = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "cyan"]
indice = 0

def cambiar_color(evento):
    global indice
    canvas.config(bg=colores[indice])
    indice = (indice + 1) % len(colores)

canvas.bind("<Button-1>", cambiar_color)

ventana.mainloop()