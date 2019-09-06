FROM python:3.6-alpine

# RUN adduser -D blog

WORKDIR /home/blog

COPY Pipfile config.py run.py uwsgi.ini start.sh ./
COPY articles ./articles
COPY blog ./blog
COPY instance ./instance

RUN     apk add linux-headers \
        && pip install pipenv \
        && apk add --update --no-cache g++ gcc libxslt-dev openrc nginx \
        && export PIPENV_VENV_IN_PROJECT=1 \
        && pipenv install --deploy --ignore-pipfile

# RUN chown -R blog ./

COPY conf/nginx-conf/ /etc/nginx/
COPY conf/systemd-conf/blog.service /etc/systemd/system/

EXPOSE 8081

# USER blog

# ENTRYPOINT ["pipenv", "run", "uwsgi", "uwsgi.ini"]    
ENTRYPOINT ["./start.sh"]
