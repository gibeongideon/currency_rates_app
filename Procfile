release: python manage.py migrate
web: gunicorn currency_app.wsgi --log-file -
worker:python manage.py qcluster