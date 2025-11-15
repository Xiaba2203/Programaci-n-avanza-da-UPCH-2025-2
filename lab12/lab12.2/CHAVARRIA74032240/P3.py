# clase nodo
class TreeNode:
    def __init__(self, e):
        self.element = e
        self.left = None
        self.right = None

# clase arbol binario basica
class BinaryTree:
    def __init__(self):
        self.root = None   # raiz
        self.size = 0      # cantidad nodos

# creamos arbol manualmente
bt = BinaryTree()
bt.root = TreeNode("5")
bt.root.left = TreeNode("3")
bt.root.right = TreeNode("7")
bt.root.left.left = TreeNode("1")

# recorremos el lado izq con un bucle
current = bt.root
while current:
    print(current.element)
    current = current.left
