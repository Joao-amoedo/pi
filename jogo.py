from write import Write
from paddle import Paddle
from ball import Ball
from turtle import Screen
import time

class Jogo:
    def __init__(self, width = 800, height = 600):
        self.wn = Screen()
        self.wn.title("Pong")
        self.wn.setup(width=width, height=height)
        self.menu()
        
        
    def jogar(self):
        self.clear_screen()
        
        padle_left = Paddle(self.wn,'white','left')
        padle_right = Paddle(self.wn,'white','right')
        
        ball = Ball(self.wn,self, padle_left, padle_right)
        self.wn.listen()

        self.wn.onkeypress(padle_left.move_up,'w')
        self.wn.onkeypress(padle_left.move_down,'s')
        
        self.wn.onkeypress(padle_right.move_up,'Up')
        self.wn.onkeypress(padle_right.move_down,'Down')
        while True:
            self.wn.update()
            ball.setxy()
    
    def clear_screen(self):
        self.wn.clear()
        self.wn.bgcolor('black')
        
    def vitoria(self, vencedor):
        self.clear_screen()
        Write('Jogador da {} venceu'.format(vencedor), (0,0), align = 'center')
        time.sleep(5)
        self.menu()
        
    def menu(self):
        self.clear_screen()
        opcoes = [Write('Jogar',(-300, 200)),Write('Evoluir',(-300, 150)) ]
        __selecao = Write('', (-320, 210), False)
        
        def move_down():
            
            y = __selecao.ycor - 50
            if y > opcoes[-1].ycor:
                __selecao.ycor = y
            
        def move_up():
            y = __selecao.ycor + 50
            if y < opcoes[0].ycor + 60:
                __selecao.ycor = y
        
        def seleciona():
            ycor = __selecao.ycor - 10
            opcao = next(filter(lambda o: o.ycor == ycor, opcoes),None)
            if opcao == opcoes[0]:
                self.jogar()
            
            if opcao == opcoes[1]:
                print('Evoluir')
            

        self.wn.listen()
        self.wn.onkeypress(move_down,'s')
        self.wn.onkeypress(move_up,'w')
        self.wn.onkeypress(seleciona, 'a')
        
        while True:
            self.wn.update()