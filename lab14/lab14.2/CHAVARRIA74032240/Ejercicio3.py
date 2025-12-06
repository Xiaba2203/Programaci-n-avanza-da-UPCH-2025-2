from tkinter import *

class GUI3:
    def __init__(self):
        window = Tk()
        window.title("Ejercicio 3")

        # Frame para los labels
        frame_labels = Frame(window)
        frame_labels.pack(pady=5)

        Label(frame_labels, text="Etiqueta 1").pack()
        Label(frame_labels, text="Etiqueta 2").pack()
        Label(frame_labels, text="Etiqueta 3").pack()

        # Frame para los entry
        frame_entry = Frame(window)
        frame_entry.pack(pady=5)

        Entry(frame_entry, width=20).pack(pady=3)
        Entry(frame_entry, width=20).pack(pady=3)

        # Frame para el Text
        frame_text = Frame(window)
        frame_text.pack(pady=10)

        Text(frame_text, width=30, height=5).pack()

        window.mainloop()

GUI3()
