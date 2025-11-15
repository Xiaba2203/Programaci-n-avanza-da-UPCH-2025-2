from BinaryTree import BinaryTree

def LCA(root, a, b):
    while root:
        if a < root.element and b < root.element:
            root = root.left
        elif a > root.element and b > root.element:
            root = root.right
        else:
            return root.element

t = BinaryTree()
for n in [18,9,36,6,12,1,8,10]:
    t.insert(n)

print(LCA(t.root, 1, 8))
print(LCA(t.root, 9, 10))
print(LCA(t.root, 10, 36))
