import tkinter as tk

ventana = tk.Tk()
ventana.title("Drag and Drop")

canvas = tk.Canvas(ventana, width=600, height=400, bg="lightgray")
canvas.pack()

circulo = canvas.create_oval(50, 50, 150, 150, fill="red", outline="black", width=2)
rectangulo = canvas.create_rectangle(200, 50, 350, 150, fill="blue", outline="black", width=2)
triangulo = canvas.create_polygon(475, 150, 425, 50, 525, 50, fill="green", outline="black", width=2)

objeto_seleccionado = None
offset_x = 0
offset_y = 0

def iniciar_arrastre(evento):
    global objeto_seleccionado, offset_x, offset_y
    objeto_seleccionado = canvas.find_closest(evento.x, evento.y)[0]
    coords = canvas.coords(objeto_seleccionado)
    offset_x = evento.x - coords[0]
    offset_y = evento.y - coords[1]

def arrastrar(evento):
    global objeto_seleccionado
    if objeto_seleccionado:
        coords = canvas.coords(objeto_seleccionado)
        dx = evento.x - offset_x - coords[0]
        dy = evento.y - offset_y - coords[1]
        canvas.move(objeto_seleccionado, dx, dy)

def soltar(evento):
    global objeto_seleccionado
    objeto_seleccionado = None

canvas.bind("<Button-1>", iniciar_arrastre)
canvas.bind("<B1-Motion>", arrastrar)
canvas.bind("<ButtonRelease-1>", soltar)

ventana.mainloop()