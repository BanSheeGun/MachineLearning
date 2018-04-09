import numpy as np
import random


def cost(m, x, y, theta, lam):
    h = x * theta
    tmp = h - y
    j = sum(np.multiply(tmp, tmp)) + lam * sum(np.multiply(theta, theta))
    j -= lam * theta[0][0] * theta[0][0]
    j = j / (2 * m)
    grad = x.T * tmp + lam * theta
    grad = grad / m
    return j, grad


def lr(m, x, y, al, lam, itor):
    theta = np.matrix([[random.random()] for _ in range(x[0].size)])
    for _ in range(itor):
        j, grad = cost(m, x, y, theta, lam)
        theta = theta - al * grad
    return theta


def work(m, x, y, rx, ry, cs, xdraw):
    for i in range(m):
        x[i] = [(j - k[0]) / k[1] for j, k in zip(x[i], rx)]
    for i in range(len(xdraw)):
        xdraw[i] = [(j - k[0]) / k[1] for j, k in zip(xdraw[i], rx)]
    for i in range(m):
        y[i][0] = (y[i][0] - ry[0]) / ry[1]
    theta = lr(m, np.matrix(x), np.matrix(y), cs[0], cs[1], cs[2])
    ydraw = (np.matrix(xdraw) * theta).T.tolist()[0]
    ydraw = [i * ry[1] + ry[0] for i in ydraw]
    return ydraw


if __name__ == '__main__':
    print("hello world!")
