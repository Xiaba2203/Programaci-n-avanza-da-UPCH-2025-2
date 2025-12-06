import tkinter as tk

class Radio1:
    def __init__(self):
        # Ventana principal creada dentro (composición)
        self.window = tk.Tk()
        self.window.geometry("200x200")

        # Variable de control
        self.var = tk.StringVar()
        self.var.set("red")

        # Radiobuttons
        self.R1 = tk.Radiobutton(
            self.window,
            text="Red",
            variable=self.var,
            value="red",
            command=self.select)
        self.R1.pack(anchor=tk.W, padx=10, pady=5)

        self.R2 = tk.Radiobutton(
            self.window,
            text="Green",
            variable=self.var,
            value="green",
            command=self.select)
        self.R2.pack(anchor=tk.W, padx=10, pady=5)

        self.R3 = tk.Radiobutton(
            self.window,
            text="Blue",
            variable=self.var,
            value="blue",
            command=self.select)
        self.R3.pack(anchor=tk.W, padx=10, pady=5)

        # Label donde se mostrará el mensaje
        self.label = tk.Label(self.window, text="You selected the option: red",
                              bg="red", fg="white")
        self.label.pack(pady=10)

    def select(self):
        color = self.var.get()

        # Texto del label
        self.label.config(text="You selected the option: " + color)

        # Cambiar color de fondo según elección
        if color == "red":
            self.label.config(bg="red", fg="white")
        elif color == "green":
            self.label.config(bg="green", fg="white")
        elif color == "blue":
            self.label.config(bg="blue", fg="white")

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    w = Radio1()
    w.run()
