import os
import numpy as np
from PIL import Image
import random


def transfer(a):
    if '0' <= a <= '9':
        return int(ord(a) - ord('0'))
    if 'a' <= a <= 'z':
        return int(ord(a) - ord('a')) + 10


def un_transfer(a):
    if 0 <= a <= 9:
        return chr(ord('0') + a)
    if 10 <= a <= 35:
        return chr(ord('a') + a - 10)


def read_images(work_dir=r".\..\VerCodeImg\trainimg"):
    os.chdir(work_dir)
    pics = os.listdir()
    x = []
    y = []
    for i in pics:
        img = np.array(Image.open(i).convert('L'))
        lis = []
        for j in img:
            for k in j:
                lis.append(float(k == 255))
        x.append(lis)
        y.append([0 for _ in range(36)])
        y[-1][transfer(i[0])] = 1
    os.chdir("..\..")
    return np.matrix(x), np.matrix(y)


def read_image(file_path):
    img = np.array(Image.open(file_path).convert('L'))
    lis = []
    for i in img:
        for j in i:
            lis.append(float(j == 255))
    return np.matrix([lis])


def read_random(work_dir):
    os.chdir(work_dir)
    pics = os.listdir()
    os.chdir("..\..")
    return random.sample(pics, 9)


def main():
    print("hello")


if __name__ == '__main__':
    main()
