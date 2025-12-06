from tkinter import *

class Aplicacion:
    def __init__(self, ventana):
        self.ventana = ventana
        ventana.title("Ejercicio 5 - Colores")
        ventana.geometry("300x150")
        ventana.config(bg="#D6EAF8")  # fondo de ventana

        self.texto_var = StringVar()

        self.entrada = Entry(ventana, textvariable=self.texto_var,
                             bg="#ABEBC6", fg="black")
        self.boton = Button(ventana, text="Copiar texto", command=self.copiar)
        self.etiqueta = Label(ventana, text="Aquí se mostrará el texto",
                              bg="#FAD7A0", fg="black")

        self.etiqueta.pack(side='bottom')
        self.boton.pack(side='bottom')
        self.entrada.pack(side='bottom')

    def copiar(self):
        self.etiqueta.config(text=self.texto_var.get())

root = Tk()
app = Aplicacion(root)
root.mainloop()
