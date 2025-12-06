# Advanced Programming Course 2024-II                 # nombre curso
# Program for Exercise N° 8                          # número ejercicio

import tkinter as tk                                 # importa tkinter

class MoveSquare(tk.Tk):                             # clase ventana
    def __init__(self):                              # inicia clase
        super().__init__()                           # inicia padre
        self.title("Move Square with Keys")          # título ventana

        self.canvas = tk.Canvas(self, width=300, height=200, bg="white")
        self.canvas.pack()                           # acomoda canvas
        
        self.sq = self.canvas.create_rectangle(120, 80, 160, 120, fill="green") # cuadrado
        
        self.bind("<Up>", self.move_up)              # tecla arriba
        self.bind("<Down>", self.move_down)          # tecla abajo
        self.bind("<Left>", self.move_left)          # tecla izquierda
        self.bind("<Right>", self.move_right)        # tecla derecha

        self.focus_set()                             # enfoca ventana

    def move_up(self, event):                        # mueve arriba
        self.canvas.move(self.sq, 0, -10)            # mueve -y

    def move_down(self, event):                      # mueve abajo
        self.canvas.move(self.sq, 0, 10)             # mueve +y

    def move_left(self, event):                      # mueve izquierda
        self.canvas.move(self.sq, -10, 0)            # mueve -x

    def move_right(self, event):                     # mueve derecha
        self.canvas.move(self.sq, 10, 0)             # mueve +x

if __name__ == "__main__":                           # si principal
    MoveSquare().mainloop()                          # corre app
