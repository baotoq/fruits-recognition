import cv2
import numpy as np
import os
import glob

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

def rotate_image(image_path, image_name):
    image = cv2.imread(image_path)
    rows, cols, _ = image.shape
    
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 270, 1)
    dst = cv2.warpAffine(image, M, (cols, rows))
    cv2.imwrite('output/{}.jpg'.format(image_name), dst)
    pass

i = 865
image_paths, image_names = load_images('dataset', 'starfruit/images/2')
for image_path,image_name in zip(image_paths, image_names):
    print(image_path)
    i += 1
    rotate_image(image_path, i)
