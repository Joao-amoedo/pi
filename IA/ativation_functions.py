import numpy as np

def sigmoid(x):
    return np.array(1 / (1 + np.exp(x)))

def relu(x):
    return np.array([[max(0,i) for i in line] for line in x])

def softmax(x):
    exps = np.exp(x)
    sum_exps = sum([sum(exp) for exp in exps])
    soft = np.array([j/sum_exps for j in exps])
    return soft

