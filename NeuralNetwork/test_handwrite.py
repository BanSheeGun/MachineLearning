import numpy as np
import nnCalc as nC
import matplotlib.pyplot as plt
from PIL import Image


fo = open("Handwritten\\semeion.data", "r")
lines = fo.readlines()
fo.close()

x, y = [], []
for line in lines:
    line = [float(i) for i in line.split()]
    x.append(line[:256])
    y.append(line[256:])
x = np.matrix(x)
y = np.matrix(y)

sizes = [[257, 100], [101, 10]]
theta, j_x, j_y = nC.learn(x, y, sizes, itor=5000, al=0.1)

pre = nC.predict(x, theta)
num, cro = 0, 0
for pic, yy, py in zip(x, y, pre):
    num += 1
    pic = (1 - pic) * 255
    img = np.reshape(pic, (16, 16))
    img_new = Image.fromarray(img.astype(np.uint8))
    predict = py[0, 0]
#   save pictures in Handwritten\Result
#   img_new.save("Handwritten\\Result\\" + str(predict) + "_" + str(num) + ".png")
    if yy[0, predict] == 1:
        cro += 1
correct = 1.0 * cro / num

plt.plot(j_x, j_y)
plt.title("correct : " + str(correct))
plt.show()
