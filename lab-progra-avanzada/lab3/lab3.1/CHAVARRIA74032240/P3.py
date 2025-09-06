s = {1, 3, 4}              # ✅ correcto
# s = {{1, 2}, {4, 5}}     # ❌ error, no se pueden usar conjuntos dentro de conjuntos
# s = {[1, 2], [4, 5]}     # ❌ error, no se pueden usar listas dentro de conjuntos
s = {(1, 2), (4, 5)}       # ✅ correcto (tuplas sí se permiten)
