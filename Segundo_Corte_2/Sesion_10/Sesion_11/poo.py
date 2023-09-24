class Estudiante:
    def __init__(self):
        self.nombre=None
        self.apellido=None
        self.edad=None
        self.nacionalidad='Colombia'
    
    def entender(self):
        return 'Si, aprendí mucho hoy :)'


def main():
    est1=Estudiante()
    est1.nombre='Juan'
    est1.apellido='Picon'
    est1.edad=17

    est2=Estudiante()
    est2.nombre='Roger'
    est2.apellido='Piñeros'
    est2.edad='17'
    est2.nacionalidad='China'

    print(f'El estudiante:{est2.nombre} {est2.apellido}', \
         f'tiene una edad de:{est2.edad}',\
            f'y su nacionalidad es:{est2.nacionalidad}')
    input('Entendió?')
    print(est2.entender())


if __name__=="__main__":
    main()