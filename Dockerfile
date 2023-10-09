FROM python:3.9-alpine
ADD project.py .
RUN pip install cowsay
CMD [ "python", "./project.py"]