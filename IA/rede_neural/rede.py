from numpy import array, exp
from random import random
import numpy as np
from functools import reduce
from activation_functions import sigmoid, relu, softmax, normal


class Rede:

    dic_functions = {
        'sigmoid': sigmoid,
        'relu': relu,
        'softmax': softmax,
        None: normal
    }

    def __init__(self, shape_in):
        self.shape_in = shape_in
        self.bias = []
        self.camadas = []
        self.activation_functions = []

    def add_camada(self, neuronios: int, actvation_function=None):
        if len(self.camadas) == 0:
            camada = [[random() for i in range(neuronios)]
                      for j in range(self.shape_in)]
        else:
            camada = [[random() for i in range(neuronios)]
                      for j in range(self.camadas[-1].shape[1])]
        camada = array(camada)

        self.bias.append(array([random() for i in range(neuronios)]))

        self.camadas.append(camada)
        self.activation_functions.append(
            Rede.dic_functions[actvation_function])

    def predict(self, x):
        assert self.camadas is not None, "Deve inserir camadas primeiro"
        assert len(
            x) == self.shape_in, 'Erro na quantidade de elementos inseridos'
        x = array(x)

        dot = np.dot(x, self.camadas[0] + self.bias[0])
        dot = self.activation_functions[0](dot)

        if len(self.camadas) > 1:
            for funcao, camada, bias in zip(self.activation_functions[1:],
                                            self.camadas[1:],
                                            self.bias[1:]):
                dot = funcao(np.dot(dot, camada) + bias)
        return dot

    def __getitem__(self, i):
        return self.camadas[i]

    def __len__(self):
        return len(self.camadas)
