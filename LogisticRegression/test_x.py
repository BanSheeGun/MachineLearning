import matplotlib.pyplot as plt
import random
import logistic as lr


def ran(seed):
    return seed * random.random() - seed / 2


x = []
y = []
for i in range(10):
    for j in range(10):
        if i * 2 + j * 3 <= 12:
            x.append([1, i + ran(2), j + ran(2)])
            y.append([1])
        else:
            x.append([1, i + ran(2), j + ran(2)])
            y.append([0])

xx = [i[1] for i in x]
yy = [i[2] for i in x]
flag = [i[0] for i in y]

cs = [0.09, 0, 5000]
rx = [[0, 1], [5, 10], [5, 10]]

xxdraw = []
for i in range(200):
    for j in range(200):
        xxdraw.append([1, i / 20, j / 20])
xdraw = [i[1] for i in xxdraw]
ydraw = [i[2] for i in xxdraw]
hdraw = lr.work(100, x, y, rx, cs, xxdraw)

css = ['r.', 'b*']
plt.figure(1, figsize=(8, 4))
plt.subplot(121)
plt.axis([0, 11, 0, 11])
for i, j, k in zip(xx, yy, flag):
    plt.plot(i, j, css[k])

plt.subplot(122)
plt.axis([0, 11, 0, 11])
for i, j, k in zip(xx, yy, flag):
    plt.plot(i, j, css[k])

eps = 1e-3
for i, j, k in zip(xdraw, ydraw, hdraw):
    if -eps < k - 0.5 < eps:
        plt.plot(i, j, color='green', linestyle='dashed', marker='.', markersize=1.5)
plt.show()
