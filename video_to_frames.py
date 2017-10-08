import cv2
import os

def video_to_frames(video, output_dir):
    cap = cv2.VideoCapture(video)
    count = 0
    while True:
        success, frame = cap.read()        
        if success:
            print('processing')
            cv2.imwrite(os.path.join(output_dir, '{0}.jpg'.format(count)), frame)
            count += 1
        else:
            print('fail')
            break
    cv2.destroyAllWindows()
    cap.release()
    pass

###############################
output_dir = 'output'

video_to_frames('input.mp4', output_dir)