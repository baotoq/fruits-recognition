import cv2
import numpy as np
import os

# Gaussian smoothing
kernel_size = 3
OUTPUT_DIR = 'output'
IMAGES_DIR = 'images'
FRUIT_DIR = ['cucumber', 'kiwi', 'mangosteen', 'starfruit', 'strawberry']

for i in range(len(FRUIT_DIR)):
    FRUIT_DIR[i] = os.path.join(IMAGES_DIR, FRUIT_DIR[i])


###################################
def grayscale(img):
	return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def hsv(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

def gaussian_blur(img, kernel_size):
	#Applies a Gaussian Noise kernel
	return cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)

def bg_subtract(img):
    fgbg = cv2.createBackgroundSubtractorMOG2()
    return fgbg.apply(img)
####################################



####################################
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))

for i in range(1, 300):
    try:
        print(i)
        img = cv2.imread(os.path.join(FRUIT_DIR[1], '{0}.jpg'.format(i)))
        img = grayscale(img)
        img = gaussian_blur(img, kernel_size)
        cv2.imwrite(os.path.join(OUTPUT_DIR, '{0}.jpg'.format(i)), img)
        pass
    except :
        print('Error {0}'.format(i))
        break

####################################