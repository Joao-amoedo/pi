from random import random, randint


class Individuo:
    def __init__(self, cromossomo, lim_inf, lim_sup):
        assert isinstance(cromossomo, list), 'Cromossomo deve ser uma lista'
        self.cromossomo = cromossomo
        self.avaliacao = None
        self.lim_inf, self.lim_sup = lim_inf, lim_sup

    @staticmethod
    def crossover(i1, i2):
        """
            Realiza o crossover uniforme e retorna 2 filhos
        """
        novo_cromo_1, novo_cromo_2 = [], []

        for cromo1, cromo2 in zip(i1, i2):
            if random() < 0.5:
                novo_cromo_1.append(cromo1)
                novo_cromo_2.append(cromo2)
            else:
                novo_cromo_1.append(cromo2)
                novo_cromo_2.append(cromo1)
        return (Individuo(novo_cromo_1, i1.lim_inf, i1.lim_sup),
                Individuo(novo_cromo_2, i2.lim_inf, i2.lim_sup))

    @staticmethod
    def gera_individuo(base_cromossomo, lim_inf, lim_sup):
        novo_cromossomo = []
        for base in base_cromossomo:
            cromossomo = ''
            for qtd in range(base):
                cromossomo += '1' if random() > 0.5 else '0'
            novo_cromossomo.append(cromossomo)
        return Individuo(novo_cromossomo, lim_inf, lim_sup)

    def mutacao(self):
        p = randint(0, len(self.cromossomo) - 1)
        novo_cromo = list(self.cromossomo[p])
        q = randint(0, len(novo_cromo) - 1)
        novo_cromo[q] = '1' if novo_cromo[q] == '0' else '0'
        novo_cromo = ''.join(novo_cromo)
        self.cromossomo[p] = novo_cromo

    def calcula_valor_inteiro(self):
        inteiro = []
        for i, gene in enumerate(self.cromossomo):
            inteiro.append(0)
            for j, bit in enumerate(reversed(gene)):
                inteiro[i] = (inteiro[i] + 2**j) if bit == '1' else inteiro[i]
        return inteiro

    def calcula_valor_real(self):
        k = len(self.lim_inf)
        real = []
        for inte, inf, sup, cro in zip(self.inteiro, self.lim_inf,
                                       self.lim_sup, self.cromossomo):
            k = len(cro)
            r = inf + ((sup - inf) / ((2**k) - 1)) * inte
            real.append(r)
        return real

    def __len__(self):
        return len(self.cromossomo)

    def __getitem__(self, i):
        return self.cromossomo[i]

    def __repr__(self):
        return str(self.cromossomo)

    inteiro = property(fget=calcula_valor_inteiro)
    real = property(fget=calcula_valor_real)