import numpy as np
import cv2
import os
import glob

s = ''
def load_images(dataset_path, fruit):
    image_paths = []
    image_names = []

    print('Now going to read {}.'.format(fruit))
    path = os.path.join(dataset_path, fruit, '*.jpg')
    files = glob.glob(path)
    for fl in files:
        image_paths.append(fl)
        flbase = os.path.basename(fl)
        image_names.append(flbase)

    return image_paths, image_names

def create_info(image_path, image_name):
    image = cv2.imread(image_path)
    height, width, channels = image.shape
    global s
    s += image_name
    s = s + ' ' + '1 0 0' + ' '
    s += str(width)
    s += ' '
    s += str(height)
    s += '\n'
    pass

o = open('info.txt', 'w')
image_paths, image_names = load_images('.', 'positive_images')
for image_path,image_name in zip(image_paths, image_names):
    print(image_path)
    create_info(image_path, image_name)
o.write(s)