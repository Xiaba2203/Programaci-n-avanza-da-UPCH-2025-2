from tkinter import *

class BuscadorOscars:
    def __init__(self, ventana):
        ventana.title("Ganador de Oscar por Año")
        ventana.geometry("400x200")

        self.anio_var = StringVar()
        self.resultado_var = StringVar()

        Label(ventana, text="Ingrese un año (1928 - 2013):").pack()
        Entry(ventana, textvariable=self.anio_var).pack()

        Button(ventana, text="Buscar", command=self.buscar).pack(pady=10)

        Label(ventana, text="Resultado:").pack()
        Label(ventana, textvariable=self.resultado_var, fg="blue").pack()

        with open("Oscars.txt", "r", encoding="utf-8") as archivo:
            self.lineas = archivo.readlines()

    def buscar(self):
        anio = int(self.anio_var.get())
        indice = anio - 1928

        if 0 <= indice < len(self.lineas):
            self.resultado_var.set(self.lineas[indice].strip())
        else:
            self.resultado_var.set("Año inválido")

root = Tk()
BuscadorOscars(root)
root.mainloop()
