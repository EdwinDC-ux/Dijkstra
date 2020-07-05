# Algoritmo Dijkstra.

## Descripción:

Este algoritmo permite encontar el camino más corto de un nodo a otro en un grafo sin nodos aislados.

## Funcionamiento:

El algoritmo recibe un parámetro el cual es un diccionario cuya clave es el nombre del nodo y el valor es un array que contiene los datos necesarios de cada nodo (nodo_inicial, vecinos, pesos_aristas).
1. El nodo_inicial es un valor booleano que indica si el algoritmo partirá desde dicho nodo.
2. Los vecinos es una lista de los nombres de nodos con los que comparte arista.
3. El pesos_aristas es el costo que tiene hacer el recorrido del nodo actual al vecino, esto siguiendo el mismo orden en el que se introdujeron los vecinos.

## Pruebas:

Al final del código vienen definidas una serie de pruebas a partir de la función "TDD" en la linea 86 (algunas las pasa y otras no).
