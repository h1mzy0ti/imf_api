web: gunicorn imf_api.imf_api.wsgi --log-file=/dev/stdout



web: python manage.py migrate && gunicorn imf_api.wsgi