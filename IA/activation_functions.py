import numpy as np
from numpy import array


def sigmoid(x):
    return array(1 / (1 + np.exp(x)))


def relu(x):
    return array([[max(0, i) for i in line] for line in x])


def softmax(x):

    exp = np.exp(x)
    sum_exp = sum(exp)
    while isinstance(sum_exp, type(x)):
        sum_exp = sum(sum_exp)
    return exp / sum_exp


def normal(x):
    return x
