# Django settings for nt project.
import json
import sys
import os

version = "1.0.0"

def save_json(json_file,obj):
    full_path = os.path.expanduser(json_file)
    full_path = os.path.abspath(full_path)
    fp = open(full_path,"w")
    out = json.dumps(obj, indent=2)
    fp.write(out)
    fp.close()


def load_json(json_file):
    full_path = os.path.expanduser(json_file)
    full_path = os.path.abspath(full_path)
    fp = open(full_path,"r")
    json_data = fp.read()
    fp.close()
    out = json.loads(json_data)
    return out

DEBUG = True
TEMPLATE_DEBUG = DEBUG

APPEND_SLASH=False
SESSION_COOKIE_AGE = 86400

json_config_file = "/etc/nodetoys.json"

conf = load_json(json_config_file)
ADMINS = tuple(conf["admins"])
MANAGERS = ADMINS
DATABASE_ENGINE = conf["db_engine"]   # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = conf["db_name"]       # Or path to database file if using sqlite3.
DATABASE_USER = conf["db_user"]       # Not used with sqlite3.
DATABASE_PASSWORD = conf["db_passwd"] # Not used with sqlite3.
DATABASE_HOST = conf["db_host"]       # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = conf["db_port"]       # Set to empty string for default. Not used with sqlite3.



# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '8-*9l_w#o52c9+2psn@j3&!kwbc&y5)q917$ld#6a@^*3binh7'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'nt.urls'

this_dir = os.path.dirname(__file__)

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'nt.nodetoys',
)
