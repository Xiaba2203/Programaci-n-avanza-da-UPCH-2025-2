from P4 import TreeNode

class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, e):
        if self.root is None:
            self.root = TreeNode(e)
            return True
        cur = self.root
        while True:
            if e < cur.element:
                if cur.left:
                    cur = cur.left
                else:
                    cur.left = TreeNode(e)
                    return True
            elif e > cur.element:
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = TreeNode(e)
                    return True
            else:
                return False

    def inorder(self):
        self._inorder(self.root)

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(node.element, end=" ")
            self._inorder(node.right)

# prueba
bt = BinaryTree()
for n in ["George", "Michael", "Tom", "Adam", "Jones", "Peter", "Daniel"]:
    bt.insert(n)
bt.inorder()
