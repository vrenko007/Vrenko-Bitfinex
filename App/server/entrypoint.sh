#!/bin/sh

# Below shells script is required because the flask container need to wait for postgres db server to startup before
# accessing it below.

HOST=db

while ! mysqladmin ping -h"$HOST" --silent; do
    sleep 1
done

echo "MySQL started!"

# Run below commands from manage.py to initialize db and have some default data.
python manage.py recreate_db
python manage.py seed_db
uwsgi --ini /etc/uwsgi.ini