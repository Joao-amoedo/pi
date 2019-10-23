from write import Write
from paddle import Paddle
from ball import Ball
from turtle import Screen
from ia.algoritmo_genetico.populacao import Populacao
from ia.rede_neural.rede import Rede
import time
import numpy as np


class Jogo:
    def __init__(self, qtd_individuos, width=800, height=600):
        self.wn = Screen()
        self.wn.title("Pong")
        self.wn.setup(width=width, height=height)
        self.qtd_individuos = qtd_individuos
        self.pop = None
        self.menu()

    def jogar(self, redes=None):

        if redes:
            assert isinstance(
                redes, tuple), 'redes deve ser uma tupla de duas redes neurais'
            rede1 = redes[0]
            rede2 = redes[1]

        self.clear_screen()

        paddle_left = Paddle(self.wn, 'white', 'left')
        paddle_right = Paddle(self.wn, 'white', 'right')

        score1, score2 = 0, 0
        scores = Write('Jogador 1: {} \t Jogador 2: {}'.format(score1, score2),
                       (0, 260),
                       align='center')

        ball = Ball(self.wn, paddle_left, paddle_right)
        if redes:
            ball.dx = 4
            ball.yx = 4
        self.wn.listen()

        self.wn.onkeypress(paddle_left.move_up, 'w')
        self.wn.onkeypress(paddle_left.move_down, 's')
        self.wn.onkeypress(paddle_right.move_up, 'Up')
        self.wn.onkeypress(paddle_right.move_down, 'Down')

        while True:
            self.wn.update()
            ball.setxy()
            vitoria = ball.check_border()
            if vitoria:
                if redes:
                    return [
                        score1 if score1 > 0 else 50,
                        score2 if score2 > 0 else 50
                    ]
                else:
                    self.vitoria(vitoria)

            if redes:
                xcor = ball.xcor
                ycor = ball.ycor

                dxball = ball.dx
                dyball = ball.dy

                dir_x_ball = 1 if dxball > 1 else -1
                dir_y_ball = 1 if dyball > 1 else -1

                paddle_left_xcor = paddle_left.xcor
                paddle_left_ycor = paddle_left.ycor

                paddle_right_xcor = paddle_right.xcor
                paddle_right_ycor = paddle_right.ycor

                inputs_1 = [
                    xcor, ycor, dxball, dyball, dir_x_ball, dir_y_ball,
                    paddle_left_xcor, paddle_left_ycor
                ]
                inputs_2 = [
                    xcor, ycor, dxball, dyball, dir_x_ball, dir_y_ball,
                    paddle_right_xcor, paddle_right_ycor
                ]

                self._movimentos_rede(rede1, paddle_left, inputs_1)
                self._movimentos_rede(rede2, paddle_right, inputs_2)

            if ball.check_colision_paddle_right():
                score1 += 100
                self._escreve_scores(scores, score1, score2)

            if ball.check_colison_paddle_left():
                score2 += 100
                self._escreve_scores(scores, score1, score2)

    def _movimentos_rede(self, rede, paddle, inputs):
        prediction = rede.predict(inputs)
        max_pred = max(prediction)
        if max_pred == prediction[0]:
            paddle.move_up()
        elif max_pred == prediction[1]:
            paddle.move_down()
        else:
            pass

    def _escreve_scores(self, scores, score1, score2):
        scores.clear()
        scores.opcao.write('Jogador 1: {} \t Jogador 2: {}'.format(
            score1, score2),
                           font=('Courrier', 14, 'normal'),
                           align='center')

    def clear_screen(self):
        self.wn.clear()
        self.wn.bgcolor('black')

    def vitoria(self, vencedor):
        self.clear_screen()
        Write('Jogador da {} venceu'.format(vencedor), (0, 0), align='center')
        time.sleep(2)
        self.menu()

    def menu(self):
        self.clear_screen()
        opcoes = [Write('Jogar', (-300, 200)), Write('Evoluir', (-300, 150))]
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
            opcao = next(filter(lambda o: o.ycor == ycor, opcoes), None)
            if opcao == opcoes[0]:
                self.jogar()

            if opcao == opcoes[1]:
                self.evoluir()

        self.wn.listen()
        self.wn.onkeypress(move_down, 's')
        self.wn.onkeypress(move_up, 'w')
        self.wn.onkeypress(seleciona, 'a')

        while True:
            self.wn.update()

    def _cria_populacao(self):
        rede = Rede(8)
        rede.add_camada(5)
        rede.add_camada(3)

        base = sum([np.prod(camada.shape) for camada in rede.camadas])
        base = [10 for i in range(base)]
        lim_inf = [-2 for i in range(len(base))]
        lim_sup = [2 for i in range(len(base))]

        self.pop = Populacao(self.qtd_individuos, base, lim_inf, lim_sup)
        self.pop.gera_populacao_inicial()

    def evoluir(self):
        if self.pop is None:
            self._cria_populacao()

        rede1 = Rede(8)
        rede1.add_camada(5)
        rede1.add_camada(3, 'softmax')

        rede2 = Rede(8)
        rede2.add_camada(5)
        rede2.add_camada(3, 'softmax')

        shapes = [cam.shape for cam in rede1 or rede2]
        divisor_camadas = [np.prod(shape) for shape in shapes]
        for ind1, ind2 in zip(self.pop[::2], self.pop[1::2]):
            camada1_1 = np.array(ind1.real[:divisor_camadas[0]]).reshape(
                shapes[0])
            camada2_1 = np.array(ind1.real[divisor_camadas[0]:]).reshape(
                shapes[1])
            camada1_2 = np.array(ind2.real[:divisor_camadas[0]]).reshape(
                shapes[0])
            camada2_2 = np.array(ind2.real[divisor_camadas[0]:]).reshape(
                shapes[1])

            rede1.camadas[0] = camada1_1
            rede1.camadas[1] = camada2_1

            rede2.camadas[0] = camada1_2
            rede2.camadas[1] = camada2_2

            ind1.avaliacao, ind2.avaliacao = self.jogar((rede1, rede2))
        self.menu()
