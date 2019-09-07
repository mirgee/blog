FROM python:3.6-alpine

WORKDIR /home/blog

COPY Pipfile ./

# TODO: Run nginx in another container and docker-compose
RUN     apk add linux-headers \
        && pip install pipenv \
        && apk add --update --no-cache g++ gcc libxslt-dev openrc nginx \
        && export PIPENV_VENV_IN_PROJECT=1 \
        && pipenv install --deploy --ignore-pipfile

COPY config.py run.py uwsgi.ini start.sh ./
COPY articles ./articles
COPY blog ./blog
COPY instance ./instance
COPY conf/nginx-conf/ /etc/nginx/
COPY conf/systemd-conf/blog.service /etc/systemd/system/

EXPOSE 8081

ENTRYPOINT ["./start.sh"]
