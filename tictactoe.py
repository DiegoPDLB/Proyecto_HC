"""Tres en Raya (Tic Tac Toe)

Ejercicios:

1. Dale a X y O un color y grosor diferentes.
2. ¿Qué sucede cuando alguien toca un espacio ocupada?
3. ¿Cómo detectarías cuando alguien ha ganado?
4. ¿Cómo podrías crear un jugador computarizado?
"""

from turtle import (
    up, down, goto, circle, width,
    setup, hideturtle, tracer, color,
    update, onscreenclick, done
)
from freegames import line

# Constantes para personalización del juego
CELL_SIZE = 133  # Tamaño de cada celda en píxeles
X_COLOR = 'blue'  # Color para el jugador X
O_COLOR = 'red'   # Color para el jugador O
X_WIDTH = 5       # Grosor de línea para X
O_WIDTH = 3       # Grosor de línea para O


def grid():
    """Dibuja la cuadrícula del juego."""
    line(-67, 200, -67, -200)  # Línea vertical izquierda
    line(67, 200, 67, -200)    # Línea vertical derecha
    line(-200, -67, 200, -67)  # Línea horizontal inferior
    line(-200, 67, 200, 67)    # Línea horizontal superior


def drawx(x, y):
    """Dibuja el jugador X."""
    color(X_COLOR)
    width(X_WIDTH)
    x_center = x + CELL_SIZE/2
    y_center = y + CELL_SIZE/2
    offset = 50
    up()
    goto(x_center - offset, y_center - offset)
    down()
    goto(x_center + offset, y_center + offset)
    up()
    goto(x_center - offset, y_center + offset)
    down()
    goto(x_center + offset, y_center - offset)


def drawo(x, y):
    """Dibuja el jugador O."""
    color(O_COLOR)
    width(O_WIDTH)
    x_center = x + CELL_SIZE/2
    y_center = y + CELL_SIZE/2
    radius = 50
    up()
    goto(x_center, y_center - radius)
    down()
    circle(radius)


def floor(value):
    """Redondea el valor a la cuadrícula con tamaño 133."""
    return ((value + 200) // 133) * 133 - 200


# Estado del juego
state = {
    'player': 0,
    'used_cells': set(),
    'moves': {'X': [], 'O': []}
}
players = [drawx, drawo]


def check_winner(moves):
    """Verifica si hay un ganador con los movimientos dados."""
    # Ajustar coordenadas para que coincidan con los movimientos reales
    winning_combinations = [
        # Horizontales
        [(-200, -200), (-67, -200), (66, -200)],  # Fila inferior
        [(-200, -67), (-67, -67), (66, -67)],     # Fila media
        [(-200, 66), (-67, 66), (66, 66)],        # Fila superior
        # Verticales
        [(-200, -200), (-200, -67), (-200, 66)],  # Columna izquierda
        [(-67, -200), (-67, -67), (-67, 66)],     # Columna media
        [(66, -200), (66, -67), (66, 66)],        # Columna derecha
        # Diagonales
        [(-200, -200), (-67, -67), (66, 66)],     # Diagonal \
        [(66, -200), (-67, -67), (-200, 66)]      # Diagonal /
    ]
    
    # Debug: imprimir los movimientos actuales con formato float
    print(f"Movimientos actuales: {moves}")
    
    # Convertir coordenadas a tuplas de float para comparación
    float_moves = [(float(x), float(y)) for x, y in moves]
    
    for line in winning_combinations:
        if all((float(x), float(y)) in float_moves for x, y in line):
            print(f"¡Línea ganadora encontrada: {line}")
            return True
    return False


def tap(x, y):
    """Dibuja X u O en el cuadro tocado si está disponible."""
    x = floor(x)
    y = floor(y)
    cell = (x, y)
    
    if cell in state['used_cells']:
        print(f'Casilla {cell} ya está ocupada')
        return
    
    player = state['player']
    draw = players[player]
    draw(x, y)
    
    player_symbol = 'X' if player == 0 else 'O'
    state['moves'][player_symbol].append(cell)
    state['used_cells'].add(cell)
    
    if check_winner(state['moves'][player_symbol]):
        print(f'¡Jugador {player_symbol} ha ganado!')
        update()
        return
    
    if len(state['used_cells']) == 9:
        print('¡Empate!')
        update()
        return
    
    update()
    state['player'] = not player


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
