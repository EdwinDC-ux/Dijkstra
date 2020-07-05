class nodo:
	pe = -1 #Peso del nodo.
	ant = "" #vecino anterior del nodo se toma por default como un caracter.
	def __init__(self, inicial, vecinos, aristas): #Al llamar a la clase nodo se deberan pasar como parámetros los siguiengtes valores.
		self.ini = inicial
		self.vec = vecinos
		self.ari = aristas


"""Función que obtiene una lista de todos los caminos del grafo
ya rresuelto por la función dijkstra, esta función iterará hasta encontrar todos los caminos encontrados por dijkstra."""
def getLista(dic):
	listaFinal = [] #Lista donde se guardarán los caminos obtenidos.
	nodos = list(dic.keys())
	tamOrig = len(nodos) - 1
	recor = []
	while len(recor) < tamOrig: #Esta parte se repetirá mientras no hayamos recorrido todos los nodos que no sean el inicial.
		lista1 = []
		if len(nodos) > 1: #Este if nos sirve como filtro ya que se usan elementos de una lista y podria causar un error si está vacia.
			mayor = dic[nodos[0]].pe #obtenemos un pivote para sacar el elemento de mayor peso (el ultimo elemento de cada camino).
			actual = nodos[0]
			for el in nodos: #A partir de ese pivote recorremos el arreglo de los nodos no visitados para obtener el de mayor peso global.
				if dic[el].pe > mayor:
					mayor = dic[el].pe
					actual = el
			if actual not in recor: #Una vez obtenido el mayor nos fijamos que no sea un nodo intermedio en lugar de un nodo final.
				while not dic[actual].ini: #Esta parte se repetirá mientras no lleguemos al nodo inicial del grafo.
					lista1.append(actual) #La etiqueta del nodo actual se guardará en una lista de camino.
					if actual not in recor: #Si es la primera vez que recorremos este nodo lo agregamos a la lista, si no no lo agregamos.
						recor.append(actual)
					if actual in nodos: #Hacemos lo mismo que en el if anterior, solamente que en este caso es para reducir los nodos de los que se verificará el peso.
						nodos.remove(actual)
					try: #Revisa si la etiqueta del nodo anterior es un numero para convertirlo en enteros.
						actual = int(dic[actual].ant)
					except: #Si no puede convertirlo en enteros la toma como el caracter que es.
						actual = dic[actual].ant
				lista1.append(actual) #Se agrega el nodo inicial a la lista de camino.
				lista1.reverse() #La invertimos para que quede ordenada de inicial a final
				listaFinal.append(lista1) #Agregamos la lista de camino a la lista final.
	return listaFinal

"""Esta funci´n encuentra todos los caminos más cortos de un grafo
utilizando el algoritmo de dijkstra."""
def dijkstra(dic):
	i = 0
	no_visit = list(dic.keys()) #hacemos una lista de los nodos que no se han visitado en la resolución.
	for asig in no_visit: #asignamos los pesos tentativos, para el nodo inicial 0, para los demás infinito.
		if dic[asig].ini:
			dic[asig].pe = 0
			actual = asig
		else:
			dic[asig].pe = 2147483647
	while len(no_visit) > 0: #Esta parte se repetirá mientras haya nodos sin visitar en el grafo.
		print('actual')
		print(actual)
		print('no visitados')
		print(no_visit)
		for va in dic[actual].vec: #para cada vecino del nodo actual calculamos el peso real con la suma del peso actual más el peso de recorrer el camino a ese vecino.
			print('Vecino actual:')
			print(va)
			new_pe=dic[actual].pe + dic[actual].ari[i]
			if dic[va].pe > new_pe: #Si el peso calculado es menor que el peso que poseia ese nodo vecino le asigamos el peso calculado.
				dic[va].pe = new_pe
				dic[va].ant = str(actual)
				print('peso nuevo:')
				print(dic[va].pe)
				print('nodo anterior:')
				print(dic[va].ant)
			else:
				print('¡Peso no actualizado!')
				print('¡Nodo anterior no actualizado!')
			i = i + 1
		i = 0
		no_visit.remove(actual) #Marcamos el nodo actual como visitado.
		print('no visitados (despues de eliminacion de actual)')
		print(no_visit)
		if len(no_visit) > 0: #Ponemos una verificación de seguridad para asignar el siguiente nodo no visitado
			menor = dic[no_visit[0]].pe #Obtenemos un pivote del nodo de menor peso que será el siguiente en ser visitado.
			actual = no_visit[0]
			for ree in no_visit: #A partir del pivote obtenemos al nodo de menor peso global que será el siguiente en ser visitado.
				if dic[ree].pe < menor:
					menor = dic[ree].pe
					actual = ree
	return getLista(dic)

def tdd(f, grafo):
	return f(grafo)

print('++++++++++tdd++++++++++')

n1 = nodo(True, ['b','c'],[1,3])
n2 = nodo(False, ['a','c','d'], [1,5,2])
n3 = nodo(False, ['a','b','d'], [3,5,2])
n4 = nodo(False, ['b','c'], [2,2])

print(tdd(dijkstra, {'a':n1, 'b':n2, 'c':n3, 'd':n4}))

print('++++++++++tdd2++++++++++')

a1 = nodo(True, [6,3,2], [14,9,7])
a2 = nodo(False, [1,3,5], [14,2,9])
a3 = nodo(False, [1,6,4,2], [9,2,11,10])
a4 = nodo(False, [1,3,4], [7,10,15])
a5 = nodo(False, [2,3,5], [15,11,6])
a6 = nodo(False, [6,4], [9,6])

print(tdd(dijkstra, {1:a1, 6:a2, 3:a3, 2:a4, 4:a5, 5:a6}))


print('++++++++++tdd3+++++++++')

n0 = nodo(False, [3,4], [4,7])
n1 = nodo(False, [6,5,2], [7,2,4])
n2 = nodo(False, [1,5,4], [4,3,1])
n3 = nodo(False, [0,5], [4,6])
n4 = nodo(False, [0,2], [7,1])
n5 = nodo(True, [6,7,1,2,3], [4,8,2,3,6])
n6 = nodo(False, [1,5], [7,4])
n7 = nodo(False, [5], [8])

print(tdd(dijkstra, {0:n0, 1:n1, 2:n2, 3:n3, 4:n4, 5:n5, 6:n6, 7:n7}))

print('++++++++++tdd4++++++++++')

a1 = nodo(True, [6,3,2], [14,9,7])
a2 = nodo(False, [1,4,3], [7,15,10])
a3 = nodo(False, [1,6,4], [9,2,11])
a4 = nodo(False, [5,2,3], [6,15,11])
a5 = nodo(False, [6,4], [9,6])
a6 = nodo(False, [1,3,5], [14,2,9])

print(tdd(dijkstra, {1:a1, 2:a2, 3:a3, 4:a4, 5:a5, 6:a6}))

print('++++++++++tdd5++++++++++')

n0 = nodo(True, [1,2,3], [2,2,2])
n1 = nodo(False, [4], [2])
n2 = nodo(False, [5,3], [3,2])
n3 = nodo(False, [4], [2])
n4 = nodo(False, [5], [3])
n5 = nodo(False, [], [])

print(tdd(dijkstra, {0:n0, 1:n1, 2:n2, 3:n3, 4:n4, 5:n5}))