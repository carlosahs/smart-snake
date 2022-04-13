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


def move_backward():
    disable_keys()
    backward(200)
    enable_keys()


def move_forward():
    disable_keys()

    forward(200)
    if abs(pos()) < 1:
        end_fill()
        left(170)
        return

    enable_keys()


def move_left():
    disable_keys()
    left(170)
    enable_keys()


def move_right():
    disable_keys()
    right(170)
    enable_keys()


def enable_keys():
    onkey(move_forward, 'k')
    onkey(move_backward, 'j')
    onkey(move_left, 'h')
    onkey(move_right, 'l')
    onkey(bye, 'q')


def disable_keys():
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
