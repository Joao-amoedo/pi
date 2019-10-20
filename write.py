from turtle import Turtle

class Write:
    def __init__(self, write, goto, hideturtle = True, 
                 font = ('Courrier',14,'normal'), align = 'left'):
        self.opcao = Turtle()
        self.opcao.speed(0)
        self.opcao.color('white')
        self.opcao.penup()
        if hideturtle:
            self.opcao.hideturtle()
        self.opcao.shape(None)
        self.opcao.goto(goto)
        self.opcao.write(write, align = align,font=font)
    
    def get_ycor(self):
        return self.opcao.ycor()
    
    def set_ycor(self, y):
        self.opcao.sety(y)
        
    ycor = property(get_ycor, set_ycor) 