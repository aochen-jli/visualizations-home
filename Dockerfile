FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7

RUN pip install pyyaml
COPY ./app /app
