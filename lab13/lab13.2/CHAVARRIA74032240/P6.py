from tkinter import *

class CalculadoraPrestamo:
    def __init__(self, ventana):
        ventana.title("Calculadora de Préstamo")
        ventana.geometry("330x270")

        self.monto = StringVar()
        self.tasa = StringVar()
        self.anios = StringVar()
        self.pago = StringVar()

        Label(ventana, text="Monto del préstamo (A):").pack()
        Entry(ventana, textvariable=self.monto).pack()

        Label(ventana, text="Tasa anual (%):").pack()
        Entry(ventana, textvariable=self.tasa).pack()

        Label(ventana, text="Años:").pack()
        Entry(ventana, textvariable=self.anios).pack()

        Button(ventana, text="Calcular pago mensual", command=self.calcular).pack(pady=10)

        Label(ventana, text="Pago mensual:").pack()
        Entry(ventana, textvariable=self.pago, state="readonly").pack()

    def calcular(self):
        A = float(self.monto.get())
        r = float(self.tasa.get()) / 100
        n = float(self.anios.get())

        tasa_mensual = r / 12
        meses = 12 * n

        pago_m = (A * tasa_mensual) / (1 - (1 + tasa_mensual)**(-meses))
        self.pago.set(f"{pago_m:.2f}")

root = Tk()
CalculadoraPrestamo(root)
root.mainloop()
