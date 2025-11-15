from P4 import TreeNode

class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, e):
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
                return False
        if e < parent.element:
            parent.left = TreeNode(e)
        else:
            parent.right = TreeNode(e)
        self.size += 1
        return True

    def search(self, e):
        cur = self.root
        while cur:
            if e < cur.element:
                cur = cur.left
            elif e > cur.element:
                cur = cur.right
            else:
                return True
        return False

# probamos busqueda
bt = BinaryTree()
for n in ["George", "Michael", "Tom", "Adam", "Jones", "Peter", "Daniel"]:
    bt.insert(n)

print("¿Peter?", bt.search("Peter"))
print("¿Steve?", bt.search("Steve"))
