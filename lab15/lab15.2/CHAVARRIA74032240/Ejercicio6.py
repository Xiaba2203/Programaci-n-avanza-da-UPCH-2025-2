# Advanced Programming Course 2024-II                 # nombre curso
# Program for Exercise N° 6                          # número ejercicio

import tkinter as tk                                 # importa tkinter

class BounceApp(tk.Tk):                              # clase ventana
    def __init__(self):                              # inicia clase
        super().__init__()                           # inicia padre
        self.title("Bouncing Ball")                  # título ventana

        self.cw = 300                                # ancho canvas
        self.ch = 200                                # alto canvas
        self.canvas = tk.Canvas(self, width=self.cw, height=self.ch, bg="white")
        self.canvas.pack()                           # acomoda canvas
        
        self.r = 15                                   # radio pelota
        self.x = 50                                   # posición x
        self.y = 50                                   # posición y
        self.dx = 3                                   # movimiento x
        self.dy = 2                                   # movimiento y
        
        self.ball = self.canvas.create_oval(          # crea pelota
            self.x, self.y,
            self.x + self.r, self.y + self.r,
            fill="blue"
        )

        self.animate()                                # inicia animación

    def animate(self):                                # función animar
        self.canvas.move(self.ball, self.dx, self.dy) # mueve pelota
        
        pos = self.canvas.coords(self.ball)           # obtiene coordenadas
        if pos[2] >= self.cw or pos[0] <= 0:          # choca horizontal
            self.dx = -self.dx                        # invierte x
        if pos[3] >= self.ch or pos[1] <= 0:          # choca vertical
            self.dy = -self.dy                        # invierte y
        
        self.canvas.after(20, self.animate)           # repite animación

if __name__ == "__main__":                           # si principal
    BounceApp().mainloop()                           # corre app
