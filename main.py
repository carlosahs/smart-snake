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


def move_forward():
    disable_keys()
    forward(200)
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
    onkey(move_forward, 's')
    onkey(move_left, 'a')
    onkey(move_right, 'd')
    onkey(bye, 'q')


def disable_keys():
    onkey(None, 's')
    onkey(None, 'a')
    onkey(None, 'd')
    onkey(None, 'q')


enable_keys()

color('red', 'yellow')

begin_fill()

while True:
    listen()
    if abs(pos()) < 1:
        break

end_fill()
done()
