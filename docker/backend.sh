#!/bin/sh

yes | python manage.py makemigrations
yes | python manage.py migrate

python manage.py runserver 8000 --settings=TrabajoTitulacion.settings