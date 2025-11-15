import random  # módulo para generar aleatorios
from P1 import Pelicula, Espectador, Sala  # clases del proyecto

if __name__ == "__main__":  # punto de entrada
    random.seed(74032240)  # usar DNI 74032240 como semilla
    
    # datos para películas aleatorias
    titulos = ["Avatar 3", "Matrix 5", "Avengers X", "Titanic 2", 
               "Jurassic World", "Star Wars IX"]  # títulos posibles
    directores = ["Cameron", "Wachowski", "Russo", "Spielberg", 
                  "Nolan", "Tarantino"]  # directores posibles
    
    # crear películas aleatorias
    pelicula1 = Pelicula(
        random.choice(titulos),
        random.randint(90, 180),
        random.choice([0, 13, 16, 18]),
        random.choice(directores)
    )  # crear película aleatoria
    
    pelicula2 = Pelicula(
        random.choice(titulos),
        random.randint(90, 180),
        random.choice([0, 13, 16, 18]),
        random.choice(directores)
    )  # otra película aleatoria
    
    # crear dos salas de cine
    sala1 = Sala(1, 8, 9, pelicula1, 15.0)  # crear sala 1
    sala2 = Sala(2, 8, 9, pelicula2, 18.0)  # crear sala 2
    
    print("=" * 60)
    print("SISTEMA DE CINE - SIMULACIÓN")  # cabecera simulación
    print("=" * 60)
    print(f"\nSALA 1: {pelicula1}")  # mostrar película sala1
    print(f"Precio: S/.{sala1.precio}")  # mostrar precio
    print(f"\nSALA 2: {pelicula2}")  # mostrar película sala2
    print(f"Precio: S/.{sala2.precio}")  # mostrar precio
    print()
    
    # generar nombres para espectadores
    nombres = ["Juan", "María", "Pedro", "Ana", "Carlos", "Lucía",
               "Diego", "Carmen", "Miguel", "Rosa", "Luis", "Elena",
               "Jorge", "Isabel", "Manuel", "Patricia", "Antonio", "Laura"]  # nombres base
    
    # generar espectadores y sentar en sala 1
    print("\n--- SENTANDO ESPECTADORES EN SALA 1 ---")
    intentos_sala1 = 0
    for i in range(80):  # intentar sentar hasta 80
        nombre = random.choice(nombres) + str(i+1)  # nombre aleatorio
        edad = random.randint(5, 65)  # edad aleatoria
        dinero = random.uniform(5, 25)  # dinero aleatorio
        
        espectador = Espectador(nombre, edad, dinero)  # construir espectador
        if sala1.sentar_espectador(espectador):  # intentar sentar espectador
            intentos_sala1 += 1
    
    print(f"Espectadores sentados: {len(sala1.espectadores_admitidos)}")  # contar sentados
    
    # generar espectadores y sentar en sala 2
    print("\n--- SENTANDO ESPECTADORES EN SALA 2 ---")
    intentos_sala2 = 0
    for i in range(80):  # intentar sentar hasta 80
        nombre = random.choice(nombres) + str(i+100)  # nombre aleatorio
        edad = random.randint(5, 65)  # edad aleatoria
        dinero = random.uniform(5, 30)  # dinero aleatorio
        
        espectador = Espectador(nombre, edad, dinero)  # construir espectador
        if sala2.sentar_espectador(espectador):  # intentar sentar espectador
            intentos_sala2 += 1
    
    print(f"Espectadores sentados: {len(sala2.espectadores_admitidos)}")  # contar sentados
    
    # mostrar recaudación total
    print("\n" + "=" * 60)
    print("RECAUDACIÓN POR SALA")
    print("=" * 60)
    print(f"Sala 1: S/.{sala1.recaudacion:.2f}")  # mostrar recaudación
    print(f"Sala 2: S/.{sala2.recaudacion:.2f}")  # mostrar recaudación
    print(f"TOTAL: S/.{sala1.recaudacion + sala2.recaudacion:.2f}")  # total recaudación
    
    # listado de espectadores sala 1
    print("\n" + "=" * 60)
    print("ESPECTADORES QUE ASISTIERON - SALA 1")
    print("=" * 60)
    for i, esp in enumerate(sala1.espectadores_admitidos, 1):
        print(f"{i}. {esp}")  # listar asistentes
    
    # listado de espectadores sala 2
    print("\n" + "=" * 60)
    print("ESPECTADORES QUE ASISTIERON - SALA 2")
    print("=" * 60)
    for i, esp in enumerate(sala2.espectadores_admitidos, 1):
        print(f"{i}. {esp}")  # listar asistentes
    
    # espectadores por edad en sala 1
    print("\n" + "=" * 60)
    print("EDADES EXTREMAS - SALA 1")
    print("=" * 60)
    menor1 = sala1.get_espectador_menor()  # obtener menor
    mayor1 = sala1.get_espectador_mayor()  # obtener mayor
    if menor1 and mayor1:
        print(f"Menor edad: {menor1}")
        print(f"Mayor edad: {mayor1}")
    
    # espectadores por edad en sala 2
    print("\n" + "=" * 60)
    print("EDADES EXTREMAS - SALA 2")
    print("=" * 60)
    menor2 = sala2.get_espectador_menor()  # obtener menor
    mayor2 = sala2.get_espectador_mayor()  # obtener mayor
    if menor2 and mayor2:
        print(f"Menor edad: {menor2}")
        print(f"Mayor edad: {mayor2}")
    
    # asientos vacíos sala 1
    print("\n" + "=" * 60)
    print("ASIENTOS VACÍOS - SALA 1")
    print("=" * 60)
    vacios1 = sala1.get_asientos_vacios()  # listar asientos vacíos
    print(f"Total vacíos: {len(vacios1)}")  # mostrar total vacíos
    if len(vacios1) <= 20:
        print(f"Asientos: {', '.join(vacios1)}")  # mostrar todos
    else:
        print(f"Primeros 20: {', '.join(vacios1[:20])}")  # mostrar primeros 20
    
    # asientos vacíos sala 2
    print("\n" + "=" * 60)
    print("ASIENTOS VACÍOS - SALA 2")
    print("=" * 60)
    vacios2 = sala2.get_asientos_vacios()  # listar asientos vacíos
    print(f"Total vacíos: {len(vacios2)}")  # mostrar total vacíos
    if len(vacios2) <= 20:
        print(f"Asientos: {', '.join(vacios2)}")  # mostrar todos
    else:
        print(f"Primeros 20: {', '.join(vacios2[:20])}")  # mostrar primeros 20
    
    # filas llenas en sala 2
    print("\n" + "=" * 60)
    print("FILAS COMPLETAMENTE LLENAS - SALA 2")
    print("=" * 60)
    filas_llenas = sala2.contar_filas_llenas()  # contar filas completas
    print(f"Cantidad de filas llenas: {filas_llenas}")  # mostrar cantidad
    
    # menores de edad en sala 1
    print("\n" + "=" * 60)
    print("MENORES DE EDAD - SALA 1")
    print("=" * 60)
    menores = sala1.get_menores_edad()  # obtener menores de edad
    print(f"Total menores de edad: {len(menores)}")  # mostrar total menores
    for i, menor in enumerate(menores, 1):
        print(f"{i}. {menor}")  # listar menores
    
    print("\n" + "=" * 60)
    print("FIN DE LA SIMULACIÓN")  # fin simulación
    print("=" * 60)