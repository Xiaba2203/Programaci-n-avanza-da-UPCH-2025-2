# 📚 README - 300 FUNCIONES PYTHON

Este documento contiene la descripción completa de las 300 funciones Python organizadas por nivel y categoría para facilitar la búsqueda y referencia rápida.

---

## 🔹 NIVEL GENERAL (100 FUNCIONES)

### CATEGORÍA: SECUENCIAS Y ESTRUCTURAS DE DATOS (10)

1. **contar_elemento(lista, elemento)** - Cuenta cuántas veces aparece un elemento específico en una lista
2. **invertir_lista(lista)** - Invierte una lista sin usar slicing, manualmente elemento por elemento
3. **encontrar_max_min(lista)** - Encuentra el valor máximo y mínimo de una lista manualmente sin usar funciones built-in
4. **calcular_estadisticas(lista)** - Calcula la media, moda y mediana de una lista de números
5. **eliminar_duplicados(lista)** - Elimina elementos duplicados de una lista manteniendo el orden original
6. **aplanar_lista(lista_listas)** - Convierte una lista de listas en una sola lista plana
7. **rotar_lista(lista, n)** - Rota una lista n posiciones hacia la derecha
8. **generar_cuadrados(n)** - Genera una lista con los cuadrados de los números del 1 al n
9. **filtrar_pares(lista)** - Filtra y retorna solo los elementos pares de una lista
10. **concatenar_listas(*listas)** - Concatena múltiples listas en una sola lista

### CATEGORÍA: STRINGS (10)

11. **es_palindromo(palabra)** - Verifica si una palabra es palíndromo (se lee igual al revés)
12. **contar_vocales(cadena)** - Cuenta el número total de vocales en una cadena de texto
13. **invertir_cadena(cadena)** - Invierte una cadena de texto manualmente sin usar slicing
14. **reemplazar_espacios(cadena)** - Reemplaza todos los espacios en blanco por guiones
15. **eliminar_no_alfabeticos(cadena)** - Elimina todos los caracteres que no sean letras del alfabeto
16. **contar_palabras(oracion)** - Cuenta el número de palabras en una oración
17. **generar_subcadenas(cadena)** - Genera todas las subcadenas posibles de una cadena
18. **comparar_strings(str1, str2)** - Compara dos strings sin usar el operador ==
19. **convertir_mayus_minus(cadena)** - Convierte cadena a mayúsculas y minúsculas
20. **comprimir_string(cadena)** - Comprime un string eliminando caracteres consecutivos repetidos

### CATEGORÍA: DICCIONARIOS Y CONJUNTOS (10)

21. **frecuencia_caracteres(cadena)** - Cuenta la frecuencia de cada carácter usando diccionario
22. **crear_diccionario_notas()** - Crea un diccionario de ejemplo con alumnos y sus notas
23. **invertir_diccionario(diccionario)** - Intercambia claves y valores de un diccionario
24. **unir_diccionarios(*diccionarios)** - Une múltiples diccionarios en uno solo
25. **interseccion_conjuntos(set1, set2)** - Encuentra la intersección entre dos conjuntos
26. **union_conjuntos(set1, set2)** - Encuentra la unión de dos conjuntos
27. **es_subconjunto(subset, superset)** - Verifica si un conjunto es subconjunto de otro
28. **eliminar_duplicados_set(lista)** - Elimina duplicados de una lista usando conjuntos
29. **mapear_cuadrados(n)** - Crea diccionario que mapea números del 1 al n con sus cuadrados
30. **ordenar_diccionario_valores(diccionario)** - Ordena un diccionario por sus valores

### CATEGORÍA: ALGORITMOS BÁSICOS (10)

31. **busqueda_lineal(lista, elemento)** - Implementa búsqueda lineal para encontrar un elemento
32. **busqueda_binaria(lista, elemento)** - Implementa búsqueda binaria en lista ordenada
33. **ordenamiento_burbuja(lista)** - Implementa algoritmo de ordenamiento burbuja
34. **ordenamiento_insercion(lista)** - Implementa algoritmo de ordenamiento por inserción
35. **ordenamiento_seleccion(lista)** - Implementa algoritmo de ordenamiento por selección
36. **fibonacci(n)** - Genera la serie de Fibonacci hasta el término n
37. **factorial(n)** - Calcula el factorial de un número de forma iterativa
38. **es_primo(n)** - Verifica si un número es primo
39. **mcd(a, b)** - Calcula el Máximo Común Divisor usando algoritmo de Euclides
40. **mcm(a, b)** - Calcula el Mínimo Común Múltiplo

