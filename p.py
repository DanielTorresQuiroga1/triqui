p
# Crear una matriz de 3x3 para representar el tablero del juego
tablero = [['-', '-', '-'],
           ['-', '-', '-'],
           ['-', '-', '-']]

# Función para imprimir el tablero en la consola
def imprimir_tablero():
    for fila in tablero:
        print('|'.join(fila))

# Función para verificar si un jugador ha ganado el juego
def verificar_ganador(jugador):
    # Verificar filas
    for fila in tablero:
        if fila == [jugador, jugador, jugador]:
            return True
    # Verificar columnas
    for i in range(3):
        if tablero[0][i] == jugador and tablero[1][i] == jugador and tablero[2][i] == jugador:
            return True
    # Verificar diagonales
    if tablero[0][0] == jugador and tablero[1][1] == jugador and tablero[2][2] == jugador:
        return True
    if tablero[0][2] == jugador and tablero[1][1] == jugador and tablero[2][0] == jugador:
        return True
    return False

# Función para permitir que un jugador haga un movimiento en el tablero
def hacer_movimiento(fila, columna, jugador):
    if tablero[fila][columna] == '-':
        tablero[fila][columna] = jugador
        return True
    else:
        return False

# Función para cambiar entre los jugadores después de cada movimiento
def cambiar_jugador(jugador):
    if jugador == 'X':
        return 'O'
    else:
        return 'X'

# Bucle principal del juego
jugador_actual = 'X'
while True:
    # Imprimir el tablero
    imprimir_tablero()
    # Solicitar al jugador que haga un movimiento
    fila = int(input(f'Jugador {jugador_actual}, elige una fila (0-2): '))
    columna = int(input(f'Jugador {jugador_actual}, elige una columna (0-2): '))
    # Hacer el movimiento
    if hacer_movimiento(fila, columna, jugador_actual):
        # Verificar si el jugador ha ganado
        if verificar_ganador(jugador_actual):
            print(f'¡Jugador {jugador_actual} ha ganado!')
            break
        # Verificar si hay un empate
        if all('-' not in fila for fila in tablero):
            print('¡Empate!')
            break
        # Cambiar al siguiente jugador
        jugador_actual = cambiar_jugador(jugador_actual)
    else:
        print('¡Esa casilla ya está ocupada! Inténtalo de nuevo.')