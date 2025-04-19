web: gunicorn imf_api.wsgi --log-file - 
#or works good with external database
web: python manage.py migrate && gunicorn imf_api.wsgi