### CATEGORÍA: ARCHIVOS (10)

41. **escribir_archivo(nombre, texto)** - Escribe texto en un archivo
42. **leer_archivo(nombre)** - Lee todo el contenido de un archivo
43. **leer_lineas(nombre)** - Lee un archivo línea por línea y retorna lista
44. **contar_lineas(nombre)** - Cuenta cuántas líneas tiene un archivo
45. **contar_palabras_archivo(nombre)** - Cuenta cuántas palabras tiene un archivo
46. **copiar_archivo(origen, destino)** - Copia el contenido de un archivo a otro
47. **invertir_archivo(nombre)** - Invierte el orden de las líneas de un archivo
48. **buscar_palabra_archivo(nombre, palabra)** - Busca si una palabra existe en un archivo
49. **reemplazar_archivo(nombre, vieja, nueva)** - Reemplaza texto en un archivo
50. **guardar_lista(nombre, lista)** - Guarda una lista en un archivo línea por línea

### CATEGORÍA: PROGRAMACIÓN ESTRUCTURADA (10)

51. **calcular_figuras(figura, *medidas)** - Calcula área y perímetro de figuras geométricas
52. **tabla_multiplicar(numero)** - Genera la tabla de multiplicar de un número
53. **promedio_numeros(numeros)** - Calcula el promedio de una lista de números
54. **calculadora(operacion, a, b)** - Simula calculadora básica con 4 operaciones
55. **generar_aleatorios(cantidad, minimo, maximo)** - Genera números aleatorios en un rango
56. **lanzar_dado()** - Simula el lanzamiento de un dado de 6 caras
57. **lanzar_moneda()** - Simula el lanzamiento de una moneda
58. **cronometro_simple(segundos)** - Simula un cronómetro que cuenta segundos
59. **generar_contraseña(longitud)** - Genera una contraseña aleatoria de longitud dada
60. **validar_contraseña(contraseña)** - Valida una contraseña según criterios de seguridad

### CATEGORÍA: PENSAMIENTO LÓGICO (10)

61. **torres_hanoi(n, origen, destino, auxiliar)** - Resuelve las Torres de Hanoi recursivamente
62. **problema_ranas()** - Implementación del puzzle clásico de las ranas
63. **generar_permutaciones(lista)** - Genera todas las permutaciones posibles de una lista
64. **generar_combinaciones(lista, r)** - Genera todas las combinaciones de r elementos
65. **cambio_monedas(cantidad, monedas)** - Resuelve el problema del cambio con algoritmo greedy
66. **automata_paridad(numero)** - Simula autómata que determina si número es par/impar
67. **suma_digitos(numero)** - Calcula la suma de todos los dígitos de un número
68. **decimal_a_binario(numero)** - Convierte número decimal a binario
69. **binario_a_decimal(binario)** - Convierte número binario a decimal
70. **triangulo_pascal(n)** - Genera el triángulo de Pascal de n filas

### CATEGORÍA: NÚMEROS Y MATEMÁTICAS (10)

71. **es_capicua(numero)** - Verifica si un número es capicúa (palíndromo numérico)
72. **suma_pares(n)** - Calcula la suma de todos los números pares hasta n
73. **suma_impares(n)** - Calcula la suma de todos los números impares hasta n
74. **es_perfecto(n)** - Verifica si un número es perfecto (suma de divisores = número)
75. **es_abundante(n)** - Verifica si un número es abundante (suma de divisores > número)
76. **es_deficiente(n)** - Verifica si un número es deficiente (suma de divisores < número)
77. **potencia_manual(base, exponente)** - Calcula potencia manualmente sin usar **
78. **raiz_babilonica(numero)** - Calcula raíz cuadrada usando método babilónico
79. **aproximar_pi(terminos)** - Aproxima el valor de π usando series infinitas
80. **ecuacion_cuadratica(a, b, c)** - Resuelve ecuación cuadrática ax²+bx+c=0

