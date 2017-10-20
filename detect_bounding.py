import cv2
import numpy as np

KERNEL_SIZE = 3

def gaussian_blur(img):
	return cv2.GaussianBlur(img, (KERNEL_SIZE, KERNEL_SIZE), 0)

def grayscale(img):
	return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def canny_edge(img):
    return cv2.Canny(img, 60, 200)

image = cv2.imread("dataset/mangosteen/images/400.jpg")

image = gaussian_blur(image)
gray = grayscale(image)
edged = canny_edge(gray)

cv2.imshow("Output", edged)
cv2.waitKey(0)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)

_, contours, hierarchy = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

i = 0
for c in contours:
    x, y, w, h = cv2.boundingRect(c)
    if w > 500 and h > 500:
        i += 1
        cv2.imwrite(str(i) + '.jpg', image[y: y + h, x: x + w])

cv2.imshow("Output", image)
cv2.waitKey(0)