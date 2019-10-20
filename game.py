import numpy as np
import turtle


class Paddle:
    def __init__(self, color='white', position='left'):
        self.paddle = turtle.Turtle()
        self.paddle.speed(0)
        self.paddle.shape('square')
        self.paddle.color(color)
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.penup()
        self.paddle.goto(-350 if position == 'left' else 350, 0)

    def get_ycor(self):
        return self.paddle.ycor()

    def get_xcor(self):
        return self.paddle.xcor()

    def move_up(self):
        y = self.ycor + 20
        self.paddle.sety(y)

    def move_down(self):
        y = self.ycor - 20
        self.paddle.sety(y)

    ycor = property(fget=get_ycor)
    xcor = property(fget=get_xcor)


class Ball:
    def __init__(self, color='white'):
        self.ball = turtle.Turtle()
        self.ball.speed()
        self.ball.shape('square')
        self.ball.color(color)
        self.ball.penup()
        self.ball.goto(0, 0)
        self.ball.dx = 0.2
        self.ball.dy = 0.2

    def get_xcor(self):
        return self.ball.xcor()

    def get_ycor(self):
        return self.ball.ycor()

    def setx(self, x=None):
        self.ball.setx((self.ball.xcor() + self.ball.dx) if x is None else x)

    def sety(self, y=None):
        self.ball.sety((self.ball.ycor() + self.ball.dy) if y is None else y)

    def get_dx(self):
        return self.ball.dx

    def get_dy(self):
        return self.ball.dy

    def set_dx(self, x):
        self.ball.dx = x

    def set_dy(self, y):
        self.ball.dy = y

    dx = property(fget=get_dx, fset=set_dx)
    dy = property(fget=get_dy, fset=set_dy)
    xcor = property(get_xcor)
    ycor = property(get_ycor)


padle_left = Paddle('white', 'left')
padle_right = Paddle('white', 'right')
ball = Ball()

width = 800
height = 600

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=width, height=height)
wn.tracer(0)

wn.listen()

wn.onkeypress(padle_left.move_up, 'w')
wn.onkeypress(padle_left.move_down, 's')

wn.onkeypress(padle_right.move_up, 'Up')
wn.onkeypress(padle_right.move_down, 'Down')

speed = 0.01
while True:
    wn.update()

    #move the ball
    ball.setx()
    ball.sety()

    #Border cheking
    if ball.ycor > (height / 2) - 10:
        ball.sety((height / 2) - 10)
        ball.dy = ball.dy * -1

    if ball.ycor < (-1 * (height / 2)) + 10:
        ball.sety((-1 * (height / 2)) + 10)
        ball.dy = ball.dy * -1

    if ball.xcor > (width / 2) - 10 or ball.xcor < (-1 * (width / 2)) + 10:
        ball.ball.goto(0, 0)
        ball.dx = ball.dx * -1
        ball.dx = 0.1
        ball.dy = 0.1

    if (ball.xcor > padle_right.xcor - 20) and (
            ball.ycor <= padle_right.ycor + 50
            and ball.ycor >= padle_right.ycor - 50):
        ball.dx *= -1
        ball.ball.goto(padle_right.xcor - 25, ball.ycor)
        ball.dx -= speed
        ball.dy -= speed
        print(ball.dx)

    if (ball.xcor <=
            padle_left.xcor + 20) and (ball.ycor <= padle_left.ycor + 50
                                       and ball.ycor >= padle_left.ycor - 50):
        ball.dx *= -1

        ball.ball.goto(padle_left.xcor + 25, ball.ycor)
        ball.dx += speed
        ball.dy += speed
