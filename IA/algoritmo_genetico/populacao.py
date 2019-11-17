from individuo import Individuo
from random import random, randint


class Populacao:
    def __init__(self,
                 quantidade: int,
                 base_cromossomo: list,
                 lim_inf: list,
                 lim_sup: list,
                 prob_mutacao=0.1):
        assert isinstance(base_cromossomo,
                          list), 'base_cromossmoo deve ser uma lista'
        self.quantidade = quantidade
        self.lim_inf, self.lim_sup = lim_inf, lim_sup
        self.base_cromossmoo = base_cromossomo
        self.populacao = []
        self.geracao = 0
        self.prob_mutacao = prob_mutacao
        self.gera_populacao_inicial()

    def gera_populacao_inicial(self):
        for i in range(self.quantidade):
            ind = Individuo.gera_individuo(self.base_cromossmoo, self.lim_inf,
                                           self.lim_sup)
            self.populacao.append(ind)

    def seleciona(self):
        
        selecao = random()
        soma = 0
        soma_av = sum([i.avaliacao for i in self])

        for idx, ind in enumerate(self.populacao):
            soma += ind.avaliacao / soma_av
            if soma >= selecao:
                return ind

    def gera_nova_populacao(self, shapes = None):
        self.populacao = sorted(self.populacao, key=lambda x: x.avaliacao) 
        nova_populacao = []
        while len(nova_populacao) < len(self):
            p1 = self.seleciona()
            p2 = self.seleciona()

            while p1 == p2:
                p2 = self.seleciona()

            if shapes:
                f1, f2 = Individuo.crossover_rede(p1, p2, shapes)
            else:
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
        self.geracao += 1

    def __getitem__(self, i):
        return self.populacao[i]

    def __len__(self):
        return len(self.populacao)
