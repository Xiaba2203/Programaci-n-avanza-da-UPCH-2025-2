import tkinter as tk  # carga tkinter
import time            # usa tiempo real

class Cronometro:
    def __init__(self, root):
        self.root = root                     # guarda ventana
        self.tiempo_inicio = 0               # guarda inicio
        self.corriendo = False               # indica si corre

        self.label = tk.Label(root,          # crea texto
                              text="0.00",   # texto inicial
                              font=("Arial", 40))  # tamaño texto
        self.label.pack()                    # muestra texto

        self.boton = tk.Button(root,         # crea botón
                               text="Iniciar", 
                               command=self.iniciar)
        self.boton.pack()                    # muestra botón

    def iniciar(self):
        self.tiempo_inicio = time.time()     # guarda tiempo
        self.corriendo = True                # marca activo
        self.actualizar()                    # llama actualización

    def actualizar(self):
        if self.corriendo:                   # si está activo
            ahora = time.time()              # tiempo actual
            diferencia = ahora - self.tiempo_inicio  # calcula
            self.label.config(text=f"{diferencia:.2f}")  # muestra
            self.root.after(50, self.actualizar)  # repite ciclo

root = tk.Tk()       # crea ventana
app = Cronometro(root)  # crea cronómetro
root.mainloop()      # inicia aplicación
