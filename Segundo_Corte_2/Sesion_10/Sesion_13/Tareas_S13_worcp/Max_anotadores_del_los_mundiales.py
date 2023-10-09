def maximos_goleadores(lista):
    goleadores = {}

    for partido in lista:
        goleador_local = partido[6]
        goleador_visitante = partido[7]

        
        if goleador_local not in goleadores:
            goleadores[goleador_local] = 0
        goleadores[goleador_local] += partido[8]

        
        if goleador_visitante not in goleadores:
            goleadores[goleador_visitante] = 0
        goleadores[goleador_visitante] + = partido[9]

    # Ordenamos los goles de mayor a menores por los mundiales dispuestos 
    goleadores_ordenados = sorted(goleadores.items(), key=lambda x: x[1], reverse=True)

    print('\n---------------Lista de mejores y mayores goleadores en los mundiales----------------\n')
    for jugador, goles in goleadores_ordenados:
        print(f'{jugador}: {goles} goles')