### CATEGORÍA: PRÁCTICAS TÍPICAS DE EXAMEN (10)

81. **validar_dni(dni)** - Valida si un número es válido como DNI (8 dígitos)
82. **calcular_descuento(monto)** - Calcula descuento en compra según el monto
83. **cajero_automatico(saldo_inicial)** - Simula cajero automático con operaciones básicas
84. **control_stock()** - Simula sistema de control de inventario
85. **reporte_ventas(ventas)** - Genera reporte estadístico de ventas
86. **calcular_edad(año_nacimiento)** - Calcula edad a partir del año de nacimiento
87. **es_bisiesto(año)** - Verifica si un año es bisiesto
88. **calendario_mes(mes, año)** - Genera lista de días de un mes específico
89. **lista_asistencia(estudiantes)** - Simula lista de asistencia aleatoria
90. **clasificar_notas(notas)** - Clasifica notas en aprobado/desaprobado

### CATEGORÍA: EXTRA (10)

91. **convertir_temperatura(valor, origen, destino)** - Convierte entre Celsius, Fahrenheit y Kelvin
92. **convertir_hora(hora, formato)** - Convierte entre formato 12h y 24h
93. **calcular_interes(principal, tasa, tiempo)** - Calcula interés simple de un préstamo
94. **piedra_papel_tijera()** - Simula juego de piedra, papel o tijera
95. **ahorcado_basico(palabra)** - Simula juego del ahorcado básico
96. **bingo_aleatorio()** - Genera cartón de bingo con números aleatorios
97. **loteria_boletos(cantidad_boletos)** - Simula lotería con boletos numerados
98. **simular_ruleta()** - Simula giro de ruleta con colores
99. **generar_qr_simple(texto)** - Genera matriz simple simulando código QR
100. **leer_codigo_barras(codigo)** - Simula lectura de código de barras

---

## 🔹 NIVEL MEDIO (100 FUNCIONES)

### CATEGORÍA A: LISTAS, TUPLAS, CONJUNTOS Y DICCIONARIOS (20)

101. **crear_20_primos()** - Crea lista con los primeros 20 números primos
102. **crear_tupla_dias()** - Crea tupla con los días de la semana
103. **intercambiar_claves_valores(diccionario)** - Intercambia claves y valores en diccionario
104. **contar_unicos(lista)** - Cuenta elementos únicos usando set
105. **combinaciones_listas(lista1, lista2)** - Genera todas las combinaciones de dos listas
106. **ordenar_notas(diccionario_notas)** - Ordena diccionario de notas de mayor a menor
107. **conjunto_caracteres(cadena)** - Crea conjunto con caracteres únicos de cadena
108. **palabras_comunes(lista1, lista2)** - Encuentra palabras comunes entre dos listas
109. **unir_diccionarios(*diccionarios)** - Une varios diccionarios en uno solo
110. **contar_repetidos(lista)** - Cuenta cuántos elementos están repetidos
111. **lista_a_diccionario(lista_listas)** - Convierte lista de listas en diccionario
112. **eliminar_duplicados_orden(lista)** - Elimina duplicados manteniendo orden original
113. **frecuencia_palabras(texto)** - Crea diccionario con frecuencias de palabras
114. **clave_max_valor(diccionario)** - Extrae clave con valor más alto
115. **multiplos_3_menores_100()** - Crea conjunto con múltiplos de 3 menores a 100
116. **interseccion_3_conjuntos(set1, set2, set3)** - Intersección entre 3 conjuntos
117. **cuadrados_10_primeros()** - Lista con cuadrados de primeros 10 números
118. **es_subdiccionario(sub_dict, dict_principal)** - Verifica si es subdiccionario
119. **crear_dict_zip(lista1, lista2)** - Crea diccionario combinando dos listas
120. **tuplas_a_dict(lista_tuplas)** - Convierte lista de tuplas en diccionario

### CATEGORÍA B: ARCHIVOS (20)

