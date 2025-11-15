def esBST(root):
    return validar(root, float("-inf"), float("inf"))

def validar(n, mn, mx):
    if n is None:
        return True
    if not (mn < n.element < mx):
        return False
    return validar(n.left, mn, n.element) and validar(n.right, n.element, mx)
