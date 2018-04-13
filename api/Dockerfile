FROM python:3.5.2

ENV PYTHONUNBUFFERED 1

# adding project to image
ADD ./ /home/

WORKDIR /home

# installing dependencies
RUN pip install -r requirements.txt
