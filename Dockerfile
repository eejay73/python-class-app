FROM eclipse/ubuntu_python:latest

## Default pip installs
RUN sudo pip install autopep8 && sudo pip install flask

EXPOSE 