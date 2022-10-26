FROM python:3.9-slim
ENV PYTHONUNBUFFERED True
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./
# RUN pip install -r requirements.txt
RUN pip install Flask gunicorn
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app

# FROM ubuntu:16.04
# ENV PORT 8080
# ENV HOST 0.0.0.0
# EXPOSE 8080
# RUN apt-get update -y && apt-get install -y python3-pip
# COPY ./requirements.txt /app/requirements.txt
# WORKDIR /app
# RUN pip3 install -r ./requirements.txt
# COPY . /app
# ENTRYPOINT [ "python3" ]
# CMD ["app.py"]