FROM python:3.6-alpine

RUN adduser -D blog

WORKDIR /home/blog

COPY Pipfile Pipfile
RUN pip install --upgrade pip \
        && pip install pipenv \
        && apk add --update --no-cache g++ gcc libxslt-dev \
        && pipenv install --deploy --ignore-pipfile \
        && pipenv install gunicorn
COPY blog config.py run.py boot.sh ./

ENV FLASK_APP run.py

RUN chown -R blog ./
USER blog

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]    
