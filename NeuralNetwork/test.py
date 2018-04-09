import nnCalc as nC
import matplotlib.pyplot as plt
import tools.tool as tl
import numpy as np
import matplotlib.image as mpimg


x, y = tl.read_images(r"VerCodeImg\trainimg")
sizes = [[301, 100], [101, 36]]
t, x, y = nC.learn(x, y, sizes, itor=5000, al=0.1)
plt.title("learn")
plt.plot(x, y, 'b')
plt.show()

x, y = tl.read_images(r"VerCodeImg\testimg")
yy = nC.predict(x, t)
yt = np.argmax(y, axis=1)
s = 0
p = 0
for i, j in zip(yy, yt):
    s += 1
    p += int(i == j)

plt.suptitle("test percent " + str(1.0 * p / s))
plt.figure(1, figsize=(10, 10))
index = 0
pics = tl.read_random("VerCodeImg\\testimg\\")
for i in pics:
    index += 1
    plt.subplot(330 + index)
    file_name = "VerCodeImg\\testimg\\" + i
    img = mpimg.imread(file_name)
    plt.imshow(img)
    x = tl.read_image(file_name)
    y = nC.predict(x, t)
    plt.title(i[0] + " predict " + tl.un_transfer(y[0][0]))
    plt.axis('off')
plt.show()
