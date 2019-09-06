#!/bin/sh
rc-service nginx restart
export VIRTUAL_ENV=$(pipenv --venv)
pipenv run uwsgi uwsgi.ini
