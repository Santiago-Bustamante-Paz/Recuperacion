Nombre: Santiago Bustamante

Descripción línea por línea
1-7 Crean la lista y la función para ordenarla
	1: Le define a "bubble_sort" como una función que recibe (y luego ordena) la lista
	2: n guarda la cantidad de números en la lista para luego poder preguntar por esa cantidad de números
	3: Controla cuántas veces se piden números
	4: Recorre la lista comparando pares de números, pero cada vez recorre uno menos ya que los anteriores ya quedaron ordenados
	5: Compara los números que están alado y si el de la izquiera es mayor que el de la derecha, va a la fila 6
	6: Intercambia los números (si es necesario en la fila 5)
	7: Guarda a la lista para que pueda ser usada
8-16 Preguntan al usuario cuántos números quiere
	8: Hace que el input se repita hasta que se ingrese un valor válido
	9: Hace que el programa no se rompa si no sirve (conectado con la línea 15)
	10: Pide la cantidad de números que van a estar en la lista
	11: Ve si la cantidad de números es positivo
	12: Da una simple indicación de volvera ingresar un número válido
	13: Regresa a la fila 8
	14: Si el dato no es válido, continúa con el programa
	15: Atrapa el error
	16: Da una simple instrucción de volvera ingresar un número válido y hace que se repita todo este proceso
17-25 Crea una lista y la deja que el usuario la llene
	17: Crea una lista vacía (numeros) donde se guardarán los números que ingrese el usuario
	18: Repite el proceso (pedir valores) la cantidad de veces que fue pedido en la línea 10
	19-25: Sirve igual que las filas 8-16, entonces no se necesita explicar otra vez
		Excepción:
		21: Acepta decimales
		22: Agrega el número que recién fue ingresado a la lista creada en la fila 17
26: Imprime la lista original (fila 17) sin ordenarla
27: Inserta la lista original (fila 17) en la función para ordenar (fila 1), entonces termina ordenada
28: Imprime la lista ordenada en una nueva fila

Descripción de Bubble Sort

	La función Bubble Sort está usada especialmente durante las primeras 7 filas, entonces ahí también está explicado

	Va viendo pares de números (en el código son llamados valores) y si el de la izquiera es mayor que el de la derecha, entonces les cambia de lugar

Complejidad computacional

	Complejidad Big O: n^2

	Cuando un loop este hace que Big O sea lineal (n) y cuando hay un loop dentro de otro, esto hace que sea (n*n o n^2)

	Esto pasa en las líneas 3-4 con los dos "for"

	Ecuación para complejidad: n(n-1)/2
	n = 10: 10(10-1)/2 = 45
	n = 100: 100(100-1)/2 = 4950