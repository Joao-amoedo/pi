from turtle import Turtle
from random import random


class Ball:
    def __init__(
            self,
            wn,
            jogo,
            paddle_left,
            paddle_right,
            color='white',
    ):
        self.ball = Turtle()
        self.ball.speed()
        self.ball.shape('square')
        self.ball.color(color)
        self.ball.penup()
        self.ball.goto(0, 0)
        self.dx_ini = 1 if random() > 0.5 else -1
        self.dy_ini = 1 if random() > 0.5 else -1
        self.ball.dx = self.dx_ini
        self.ball.dy = self.dy_ini
        self.wn = wn
        self.width = wn.window_width()
        self.height = wn.window_height()
        self.paddle_left = paddle_left
        self.paddle_right = paddle_right
        self.jogo = jogo

    def get_xcor(self):
        return self.ball.xcor()

    def get_ycor(self):
        return self.ball.ycor()

    def setx(self, x=None):
        self.ball.setx((self.ball.xcor() + self.ball.dx) if x is None else x)
        self.check_border()

    def sety(self, y=None):
        self.ball.sety((self.ball.ycor() + self.ball.dy) if y is None else y)
        self.check_border()

    def setxy(self):
        self.ball.goto((self.xcor + self.dx, self.ycor + self.dy))
        #self.setx()
        #self.sety()

    def check_border(self):
        if self.ycor > (self.height / 2) - 10:
            self.ball.sety((self.height / 2) - 10)
            self.ball.dy = self.ball.dy * -1

        if self.ycor < (-1 * (self.height / 2)) + 10:
            self.ball.sety((-1 * (self.height / 2)) + 10)
            self.ball.dy = self.ball.dy * -1

        if self.xcor > (self.width / 2) - 10:
            self.jogo.vitoria('esquerda')

        if self.xcor < (-1 * (self.width / 2)) + 10:
            self.jogo.vitoria('direita')

    def check_colision_paddle_right(self):
        speed = 0.2
        if (self.xcor > self.paddle_right.xcor - 20) and (
                self.ycor <= self.paddle_right.ycor + 50
                and self.ycor >= self.paddle_right.ycor - 50):
            self.ball.dx *= -1
            self.ball.goto(self.paddle_right.xcor - 25, self.ycor)
            self.ball.dx -= speed
            self.ball.dy -= speed
            return True

    def check_colison_paddle_left(self):
        speed = 0.2
        if (self.xcor <= self.paddle_left.xcor + 20) and (
                self.ycor <= self.paddle_left.ycor + 50
                and self.ycor >= self.paddle_left.ycor - 50):
            self.ball.dx *= -1

            self.ball.goto(self.paddle_left.xcor + 25, self.ycor)
            self.ball.dx += speed
            self.ball.dy += speed
            return True

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
