    perl bin/createsamples.pl positives.txt negatives.txt samples 9600 "opencv_createsamples -bgcolor 0 -bgthresh 0 -maxxangle 1.1 -maxyangle 1.1 maxzangle 0.3 -w 24 -h 24"
    
    opencv_createsamples -maxxangle 1.1 -maxyangle 1.1 -maxzangle 0.3 -w 24 -h 24 -num 3520 -info samples/info.txt -vec samples.vec

    opencv_traincascade -vec samples.vec -bg bg.txt -w 24 -h 24 -data classifier -numPos 3000 -numNeg 900 -numStages 30