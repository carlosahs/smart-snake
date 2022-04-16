import turtle

from turtle import backward
from turtle import begin_fill
from turtle import bye
from turtle import color
from turtle import done
from turtle import end_fill
from turtle import forward
from turtle import listen
from turtle import left
from turtle import onkey
from turtle import pos
from turtle import right

SNAKE_COLOR = (0, 0, 0)
SNAKE_SIZE = 0.5

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480


class Square(turtle.Turtle):
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

        turtle.Turtle.__init__(self, shape="square", visible=False)

        self.pu()
        self.shapesize(SNAKE_SIZE)
        self.fillcolor(SNAKE_COLOR)
        self.st()

        self.setx(x)
        self.sety(y)


def move_backward() -> None:
    disable_keys()
    backward(200)
    enable_keys()


def move_forward() -> None:
    disable_keys()

    forward(200)
    if abs(pos()) < 1:
        end_fill()
        left(170)
        return

    enable_keys()


def move_left() -> None:
    disable_keys()
    left(170)
    enable_keys()


def move_right() -> None:
    disable_keys()
    right(170)
    enable_keys()


def enable_keys() -> None:
    onkey(move_forward, 'k')
    onkey(move_backward, 'j')
    onkey(move_left, 'h')
    onkey(move_right, 'l')
    onkey(bye, 'q')


def disable_keys() -> None:
    onkey(None, 'k')
    onkey(None, 'j')
    onkey(None, 'h')
    onkey(None, 'l')
    onkey(None, 'q')


if __name__ == '__main__':
    enable_keys()

    color('red', 'yellow')
    begin_fill()

    listen()
    done()
