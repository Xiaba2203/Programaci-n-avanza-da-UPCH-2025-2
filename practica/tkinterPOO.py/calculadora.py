import tkinter as tk
from tkinter import messagebox

# ==================== CLASE CALCULADORA ====================
class Calculadora:
    """Calculadora básica con interfaz gráfica"""
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Calculadora POO")
        self.ventana.geometry("350x520")
        self.ventana.resizable(False, False)
        
        # Variables
        self.expresion = ""
        self.resultado_mostrado = False
        
        # Crear interfaz
        self._crear_pantalla()
        self._crear_botones()
    
    def _crear_pantalla(self):
        """Crea la pantalla de la calculadora"""
        # Frame para la pantalla
        frame_pantalla = tk.Frame(self.ventana, bg="black")
        frame_pantalla.pack(pady=20)
        
        # Entry para mostrar números y resultados
        self.pantalla = tk.Entry(frame_pantalla, font=("Arial", 24), 
                                width=15, bd=10, bg="white", 
                                justify="right")
        self.pantalla.pack()
        self.pantalla.insert(0, "0")
    
    def _crear_botones(self):
        """Crea todos los botones de la calculadora"""
        # Frame para botones
        frame_botones = tk.Frame(self.ventana)
        frame_botones.pack()
        
        # Definir botones (texto, fila, columna, ancho)
        botones = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 0, 0), ('←', 0, 1), ('(', 0, 2), (')', 0, 3)
        ]
        
        # Crear botones
        for (texto, fila, col) in botones:
            if texto == '=':
                # Botón igual más destacado
                boton = tk.Button(frame_botones, text=texto, font=("Arial", 18, "bold"),
                                width=5, height=2, bg="lightgreen",
                                command=lambda: self.calcular())
            elif texto == 'C':
                # Botón limpiar
                boton = tk.Button(frame_botones, text=texto, font=("Arial", 18, "bold"),
                                width=5, height=2, bg="lightcoral",
                                command=lambda: self.limpiar())
            elif texto == '←':
                # Botón borrar último
                boton = tk.Button(frame_botones, text=texto, font=("Arial", 18, "bold"),
                                width=5, height=2, bg="lightyellow",
                                command=lambda: self.borrar_ultimo())
            elif texto in ['+', '-', '*', '/']:
                # Botones de operadores
                boton = tk.Button(frame_botones, text=texto, font=("Arial", 18, "bold"),
                                width=5, height=2, bg="lightblue",
                                command=lambda t=texto: self.agregar(t))
            else:
                # Botones de números y paréntesis
                boton = tk.Button(frame_botones, text=texto, font=("Arial", 18),
                                width=5, height=2, bg="white",
                                command=lambda t=texto: self.agregar(t))
            
            boton.grid(row=fila, column=col, padx=2, pady=2)
    
    def agregar(self, valor):
        """Agrega un número u operador a la expresión"""
        # Si se mostró un resultado, limpiar para nueva operación
        if self.resultado_mostrado and valor not in ['+', '-', '*', '/']:
            self.limpiar()
            self.resultado_mostrado = False
        
        # Si la pantalla muestra "0", reemplazarlo
        if self.pantalla.get() == "0" and valor != '.':
            self.pantalla.delete(0, tk.END)
        
        # Agregar el valor
        self.expresion += valor
        self.pantalla.delete(0, tk.END)
        self.pantalla.insert(0, self.expresion)
        
        self.resultado_mostrado = False
    
    def calcular(self):
        """Calcula el resultado de la expresión"""
        try:
            # Evaluar la expresión
            resultado = eval(self.expresion)
            
            # Mostrar resultado
            self.pantalla.delete(0, tk.END)
            self.pantalla.insert(0, str(resultado))
            
            # Guardar resultado como nueva expresión
            self.expresion = str(resultado)
            self.resultado_mostrado = True
            
        except ZeroDivisionError:
            messagebox.showerror("Error", "No se puede dividir entre cero")
            self.limpiar()
        except Exception as e:
            messagebox.showerror("Error", f"Expresión inválida: {e}")
            self.limpiar()
    
    def limpiar(self):
        """Limpia la pantalla y la expresión"""
        self.expresion = ""
        self.pantalla.delete(0, tk.END)
        self.pantalla.insert(0, "0")
        self.resultado_mostrado = False
    
    def borrar_ultimo(self):
        """Borra el último carácter"""
        if len(self.expresion) > 0:
            self.expresion = self.expresion[:-1]
            self.pantalla.delete(0, tk.END)
            if self.expresion:
                self.pantalla.insert(0, self.expresion)
            else:
                self.pantalla.insert(0, "0")
    
    def ejecutar(self):
        """Inicia la aplicación"""
        self.ventana.mainloop()

# ==================== CALCULADORA CIENTIFICA (EXTRA) ====================
class CalculadoraCientifica(Calculadora):
    """Calculadora con funciones científicas adicionales"""
    def __init__(self):
        super().__init__()
        self.ventana.title("Calculadora Científica")
        self.ventana.geometry("450x500")
        self._agregar_botones_cientificos()
    
    def _agregar_botones_cientificos(self):
        """Agrega botones científicos"""
        import math
        
        frame_cientifico = tk.Frame(self.ventana)
        frame_cientifico.pack()
        
        # Botones científicos
        botones_cient = [
            ('sin', lambda: self.funcion_cientifica('math.sin')),
            ('cos', lambda: self.funcion_cientifica('math.cos')),
            ('tan', lambda: self.funcion_cientifica('math.tan')),
            ('√', lambda: self.funcion_cientifica('math.sqrt')),
            ('x²', lambda: self.agregar('**2')),
            ('π', lambda: self.agregar(str(math.pi)))
        ]
        
        for i, (texto, comando) in enumerate(botones_cient):
            boton = tk.Button(frame_cientifico, text=texto, font=("Arial", 12),
                            width=8, height=1, bg="lightgray", command=comando)
            boton.grid(row=0, column=i, padx=2, pady=5)
    
    def funcion_cientifica(self, funcion):
        """Aplica una función científica"""
        try:
            import math
            if self.expresion:
                resultado = eval(f"{funcion}({self.expresion})")
                self.pantalla.delete(0, tk.END)
                self.pantalla.insert(0, str(resultado))
                self.expresion = str(resultado)
                self.resultado_mostrado = True
        except Exception as e:
            messagebox.showerror("Error", f"Error en función: {e}")

# ==================== EJECUTAR ====================
if __name__ == "__main__":
    # Calculadora básica
    calc = Calculadora()
    calc.ejecutar()
    
    # Para usar calculadora científica, comenta la línea anterior y descomenta:
    # calc = CalculadoraCientifica()
    # calc.ejecutar()

# ==================== CÓMO USAR ====================
# 1. Click en los números para escribir
# 2. Click en operadores (+, -, *, /)
# 3. Click en = para calcular
# 4. C limpia todo
# 5. ← borra el último carácter
# 6. Puedes usar paréntesis para operaciones complejas
#
# PARA TU EXAMEN:
# - Esta calculadora tiene toda la estructura básica
# - Usa Entry para mostrar números
# - Usa grid() para organizar botones
# - Usa eval() para calcular (cuidado, solo en ejemplos controlados)
# - Puedes agregar más funciones científicas si te piden
# - Maneja errores con try-except
#
# MODIFICAR:
# - Cambia colores en bg="..."
# - Cambia tamaños en width y height
# - Agrega más botones copiando el formato
# - Para botón personalizado: ('texto', fila, col) en la lista