121. **leer_csv_primeras_10(nombre_archivo)** - Lee primeras 10 líneas de CSV
122. **guardar_lista_txt(lista, nombre_archivo)** - Guarda lista en archivo .txt
123. **leer_numerar_lineas(nombre_archivo)** - Lee archivo numerando cada línea
124. **crear_archivo_100()** - Crea archivo con números del 1 al 100
125. **guardar_dict_json_simple(diccionario, nombre_archivo)** - Guarda diccionario como JSON simple
126. **leer_json_simple(nombre_archivo)** - Lee archivo JSON simple como diccionario
127. **escribir_binario(lista_enteros, nombre_archivo)** - Escribe enteros en archivo binario
128. **leer_binario(nombre_archivo)** - Lee archivo binario y retorna enteros
129. **contar_palabra_archivo(nombre_archivo, palabra)** - Cuenta apariciones de palabra en archivo
130. **copiar_archivo_simple(origen, destino)** - Copia contenido entre archivos
131. **reemplazar_vocales_archivo(nombre_archivo)** - Reemplaza vocales por asteriscos
132. **guardar_primos_500()** - Guarda números primos hasta 500 en archivo
133. **contar_lineas_no_vacias(nombre_archivo)** - Cuenta líneas que no están vacías
134. **generar_log_errores()** - Genera archivo log con errores de ejemplo
135. **guardar_lista_dict_json(lista_dict, nombre_archivo)** - Guarda lista de diccionarios como JSON
136. **leer_csv_lista_listas(nombre_archivo)** - Lee CSV y convierte en lista de listas
137. **escribir_tabla_multiplicar_archivo(numero)** - Escribe tabla de multiplicar en archivo
138. **guardar_pares_200()** - Guarda números pares hasta 200 en archivo
139. **crear_historial_operaciones()** - Crea historial de operaciones matemáticas
140. **guardar_aprobados(diccionario_notas)** - Guarda solo alumnos aprobados en archivo

### CATEGORÍA C: NUMPY (20)

141. **crear_array_1_100()** - Crea array NumPy con números del 1 al 100
142. **crear_matriz_3x3_aleatoria()** - Crea matriz 3x3 con números aleatorios
143. **calcular_estadisticas_array(array)** - Calcula media, mediana y desviación estándar
144. **crear_matriz_identidad_5()** - Crea matriz identidad de tamaño 5x5
145. **generar_20_aleatorios_0_1()** - Genera 20 números aleatorios entre 0 y 1
146. **crear_matriz_4x4_1_16()** - Crea matriz 4x4 con números del 1 al 16
147. **transponer_matriz(matriz)** - Calcula la transpuesta de una matriz
148. **calcular_determinante_3x3(matriz)** - Calcula determinante de matriz 3x3
149. **calcular_inversa_3x3(matriz)** - Calcula inversa de matriz 3x3
150. **suma_elementos_matriz(matriz)** - Suma todos los elementos de matriz
151. **producto_punto_vectores(vector1, vector2)** - Calcula producto punto entre vectores
152. **multiplicar_matrices(matriz1, matriz2)** - Multiplica dos matrices
153. **max_min_array(array)** - Encuentra máximo y mínimo de array
154. **crear_array_ceros_10()** - Crea array de 10 ceros
155. **crear_array_unos_10()** - Crea array de 10 unos
156. **crear_array_equidistante()** - Crea array con números equidistantes entre 0 y 1
157. **crear_matriz_diagonal(lista)** - Genera matriz diagonal con valores dados
158. **sumar_matrices(matriz1, matriz2)** - Suma dos matrices elemento por elemento
159. **restar_matrices(matriz1, matriz2)** - Resta dos matrices elemento por elemento
160. **resolver_sistema_ecuaciones(A, b)** - Resuelve sistema de ecuaciones lineales

### CATEGORÍA D: PANDAS (20)

