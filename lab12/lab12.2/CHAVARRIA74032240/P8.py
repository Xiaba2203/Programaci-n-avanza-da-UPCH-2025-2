# nodo simple
class TreeNode:
    def __init__(self, e):
        self.element = e
        self.left = None
        self.right = None

# arbol con utilidades
class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0

    # inserta elemento en BST
    def insert(self, e):
        if self.root is None:
            self.root = TreeNode(e)
            self.size += 1
            return True

        cur = self.root
        while True:
            if e < cur.element:
                if cur.left:
                    cur = cur.left
                else:
                    cur.left = TreeNode(e)
                    self.size += 1
                    return True
            elif e > cur.element:
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = TreeNode(e)
                    self.size += 1
                    return True
            else:
                # ya existe, no insertar
                return False

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def clear(self):
        self.root = None
        self.size = 0

    # devuelve lista con camino desde raiz hasta donde terminó búsqueda
    def path(self, e):
        camino = []
        cur = self.root
        while cur:
            camino.append(cur.element)
            if e < cur.element:
                cur = cur.left
            elif e > cur.element:
                cur = cur.right
            else:
                # encontrado, devolvemos camino completo
                return camino
        # no encontrado: devolvemos la ruta recorrida
        return camino

# ---- prueba rápida ----
if __name__ == "__main__":
    bt = BinaryTree()
    for n in ["George", "Michael", "Tom", "Adam", "Jones", "Peter", "Daniel"]:
        bt.insert(n)

    print("Tamaño:", bt.getSize())                 # debe ser 7
    print("¿Vacío?", bt.isEmpty())                # False
    print("Ruta a Peter:", bt.path("Peter"))      # ejemplo: ['George', 'Michael', 'Tom', 'Peter'] (según estructura)
    print("Ruta a Steve:", bt.path("Steve"))      # ruta hasta donde se detuvo
    bt.clear()
    print("Luego de clear, vacío?", bt.isEmpty()) # True
