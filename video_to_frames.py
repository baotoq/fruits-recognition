import cv2
import os
from optparse import OptionParser

def video_to_frames(video, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    cap = cv2.VideoCapture(video)
    count = 402
    while True:
        success, frame = cap.read()        
        if success:
            count += 1
            print('processing')
            #frame = frame[10: 1400, 200: 1400]
            cv2.imwrite(os.path.join(output_dir, '{0}.jpg'.format(count)), frame)
        else:
            print('fail')
            break
    cap.release()
    pass


# Configure command line options
parser = OptionParser()
parser.add_option('-i', '--input', dest='input', help='input video file')
parser.add_option('-o', '--output', dest='output', help='output location', default='output')

# Get and parse command line options
options, args = parser.parse_args()
input = options.input
output = options.output

video_to_frames(input, output)