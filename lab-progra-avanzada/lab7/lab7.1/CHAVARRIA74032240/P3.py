# 3 clase Escuela
class Escuela:
    def __init__(self):
        self.grados = {}  # grados
    # 3.a agregar
    def agregar(self, nombre, grado):
        if grado not in self.grados:
            self.grados[grado] = []
        self.grados[grado].append(nombre)
    # 3.b mostrar grado
    def mostrar_grado(self, grado):
        return self.grados.get(grado, [])
    # 3.c mostrar todos
    def mostrar_todos(self):
        for g in sorted(self.grados.keys()):
            lista = sorted(self.grados[g])
            print(f"Grado {g}: {', '.join(lista)}")
