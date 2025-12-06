# Advanced Programming Course 2024-II                 # nombre curso
# Program for Exercise N° 5                          # versión final

import tkinter as tk                                 # importa tkinter

class AniApp(tk.Tk):                                  # clase ventana
    def __init__(self):                               # inicia clase
        super().__init__()                            # inicia padre
        self.title("Shifted Sequence")                # título ventana

        cw = 250                                      # ancho canvas
        ch = 130                                      # alto canvas
        self.canvas = tk.Canvas(self, width=cw, height=ch, background="white")  
        self.canvas.grid(row=0, column=0)             # coloca canvas
        
        # parámetros iniciales                        # comentario simple
        self.posn_x = 1                               # posición x
        self.posn_y = 1                               # posición y
        self.shift_x = 2                              # movimiento x
        self.shift_y = 1                              # movimiento y
        self.ball_width = 18                          # ancho bola
        self.ball_height = 18                         # alto bola
        self.color = "cyan"                           # color bola
        self.cycle_period = 50                        # tiempo ciclo

        # crea bola inicial                           # crea ovalo
        self.ball = self.canvas.create_oval(
            self.posn_x, self.posn_y,
            self.posn_x + self.ball_width,
            self.posn_y + self.ball_height,
            fill=self.color
        )

        self.animate()                                # inicia animación

    def animate(self):                                # mueve pelota
        self.canvas.move(self.ball, self.shift_x, self.shift_y)  # mueve bola

        self.canvas.update()                          # refresca dibujo
        
        self.canvas.after(self.cycle_period, self.animate)  # repite animación

if __name__ == "__main__":                            # si principal
    app = AniApp()                                    # crea app
    app.mainloop()                                    # corre ventana
