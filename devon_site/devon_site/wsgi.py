# TURN ON THE VIRTUAL ENVIRONMENT FOR YOUR APPLICATION
activate_this = '/home/devon/.virtualenvs/devon/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

import os
import sys

# ADD YOUR PROJECT TO THE PYTHONPATH FOR THE PYTHON INSTANCE
path = '/home/devon/devon_site/devon_site'

if path not in sys.path:
    sys.path.append(path)

os.chdir(path)

# TELL DJANGO WHERE YOUR SETTINGS MODULE IS LOCATED
os.environ['DJANGO_SETTINGS_MODULE'] = 'devon_site.settings'

# IMPORT THE DJANGO WSGI HANDLER TO TAKE CARE OF REQUESTS
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
