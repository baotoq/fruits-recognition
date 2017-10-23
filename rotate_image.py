import cv2
import numpy as np
import os

def rotate_image(folder, image_name):
    image = cv2.imread(folder + '/{}.jpg'.format(i))
    rows, cols, _ = image.shape

    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 180, 1)
    dst = cv2.warpAffine(image, M, (cols, rows))
    cv2.imwrite('output/{}.jpg'.format(image_name), dst)
    pass

for i in range(353, 755):
    print(i)
    rotate_image('dataset/mangosteen/pre-images', i)