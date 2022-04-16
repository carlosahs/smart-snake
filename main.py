import turtle
import random

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


class App:
    def __init__(self, rate: float) -> None:
        main_screen = turtle.Screen()

        main_screen.mode("standard")
        main_screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

        self.square = Square(
            random.randint(0, int(SCREEN_WIDTH / rate))
            * rate - SCREEN_WIDTH / 2,
            random.randint(0, int(SCREEN_HEIGHT / rate))
            * rate - SCREEN_HEIGHT / 2,
            SNAKE_SIZE,
            SNAKE_COLOR,
        )
        self.rate = rate

        self.enable_keys()

        turtle.listen()

    def enable_keys(self) -> None:
        turtle.onkey(self.move_left, "h")
        turtle.onkey(self.move_down, "j")
        turtle.onkey(self.move_up, "k")
        turtle.onkey(self.move_right, "l")
        turtle.onkey(turtle.bye, "q")

    def disable_keys(self) -> None:
        turtle.onkey(None, "h")
        turtle.onkey(None, "j")
        turtle.onkey(None, "k")
        turtle.onkey(None, "l")
        turtle.onkey(None, "q")

    def move_left(self) -> None:
        self.square.left(self.rate)

    def move_right(self) -> None:
        self.square.right(self.rate)

    def move_down(self) -> None:
        self.square.down(self.rate)

    def move_up(self) -> None:
        self.square.up(self.rate)


if __name__ == "__main__":
    app = App(SNAKE_SIZE)
    turtle.mainloop()
