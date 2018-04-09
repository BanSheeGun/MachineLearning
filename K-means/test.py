import kmeans as km
import matplotlib.pyplot as plt
import random

x = []
for _ in range(40):
    xx = 3 + (random.random() - 0.5) * 3
    yy = 4 + (random.random() - 0.5) * 4
    x.append([xx, yy])

for _ in range(40):
    xx = 8 + (random.random() - 0.5) * 5
    yy = 8 + (random.random() - 0.5) * 6
    x.append([xx, yy])

for _ in range(40):
    xx = 8 + (random.random() - 0.5) * 2
    yy = 3 + (random.random() - 0.5) * 2
    x.append([xx, yy])

K = 4
mn, c = km.learn(x, 120, K, random.sample(x, K))
plt.figure(1, figsize=(12, 6))
plt.subplot(121)
plt.axis([0, 13, 0, 13])
for xe in x:
    plt.plot([xe[0]], [xe[1]], 'b.')

plt.subplot(122)
index = 0
plt.axis([0, 13, 0, 13])


for i in range(K):
    xx = [j[i][0] for j in mn]
    yy = [j[i][1] for j in mn]
    plt.plot(xx, yy, 'k-')
    plt.plot(xx, yy, 'y*')
    plt.plot(xx[-1], yy[-1], 'yo')

tmp = ['r.', 'g.', 'b.', 'c.', 'm.']
for xe in x:
    plt.plot([xe[0]], [xe[1]], tmp[c[index]])
    index += 1

plt.show()
