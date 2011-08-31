#Place the below lines in /var/www/django-app/nt.wsgi
#Then place the app in the /var/www/django-app/nt directory

import sys
import os

user_dir = "/var/www/django-app"
proj     = "nt.settings"
egg_cache  = os.path.join(user_dir,"egg_cache")
egg_path   = os.path.join(user_dir,"eggs")
sys.path.append(user_dir)
sys.path.append(egg_path)

from pkg_resources import require
os.environ["BASE_PATH"]=user_dir
os.environ["DJANGO_SETTINGS_MODULE"]=proj
os.environ['PYTHON_EGG_CACHE']=egg_cache
os.environ['MPLCONFIGDIR'] = "/tmp"
import django.core.handlers.wsgi
sys.path.insert(0,user_dir)
application = django.core.handlers.wsgi.WSGIHandler()



