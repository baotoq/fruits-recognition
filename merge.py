import cv2
import numpy as np
import os

o = open('samples/info.txt', 'w')
str = ''
for i in range(1, 1000):
    try:
        f = open(os.path.join('samples', '{}.jpg.txt'.format(i)), 'r')
        for line in f:
            if str.find(line) == -1:
                str += line
    except:
        pass

o.write(str)
