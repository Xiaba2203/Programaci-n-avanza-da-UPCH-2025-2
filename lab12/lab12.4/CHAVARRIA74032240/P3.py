from BinaryTree import BinaryTree

def imprimirMenores(root, x):
    if root is None:
        return
    if root.element < x:
        print(root.element, end=" ")
        imprimirMenores(root.left, x)
        imprimirMenores(root.right, x)
    else:
        imprimirMenores(root.left, x)

t = BinaryTree()
for n in [8,3,10,1,6,4,7,14,13]:
    t.insert(n)

imprimirMenores(t.root, 7)
print()
imprimirMenores(t.root, 11)
print()
