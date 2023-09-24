def imprimir_la_matriz(matriz):
    for fila in matriz:
        print(fila)

def encontrar_min_max(matriz):
    minimo  = matriz [0][0]
    maximo  = matriz [0][0]
    pos_min =        (0, 0)
    pos_max =        (0, 0)

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] < minimo:
                minimo = matriz[i][j]
                pos_min = (i, j)
            if matriz[i][j] > maximo:
                maximo = matriz[i][j]
                pos_max = (i, j)

    return minimo, maximo, pos_min, pos_max

def ordenar_matriz_descendente(matriz):
    matriz_flatten = [num for fila in matriz for num in fila]
    matriz_flatten.sort(reverse=True)           #usamos el .sort para darle un orden determinado a la matriz 
    
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matriz[i][j] = matriz_flatten.pop(0)    #implementamos el .pop para quitar el retorno del ultimo elemento de la matriz 


import random

matriz = [[random.randint(1, 100) for in range(10)] for in range(5)]

print("Matriz original:")
imprimir_la_matriz(matriz)

minimo, maximo, pos_min, pos_max = encontrar_min_max(matriz)
print("\nNúmero más bajo:", minimo, "en la posición:", pos_min)
print("Número más alto:", maximo, "en la posición:", pos_max)

ordenar_matriz_descendente(matriz)
print("\n Matriz ordenada de mayor a menor:")
imprimir_la_matriz(matriz)

