#!/bin/sh
pipenv shell
exec gunicorn -b :5000 --access-logfile - --error-logfile - microblog:app