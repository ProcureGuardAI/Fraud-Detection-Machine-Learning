FROM python:3.10

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN set -e; \
    apt-get update && \
    apt-get -y install netcat-openbsd gettext httpie && \
    pip install --upgrade pip && \
    pip install flask && \
    pip install psycopg2-binary

RUN mkdir /code
COPY . /code/
WORKDIR /code

RUN set -e; \
    /usr/local/bin/python -m pip install --upgrade pip ;\
    python -m pip install -r /code/requirements.txt ;\
    chmod +x /code/entrypoints/entrypoint.sh ;

EXPOSE 8080
ENTRYPOINT ["/code/entrypoints/entrypoint.sh"]

