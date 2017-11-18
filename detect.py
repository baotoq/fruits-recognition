import numpy as np
import cv2
import os

cascade = cv2.CascadeClassifier("cascade/cascade.xml")

def detect(img):
	#img = cv2.resize(img, (500, 500))
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	fruit = cascade.detectMultiScale(gray, 1.3, 5)
	for (x, y, w, h) in fruit:
			cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)

	return img
def real_time():
    i = 0
    cap = cv2.VideoCapture('dataset/starfruit/videos/2.mp4')
    while True:
        success, frame = cap.read()
        if success:
            img = detect(frame)
            #cv2.imshow('img', img)
            #if cv2.waitKey(1) & 0xFF == ord('q'):
                #break
            i+=1
            cv2.imwrite('output/{}.jpg'.format(i), img)
        else:
            print('fail')
            break
    cap.release()
    cv2.destroyAllWindows()

real_time()
#img = detect(cv2.imread('dataset/kiwi/images/1.jpg'))
#cv2.imwrite('output/{}.jpg'.format(1), img)
