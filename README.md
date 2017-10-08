## PREREQUISITES
1) Install [Docker](https://www.docker.com/)
2) Open command-line tool, change directory (cd) to your project

## HOW TO RUN

### Terminal
```
docker run -it --rm -v `pwd`:/src bao2703/opencv
```

### PowerShell
```
docker run -it --rm -v ${PWD}:/src bao2703/opencv
```

### CMD
```
docker run -it --rm -v %cd%:/src bao2703/opencv
```