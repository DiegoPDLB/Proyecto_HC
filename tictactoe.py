"""Tres en Raya (Tic Tac Toe)

Ejercicios:

1. Dale a X y O un color y grosor diferentes.
2. ¿Qué sucede cuando alguien toca un espacio ocupado?
3. ¿Cómo detectarías cuando alguien ha ganado?
4. ¿Cómo podrías crear un jugador computarizado?
"""

# Importaciones específicas de turtle y freegames
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
    # Dibuja las líneas verticales
    line(-67, 200, -67, -200)  # Línea vertical izquierda
    line(67, 200, 67, -200)    # Línea vertical derecha
    # Dibuja las líneas horizontales
    line(-200, -67, 200, -67)  # Línea horizontal inferior
    line(-200, 67, 200, 67)    # Línea horizontal superior


def drawx(x, y):
    """Dibuja el jugador X."""
    # Aplica estilo personalizado para X
    color(X_COLOR)
    width(X_WIDTH)
    # Calcula el centro de la celda
    x_center = x + CELL_SIZE/2
    y_center = y + CELL_SIZE/2
    offset = 50  # Distancia desde el centro para dibujar X

    # Dibuja la primera línea diagonal
    up()
    goto(x_center - offset, y_center - offset)
    down()
    goto(x_center + offset, y_center + offset)
    
    # Dibuja la segunda línea diagonal
    up()
    goto(x_center - offset, y_center + offset)
    down()
    goto(x_center + offset, y_center - offset)


def drawo(x, y):
    """Dibuja el jugador O."""
    # Aplica estilo personalizado para O
    color(O_COLOR)
    width(O_WIDTH)
    # Calcula el centro de la celda
    x_center = x + CELL_SIZE/2
    y_center = y + CELL_SIZE/2
    radius = 50  # Radio del círculo

    # Dibuja el círculo
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
    'used_cells': set()  # Conjunto para almacenar casillas ocupadas
}
players = [drawx, drawo]


def tap(x, y):
    """Dibuja X u O en el cuadro tocado si está disponible."""
    x = floor(x)
    y = floor(y)
    
    # Crear una tupla con las coordenadas de la celda
    cell = (x, y)
    
    # Verificar si la celda ya está ocupada
    if cell in state['used_cells']:
        print(f'Casilla {cell} ya está ocupada')
        return
    
    # Si la celda está libre, proceder con el movimiento
    player = state['player']
    draw = players[player]
    draw(x, y)
    
    # Registrar la celda como ocupada
    state['used_cells'].add(cell)
    
    update()
    state['player'] = not player


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
