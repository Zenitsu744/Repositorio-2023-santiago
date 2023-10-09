def calcular_promedio_goles(promedio_de_goles_por_mundial):
    total_goles = sum(promedio_de_goles_por_mundial.values())
    total_mundiales = len(promedio_de_goles_por_mundial)
    return total_goles / total_mundiales if total_mundiales > 0 else 0

    #ejemplo de asignacion de partidos, resultadosy fechas 

def main():
    partidos = [
        {"Equipo1": "Brasil", "Equipo2": "Alemania", "Resultado": 2, "Mundial": "1998"},
        {"Equipo1": "Italia", "Equipo2": "Francia", "Resultado": 3, "Mundial": "2006"},
        {"Equipo1": "Argentina", "Equipo2": "Holanda", "Resultado": 1, "Mundial": "2014"},
    ]

    goles_por_mundial = {}

    for partido in partidos:
        goles = partido["Resultado"]
        mundial = partido["Mundial"]

        if mundial not in promedio_de_goles_por_mundial:
            promedio_de_goles_por_mundial[mundial] = 0
        promedio_de_goles_por_mundial[mundial] += goles

    while True:
        print("Menú:")
        print("1. Calcular promedio de goles de todos los Mundiales")
        print("2. Consultar el número de goles de un Mundial específico")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            promedio = calcular_promedio_goles(promedio_de_goles_por_mundial)
            print(f"El promedio de goles de todos los Mundiales es: {promedio:.2f}")
        elif opcion == "2":
            mundial = input("Ingrese el nombre especifico del Mundial el cual desea investigar: ")
            if mundial in promedio_de_goles_por_mundial:
                goles = promedio_de_goles_por_mundial[mundial]
                print(f"El número de goles del Mundial {mundial} es: {goles}")
            else:
                print(f"No se encontraron datos para el Mundial {mundial}.")
        elif opcion == "3":
            print("¡Adiós!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
