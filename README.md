## PREREQUISITES
1) Install [Docker](https://www.docker.com/)
2) Open command-line tool, change directory (cd) to your project


    opencv_createsamples -maxxangle 1.1 -maxyangle 1.1 -maxzangle 0.3 -w 24 -h 24 -num 1115 -info samples/info.txt -bg bg.txt -img logo.jpg

    opencv_createsamples -maxxangle 1.1 -maxyangle 1.1 -maxzangle 0.3 -w 24 -h 24 -num 1115 -info samples/info.txt -vec samples.vec

    opencv_traincascade -vec samples.vec -bg bg.txt -w 24 -h 24 -data classifier -numPos 1300 -numNeg 1000 -numStages 20

    perl bin/createsamples.pl positives.txt negatives.txt samples 7000 "opencv_createsamples -bgcolor 0 -bgthresh 0 -maxxangle 1.1 -maxyangle 1.1 maxzangle 0.3 -w 24 -h 24"
