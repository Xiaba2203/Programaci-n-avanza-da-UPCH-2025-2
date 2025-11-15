from P4 import TreeNode

class BinaryTree:
    def __init__(self):
        self.root = None

    def preorder(self, node):
        if node:
            print(node.element, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.element, end=" ")

# armamos arbol pequeño
r = TreeNode("A")
r.left = TreeNode("B")
r.right = TreeNode("C")
r.left.left = TreeNode("D")
r.right.right = TreeNode("E")

bt = BinaryTree()
bt.root = r

print("Preorder:")
bt.preorder(bt.root)
print("\nPostorder:")
bt.postorder(bt.root)