161. **leer_csv_dataframe(nombre_archivo)** - Lee archivo CSV en DataFrame
162. **mostrar_primeras_5(df)** - Muestra las primeras 5 filas del DataFrame
163. **mostrar_ultimas_10(df)** - Muestra las últimas 10 filas del DataFrame
164. **mostrar_nombres_columnas(df)** - Retorna lista con nombres de columnas
165. **acceder_columna(df, nombre_columna)** - Accede a una columna específica
166. **acceder_varias_columnas(df, lista_columnas)** - Accede a varias columnas a la vez
167. **filtrar_filas(df, columna, valor)** - Filtra filas que cumplen condición específica
168. **ordenar_dataframe(df, columna)** - Ordena DataFrame por una columna
169. **promedio_columna(df, columna)** - Calcula promedio de columna numérica
170. **contar_unicos_columna(df, columna)** - Cuenta valores únicos en columna
171. **reemplazar_nulos_media(df, columna)** - Reemplaza valores nulos con la media
172. **eliminar_filas_nulos(df)** - Elimina todas las filas con valores nulos
173. **crear_nueva_columna(df, nueva_col, col1, col2)** - Crea columna combinando otras dos
174. **agrupar_dataframe(df, columna)** - Agrupa DataFrame por una columna
175. **estadisticas_basicas(df)** - Calcula estadísticas básicas del DataFrame
176. **guardar_csv(df, nombre_archivo)** - Guarda DataFrame en archivo CSV
177. **leer_excel_dataframe(nombre_archivo)** - Lee archivo Excel en DataFrame
178. **fusionar_dataframes(df1, df2, columna)** - Fusiona dos DataFrames por columna común
179. **concatenar_dataframes(df1, df2)** - Concatena dos DataFrames verticalmente
180. **convertir_categorica_numerica(df, columna)** - Convierte columna categórica en numérica

### CATEGORÍA E: MATPLOTLIB (20)

181. **graficar_lineas(lista_numeros)** - Grafica lista de números en gráfico de líneas
182. **graficar_barras(lista_numeros)** - Grafica lista de números en gráfico de barras
183. **crear_histograma()** - Crea histograma de 100 números aleatorios
184. **graficar_cuadratica()** - Grafica función cuadrática x²
185. **graficar_seno(inicio, fin)** - Grafica función seno en rango dado
186. **graficar_coseno(inicio, fin)** - Grafica función coseno en rango dado
187. **graficar_dos_funciones()** - Grafica seno y coseno en mismo gráfico
188. **personalizar_grafico(lista_numeros)** - Personaliza color y estilo de línea
189. **agregar_titulo_etiquetas(x, y, titulo, xlabel, ylabel)** - Añade título y etiquetas
190. **agregar_leyenda(x, y1, y2, etiqueta1, etiqueta2)** - Añade leyenda al gráfico
191. **guardar_grafico_png(lista_numeros, nombre_archivo)** - Guarda gráfico como PNG
192. **graficar_dispersion(x, y)** - Crea gráfico de dispersión
193. **graficar_mapa_calor(matriz)** - Grafica matriz como mapa de calor
194. **grafico_circular(valores, etiquetas)** - Crea gráfico circular de porcentajes
195. **graficar_polinomio_grado3()** - Grafica polinomio de grado 3
196. **diagrama_caja(datos)** - Crea diagrama de caja (boxplot)
197. **graficar_exponencial()** - Grafica curva exponencial
198. **subplots_multiples()** - Muestra varias gráficas en subplots
199. **graficar_acumulados(lista_valores)** - Grafica valores acumulados (escalera)
200. **animar_onda_seno()** - Crea animación simple de onda seno

---

## 🔹 NIVEL ESPECÍFICO (100 FUNCIONES)

### CATEGORÍA A: GESTIÓN Y SIMULACIONES (20)

