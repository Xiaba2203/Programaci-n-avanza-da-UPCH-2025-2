from tkinter import *

class Aplicacion:
    def __init__(self, ventana):
        self.ventana = ventana
        ventana.title("Ejercicio 4")
        ventana.geometry("300x150")

        self.texto_var = StringVar()
        self.modo_copiar = True   # True = copiar, False = limpiar

        self.entrada = Entry(ventana, textvariable=self.texto_var)
        self.boton = Button(ventana, text="Copiar texto", command=self.accion_boton)
        self.etiqueta = Label(ventana, text="El texto aparecerá aquí")

        self.etiqueta.pack(side='bottom')
        self.boton.pack(side='bottom')
        self.entrada.pack(side='bottom')

    def accion_boton(self):
        texto = self.texto_var.get()

        if self.modo_copiar:
            # Copia
            if texto == "":
                self.boton.config(bg="red", fg="white")
            else:
                self.boton.config(bg="SystemButtonFace", fg="black")
                self.etiqueta.config(text=texto)
                self.entrada.delete(0, END)
                self.boton.config(text="Limpiar texto")
                self.modo_copiar = False
        else:
            # Limpia
            self.texto_var.set("")
            self.etiqueta.config(text="El texto aparecerá aquí")
            self.boton.config(text="Copiar texto")
            self.boton.config(bg="SystemButtonFace", fg="black")
            self.modo_copiar = True

root = Tk()
app = Aplicacion(root)
root.mainloop()
