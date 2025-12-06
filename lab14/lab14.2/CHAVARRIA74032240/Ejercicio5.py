from tkinter import *

class GUI5:
    def __init__(self):
        window = Tk()
        window.title("Ejercicio 5")

        # Primera fila
        Label(window, text="Etiqueta A").grid(row=0, column=0, padx=5, pady=5)
        Entry(window, width=20).grid(row=0, column=1, padx=5, pady=5)

        # Segunda fila
        Label(window, text="Etiqueta B").grid(row=1, column=0, padx=5, pady=5)
        Entry(window, width=20).grid(row=1, column=1, padx=5, pady=5)

        # Área de texto
        Text(window, width=40, height=10).grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        window.mainloop()

GUI5()
