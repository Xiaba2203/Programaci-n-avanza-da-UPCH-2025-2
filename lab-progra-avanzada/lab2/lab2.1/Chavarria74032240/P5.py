def leer_booleano(texto):
    r=input(texto+" (s/n): ").lower() # pedimos s o n
    if r=="s": # si dijo s
        return True
    else:
        return False

def imprimir_ordenados(alumnos): # función para mostrar la lista de mayor a menor peso
    ordenados=sorted(alumnos,key=lambda x:x[3],reverse=True) # ordena usando el peso (posición 3)
    print("\nLISTADO ORDENADO POR PESO") # título de salida
    for a in ordenados: # recorro cada alumno en el orden ya calculado
        print("Nombre:",a[0],"- Peso:",a[3],"- Gripe:",a[1],"- Tos:",a[2]) # muestro todos los datos

def main():
    N=int(input("Número de alumnos: ")) # pedimos cuantos alumnos
    alumnos=[] # aca guardo la info

    for i in range(N): # repetimos N veces
        print("\nAlumno", i+1) 
        nombre=input("Nombre: ") # pedimos nombre
        gripe=leer_booleano("¿Tuvo gripe en los últimos 3 meses?") # pedimos gripe
        tos=leer_booleano("¿Tuvo tos en los últimos 3 meses?") # pedimos tos
        peso=float(input("Peso: ")) # pedimos peso
        alumnos.append([nombre,gripe,tos,peso]) # guardamos todo en una lista

    # a) mostrar datos
    print("\nLISTA DE ALUMNOS")
    for a in alumnos:
        print("Nombre:",a[0],"- Gripe:",a[1],"- Tos:",a[2],"- Peso:",a[3])

    # b) % gripe y tos
    ambos=0
    for a in alumnos:
        if a[1] and a[2]: # si tuvo ambas
            ambos+=1
    if N>0:
        porcentaje=ambos*100.0/N # regla de tres
    else:
        porcentaje=0
    print("\n% con gripe y tos:",porcentaje)

    # c) promedio peso de los que tuvieron algo
    suma=0
    cuenta=0
    for a in alumnos:
        if a[1] or a[2]: # si tuvo gripe o tos
            suma+=a[3] # sumamos peso
            cuenta+=1
    if cuenta>0:
        promedio=suma/cuenta
        print("Promedio peso de afectados:",promedio)
    else:
        print("No hubo afectados")

    # ordenar por peso descendente
    imprimir_ordenados(alumnos) # llamo a la función para mostrar ordenados

if __name__=="__main__":
    main()
