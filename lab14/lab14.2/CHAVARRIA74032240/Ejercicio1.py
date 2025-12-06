from tkinter import *

class FrameApp:
    def __init__(self):
        window = Tk()
        window.title("Frame Demo")
        window.geometry("200x300")

        # (a) Cambiar color del fondo del contenedor principal
        window.config(bg="lightblue")

        # FRAME 1
        frame1 = Frame(
            window, bg="yellow",
            highlightbackground="red",
            highlightthickness=2,
            width=100,
            height=100
        )
        frame1.pack()
        frame1.pack_propagate(False)
        frame1.config(bd=25)

        self.entry1 = Entry(frame1)
        self.entry1.pack()

        # Botón para Entry 1
        boton1 = Button(frame1, text="print", command=self.print1)
        boton1.pack()

        # FRAME 2
        frame2 = Frame(window,
                       highlightbackground="red",
                       highlightthickness=1,
                       width=100,
                       height=100,
                       bd=25)
        frame2.pack()
        frame2.pack_propagate(False)

        self.entry2 = Entry(frame2)
        self.entry2.pack()

        # Botón para Entry 2
        boton2 = Button(frame2, text="print", command=self.print2)
        boton2.pack()

        # Label
        self.label = Label(window, text="This is a Label", bg="lightgreen")  # (b) cambiar fondo del Label
        self.label.pack()

        window.mainloop()

    # Funciones que imprimen contenido y actualizan Label
    def print1(self):
        print(self.entry1.get())
        self.label.config(text="Botón 1 presionado")

    def print2(self):
        print(self.entry2.get())
        self.label.config(text="Botón 2 presionado")


FrameApp()

