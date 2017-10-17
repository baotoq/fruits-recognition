import cv2
import numpy as np
import os

KERNEL_SIZE = 3
OUTPUT_DIR = 'output'
IMAGES_DIR = 'images'
FRUIT_DIR = ['cucumber', 'kiwi', 'mangosteen', 'starfruit', 'strawberry']

for i in range(len(FRUIT_DIR)):
    FRUIT_DIR[i] = os.path.join(IMAGES_DIR, FRUIT_DIR[i])

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

######################################
def grayscale(img):
	return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def hsv(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

def gaussian_blur(img):
	#Applies a Gaussian Noise kernel
	return cv2.GaussianBlur(img, (KERNEL_SIZE, KERNEL_SIZE), 0)

def bg_subtract(img):
    fgbg = cv2.createBackgroundSubtractorMOG2()
    return fgbg.apply(img)

def canny_edge(img, sigma=0.33):
    # compute the median of the single channel pixel intensities
    v = np.median(img)

    # apply automatic Canny edge detection using the computed median
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    return cv2.Canny(img, 50, 150)

####################################


# for i in range(1, 301):
#     try:
#         print(i)
#         img = cv2.imread(os.path.join(FRUIT_DIR[0], '{0}.jpg'.format(i)))
#         img = grayscale(img)
#         img = gaussian_blur(img)
#         img = canny_edge(img)
#         cv2.imwrite(os.path.join(OUTPUT_DIR, '{0}.jpg'.format(i)), img)
#         pass
#     except :
#         print('Error {0}'.format(i))