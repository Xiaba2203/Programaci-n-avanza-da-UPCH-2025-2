# clase simple para nodo
class TreeNode:
    def __init__(self, e):
        self.element = e
        self.left = None   # hijo izq
        self.right = None  # hijo der

# creamos los nodos
n1 = TreeNode("root node")
n2 = TreeNode("left child node")
n3 = TreeNode("right child node")
n4 = TreeNode("left grandchild node")

# conectamos los nodos
n1.left = n2
n1.right = n3
n2.left = n4

# recorremos hacia la izquierda
cur = n1
while cur:
    print(cur.element)
    cur = cur.left
