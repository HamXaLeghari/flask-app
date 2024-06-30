FROM python:3.10.14-alpine


RUN mkdir -p /var/www/html/flask && \
    apk update && \
    apk add --no-cache  gcc musl-dev mariadb-dev shadow mariadb-connector-c-dev && \
    pip install --upgrade pip && \
    adduser -H -S -s /sbin/nologin -u 33 www-data &&\
    groupmod -g 33 www-data


WORKDIR /var/www/html/flask


COPY  . .


RUN chown -R :www-data ./ && \
    pip install -r requirements.txt


ENTRYPOINT ["gunicorn", "app:app"]
