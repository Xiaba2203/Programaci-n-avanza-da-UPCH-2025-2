import tkinter as tk

class CheckColors:
    def __init__(self):
        self.window = tk.Tk()

        # Variables IntVar (una para cada checkbox)
        self.red = tk.IntVar()
        self.green = tk.IntVar()
        self.blue = tk.IntVar()

        # EJERCICIO 7a: Crear checkboxes uno por uno, sin bucle
        self.checkR = tk.Checkbutton(self.window, text='R', variable=self.red)
        self.checkG = tk.Checkbutton(self.window, text='G', variable=self.green)
        self.checkB = tk.Checkbutton(self.window, text='B', variable=self.blue)

        self.checkR.pack(side='top')
        self.checkG.pack(side='top')
        self.checkB.pack(side='top')

        # Label
        self.label = tk.Label(self.window, text='Color code:')
        self.label.pack(side='left')

        # Botón (EJERCICIO 7b: recolor SIN parámetros)
        self.button = tk.Button(self.window, text='Show code', command=self.recolor)
        self.button.pack(side='left')

    # recolor solo recibe self (como pide el ejercicio 7)
    def recolor(self):
        color = '#'

        # Construir el color usando sus propias variables (ya no se reciben como parámetros)
        for var in (self.red, self.green, self.blue):
            color += 'FF' if var.get() else '00'

        # Actualizar el label
        self.label.config(text="Color code: " + color, bg=color)

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = CheckColors()
    app.run()
