import numpy as np

jugador = '🔴'
computadora = '🟡'
vacio = '⚪'


filas = 6
columnas = 7

def crear_tablero():
    return np.full((6, 7), vacio, dtype=str)

def imprimir_tablero(tablero):
    print(' 1  2  3  4  5  6  7')
    for fila in tablero:
        print(' '.join(fila))
    

def es_movimiento_valido(tablero, columna):
    return tablero[filas - 1][columna] == vacio

def realizar_movimiento(tablero, columna, ficha):
    for fila in range(filas):
        if tablero[fila][columna] == vacio:
            tablero[fila][columna] = ficha
            return True
    return False

def hay_ganador(tablero, ficha):
    for fila in range(filas):
        for columna in range(columnas - 3):
            if all(tablero[fila][columna + i] == ficha for i in range(4)):
                return True

    
    for columna in range(columnas):
        for fila in range(filas - 3):
            if all(tablero[fila + i][columna] == ficha for i in range(4)):
                return True

    #Se revisa las diagonales izq y der
    for fila in range(filas - 3):
        for columna in range(columnas - 3):
            if all(tablero[fila + i][columna + i] == ficha for i in range(4)):
                return True

    for fila in range(filas - 3):
        for columna in range(3, columnas):
            if all(tablero[fila + i][columna - i] == ficha for i in range(4)):
                return True

    return False

#Lógica para que la computadora intente ganar siempre

def obtener_columna_maquina(tablero):

    for columna in range(columnas):
        if es_movimiento_valido(tablero, columna):
            copia_tablero = tablero.copy()
            realizar_movimiento(copia_tablero, columna, computadora)
            if hay_ganador(copia_tablero, computadora):
                return columna

    for columna in range(columnas):
        if es_movimiento_valido(tablero, columna):
            copia_tablero = tablero.copy()
            realizar_movimiento(copia_tablero, columna, jugador)
            if hay_ganador(copia_tablero, jugador):
                return columna

    movimiento_v = [col for col in range(columnas) if es_movimiento_valido(tablero, col)]
    return np.random.choice(movimiento_v)




tablero = crear_tablero()
turno = jugador

while True:
    imprimir_tablero(tablero)

    if turno == jugador:
        while True:
            try:
                columna = int(input("Ingrese el número de columna (1-7): ")) - 1
                print("\n")
                if 0 <= columna < columnas and es_movimiento_valido(tablero, columna):
                    break
                else:
                    print("Movimiento inválido")
            except ValueError:
                print("Ingrese un número dentro del rango (1-7)")

        realizar_movimiento(tablero, columna, jugador)

        if hay_ganador(tablero, jugador):
            imprimir_tablero(tablero)
            print("¡Felicidades! Ganó")
            break
    else:
        print("Es el turno de la computadora\n")
        columna_maquina = obtener_columna_maquina(tablero)
        realizar_movimiento(tablero, columna_maquina, computadora)

        if hay_ganador(tablero, computadora):
            imprimir_tablero(tablero)
            print("La computadora ha ganado")
            break

    turno = jugador if turno == computadora else computadora

