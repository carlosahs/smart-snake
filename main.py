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

        # self.pu()
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
        self.screen = turtle.Screen()

        self.screen.mode("standard")
        self.screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

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

        self.screen.listen()

    def enable_keys(self) -> None:
        self.screen.onkey(self.move_left, "h")
        self.screen.onkey(self.move_down, "j")
        self.screen.onkey(self.move_up, "k")
        self.screen.onkey(self.move_right, "l")
        self.screen.onkey(turtle.bye, "q")

    def disable_keys(self) -> None:
        self.screen.onkey(None, "h")
        self.screen.onkey(None, "j")
        self.screen.onkey(None, "k")
        self.screen.onkey(None, "l")
        self.screen.onkey(None, "q")

    def move_left(self) -> None:
        self.disable_keys()
        self.square.left(self.rate)
        self.enable_keys()

    def move_right(self) -> None:
        self.disable_keys()
        self.square.right(self.rate)
        self.enable_keys()

    def move_down(self) -> None:
        self.disable_keys()
        self.square.down(self.rate)
        self.enable_keys()

    def move_up(self) -> None:
        self.disable_keys()
        self.square.up(self.rate)
        self.enable_keys()


if __name__ == "__main__":
    app = App(SNAKE_SIZE)
    turtle.mainloop()
