FROM bao2703/ffmpeg

RUN apt-get update
RUN apt-get install -y python3 \
	python3-pip \
	python3-tk \
	python-opencv

RUN pip3 install --upgrade pip
RUN pip3 install numpy \
	matplotlib \
	moviepy \
	opencv-python

WORKDIR /src