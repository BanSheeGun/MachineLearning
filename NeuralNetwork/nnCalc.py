import numpy as np
import sys


def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))


def add_one(x):
    one = np.matrix(np.ones((len(x), 1)))
    return np.concatenate((one, x), axis=1)


def set_zeros(x):
    res = []
    for i in x:
        zero = np.matrix(np.zeros((1, i.shape[1])))
        res.append(np.concatenate((zero, i[1:]), axis=0))
    return res


def random_matrix(size):
    return np.matrix(np.random.rand(size[0], size[1])) / size[0]


def cost_function(x, theta, y, lam=0):
    n_l = len(theta)
    n_m = len(x)
    theta_ze = set_zeros(theta)
    a = [add_one(x)]
    for i in range(n_l):
        theta_now = theta[i]
        a_tmp = a[-1] * theta_now
        a.append(add_one(sigmoid(a_tmp)))
    j = np.multiply(y, np.log(a[-1][:, 1:])) \
        + np.multiply(1 - y, np.log(1 - a[-1][:, 1:]))
    j = -np.sum(j)
    for i in theta_ze:
        j += lam * np.sum(np.multiply(i, i)) / 2
    j /= n_m

    det = [[] for _ in range(n_l + 1)]
    det[-1] = a[-1][:, 1:] - y
    for i in range(n_l - 1, 0, -1):
        det[i] = det[i+1] * theta[i].T[:, 1:]
        det[i] = np.multiply(det[i], a[i][:, 1:])
        det[i] = np.multiply(det[i], 1 - a[i][:, 1:])
    theta_grad = [[] for _ in range(n_l)]
    for i in range(n_l):
        i = n_l - i - 1
        theta_grad[i] = a[i].T * det[i+1] / n_m
    for i in range(n_l):
        theta_grad[i] -= np.multiply(lam, theta_ze[i])
    return j, theta_grad


def predict(x, theta):
    n_l = len(theta)
    a = [add_one(x)]
    for i in range(n_l):
        theta_now = theta[i]
        a_tmp = a[-1] * theta_now
        a.append(add_one(sigmoid(a_tmp)))
    pre = a[-1][:, 1:]
    pre = np.argmax(pre, axis=1)
    return pre


def learn(x, y, sizes, itor=5000, lam=0, al=1):
    theta = []
    for size in sizes:
        theta.append(random_matrix(size))
    t = []
    j_s = []
    for i in range(itor):
        if i % 100 == 0:
            print('-', end='')
            sys.stdout.flush()
        j, theta_grad = cost_function(x, theta, y, lam)
        j_s.append(j)
        t.append(i+1)
        for j in range(len(theta)):
            theta[j] = theta[j] - np.multiply(al, theta_grad[j])
    print("train finish")
    return theta, t, j_s


def main():
    print("Hello")


if __name__ == '__main__':
    main()

