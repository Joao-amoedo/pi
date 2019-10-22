import numpy as np
from ia.algoritmo_genetico.populacao import Populacao
from ia.rede_neural.rede import Rede


def main():
    rede = Rede(7)
    rede.add_camada(5)
    rede.add_camada(3, 'softmax')
    base = np.prod([np.prod(camada.shape) for camada in rede.camadas])
    base = [10 for i in range(base)]
    lim_inf = [-2 for i in range(len(base))]
    lim_sup = [2 for i in range(len(base))]
    p1 = Populacao(100, base, lim_inf, lim_sup)
    p1.gera_populacao_inicial()
    print(p1[0].real)


if __name__ == '__main__':
    main()
