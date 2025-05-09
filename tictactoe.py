"""Tic Tac Toe

Ejercicios:

1. Dale a X y O un color y grosor diferentes.
2. ¿Qué sucede cuando alguien toca un espacio ocupado?
3. ¿Cómo detectarías cuando alguien ha ganado?
4. ¿Cómo podrías crear un jugador computarizado?
"""

# Se importan funciones específicas de turtle para evitar F403 y F405
from turtle import (
    up, down, goto, circle,
    setup, hideturtle, tracer,
    update, onscreenclick, done
)
from freegames import line


def grid():
    """Dibuja la cuadrícula del juego."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):
    """Dibuja el jugador X."""
    line(x, y, x + 133, y + 133)
    line(x, y + 133, x + 133, y)


def drawo(x, y):
    """Dibuja el jugador O."""
    up()
    goto(x + 67, y + 5)
    down()
    circle(62)


def floor(value):
    """Redondea el valor a la cuadrícula con tamaño 133."""
    return ((value + 200) // 133) * 133 - 200


state = {'player': 0}
players = [drawx, drawo]


def tap(x, y):
    """Dibuja X u O en el cuadro tocado."""
    x = floor(x)
    y = floor(y)
    player = state['player']
    draw = players[player]
    draw(x, y)
    update()
    state['player'] = not player


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
