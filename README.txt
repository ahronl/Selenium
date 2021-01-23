

## docker build . -t test

## to run from command line
## docker run test

## to run the container in interactive mode
docker run -it --mount type=bind,source="$(pwd)",target=/app test /bin/bash

## run tests from container
python src/app.py