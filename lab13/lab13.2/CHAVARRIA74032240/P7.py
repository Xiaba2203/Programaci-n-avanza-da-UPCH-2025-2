from tkinter import *

class CalculadoraPrestamo:
    def __init__(self, ventana):
        ventana.title("Préstamo sin StringVar")
        ventana.geometry("330x270")

        Label(ventana, text="Monto (A):").pack()
        self.e_monto = Entry(ventana)
        self.e_monto.pack()

        Label(ventana, text="Tasa anual (%):").pack()
        self.e_tasa = Entry(ventana)
        self.e_tasa.pack()

        Label(ventana, text="Años:").pack()
        self.e_anios = Entry(ventana)
        self.e_anios.pack()

        Button(ventana, text="Calcular", command=self.calcular).pack(pady=10)

        Label(ventana, text="Pago mensual:").pack()
        self.e_pago = Entry(ventana, state="readonly")
        self.e_pago.pack()

    def calcular(self):
        A = float(self.e_monto.get())
        r = float(self.e_tasa.get()) / 100
        n = float(self.e_anios.get())

        r_m = r / 12
        meses = n * 12

        pago = (A * r_m) / (1 - (1 + r_m)**(-meses))

        self.e_pago.config(state="normal")
        self.e_pago.delete(0, END)
        self.e_pago.insert(0, f"{pago:.2f}")
        self.e_pago.config(state="readonly")

root = Tk()
CalculadoraPrestamo(root)
root.mainloop()
