import os

def dir_size(path):
    total = 0
    try:
        for entry in os.listdir(path):
            full = os.path.join(path, entry)
            # Evitar seguir enlaces simbólicos que puedan crear bucles
            if os.path.islink(full):
                continue
            if os.path.isfile(full):
                try:
                    total += os.path.getsize(full)
                except OSError:
                    # archivo inaccesible: ignorar o manejar según necesidad
                    pass
            elif os.path.isdir(full):
                total += dir_size(full)
    except PermissionError:
        # Si no hay permiso para listar el directorio, lo ignoramos o se podría manejar
        pass
    return total

if __name__ == "__main__":
    # Cambia esto por el directorio que quieras probar
    carpeta = "."  # directorio actual
    print(f"Tamaño total de '{carpeta}': {dir_size(carpeta)} bytes")
