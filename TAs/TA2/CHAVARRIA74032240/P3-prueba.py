import random  # importar módulo random
from P3 import ProfesorNombrado, ProfesorContratado, Departamento, Facultad  # importar clases principales

if __name__ == "__main__":  # punto de entrada principal
    random.seed(74032240)  # fijar semilla con DNI 74032240
    
    # crear facultad
    facultad = Facultad()  # crear instancia de Facultad
    
    # crear departamentos
    nombres_deptos = ["Matemáticas", "Física", "Química", "Biología"]  # lista nombres departamentos
    for nombre in nombres_deptos:  # iterar nombres departamentos
        facultad.agregar_departamento(nombre)  # agregar departamento a facultad
    
    # parámetros
    N = 40  # total de profesores
    
    print("=" * 80)  # imprimir separador
    print("SISTEMA DE GESTIÓN ACADÉMICA - FACULTAD")  # título del sistema
    print("=" * 80)  # imprimir separador
    
    # a) Generar planilla inicial
    print("\n" + "=" * 80)  # encabezado sección
    print("a) PLANILLA INICIAL - AÑO 1")  # subtítulo sección
    print("=" * 80)  # separador
    
    nombres = ["Juan", "María", "Carlos", "Ana", "Luis", "Carmen", "José",  # lista nombres
               "Isabel", "Miguel", "Laura", "Pedro", "Rosa", "Diego", "Elena",  # continuación lista nombres
               "Antonio", "Patricia", "Manuel", "Sofía", "Fernando", "Gloria"]  # continuación lista nombres
    
    apellidos = ["García", "Rodríguez", "Martínez", "López", "González",  # lista apellidos
                 "Pérez", "Sánchez", "Ramírez", "Torres", "Flores"]  # continuación apellidos
    
    # generar profesores aleatorios
    for i in range(N):  # repetir N veces
        num_id = f"P{10000 + i}"  # generar id único
        nombre = f"{random.choice(nombres)} {random.choice(apellidos)}"  # nombre aleatorio
        edad = random.randint(30, 68)  # edad aleatoria
        depto = random.choice(nombres_deptos)  # departamento aleatorio
        
        if random.random() < 0.7:  # 70% nombrados
            categoria = random.choice(["Auxiliar", "Asociado", "Principal"])  # elegir categoría
            prof = ProfesorNombrado(num_id, nombre, edad, depto, categoria)  # crear nombrado
        else:  # 30% contratados
            horas = random.randint(5, 19)  # horas contrato
            anios = random.randint(0, 7)  # años servicio
            prof = ProfesorContratado(num_id, nombre, edad, depto, horas, anios)  # crear contratado
        
        facultad.agregar_profesor(prof)  # añadir profesor a facultad
    
    # elegir autoridades año 1
    for dept in facultad.departamentos.values():  # recorrer departamentos
        dept.elegir_jefe(1)  # elegir jefe año 1
    facultad.elegir_vicedecano(1)  # elegir vicedecano año 1
    facultad.elegir_decano(1)  # elegir decano año 1
    
    # mostrar nombrados por departamento
    for nombre_dept, dept in facultad.departamentos.items():  # recorrer departamentos
        print(f"\n--- DEPARTAMENTO DE {nombre_dept.upper()} ---")  # título departamento
        print(f"Jefe: {dept.jefe.nombre if dept.jefe else 'Sin jefe'}")  # mostrar jefe
        print("\nProfesores Nombrados:")  # encabezado nombrados
        nombrados = dept.get_nombrados()  # obtener nombrados del depto
        for i, prof in enumerate(nombrados, 1):  # enumerar nombrados
            print(f"  {i}. {prof.nombre} - {prof.categoria} ({prof.edad} años)")  # imprimir nombrado
    
    print(f"\n--- AUTORIDADES DE LA FACULTAD ---")  # encabezado autoridades
    print(f"Decano: {facultad.decano.nombre if facultad.decano else 'Sin decano'}")  # mostrar decano
    print(f"Vicedecano: {facultad.vicedecano.nombre if facultad.vicedecano else 'Sin vicedecano'}")  # mostrar vicedecano
    
    # verificar ceses año 1
    cesados_1 = [p for dept in facultad.departamentos.values()  # lista cesados
                 for p in dept.profesores if p.debe_cesar()]  # condición cese
    if cesados_1:  # si hay cesados
        print(f"\nProfesores que cesarán al término del año:")  # encabezado ceses
        for prof in cesados_1:  # listar cesados
            print(f"  - {prof.nombre} ({prof.edad} años)")  # imprimir cesado
    else:  # si no hay cesados
        print(f"\nNo hay profesores que cesen este año.")  # mensaje ninguno
    
    # guardar estado año 1
    facultad.guardar_estado(1)  # almacenar estado
    
    # b) Mostrar contratados
    print("\n" + "=" * 80)  # separador sección b
    print("b) PROFESORES CONTRATADOS - AÑO 1")  # subtítulo sección b
    print("=" * 80)  # separador
    
    for nombre_dept, dept in facultad.departamentos.items():  # recorrer departamentos
        print(f"\n--- DEPARTAMENTO DE {nombre_dept.upper()} ---")  # título departamento
        contratados = dept.get_contratados()  # obtener contratados
        if contratados:  # si hay contratados
            print("Profesores Contratados:")  # encabezado contratados
            for i, prof in enumerate(contratados, 1):  # enumerar contratados
                print(f"  {i}. {prof.nombre} - {prof.horas}h "  # imprimir contratado
                      f"({prof.anios_servicio} años servicio, {prof.edad} años)")  # detalles contratado
        else:  # si no hay contratados
            print("No hay profesores contratados")  # mensaje ninguno
    
    # c) Simulación 10 años
    print("\n" + "=" * 80)  # separador sección c
    print("c) SIMULACIÓN DE 10 AÑOS")  # subtítulo sección c
    print("=" * 80)  # separador
    
    for anio in range(2, 11):  # años 2 a 10
        print(f"\n{'=' * 80}")  # separador año
        print(f"AÑO {anio}")  # mostrar año
        print(f"{'=' * 80}")  # separador año
        
        # avanzar año
        facultad.avanzar_anio(anio)  # actualizar edad y años
        
        # procesar ceses
        cesados = facultad.procesar_ceses()  # obtener ceses
        if cesados:  # si hubo ceses
            print("\nProfesores CESANTES:")  # encabezado cesantes
            for prof in cesados:  # listar cesantes
                print(f"  - {prof.nombre} ({prof.edad} años)")  # imprimir cesante
        
        # procesar contratados
        promovidos = facultad.procesar_contratados()  # promover contratados
        if promovidos:  # si hubo promociones
            print("\nProfesores PROMOVIDOS a Auxiliar:")  # encabezado promovidos
            for prof in promovidos:  # listar promovidos
                print(f"  - {prof.nombre} (Depto: {prof.departamento})")  # imprimir promovido
        
        # verificar cargos terminados
        facultad.verificar_cargos_terminados(anio)  # verificar cargos acabados
        
        # reelegir autoridades si es necesario
        for dept in facultad.departamentos.values():  # recorrer departamentos
            if dept.jefe is None:  # si no hay jefe
                dept.elegir_jefe(anio)  # elegir nuevo jefe
        
        if facultad.vicedecano is None:  # si no hay vicedecano
            facultad.elegir_vicedecano(anio)  # elegir nuevo vicedecano
        
        if facultad.decano is None:  # si no hay decano
            facultad.elegir_decano(anio)  # elegir nuevo decano
        
        # mostrar planilla
        for nombre_dept, dept in facultad.departamentos.items():  # recorrer departamentos
            print(f"\n--- DEPARTAMENTO DE {nombre_dept.upper()} ---")  # título departamento
            print(f"Jefe: {dept.jefe.nombre if dept.jefe else 'Sin jefe'}")  # mostrar jefe
            
            nombrados = dept.get_nombrados()  # obtener nombrados
            if nombrados:  # si hay nombrados
                print(f"Nombrados ({len(nombrados)}):")  # mostrar cantidad nombrados
                for prof in nombrados[:3]:  # primeros tres nombrados
                    print(f"  - {prof.nombre} ({prof.categoria})")  # imprimir nombrado
                if len(nombrados) > 3:  # si hay más
                    print(f"  ... y {len(nombrados) - 3} más")  # indicar cantidad restante
            
            contratados = dept.get_contratados()  # obtener contratados
            if contratados:  # si hay contratados
                print(f"Contratados ({len(contratados)}):")  # mostrar cantidad contratados
                for prof in contratados[:3]:  # primeros tres contratados
                    print(f"  - {prof.nombre} ({prof.horas}h)")  # imprimir contratado
                if len(contratados) > 3:  # si hay más
                    print(f"  ... y {len(contratados) - 3} más")  # indicar cantidad restante
        
        print(f"\n--- AUTORIDADES ---")  # encabezado autoridades
        print(f"Decano: {facultad.decano.nombre if facultad.decano else 'Sin decano'}")  # mostrar decano
        print(f"Vicedecano: {facultad.vicedecano.nombre if facultad.vicedecano else 'Sin vicedecano'}")  # mostrar vicedecano
        
        # guardar estado
        facultad.guardar_estado(anio)  # guardar estado anual
    
    # d) Mostrar histórico completo
    print("\n" + "=" * 80)  # separador sección d
    print("d) HISTÓRICO COMPLETO - RESUMEN")  # subtítulo histórico
    print("=" * 80)  # separador
    
    for estado in facultad.historico:  # recorrer histórico guardado
        anio = estado['anio']  # año del estado
        print(f"\n--- AÑO {anio} ---")  # imprimir año
        print(f"Decano: {estado['decano']}")  # mostrar decano guardado
        print(f"Vicedecano: {estado['vicedecano']}")  # mostrar vicedecano guardado
        
        for nombre_dept, datos in estado['departamentos'].items():  # recorrer departamentos históricos
            total_nom = len(datos['nombrados'])  # contar nombrados
            total_con = len(datos['contratados'])  # contar contratados
            print(f"  {nombre_dept}: {total_nom} nombrados, {total_con} contratados "  # imprimir resumen
                  f"(Jefe: {datos['jefe']})")  # mostrar jefe
    
    # e) Consulta específica
    print("\n" + "=" * 80)  # separador sección e
    print("e) CONSULTA ESPECÍFICA - AÑO Y DEPARTAMENTO")  # subtítulo consulta
    print("=" * 80)  # separador
    
    # usar valores fijos para ejemplo
    anio_consulta = 5  # año ejemplo
    depto_consulta = "Matemáticas"  # departamento ejemplo
    
    print(f"\nConsulta: Año {anio_consulta}, Departamento {depto_consulta}")  # imprimir consulta
    
    estado = facultad.get_estado_anio(anio_consulta)  # obtener estado consultado
    if estado:  # si existe estado
        print(f"\n--- INFORMACIÓN DEL AÑO {anio_consulta} ---")  # encabezado año
        print(f"Decano de la Facultad: {estado['decano']}")  # mostrar decano
        print(f"Vicedecano de la Facultad: {estado['vicedecano']}")  # mostrar vicedecano
        
        if depto_consulta in estado['departamentos']:  # si depto en estado
            datos = estado['departamentos'][depto_consulta]  # datos del depto
            print(f"\n--- DEPARTAMENTO DE {depto_consulta.upper()} ---")  # título depto
            print(f"Jefe de Departamento: {datos['jefe']}")  # mostrar jefe depto
            
            print(f"\nProfesores Nombrados ({len(datos['nombrados'])}):")  # encabezado nombrados
            for i, prof_data in enumerate(datos['nombrados'], 1):  # enumerar nombrados
                print(f"  {i}. {prof_data[1]} - {prof_data[2]} ({prof_data[3]} años)")  # imprimir nombrado
            
            print(f"\nProfesores Contratados ({len(datos['contratados'])}):")  # encabezado contratados
            for i, prof_data in enumerate(datos['contratados'], 1):  # enumerar contratados
                print(f"  {i}. {prof_data[1]} - {prof_data[2]}h ({prof_data[3]} años)")  # imprimir contratado
    else:  # si no existe estado
        print("No se encontró información para ese año")  # mensaje no encontrado
    
    print("\n" + "=" * 80)  # separador final
    print("FIN DE LA SIMULACIÓN")  # mensaje final
    print("=" * 80)  # separador final
    print(f"\nTotal profesores cesantes en 10 años: {len(facultad.profesores_cesantes)}")  # imprimir total cesantes