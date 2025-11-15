def masCercano(root, ref):
    c = root
    cercano = c.element
    while c:
        if abs(c.element - ref) < abs(cercano - ref):
            cercano = c.element
        if ref < c.element:
            c = c.left
        elif ref > c.element:
            c = c.right
        else:
            return c.element
    return cercano
