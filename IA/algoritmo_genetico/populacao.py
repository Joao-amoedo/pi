from individuo import Individuo
from random import random


class Populacao:
    def __init__(self, quantidade: int, base_cromossomo: list, lim_inf: list,
                 lim_sup: list):
        assert isinstance(base_cromossomo,
                          list), 'base_cromossmoo deve ser uma lista'
        self.quantidade = quantidade
        self.lim_inf, self.lim_sup = lim_inf, lim_sup
        self.base_cromossmoo = base_cromossomo
        self.populacao = []

    def gera_populacao_inicial(self):
        for i in range(self.quantidade):
            ind = Individuo.gera_individuo(self.base_cromossmoo, self.lim_inf,
                                           self.lim_sup)
            self.populacao.append(ind)

    def seleciona(self):
        self.populacao = sorted(self.populacao, key=lambda x: x.avaliacao)
        selecao = random()
        soma = 0
        soma_av = sum([i.avaliacao for i in self])

        for idx, ind in enumerate(self.populacao):
            soma += ind.avaliacao / soma_av
            if soma >= selecao:
                return ind

    def __getitem__(self, i):
        return self.populacao[i]

    def __len__(self):
        return len(self.populacao)
