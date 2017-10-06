import cv2
import numpy as np
import os

# Gaussian smoothing
kernel_size = 3

def grayscale(img):
	return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def gaussian_blur(img, kernel_size):
	#Applies a Gaussian Noise kernel
	return cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)

output_dir = 'output'
images_dir = 'images'
fruit_dir = ['cucumber', 'kiwi', 'mangosteen', 'starfruit', 'strawberry']

for i in range(len(fruit_dir)):
    fruit_dir[i] = os.path.join(images_dir, fruit_dir[i])

for i in range(1, 11):
    img = cv2.imread(os.path.join(fruit_dir[0], '{0}.jpg'.format(i)))
    img = grayscale(img)
    img = gaussian_blur(img, kernel_size)
    cv2.imwrite(os.path.join(output_dir, '{0}.jpg'.format(i)), img)