# Selenium skeleton project

this project contains the basic for selenium automation project using docker container.

## use from command line
docker build . -t test
docker run test

## development from command line
docker run -it --mount type=bind,source="$(pwd)",target=/app test /bin/bash
python src/app.py

## development in vscode
run debugger with configuration Docker: Python - General
