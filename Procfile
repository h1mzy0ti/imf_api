web: gunicorn imf_api.imf_api.wsgi  --bind 0.0.0.0:$PORT --log-file=/dev/stdout

web: python manage.py migrate && gunicorn imf_api.wsgi