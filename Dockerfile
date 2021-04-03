FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7

EXPOSE 80

RUN pip install -U pip pyyaml
COPY ./app /app
