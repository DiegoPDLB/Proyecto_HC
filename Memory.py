# Memory, puzzle game of number pairs.

# Create square options for different game sizes
size = 0

# Prompt user for difficulty level
while True:
    try:
        choice = int(input("Input an even number for size of board: "))
        if choice % 2 == 0:
            size = choice
            break
        print("Please enter a positive even number")
    except ValueError:
        print("Please enter a valid number")

import turtle
import random
from freegames import path

car = path('car.gif')
# board array setup now dynamically sized based on user input
listSize = int(size * size / 2)
tiles = list(range(listSize)) * 2
state = {'mark': None}
hide = [True] * (size * size)

# Create var to count number of discovered pairs
discovered = 0


def square(x, y):
    """Draw white square with black outline at (x, y)."""
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.color('black', 'white')
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(50)
        turtle.left(90)
    turtle.end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    # calculate starting position based on size
    start_x = -(size * 50) // 2
    start_y = -(size * 50) // 2
    # calculate column and row based on x, y coordinates
    col = int((x - start_x) // 50)
    row = int((y - start_y) // 50)
    # dimensions check for valid coordinate positions on grid
    if 0 <= col < size and 0 <= row < size:
        return row * size + col
    return None  # out-of-bounds click


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    # calculate starting position based on size
    start_x = -(size * 50) // 2
    start_y = -(size * 50) // 2
    # return x, y coordinates based on count
    return start_x + (count % size) * 50, start_y + (count // size) * 50


def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    spot = index(x, y)
    mark = state['mark']

    # tell game that 'discovered' variable is global
    # to prevent UnboundLocalError
    global discovered

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        # increase discovered pairs by 1 when tiles are a match
        discovered += 1


def draw():
    """Draw image and tiles."""
    turtle.clear()
    turtle.goto(0, 0)
    turtle.shape(car)
    turtle.stamp()

    for count in range(size * size):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        turtle.up()
        turtle.goto(x + 2, y)
        turtle.color('black')
        turtle.write(tiles[mark], font=('Arial', 30, 'normal'))

    # return Turtle to top to draw game stats
    turtle.up()
    # instead of hardcoded grid position for game stats
    turtle.goto(-(size * 25), (size * 25) + 10)
    # write current number of discovered pairs
    turtle.write(
        f'Discovered Pairs: {discovered}',
        font=('Arial', 16, 'normal')
    )
    # check whether all tiles are no longer hidden
    if all(not h for h in hide):
        turtle.goto(-70, 0)
        turtle.color('green')
        # write message to let user know they have won
        turtle.write("You Win!", font=('Arial', 20, 'bold'))
    turtle.update()
    turtle.ontimer(draw, 100)


# Calculate window dimensions
tile_size = 50  # Each tile is 50x50 pixels
margin = 20  # Margin around the grid
stats_height = 40  # Extra height for stats display

# Calculate window size based on grid size and tile size
window_width = (size * tile_size) + (2 * margin)
window_height = (size * tile_size) + (2 * margin) + stats_height

random.shuffle(tiles)
# pass dynamic sizes to setup window instead of hardcoded values
turtle.setup(window_width, window_height, 370, 0)
turtle.addshape(car)
turtle.hideturtle()
turtle.tracer(False)
turtle.onscreenclick(tap)
draw()
turtle.done()
