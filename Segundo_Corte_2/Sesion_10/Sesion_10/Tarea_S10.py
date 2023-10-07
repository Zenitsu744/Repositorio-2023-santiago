def mostrar_menu():
    print("\n1) Mostrar la lista de productos disponibles.",\
        "\n2) Calcular el valor base de un producto.\n3) Salir.")

def mostrar_productos():
    f = open("Alimentos.txt", "rt")
    lista_productos = f.readlines()
    f.close()
    productos = []
    for item in lista_productos[1:]:
        productos.append(item.split(','))
        productos.sort(key=lambda x: x[2])
    print('\n-------------------------\n')
    for i, producto in enumerate(productos):
        print(f'{i+1}. {producto[0]}')
    print('\n-------------------------\n')

def importar_datos():
    f = open("Alimentos.txt", "rt")
    lista_productos = f.read()
    f.close()
    datos = {}
    for item in lista_productos.split('\n')[1:]:
        elementos = item.split(',')
        datos[elementos[0]] = [elementos[1], float(elementos[2])]
    return datos

def calcular_valor_base(datos, nombre_producto):
    for valor in datos.values():
        if valor[0] == nombre_producto:
            valor_neto = float(input('Ingrese el valor neto del producto: '))
            valor_base = valor_neto / (1 + valor[1])
            return round(valor_base, 2), valor[1] * 100
    print("\nUsted ha ingresado un valor incorrecto, Por favor respete tanto las mayusculas y minusculas a la hora de ingresar el valor.")
    return False

def main():
    datos = importar_datos()
    while True:
        mostrar_menu()
        opcion = input("\nEscriba la opcion que desea investigar: ")
        if opcion == '1':
            mostrar_productos()
        elif opcion == '2':    
            producto = input('Por favor ingrese el nombre del producto tal y como aparece en la lista: ')
            valor_base = calcular_valor_base(datos, producto)
            if valor_base != False:
                print(f"\nEl valor base es: ${valor_base[0]}\nEl IVA es: {valor_base[1]}%")
        elif opcion == '3' or opcion.lower() == 'salir':
            break
        else:
            print("Error, eata selección es inválida, verifque de nuevo por fvor.")

if __name__ == "__main__":
    main()