201. **registrar_libro(titulo, autor, anio, disponible)** - Agrega libro a biblioteca con todos sus datos
202. **registrar_prestamo(titulo, ubicacion)** - Cambia estado de libro a prestado
203. **registrar_devolucion(titulo)** - Cambia estado de libro a disponible
204. **consultar_disponibilidad(libros, titulo)** - Verifica si libro está disponible
205. **listar_libros(libros)** - Lista todos los libros con formato legible
206. **libros_por_anio(libros, anio)** - Retorna libros publicados en año específico
207. **contar_prestados(libros)** - Cuenta cuántos libros están prestados
208. **uso_sala_vs_domicilio(libros)** - Compara préstamos en sala vs domicilio
209. **libro_mas_nuevo(libros)** - Encuentra libro con mayor año de edición
210. **libro_mas_antiguo(libros)** - Encuentra libro más antiguo
211. **libro_nombre_mas_largo(libros)** - Encuentra libro con título más largo
212. **guardar_libros_csv(libros, archivo)** - Exporta biblioteca a archivo CSV
213. **leer_libros_csv(archivo)** - Importa biblioteca desde archivo CSV
214. **buscar_libros_por_autor(libros, autor)** - Busca todos los libros de un autor
215. **borrar_libro(libros, titulo)** - Elimina libro del registro
216. **top_autores(libros)** - Muestra autores con más publicaciones
217. **filtrar_libros_rango_anios(libros, inicio, fin)** - Filtra libros por rango de años
218. **contar_libros_por_anio(libros)** - Cuenta libros agrupados por año
219. **estadisticas_biblioteca(libros)** - Genera resumen estadístico completo
220. **menu_biblioteca()** - Retorna opciones del menú de biblioteca

### CATEGORÍA B: JUEGOS Y SIMULACIONES ALEATORIAS (20)

221. **generar_carton_bingo(n)** - Crea cartón de bingo con n números únicos
222. **verificar_numero(carton, numero)** - Verifica si número está en cartón
223. **simular_bingo_jugadores(n)** - Simula juego de bingo entre 2 jugadores
224. **jugar_bingo_varios(jugadores, n)** - Simula bingo con múltiples jugadores
225. **generar_carton_matriz(filas, cols)** - Crea cartón de bingo en formato matriz
226. **contar_aciertos(carton, numeros_sorteados)** - Cuenta números coincidentes
227. **determinar_ganador(jugadores, sorteos)** - Determina ganador de bingo
228. **simular_tirada_dados(n)** - Simula n tiradas de dos dados
229. **frecuencia_dados(n)** - Calcula frecuencias de sumas en tiradas
230. **graficar_histograma_dados(n)** - Histograma de resultados de dados
231. **simular_ruleta(n)** - Simula n giros de ruleta europea
232. **probabilidad_ruleta_color(n)** - Estima probabilidades de colores en ruleta
233. **simulacion_moneda(n)** - Simula n lanzamientos de moneda
234. **frecuencia_moneda(n)** - Calcula proporciones de cara/sello
235. **graficar_moneda(n)** - Gráfico circular de frecuencias de moneda
236. **simular_loteria(numeros_totales, seleccionados)** - Simula sorteo de lotería
237. **probabilidad_loteria(numeros_totales, seleccionados, repeticiones)** - Calcula probabilidad lotería
238. **simulacion_cola_clientes(tiempo, tasa)** - Simula llegada de clientes a cola
239. **simulacion_atencion(tiempo, tasa_servicio)** - Modela tiempo de atención
240. **grafico_simulacion_clientes()** - Visualiza comportamiento de cola de clientes

### CATEGORÍA C: NUMPY (20)

241. **crear_matriz_aleatoria(filas, columnas)** - Crea matriz aleatoria de enteros 1-100
242. **suma_matriz(m)** - Suma todos los elementos de matriz
243. **maximo_minimo_matriz(m)** - Encuentra máximo y mínimo de matriz
244. **promedio_columnas(m)** - Calcula promedio por cada columna
245. **promedio_filas(m)** - Calcula promedio por cada fila
246. **multiplicar_matrices(a, b)** - Multiplica dos matrices NumPy
247. **resolver_sistema_lineal(a, b)** - Resuelve sistema Ax = b
248. **generar_matriz_identidad(n)** - Crea matriz identidad n×n
249. **calcular_determinante(m)** - Calcula determinante de matriz
250. **calcular_inversa(m)** - Calcula matriz inversa
251. **vector_norma(v)** - Calcula norma euclidiana de vector
252. **producto_punto(v1, v2)** - Producto escalar de dos vectores
253. **producto_cruz(v1, v2)** - Producto vectorial de dos vectores
254. **media_movil(arr, n)** - Calcula media móvil de ventana n
255. **matriz_diagonal(valores)** - Genera matriz diagonal con valores dados
256. **graficar_matriz_calor(m)** - Visualiza matriz como mapa de calor
257. **aplanar_matriz(m)** - Convierte matriz 2D en vector 1D
258. **reshape_matriz(m, filas, cols)** - Cambia dimensiones de matriz
259. **valores_propios(m)** - Calcula autovalores y autovectores
260. **comparar_vectores(v1, v2)** - Verifica igualdad entre vectores

