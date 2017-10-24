import cv2
import numpy as np
import os

KERNEL_SIZE = 3

def gaussian_blur(img):
	return cv2.GaussianBlur(img, (KERNEL_SIZE, KERNEL_SIZE), 0)

def crop_image(image_path, image_name, x, y, w, h):
    image = cv2.imread(image_path)
    image = gaussian_blur(image)
    cv2.imwrite('output/{}'.format(image_name), image[y: y + h, x: x + w])
    pass

def crop():
    folder = 'dataset/mangosteen/images';
    f = open(os.path.join(folder, 'mangosteen.txt'), 'r')
    for line in f:
        print(line)
        s = line.split()
        crop_image(os.path.join(folder, s[0]), s[0], int(s[2]), int(s[3]), int(s[4]), int(s[5]))
    pass

# crop()

o = open('info.txt', 'w')
for i in range(10, 755):
    if not (i == 99 or i == 312):
        f = open(os.path.join('dataset/samples', '{}.jpg.txt'.format(i)), 'r')
        for line in f:
            print(line)
            o.write(line)