import matplotlib.pyplot as plt
import random
import logistic as lr


def ran(seed):
    return seed * random.random() - seed / 2


x = []
y = []
for i in range(10):
    for j in range(10):
        xx = i + ran(2)
        yy = j + ran(2)
        if 2 * (i - 5) ** 2 + 3 * (j - 6) ** 2 <= 20:
            x.append([1, xx, yy, xx * xx, yy * yy, xx * yy])
            y.append([1])
        else:
            x.append([1, xx, yy, xx * xx, yy * yy, xx * yy])
            y.append([0])

xx = [i[1] for i in x]
yy = [i[2] for i in x]
flag = [i[0] for i in y]

cs = [3, 0, 20000]
rx = [[0, 1], [5, 10], [5, 10], [50, 100], [50, 100], [50, 100]]

xxdraw = []
for i in range(200):
    for j in range(200):
        xxdraw.append([1, i / 20, j / 20, i * i / 400, j * j / 400, i * j / 400])
xdraw = [i[1] for i in xxdraw]
ydraw = [i[2] for i in xxdraw]
hdraw = lr.work(100, x, y, rx, cs, xxdraw)

css = ['r.', 'b*']
plt.figure(1, figsize=(8, 4))
plt.subplot(121)
plt.axis([0, 10, 0, 10])
for i, j, k in zip(xx, yy, flag):
    plt.plot(i, j, css[k])

plt.subplot(122)
plt.axis([0, 10, 0, 10])
for i, j, k in zip(xx, yy, flag):
    plt.plot(i, j, css[k])

eps = 5 * 1e-3
for i, j, k in zip(xdraw, ydraw, hdraw):
    if -eps < k - 0.5 < eps:
        plt.plot(i, j, color='green', linestyle='dashed', marker='.', markersize=1.5)
plt.show()