### CATEGORÍA D: PANDAS (20)

261. **leer_dataset(url)** - Lee CSV desde URL en DataFrame
262. **mostrar_rango_filas(df, inicio, fin)** - Muestra filas entre índices dados
263. **ultima_fila(df)** - Retorna la última fila del DataFrame
264. **contar_condicion(df, columna, valor)** - Cuenta filas que cumplen condición
265. **frecuencia_combinaciones(df, col1, col2)** - Cuenta combinaciones de dos columnas
266. **proporcion_trabajo(df, col, limite)** - Calcula proporción que supera límite
267. **filtrar_por_rango(df, col, min, max)** - Filtra filas en rango de valores
268. **nueva_columna_cuadrado(df, col)** - Agrega columna con valores al cuadrado
269. **proporcion_minima(df, col1, col2)** - Encuentra grupo con menor proporción
270. **resumen_categoria(df, col)** - Resume registros por categoría
271. **agrupar_y_promediar(df, grupo, col)** - Agrupa y calcula promedios
272. **convertir_a_diccionario(df)** - Convierte DataFrame en lista de diccionarios
273. **guardar_csv(df, archivo)** - Exporta DataFrame a archivo CSV
274. **cargar_csv(archivo)** - Importa CSV a DataFrame
275. **fusionar_datasets(df1, df2, col)** - Une DataFrames por columna común
276. **concatenar_datasets(df1, df2)** - Une DataFrames verticalmente
277. **graficar_histograma_columna(df, col)** - Histograma de columna específica
278. **graficar_barras_columna(df, col)** - Gráfico de barras de frecuencias
279. **graficar_dos_columnas(df, col1, col2)** - Scatter plot de dos columnas
280. **resumen_estadistico(df)** - Descripción estadística completa del DataFrame

### CATEGORÍA E: GRÁFICOS AVANZADOS CON MATPLOTLIB (20)

281. **graficar_libros_anio(libros)** - Gráfico de barras con cantidad de libros por año
282. **graficar_prestamos(libros)** - Gráfico circular comparando préstamos sala vs domicilio
283. **graficar_uso_autores(libros)** - Gráfico de barras con autores más frecuentes
284. **graficar_numeros_primos(n)** - Gráfico de línea con los primeros n números primos
285. **graficar_matriz(m)** - Visualiza matriz NumPy como mapa de calor
286. **graficar_comparacion_vectores(v1, v2)** - Gráfico de barras comparando dos vectores
287. **graficar_resultados_bingo(jugadores)** - Gráfico circular con victorias de bingo
288. **graficar_histograma_aleatorio(n)** - Histograma de n números aleatorios
289. **graficar_funcion_cuadratica(a, b, c)** - Gráfica curva de función ax²+bx+c
290. **graficar_funcion_trigonometrica(func, inicio, fin)** - Gráfica seno/coseno/tangente
291. **graficar_boxplot_columna(df, col)** - Diagrama de caja de columna de DataFrame
292. **graficar_series_temporales(df, col)** - Gráfico de línea de evolución temporal
293. **graficar_pie_categoria(df, col)** - Gráfico circular de proporciones categóricas
294. **graficar_corr_matrix(df)** - Mapa de calor de matriz de correlaciones
295. **graficar_dispersion_colores(df, x, y, c)** - Scatter plot con colores por tercera variable
296. **graficar_comparacion_hist(df, col1, col2)** - Histogramas superpuestos de dos columnas
297. **graficar_doble_eje(x, y1, y2)** - Gráfico con dos series y doble eje Y
298. **graficar_animacion_seno()** - Animación simple de onda seno en movimiento
299. **graficar_barras_apiladas(df, col1, col2)** - Gráfico de barras apiladas por categorías
300. **graficar_polinomio(coef)** - Gráfica polinomio según lista de coeficientes

