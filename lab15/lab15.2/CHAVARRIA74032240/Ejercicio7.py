# Advanced Programming Course 2024-II                 # nombre curso
# Program for Exercise N° 7                          # número ejercicio

import tkinter as tk                                 # importa tkinter

class DragSquares(tk.Tk):                            # clase ventana
    def __init__(self):                              # inicia clase
        super().__init__()                           # inicia padre
        self.title("Draggable Squares")              # título ventana
        
        self.canvas = tk.Canvas(self, width=300, height=200, bg="white")
        self.canvas.pack()                           # acomoda canvas
        
        self.blue = self.canvas.create_rectangle(50, 50, 90, 90, fill="blue")   # cuadrado azul
        self.red = self.canvas.create_rectangle(150, 50, 190, 90, fill="red")   # cuadrado rojo

        self.drag_data = {"item": None, "x": 0, "y": 0}   # datos arrastre
        
        self.canvas.bind("<Button-1>", self.start_drag)   # iniciar arrastre
        self.canvas.bind("<B1-Motion>", self.do_drag)     # mover arrastre
        self.canvas.bind("<ButtonRelease-1>", self.stop_drag)  # soltar arrastre

    def start_drag(self, event):                           # inicia arrastre
        item = self.canvas.find_closest(event.x, event.y)  # encuentra objeto
        self.drag_data["item"] = item                      # guarda item
        self.drag_data["x"] = event.x                      # guarda x
        self.drag_data["y"] = event.y                      # guarda y

    def do_drag(self, event):                             # mueve objeto
        dx = event.x - self.drag_data["x"]                # delta x
        dy = event.y - self.drag_data["y"]                # delta y
        self.canvas.move(self.drag_data["item"], dx, dy)  # mueve figura
        self.drag_data["x"] = event.x                     # actualiza x
        self.drag_data["y"] = event.y                     # actualiza y

    def stop_drag(self, event):                           # termina arrastre
        self.drag_data["item"] = None                     # limpia item

if __name__ == "__main__":                               # si principal
    DragSquares().mainloop()                             # corre app
