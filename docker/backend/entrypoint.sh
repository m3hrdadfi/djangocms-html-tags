#!/bin/sh

cd demo
python manage.py migrate --noinput
# python manage.py initdb
# python manage.py compilemessages
exec "$@"
