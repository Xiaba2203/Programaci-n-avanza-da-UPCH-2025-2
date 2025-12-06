import tkinter as tk

ventana = tk.Tk()
ventana.title("Seleccionar y Mover Figuras")

canvas = tk.Canvas(ventana, width=600, height=400, bg="white")
canvas.pack()

circulo = canvas.create_oval(50, 50, 150, 150, fill="red", outline="black", width=2)
rectangulo = canvas.create_rectangle(200, 50, 350, 150, fill="blue", outline="black", width=2)
triangulo = canvas.create_polygon(475, 150, 425, 50, 525, 50, fill="green", outline="black", width=2)

objeto_seleccionado = None
offset_x = 0
offset_y = 0

etiqueta = tk.Label(ventana, text="Click para seleccionar, arrastra para mover")
etiqueta.pack()

def seleccionar(evento):
    global objeto_seleccionado, offset_x, offset_y
    objeto = canvas.find_closest(evento.x, evento.y)[0]
    
    canvas.itemconfig(circulo, width=2)
    canvas.itemconfig(rectangulo, width=2)
    canvas.itemconfig(triangulo, width=2)
    
    canvas.itemconfig(objeto, width=5)
    objeto_seleccionado = objeto
    
    coords = canvas.coords(objeto_seleccionado)
    offset_x = evento.x - coords[0]
    offset_y = evento.y - coords[1]
    
    etiqueta.config(text=f"Objeto {objeto} seleccionado")

def mover(evento):
    if objeto_seleccionado:
        coords = canvas.coords(objeto_seleccionado)
        dx = evento.x - offset_x - coords[0]
        dy = evento.y - offset_y - coords[1]
        canvas.move(objeto_seleccionado, dx, dy)

canvas.bind("<Button-1>", seleccionar)
canvas.bind("<B1-Motion>", mover)

ventana.mainloop()