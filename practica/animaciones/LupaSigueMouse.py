import tkinter as tk

ventana = tk.Tk()
ventana.title("Lupa que Sigue el Mouse")

canvas = tk.Canvas(ventana, width=600, height=400, bg="white")
canvas.pack()

canvas.create_text(300, 200, text="Mueve el mouse", font=("Arial", 20), fill="gray")

for i in range(10):
    x = 60 * i + 30
    canvas.create_oval(x, 100, x+40, 140, fill="lightblue", outline="blue")

lupa = canvas.create_oval(0, 0, 100, 100, outline="black", width=4, fill="")

def mover_lupa(evento):
    x1 = evento.x - 50
    y1 = evento.y - 50
    x2 = evento.x + 50
    y2 = evento.y + 50
    canvas.coords(lupa, x1, y1, x2, y2)

canvas.bind("<Motion>", mover_lupa)

ventana.mainloop()