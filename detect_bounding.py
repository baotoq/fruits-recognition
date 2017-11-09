import cv2
import numpy as np
import os
import glob

KERNEL_SIZE = 3

def gaussian_blur(img):
	return cv2.GaussianBlur(img, (KERNEL_SIZE, KERNEL_SIZE), 0)

def grayscale(img):
	return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def canny_edge(img):
    return cv2.Canny(img, 10, 30)

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

def detect_bounding(image_path, image_name):
    image = cv2.imread(image_path)
    image = image[10: 1440, 100: 1320]
    image = gaussian_blur(image)
    gray = grayscale(image)
    edged = canny_edge(gray)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
    closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)

    _, contours, hierarchy = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    #cv2.imwrite('output/{}_1.jpg'.format(image_name), edged)
    #cv2.imwrite('output/{}_2.jpg'.format(image_name), image)

    i = 0
    for c in contours:
        x, y, w, h = cv2.boundingRect(c)
        if w > 100 and h > 200:
            i += 1
            cv2.imwrite('output/{}'.format(image_name, i), image[y: y + h, x: x + w])
    pass

#detect_bounding('dataset/cucumber/images/135.jpg', '1')
image_paths, image_names = load_images('dataset', 'starfruit/images/3')
for image_path,image_name in zip(image_paths, image_names):
    print(image_path)
    detect_bounding(image_path, image_name)