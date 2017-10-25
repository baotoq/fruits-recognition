    opencv_createsamples -maxxangle 1.1 -maxyangle 1.1 -maxzangle 0.3 -w 24 -h 16 -num 1500 -info samples/info.txt -vec samples.vec

    opencv_traincascade -vec samples.vec -bg bg.txt -w 24 -h 16 -data classifier -numPos 1300 -numNeg 1000 -numStages 20