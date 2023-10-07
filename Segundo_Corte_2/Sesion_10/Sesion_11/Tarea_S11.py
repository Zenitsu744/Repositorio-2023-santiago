class PersonaIMC:

    def __init__(self):
        self._nombre = None
        self._estatura = None
        self._peso = None

def calcular_IMC(peso, estatura):
    imc = peso / ((estatura / 100) ** 2)
    estados = [
        (18.5, 'Por debajo'),
        (24.9, 'Saludable'),
        (29.9, 'Sobrepeso'),
        (34.9, 'Obesidad I'),
        (39.9, 'Obesidad II'),
        (float('inf'), 'Obesidad III')
    ]
    estado = next(s for limite, s in estados if imc <= limite)
    return round(imc, 2), estado

def crear_lista_defecto():
    nombres = ['Pedro Caceres', 'Maria Pérez', 'Julian Dominguez', 'Jessica Fuentes']
    estaturas = [188, 160, 158, 170]
    pesos = [97, 47, 58, 73]
    lista = []
    for i in range(len(nombres)):
        persona = Persona()
        persona.nombre = nombres[i]
        persona.estatura = estaturas[i]
        persona.peso = pesos[i]
        lista.append(persona)
    return lista

def crear_lista_usuario():
    lista = []
    while True:
        continuar = input('¿Desea agregar más personas a la lista? (Y/N): ')
        if continuar.upper() == 'N':
            break
        elif continuar.upper() == 'Y':
            persona = Persona()
            persona.nombre = input('\nIngrese el nombre de la persona: ')
            persona.estatura = float(input('Ingrese la respectiva altura de la persona en cm: '))
            persona.peso = int(input('Ingrese el peso de la persona en kg: '))
            lista.append(persona)
        else:
            print('Valor inválido')
    return lista

def main():
    while True:
        print('\nBienvenido/a, para iniciar seleccione uno de los siguientes procesos.',\
            '\n1) Conocer el valor de IMC de una lista creada por defecto.',\
            '\n2) Crear su propia lista de personas para calcular su IMC.',\
            '\n3) Salir del programa.')

        opcion = input('\nPor favor ingrese una opción: ')
        if opcion == '1':
            lista = crear_lista_defecto()
        elif opcion == '2':
            lista = crear_lista_usuario()
        elif opcion == '3':
            break
        else:
            print('No ha seleccionado una opción válida')

        for persona in lista:
            imc, estado = calcular_IMC(persona.peso, persona.estatura)
            print(f'\nEl IMC de {persona.nombre} es de: {imc}.',\
                f'\nSu estado de salud es {estado}.\n')

if __name__ == '__main__':
    main()