---

## 📋 RESUMEN POR NIVEL

### NIVEL GENERAL (100 funciones)
- **Secuencias y estructuras de datos:** 10 funciones básicas de listas, tuplas y arrays
- **Strings:** 10 funciones de manipulación y análisis de cadenas
- **Diccionarios y conjuntos:** 10 funciones de estructuras de datos avanzadas
- **Algoritmos básicos:** 10 implementaciones de algoritmos fundamentales
- **Archivos:** 10 funciones de lectura/escritura de archivos
- **Programación estructurada:** 10 funciones de lógica de programación
- **Pensamiento lógico:** 10 funciones de resolución de problemas complejos
- **Números y matemáticas:** 10 funciones matemáticas y numéricas
- **Prácticas típicas de examen:** 10 ejercicios comunes en evaluaciones
- **Extra:** 10 funciones adicionales variadas

### NIVEL MEDIO (100 funciones)
- **Listas, tuplas, conjuntos y diccionarios:** 20 funciones avanzadas de estructuras
- **Archivos:** 20 funciones de manejo avanzado de archivos y formatos
- **NumPy:** 20 funciones básicas de arrays y operaciones matemáticas
- **Pandas:** 20 funciones básicas de manipulación de DataFrames
- **Matplotlib:** 20 funciones básicas de visualización y gráficos

### NIVEL ESPECÍFICO (100 funciones)
- **Gestión y simulaciones:** 20 funciones de sistema de biblioteca completo
- **Juegos y simulaciones aleatorias:** 20 funciones de juegos y probabilidades
- **NumPy:** 20 funciones avanzadas de álgebra lineal y matemáticas
- **Pandas:** 20 funciones avanzadas de análisis de datos
- **Gráficos avanzados con Matplotlib:** 20 funciones de visualización compleja

---

## 🔍 ÍNDICE TEMÁTICO RÁPIDO

### OPERACIONES CON LISTAS
- Funciones: 1-10, 101, 104-112, 117, 119-120

### MANIPULACIÓN DE STRINGS  
- Funciones: 11-20, 107, 113

### DICCIONARIOS Y MAPEO
- Funciones: 21-30, 103, 105-106, 108-116, 118-120

### ALGORITMOS CLÁSICOS
- Funciones: 31-40, 61-70

### MANEJO DE ARCHIVOS
- Funciones: 41-50, 121-140, 212-213, 273-274

### MATEMÁTICAS Y CÁLCULO
- Funciones: 71-80, 141-160, 241-260

### ESTADÍSTICAS Y ANÁLISIS
- Funciones: 4, 85, 143, 161-180, 261-280

### SIMULACIONES Y JUEGOS
- Funciones: 54-60, 94-98, 201-220, 221-240

### VISUALIZACIÓN DE DATOS
- Funciones: 181-200, 229-230, 235, 240, 256, 277-299

### SISTEMAS COMPLETOS
- Funciones: 83-84, 89, 201-220 (Sistema de Biblioteca)

---

## 💡 CONSEJOS DE USO

**Para Búsqueda Rápida:**
1. Usar Ctrl+F y buscar por nombre de función
2. Buscar por número de función si se conoce
3. Buscar por palabra clave del tema (ej: "matriz", "archivo", "grafico")

**Organización por Complejidad:**
- **Principiantes:** Usar funciones 1-100 (Nivel General)
- **Intermedio:** Combinar funciones 1-200 (General + Medio)  
- **Avanzado:** Todas las funciones 1-300

**Librerías Requeridas:**
- **Nivel General:** Solo `random`
- **Nivel Medio:** `random`, `numpy`, `pandas`, `matplotlib`
- **Nivel Específico:** `random`, `numpy`, `pandas`, `matplotlib`

---

## 📌 NOTAS IMPORTANTES

- Todas las funciones están comentadas línea por línea
- Código optimizado para aprendizaje estudiantil
- Sin dependencias externas no autorizadas
- Compatible con Python 3.6+
- Funciones probadas y funcionales

**Total: 300 funciones Python organizadas y documentadas**