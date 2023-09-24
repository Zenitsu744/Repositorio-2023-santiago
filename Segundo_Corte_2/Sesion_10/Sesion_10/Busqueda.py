Estudiantes={'Juan Diego':{'Edad':19,'Documento':12763729,'Genero':'M'},\
    'Natalia':{'Edad':20,'Documento':12767364,'Genero':'F'},\
        'Jairo':{'Edad':18,'Documento':1254532,'Genero':'M'}}
nombres = {4:'Juan Diego',3:'Natalia',5:'Jairo'}

busqueda = int(input('Ingrese un codigo estudiantil: '))
persona = nombres[busqueda]
print(f'La edad de {nombres[busqueda]} es {Estudiantes[persona]["Edad"]}')
estudiante=int(input('Ingrese el codigo: '))
a=input('Ingrese su nombre: ')
nombres[estudiante]=a
print(nombres[estudiante])
Estudiantes[a]={'Edad':18}
print('-----')