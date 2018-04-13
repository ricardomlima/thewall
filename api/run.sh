#!/bin/bash

python manage.py migrate

gunicorn thewall.wsgi -b 0.0.0.0:8000 --reload
