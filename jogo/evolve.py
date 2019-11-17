import numpy as np
from sys import path
from os.path import dirname
from random import random

path.append(dirname(dirname(__file__)) + '/ia/rede_neural/')
path.append(dirname(dirname(__file__)) + '/ia/algoritmo_genetico/')

from rede import Rede
from algoritmo_genetico import Populacao

class Envolve:
    def __init__(self, qtd_populacao, qtd_inimigos, prob_mutacao=0.5):
        self.qtd_populacao = qtd_populacao
        self.qtd_inimigos = qtd_inimigos
        self.prob_mutacao = prob_mutacao
        cria_populacao()
        pass

    def cria_populacao(self):
        base = 1 + (self.qtd_inimigos * 3)
        lim_inf = [-2 for i in range(base)]
        lim_sup = [2 for i in range(base)]
        base = [10 for i in range(base)]
        self.populacao = Populacao(self.qtd_populacao, base, lim_inf, lim_sup,
                                   self.prob_mutacao)
        self.populacao.gera_populacao_inicial()

    def cria_redes(self):
        qtd_inputs = 1 + (self.qtd_inimigos * 3)
        rede = Rede(base)
        rede.add_camada(5)
        rede.add_camada(3)

        base = rede.sum_shapes

        lim_inf = [-2 for i in range(base)]
        lim_sup = [2 for i in range(base)]
        base = [10 for i in range(base)]

        p1 = Populacao(10, base, lim_inf, lim_sup, prob_mutacao = 1)
        p1.gera_populacao_inicial()

        np.array(rede.camadas[0]).reshape(rede.shapes[0])

        aux = 0
        ind = p1[0].real
        ind2 = p1[1].real
        camadas = []
        camadas2 = []

        for idx, prod in enumerate(rede.prod_shapes):
            camadas.append(np.array(ind[aux:aux+prod]).reshape(rede.shapes[idx]))
            camadas2.append(np.array(ind2[aux:aux+prod]).reshape(rede.shapes[idx]))
            aux += prod

        np.append(camadas[0][:,1].reshape(-1,1), camadas2[0][:,2].reshape(-1,1), axis=1)

        novas_camadas = []
        for i in range(len(camadas)):
            camada1 = camadas[i]
            camada2 = camadas2[i]
            nova_camada = []
            for j in range(camada1.shape[1]):
                neuronio1 = np.array(camada1[:,j]).reshape(-1,1)
                neuronio2 = np.array(camada2[:,j]).reshape(-1,1)
                if random() < 0.5:
                    if len(nova_camada) == 0:
                        nova_camada = neuronio1
                    else:
                        nova_camada = np.append(nova_camada, neuronio1, axis=1)
                else:
                    if len(nova_camada) == 0:
                        nova_camada = neuronio2
                    else:
                        nova_camada = np.append(nova_camada, neuronio2, axis=1)
            novas_camadas.append(nova_camada)
            print('''
        Camada1:
        {}

        Camada2:
        {}

        Nova Camada:
        {}      
            '''.format(camada1, camada2, nova_camada))
                
        

