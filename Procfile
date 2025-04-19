
web: gunicorn imf_api.wsgi --log-file - 

web: python manage.py migrate && gunicorn imf_api.wsgi