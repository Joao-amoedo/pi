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

    def gera_nova_populacao(self):
        nova_populacao = []
        while len(nova_populacao) < len(self):
            p1 = self.seleciona_individuos()
            p2 = self.seleciona_individuos()

            while p1 == p2:
                p2 = self.seleciona_individuos()

            f1, f2 = Individuo.crossover(p1, p2)

            if random() < self.prob_mutacao:
                f1.mutacao()
            if random() < self.prob_mutacao:
                f2.mutacao()

            nova_populacao.append(f1)
            nova_populacao.append(f2)

        while len(nova_populacao) > len(self):
            nova_populacao.remove(nova_populacao[randint(
                0, len(nova_populacao))])

        self.populacao = nova_populacao

    def __getitem__(self, i):
        return self.populacao[i]

    def __len__(self):
        return len(self.populacao)
