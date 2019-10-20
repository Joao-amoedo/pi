from turtle import Turtle


class Paddle:
    def __init__(self, wn, color='white', position='left'):
        self.paddle = Turtle()
        self.paddle.speed(0)
        self.paddle.shape('square')
        self.paddle.color(color)
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.penup()
        self.paddle.goto(-350 if position == 'left' else 350, 0)
        self.wn = wn
        self.width = wn.window_width()
        self.height = wn.window_height()

    def get_ycor(self):
        return self.paddle.ycor()

    def get_xcor(self):
        return self.paddle.xcor()

    def move_up(self):
        y = self.ycor + 20
        if y + 20 < self.height:
            self.paddle.sety(y)

    def move_down(self):
        y = self.ycor - 20
        if y + 20 > (self.height / 2) * -1:
            self.paddle.sety(y)

    ycor = property(fget=get_ycor)
    xcor = property(fget=get_xcor)
