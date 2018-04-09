import numpy as np
import random
import math


def g(x):
    x = x.T.tolist()[0]
    y = [[1 / (1 + math.e ** (-i))] for i in x]
    return np.matrix(y)


def cost(m, x, y, theta, lam):
    tmp = x * theta
    h = g(tmp)
    tmp3 = 1 - h
    tmp4 = 1 - y
    tmp1 = np.matrix([[math.log(i)] for i in h.T.tolist()[0]])
    tmp2 = np.matrix([[math.log(i)] for i in tmp3.T.tolist()[0]])
    j = -(y.T * tmp1 + tmp4.T * tmp2) + lam * sum(np.multiply(theta, theta)) / 2
    j -= lam * theta[0][0] ** 2 / 2
    j = j / m
    grad = x.T * (h - y) + lam * theta
    grad = grad / m
    return j, grad


def lr(m, x, y, al, lam, itor):
    theta = np.matrix([[1 + random.random()] for _ in range(x[0].size)])
    for _ in range(itor):
        j, grad = cost(m, x, y, theta, lam)
        theta = theta - al * grad
    return theta


def work(m, x, y, rx, cs, xdraw):
    for i in range(m):
        x[i] = [(j - k[0]) / k[1] for j, k in zip(x[i], rx)]
    for i in range(len(xdraw)):
        xdraw[i] = [(j - k[0]) / k[1] for j, k in zip(xdraw[i], rx)]
    theta = lr(m, np.matrix(x), np.matrix(y), cs[0], cs[1], cs[2])
    ydraw = g(xdraw * theta).T.tolist()[0]
    return ydraw


if __name__ == '__main__':
    print("Hello world")
