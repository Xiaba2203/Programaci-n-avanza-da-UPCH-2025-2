import urllib.request # libreria para bajar cosas del internet

URL="https://svnweb.freebsd.org/csrg/share/dict/words?revision=61569&view=co" # la pagina

def descargar_palabras():
    with urllib.request.urlopen(URL) as resp: # abrimos el enlace
        texto=resp.read().decode("utf-8") # leemos todo y lo pasamos a texto
    palabras=[] # aca van las palabras
    for linea in texto.splitlines(): # por cada linea
        if linea.strip()!="": # si no esta vacio
            palabras.append(linea.strip()) # la guardo
    return palabras # regreso la lista

def main():
    palabras=descargar_palabras() # descargo las palabras
    print("Total palabras:", len(palabras)) # muestro cuantas hay

    # b) palabras en mayus
    mayus=[] 
    for w in palabras: 
        if w.isalpha() and w==w.upper(): # si son solo letras y todas en mayus
            mayus.append(w) # la guardo
    print("Total en MAYÚSCULAS:", len(mayus))

    # c) palabras que empiezan con w
    con_w=[] 
    for w in palabras:
        if w.startswith("w"): # si empieza con w
            con_w.append(w)
    print("Total que empiezan con w:", len(con_w))

    # d) palabras de 3 letras
    len3=[] 
    for w in palabras:
        if len(w)==3: # si mide 3
            len3.append(w)
    print("Total de longitud 3:", len(len3))

    # e) buscamos la mas larga
    max_len=0 
    for w in palabras:
        if len(w)>max_len: # si encuentro una mas larga
            max_len=len(w) # actualizo
    mas_largas=[] 
    for w in palabras:
        if len(w)==max_len: # si tienen la max longitud
            mas_largas.append(w)
    print("Longitud máxima encontrada:", max_len)
    print("Palabras más largas:", mas_largas)

if __name__=="__main__":
    main()