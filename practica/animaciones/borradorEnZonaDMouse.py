import tkinter as tk

ventana = tk.Tk()
ventana.title("Borrador en Zona del Mouse")

canvas = tk.Canvas(ventana, width=600, height=400, bg="white")
canvas.pack()

for i in range(20):
    canvas.create_line(0, i*20, 600, i*20, fill="black", width=2)
    canvas.create_line(i*30, 0, i*30, 400, fill="blue", width=2)

etiqueta = tk.Label(ventana, text="Arrastra para borrar líneas")
etiqueta.pack()

radio_borrador = 30

def borrar(evento):
    objetos = canvas.find_overlapping(evento.x-radio_borrador, evento.y-radio_borrador,
                                     evento.x+radio_borrador, evento.y+radio_borrador)
    for obj in objetos:
        canvas.delete(obj)

canvas.bind("<B1-Motion>", borrar)

ventana.mainloop()