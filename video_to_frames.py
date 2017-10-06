import cv2
import os

def video_to_frames(video, output_dir):
    # extract frames from a video and save to directory as 'x.jpg' where 
    # x is the frame index
    cap = cv2.VideoCapture(video)
    count = 0
    while 1:
        success, frame = cap.read()        
        if success:
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

video_to_frames('white.mp4', output_dir)