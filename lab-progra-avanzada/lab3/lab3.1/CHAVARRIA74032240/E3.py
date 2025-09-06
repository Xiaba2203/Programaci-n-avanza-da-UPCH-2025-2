#Utilicé la librería os para manejar los archivos en la carpeta, ya que lo tengo como carpeta en mi computadora, en vez de descargarlos uno por uno
import os

def autores_pdb(carpeta):
    autores = set()
    for archivo in os.listdir(carpeta):
        if archivo.endswith(".pdb"):
            ruta = os.path.join(carpeta, archivo)
            with open(ruta, "r") as f:
                for linea in f:
                    if linea.strip().lower().startswith("author"):
                        partes = linea.split()
                        nombres = " ".join(partes[1:])  # omitir "AUTHOR"
                        autores.add(nombres)
    return autores

# Uso
carpeta_pdb = "PDB files"   # asegúrate de que la carpeta esté en la misma ruta que tu script
autores = sorted(autores_pdb(carpeta_pdb))  # ordenamos alfabéticamente

print("\n=== Lista de Autores encontrados en los archivos PDB ===")
for i, autor in enumerate(autores, 1):
    print(f"{i}. {autor}")
