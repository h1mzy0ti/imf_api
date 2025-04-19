
web: gunicorn mf_api.imf_api.wsgii --log-file - 
#or works good with external database
web: python manage.py migrate && gunicorn mf_api.imf_api.wsgi