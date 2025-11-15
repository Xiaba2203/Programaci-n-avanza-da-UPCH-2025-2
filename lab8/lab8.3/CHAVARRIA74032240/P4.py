def flatten(matrix):
    """Aplica aplanado recursivo. matrix puede ser lista de listas anidadas."""
    result = []
    for element in matrix:
        if isinstance(element, list) or isinstance(element, tuple):
            result.extend(flatten(element))
        else:
            result.append(element)
    return result

if __name__ == "__main__":
    M = [
        [5, 8, 15],
        [3, 0, 9],
        [11, 48, 22]
    ]
    print("Matriz:", M)
    print("Salida:", flatten(M))
