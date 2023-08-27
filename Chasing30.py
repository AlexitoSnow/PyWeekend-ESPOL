import random
import time

tablero = []
posicion = 0
casilla = 1
contador = 0

def imprimir_tablero(tablero, casilla_actual=0):
    for i in range(0, len(tablero), 6):
        vacios = '*      ' * 6 + '*'  # 6 espacios
        lineas = '*' * len(vacios)
        numeros = ''
        for j in range(6):
            if i + j < len(tablero):
                numero = tablero[i + j]
                if casilla_actual == 30 and numero == 30:
                    numeros += f'*  \033[36m{numero:02d}\033[0m  '  # Colorear en celeste el ganador
                elif numero == casilla_actual:
                    numeros += f'*  \033[31m{numero:02d}\033[0m  '  # Colorear en rojo la ubicacion actual
                elif numero == 30:
                    numeros += f'*  \033[32m{numero:02d}\033[0m  '  # Colorear en verde el objetivo
                else:
                    numeros += f'*  {numero:02d}  '
            else:
                numeros += '*       ' # Espacios en blanco si no hay más elementos
        numeros += '*'
        print(lineas)
        print(vacios)
        print(numeros)
        print(vacios)
    print(lineas)

def llenar_tablero():
    return list(range(1, 31))

tablero = llenar_tablero()

while casilla != 30:
    imprimir_tablero(tablero, casilla)
    if casilla != 30:
        posicion = 0 if posicion == 29 else (posicion + 1)
        casilla = tablero[posicion]
        if contador == 5:
            random.shuffle(tablero)
            contador = 0
            print("Tablero reordenado!")
            casilla = tablero[posicion]
        contador += 1
        time.sleep(1)
print("Jugador ha ganado!")
imprimir_tablero(tablero, casilla)
