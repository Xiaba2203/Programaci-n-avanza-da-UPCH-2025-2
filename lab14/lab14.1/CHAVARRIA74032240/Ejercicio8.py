from tkinter import *

class ListboxApp:
    def __init__(self):
        self.window = Tk()
        self.window.title("Listbox Example")

        # Listbox
        self.listbox = Listbox(self.window)
        self.listbox.insert(1, "HTML5 in easy steps")
        self.listbox.insert(2, "CSS3 in easy steps")
        self.listbox.insert(3, "JavaScript in easy steps")
        self.listbox.pack(side=LEFT, padx=30, pady=30)

        # Label donde se mostrará el mensaje (Ejercicio 10)
        self.label = Label(self.window, text="", width=25)
        self.label.pack(side=RIGHT, padx=5)

        # Botón que ejecuta el método dialog
        self.btn = Button(self.window, text="Choose", command=self.dialog)
        self.btn.pack(side=RIGHT, padx=5)

    def dialog(self):
        # Obtener item seleccionado
        choice = self.listbox.get(self.listbox.curselection())
        self.label.config(text="Your Choice: " + choice)

        # Ejercicio 11: cambiar color según ítem seleccionado
        index = self.listbox.curselection()[0]  # 0, 1 o 2

        if index == 0:  # Primer ítem
            color = "yellow"
        elif index == 1:  # Segundo ítem
            color = "magenta"
        else:  # Tercer ítem
            color = "cyan"

        # Cambiar fondo de Listbox y Label
        self.listbox.config(bg=color)
        self.label.config(bg=color)

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = ListboxApp()
    app.run()
