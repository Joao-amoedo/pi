from random import random, randint
import numpy as np

class Individuo:
    def __init__(self, cromossomo, lim_inf, lim_sup):
        assert isinstance(cromossomo, list), 'Cromossomo deve ser uma lista'
        self.cromossomo = cromossomo
        self.avaliacao = None
        self.lim_inf, self.lim_sup = lim_inf, lim_sup
        self.avaliacao = None

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
    def crossover_rede(i1, i2, shapes):
        novo_cromo_1 = []
        novo_cromo_2 = []
        prod_shapes = [np.prod(shape) for shape in shapes]
        sum_shapes = 0
        for i in range(len(shapes)):
            n_cro_1 = np.array([])
            n_cro_2 = np.array([])
            cromo1 = i1[sum_shapes:prod_shapes[i] + sum_shapes]
            cromo2 = i2[sum_shapes:prod_shapes[i] + sum_shapes]
                       
            cromo1 = np.array(cromo1).reshape(shapes[i])
            cromo2 = np.array(cromo2).reshape(shapes[i])

            for j in range(cromo1.shape[1]):
                if random() < 0.5:
                    if len(n_cro_1) == 0:
                        n_cro_1 = cromo1[:,j].reshape(-1,1)
                        n_cro_2 = cromo2[:,j].reshape(-1,1)
                    else:
                        n_cro_1 = np.append(n_cro_1, cromo1[:,j].reshape(-1,1), axis = 1)
                        n_cro_2 = np.append(n_cro_2, cromo2[:,j].reshape(-1,1), axis = 1)
                else:
                    if len(n_cro_1) == 0:
                        n_cro_1 = cromo2[:,j].reshape(-1,1)
                        n_cro_2 = cromo1[:,j].reshape(-1,1)
                    else:
                        n_cro_1 = np.append(n_cro_1, cromo2[:,j].reshape(-1,1), axis = 1)
                        n_cro_2 = np.append(n_cro_2, cromo1[:,j].reshape(-1,1), axis = 1)
                
            novo_cromo_1 += [cro[0] for cro in n_cro_1.reshape(-1,1)]
            novo_cromo_2 += [cro[0] for cro in n_cro_2.reshape(-1,1)]
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
