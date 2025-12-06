import tkinter as tk                     # importa tkinter
import tkinter.messagebox as mb          # importa messagebox

class HyperApp(tk.Tk):                   # clase ventana
    def __init__(self):                  # inicia clase
        super().__init__()               # inicia padre

        self.t = tk.Text(self, width=50, height=12)   # crea texto
        self.t.pack(padx=10, pady=10)    # acomoda texto

        self.e = tk.Entry(self, width=40)  # entrada link
        self.e.pack(pady=5)              # acomoda entrada

        tk.Button(self, text="Insert link", command=self.insert_link).pack(pady=10) # botón

        self.t.tag_config("link", foreground="blue", underline=1)   # estilo link
        self.t.tag_bind("link", "<Button-1>", self.open_link)       # click link

    def insert_link(self):               # inserta link
        text = self.e.get()              # obtiene texto
        if text.strip():                 # si no vacío
            self.t.insert(tk.END, text, "link")   # agrega link
            self.t.insert(tk.END, "\n")           # salto línea

    def open_link(self, event):          # abre link
        index = self.t.index("@%s,%s" % (event.x, event.y))  # posición click
        link = self.t.get(index + " wordstart", index + " wordend") # obtiene palabra
        mb.showinfo("Hyperlink", f"You clicked:\n{link}")   # muestra info

if __name__ == "__main__":              # si principal
    HyperApp().mainloop()               # corre app

