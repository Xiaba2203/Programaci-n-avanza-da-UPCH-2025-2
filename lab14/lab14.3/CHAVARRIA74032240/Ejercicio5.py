from tkinter import *
import random

class DemostracionCanvas:
    def __init__(self):
        ventana = Tk()
        ventana.title("Canvas Demo")

        self.colores = ["lightblue", "lightgreen", "pink"]

        self.canvas = Canvas(ventana, width=200, height=100, bg="white")
        self.canvas.pack()

        # Cambiar color al hacer click
        self.canvas.bind("<Button-1>", self.cambiar_color)

        marco = Frame(ventana)
        marco.pack()

        btRectangle = Button(marco, text="Rectángulo", command=self.displayRect)
        btOval = Button(marco, text="Óvalo", command=self.displayOval)
        btArc = Button(marco, text="Arco", command=self.displayArc)
        btPolygon = Button(marco, text="Polígono", command=self.displayPolygon)
        btLine = Button(marco, text="Línea", command=self.displayLine)
        btString = Button(marco, text="Texto", command=self.displayString)
        btClear = Button(marco, text="Limpiar", command=self.clearCanvas)

        btRectangle.grid(row=1, column=1)
        btOval.grid(row=1, column=2)
        btArc.grid(row=1, column=3)
        btPolygon.grid(row=1, column=4)
        btLine.grid(row=1, column=5)
        btString.grid(row=1, column=6)
        btClear.grid(row=1, column=7)

        ventana.mainloop()

    def cambiar_color(self, e):
        nuevo = random.choice(self.colores)
        self.canvas.config(bg=nuevo)

    def displayRect(self):
        self.canvas.create_rectangle(10, 10, 190, 90, tags="rect")

    def displayOval(self):
        self.canvas.create_oval(10, 10, 190, 90, fill="red", tags="oval")

    def displayArc(self):
        self.canvas.create_arc(10,10,190,90,start=0,extent=90,width=8, fill="red", tags="arc")

    def displayPolygon(self):
        self.canvas.create_polygon(10, 10, 190, 90, 30, 50, tags="polygon")

    def displayLine(self):
        self.canvas.create_line(10, 10, 190, 90, fill="red", tags="line")
        self.canvas.create_line(10, 90, 190, 10, width=9, arrow="last", activefill="blue", tags="line")

    def displayString(self):
        self.canvas.create_text(60, 40, text="Hola, soy un texto",
                                font="Times 10 bold underline", tags="string")

    def clearCanvas(self):
        self.canvas.delete("rect","oval","arc","polygon","line","string")


DemostracionCanvas()
