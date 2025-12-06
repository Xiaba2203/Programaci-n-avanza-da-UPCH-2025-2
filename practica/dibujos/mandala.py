# mandala_comentado.py
import tkinter as tk        # importa tkinter
from tkinter import ttk     # importa ttk (widgets modernos)
import math, random         # importa math y random

class MandalaApp:
    def __init__(self, root):
        self.root = root                             # guarda la ventana
        self.root.title("Mandala - POO")             # pone título a la ventana
        self.root.geometry("650x650")                # ajusta tamaño de la ventana

        self.canvas = tk.Canvas(self.root,           # crea el canvas
                                width=600,           # ancho del canvas
                                height=600,          # alto del canvas
                                bg="white")          # fondo blanco
        self.canvas.pack(pady=10)                    # muestra el canvas

        self.cx, self.cy = 300, 300                  # centro del canvas
        self.R = 150                                 # distancia a los centros
        self.r = 150                                 # radio de cada círculo
        self.num_circles = 12                        # cantidad de círculos
        self.circle_ids = []                         # lista de ids

        self.draw_mandala()                          # dibuja la figura
        self.canvas.bind("<Button-1>", self.recolor) # bind para click izquierdo

    def draw_mandala(self):
        # recorre cada círculo a dibujar
        for i in range(self.num_circles):
            angle = (2 * math.pi / self.num_circles) * i
            # calcula el centro x del círculo
            x = self.cx + self.R * math.cos(angle)
            # calcula el centro y del círculo
            y = self.cy + self.R * math.sin(angle)

            # dibuja el círculo y guarda su id
            cid = self.canvas.create_oval(
                x - self.r, y - self.r,               # esquina superior izquierda
                x + self.r, y + self.r,               # esquina inferior derecha
                outline="black",                      # color borde negro
                width=2)                              # grosor del borde
            self.circle_ids.append(cid)               # añade id a la lista

    def random_color(self):
        # genera color hex aleatorio
        return "#" + "".join(random.choice("0123456789ABCDEF") for _ in range(6))

    def recolor(self, event):
        # cambia color de cada círculo
        for cid in self.circle_ids:
            color = self.random_color()              # color nuevo aleatorio
            self.canvas.itemconfig(cid, outline=color) # aplica color al borde

def main():
    root = tk.Tk()                                   # crea la ventana principal
    app = MandalaApp(root)                           # instancia la app
    root.mainloop()                                  # inicia el loop principal

if __name__ == "__main__":
    main()                                           # ejecuta main si es principal
