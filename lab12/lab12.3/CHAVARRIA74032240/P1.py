def minimo(root):
    c = root
    while c.left:
        c = c.left
    return c.element

def maximo(root):
    c = root
    while c.right:
        c = c.right
    return c.element

def contarHojas(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return contarHojas(root.left) + contarHojas(root.right)



