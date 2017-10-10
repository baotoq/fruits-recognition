## PREREQUISITES
1) Install [Docker](https://www.docker.com/)
2) Open command-line tool, change directory (cd) to your project

## HOW TO RUN

### RUN 
```
docker build -t fruits-recognition .
```

#### Terminal
```
docker run -it --rm -v `pwd`:/src --user `id -u` fruits-recognition
```

#### PowerShell
```
docker run -it --rm -v ${PWD}:/src fruits-recognition
```

#### CMD
```
docker run -it --rm -v %cd%:/src fruits-recognition
```