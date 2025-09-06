import urllib.request

url = "https://www.gutenberg.org/files/2000/2000-0.txt"
resp = urllib.request.urlopen(url)  
texto = resp.read().decode("utf-8")  # leer texto

lineas = texto.splitlines()  
palabras = texto.split()  

print("Cantidad de palabras:", len(palabras))  # a

print("Primeras 10 líneas:")  # b
for i in range(10):
    print(lineas[i])

unicas = [p for p in set(palabras) if palabras.count(p) == 1]  # c
print("Palabras únicas (ejemplo):", unicas[:20])

especiales = [p for p in palabras if len(p) > 2 and p[0] == p[-1]]  # d
print("Cantidad de palabras especiales:", len(especiales))
