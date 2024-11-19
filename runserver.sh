python manage.py collectstatic --no-input

python manage.py migrate

gunicorn djangocrm.wsgi:application