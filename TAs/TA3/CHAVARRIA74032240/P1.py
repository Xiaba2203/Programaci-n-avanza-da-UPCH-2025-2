def contar_chocolates(envoltorios, envoltorio_requerido): # Calcula chocolates extra
    if envoltorios < envoltorio_requerido: # No hay suficientes envoltorios
        return 0
    
    nuevos_chocolates = envoltorios // envoltorio_requerido # Chocolates obtenidos
    envoltorios_sobrantes = envoltorios % envoltorio_requerido # Envoltorios sobrantes
    total_envoltorios = nuevos_chocolates + envoltorios_sobrantes # Envoltorios para siguiente ronda
    
    return nuevos_chocolates + contar_chocolates(total_envoltorios, envoltorio_requerido) # Suma y repite

def calcular_total_chocolates(dinero, precio, envoltorio): # Total de chocolates
    chocolates_comprados = dinero // precio # Chocolates comprados
    chocolates_extras = contar_chocolates(chocolates_comprados, envoltorio) # Chocolates extra
    return chocolates_comprados + chocolates_extras # Total final

if __name__ == "__main__": # Inicio del main
    print("Calculadora de chocolates\n")

    dinero = 16
    precio = 2
    envoltorio = 2 
    resultado = calcular_total_chocolates(dinero, precio, envoltorio)
    print(f"Dinero: {dinero}, Precio: {precio}, Envoltorio: {envoltorio}") 
    print(f"Total de chocolates: {resultado}\n")

    dinero = 15 # Caso prueba
    precio = 1
    envoltorio = 3
    resultado = calcular_total_chocolates(dinero, precio, envoltorio)
    print(f"Dinero: {dinero}, Precio: {precio}, Envoltorio: {envoltorio}")
    print(f"Total de chocolates: {resultado}\n")

    dinero = 20 # Otro caso
    precio = 3
    envoltorio = 5
    resultado = calcular_total_chocolates(dinero, precio, envoltorio)
    print(f"Dinero: {dinero}, Precio: {precio}, Envoltorio: {envoltorio}")
    print(f"Total de chocolates: {resultado}")
