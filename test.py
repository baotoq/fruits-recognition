import cv2
import numpy as np
import os

outputFolder = 'output'
imagesFolder = 'images'
fruitFolder = ['cucumber', 'kiwi', 'mangosteen', 'starfruit', 'strawberry']

for i in range(len(fruitFolder)):
    fruitFolder[i] = os.path.join(imagesFolder, fruitFolder[i])

for i in range(1, 201):
    img = cv2.imread(os.path.join(fruitFolder[2], '{0}.jpg'.format(i)))
    cv2.imwrite(os.path.join(outputFolder, '{0}.jpg'.format(i)), img)