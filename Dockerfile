# https://www.youtube.com/watch?v=Oy71OgKZbOQ
# get python 
FROM python:3.10-alpine
# copy requirements.txt to app folder
COPY requirements.txt /app/requirements.txt
# install requirements
RUN set -ex \
    && pip install --upgrade pip \
    pip install --no-cache-dir -r /app/requirements.txt
# set workdir
WORKDIR /app
# copy all files to app folder
ADD . .
# local configuration
# EXPOSE 8000
# CMD ["gunicorn", "--bind", ":8000", "--workers", "4", "recipesbook.wsgi:application"]

#heroku configuration
CMD gunicorn recipesbook.wsgi:application --bind 0.0.0.0:$PORT