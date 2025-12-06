from tkinter import *

class GUI4:
    def __init__(self):
        window = Tk()
        window.title("Ejercicio 4")

        # Cuatro botones arriba
        Button(window, text="Botón 1").grid(row=0, column=0, padx=5, pady=5)
        Button(window, text="Botón 2").grid(row=0, column=1, padx=5, pady=5)
        Button(window, text="Botón 3").grid(row=0, column=2, padx=5, pady=5)
        Button(window, text="Botón 4").grid(row=0, column=3, padx=5, pady=5)

        # Label
        Label(window, text="Aquí va una etiqueta").grid(row=1, column=0, columnspan=4, pady=5)

        # Text
        Text(window, width=40, height=6).grid(row=2, column=0, columnspan=4, padx=10, pady=10)

        window.mainloop()

GUI4()
