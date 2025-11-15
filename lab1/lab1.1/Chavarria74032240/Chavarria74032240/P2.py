def encontrar_genes(genoma):
    stop_codons = {"TAG", "TAA", "TGA"}  # codones de parada
    genes = []  # lista de genes encontrados
    i = 0
    while i < len(genoma) - 2:  # recorrer el genoma
        if genoma[i:i+3] == "ATG":  # inicio de gen
            for j in range(i+3, len(genoma)-2, 3):  # avanzar de 3 en 3
                codon = genoma[j:j+3]
                if codon in stop_codons:  # si es stop
                    gen = genoma[i+3:j]  # extraer el gen
                    if gen and all(gen[k:k+3] not in ["ATG", "TAG", "TAA", "TGA"] for k in range(0, len(gen), 3)):
                        genes.append(gen)  # guardar el gen
                    i = j
                    break
        i += 1
    return genes if genes else ["No se encontró ningún gen"]

cadena = input("Ingrese una cadena de genoma: ")
for g in encontrar_genes(cadena):
    print(g)
