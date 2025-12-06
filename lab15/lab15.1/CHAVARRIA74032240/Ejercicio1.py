import tkinter as tk                     # importa tkinter
import tkinter.messagebox as mb          # importa messagebox
import random                             # importa random

class MsbxApp(tk.Tk):                     # crea clase ventana
    def __init__(self):                   # inicia clase
        super().__init__()                # inicia padre
        self.geometry("250x200")          # fija tamaño

        self.options = [                  # lista opciones
            ("Show Info", self.show_info),
            ("Show Warning", self.show_warning),
            ("Show Error", self.show_error)
        ]

        text, func = random.choice(self.options)   # elige opción
        btn = tk.Button(self, text=text, command=func)  # crea botón
        btn.pack(expand=True, fill=tk.BOTH)        # centra botón

    def show_info(self):                  # función info
        msg = "Your user preferences have been saved"   # mensaje info
        mb.showinfo("Information", msg)   # muestra info

    def show_warning(self):               # función warning
        msg = "Temporary files have not been correctly removed"   # mensaje warn
        mb.showwarning("Warning", msg)    # muestra warning

    def show_error(self):                 # función error
        msg = "The application has encountered an unknown error"  # mensaje error
        mb.showerror("Error", msg)        # muestra error

if __name__ == "__main__":                # si archivo principal
    app = MsbxApp()                       # crea app
    app.mainloop()                        # corre ventana
