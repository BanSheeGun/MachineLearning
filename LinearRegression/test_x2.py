import liner as lr
import random
import matplotlib.pyplot as plt

x = []
y = []
for i in range(20):
    xx = 10 * random.random()
    x.append([1, xx, xx * xx])
    y.append([0.5 * xx * xx - xx * 4 + 2 * random.random() + 10])

cs = [0.8, 0, 10000]
rx = [[0, 1], [5, 10], [50, 100]]
ry = [12.5, 25]
xdraw = [[1, i / 50, i * i / 2500] for i in range(500)]
xx = [i[1] for i in x]
yy = [i[0] for i in y]
xxdraw = [i[1] for i in xdraw]
ydraw = lr.work(20, x, y, rx, ry, cs, xdraw)

plt.figure(1, figsize=(8, 4))
plt.subplot(121)
plt.axis([0, 10, 0, 25])
plt.plot(xx, yy, 'r.')

plt.subplot(122)
plt.axis([0, 10, 0, 25])
plt.plot(xx, yy, 'r.')
plt.plot(xxdraw, ydraw, 'b')
plt.show()
