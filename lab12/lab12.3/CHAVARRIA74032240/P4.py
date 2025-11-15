from BinaryTree import BinaryTree

t = BinaryTree()

t.insert(8)
t.insert(3)
t.insert(10)
t.insert(1)
t.insert(6)
t.insert(14)
t.insert(4)
t.insert(7)
t.insert(13)

print("Original:")
t.inorder()
print()

t.delete(7)
print("Borrar hoja (7):")
t.inorder()
print()

t.delete(6)
print("Borrar nodo con un hijo (6):")
t.inorder()
print()

t.delete(3)
print("Borrar nodo con dos hijos (3):")
t.inorder()
print()
