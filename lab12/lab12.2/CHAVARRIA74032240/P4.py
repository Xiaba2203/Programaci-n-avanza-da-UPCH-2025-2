class TreeNode:
    def __init__(self, e):
        self.element = e
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, e):
        # si no hay raiz, el nuevo es raiz
        if self.root is None:
            self.root = TreeNode(e)
            self.size += 1
            return True

        parent = None
        cur = self.root
        while cur:
            if e < cur.element:
                parent = cur
                cur = cur.left
            elif e > cur.element:
                parent = cur
                cur = cur.right
            else:
                return False  # ya existe

        # insertamos donde corresponde
        if e < parent.element:
            parent.left = TreeNode(e)
        else:
            parent.right = TreeNode(e)
        self.size += 1
        return True

# prueba con nombres
bt = BinaryTree()
for name in ["George", "Michael", "Tom", "Adam", "Jones", "Peter", "Daniel"]:
    bt.insert(name)

# imprimimos nodos en recorrido simple
def print_tree(cur):
    if cur:
        print_tree(cur.left)
        print(cur.element)
        print_tree(cur.right)

print_tree(bt.root)
