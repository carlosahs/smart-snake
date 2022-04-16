import turtle

from typing import Tuple

SNAKE_COLOR = (0, 0, 0)
SNAKE_SIZE = 0.5

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480


class Square(turtle.Turtle):
    def __init__(
        self, x: float, y: float, size: float, color: Tuple[int, int, int]
    ) -> None:
        self.x = x
        self.y = y

        turtle.Turtle.__init__(self, shape="square", visible=False)

        self.pu()
        self.shapesize(size)
        self.fillcolor(color)
        self.st()

        self.setx(x)
        self.sety(y)

    def left(self, distance: float) -> None:
        self.x -= distance
        self.setx(self.x)

    def right(self, distance: float) -> None:
        self.x += distance
        self.setx(self.x)

    def down(self, distance: float) -> None:
        self.y -= distance
        self.sety(self.y)

    def up(self, distance: float) -> None:
        self.y += distance
        self.sety(self.y)


def move_backward() -> None:
    disable_keys()
    turtle.backward(200)
    enable_keys()


def move_forward() -> None:
    disable_keys()

    turtle.forward(200)
    if abs(turtle.pos()) < 1:
        turtle.end_fill()
        turtle.left(170)
        return

    enable_keys()


def move_left() -> None:
    disable_keys()
    turtle.left(170)
    enable_keys()


def move_right() -> None:
    disable_keys()
    turtle.right(170)
    enable_keys()


def enable_keys() -> None:
    turtle.onkey(move_forward, 'k')
    turtle.onkey(move_backward, 'j')
    turtle.onkey(move_left, 'h')
    turtle.onkey(move_right, 'l')
    turtle.onkey(turtle.bye, 'q')


def disable_keys() -> None:
    turtle.onkey(None, 'k')
    turtle.onkey(None, 'j')
    turtle.onkey(None, 'h')
    turtle.onkey(None, 'l')
    turtle.onkey(None, 'q')


if __name__ == '__main__':
    main_screen = turtle.Screen()

    main_screen.mode("standard")
    main_screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

    sqr = Square(10, 50, SNAKE_SIZE, SNAKE_COLOR)

    # enable_keys()
    #
    # color('red', 'yellow')
    # begin_fill()
    #
    # listen()
    turtle.done()
