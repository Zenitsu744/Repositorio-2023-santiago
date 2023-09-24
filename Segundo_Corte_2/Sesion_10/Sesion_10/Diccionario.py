festivo={
    'Enero':['1 - año nuevo','6- reyes magos'],
    'Febrero':['No tiene festivos'],
    'Marzo':['20 - Dia de San Jose']}

def main():
    mes=input('Ingrese un mes: ')
    print(festivo[mes])


if __name__=="__main__":
    main()