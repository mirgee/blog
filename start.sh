#!/bin/sh
nginx
export VIRTUAL_ENV=$(pipenv --venv)
pipenv run uwsgi uwsgi.ini
