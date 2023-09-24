def encontrar_mayor_recursivo(lista):
    if len(lista) == 0:
        return None
    
    if len(lista) == 1:
        return lista[0]
    
    max_resto = encontrar_mayor_recursivo(lista[1:])
    
    if lista[0] > max_resto:
        return lista[0]
    else:
        return max_resto


 if mi_lista = [10, 4, 8, 15, 3, 20, 5]:
mayor = encontrar_mayor_recursivo(mi_lista)
print("El mayor elemento en la lista es:", mayor)
