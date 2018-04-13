FROM python:3.5.2

ENV PYTHONUNBUFFERED 1

# adding project to image
ADD ./ /home/

WORKDIR /home

# installing dependencies
RUN pip install -r requirements.txt

# migrating application
#RUN python manage.py migrate

# running the websever with gunicorn
#CMD ["gunicorn", "thewall.wsgi", "-b", "0.0.0.0:8000", "--reload"]
