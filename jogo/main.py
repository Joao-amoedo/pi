import numpy as np
from turtle import Turtle, Screen
from jogo import Jogo
from IA.algoritmo_genetico import populacao
from IA.rede_neural import Rede

def main():
    rede = Rede(7)
    rede.add_camada(5)
    rede.add_camada(3,'softmax')


if __name__ == '__main__':
    main()
