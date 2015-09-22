"""
Django settings for scoutcharter project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
DJ_PROJECT_DIR = os.path.dirname(__file__)
BASE_DIR = os.path.dirname(DJ_PROJECT_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SC_SECRET_KEY']

ON_OPENSHIFT = False
if os.environ.has_key('OPENSHIFT_REPO_DIR'):
    ON_OPENSHIFT = True

PROJECT_DIR = os.path.dirname(os.path.realpath(__file__))
if ON_OPENSHIFT:
    DEBUG = bool(os.environ.get('DEBUG', False))
    if DEBUG:
        print("WARNING: The DEBUG environment is set to True.")
else:
    DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = [
    '.scoutcharter.com',
    '.rhcloud.com',
]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'raven.contrib.django.raven_compat',
    'advancement',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# GETTING-STARTED: change 'scoutcharter' to your project name:
ROOT_URLCONF = 'scoutcharter.urls'

WSGI_APPLICATION = 'scoutcharter.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

if ON_OPENSHIFT:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',  # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': os.environ['OPENSHIFT_APP_NAME'],               # Or path to database file if using sqlite3.
            'USER': os.environ['OPENSHIFT_POSTGRESQL_DB_USERNAME'],               # Not used with sqlite3.
            'PASSWORD': os.environ['OPENSHIFT_POSTGRESQL_DB_PASSWORD'],         # Not used with sqlite3.
            'HOST': os.environ['OPENSHIFT_POSTGRESQL_DB_HOST'],               # Set to empty string for localhost. Not used with sqlite3.
            'PORT': os.environ['OPENSHIFT_POSTGRESQL_DB_PORT'],               # Set to empty string for default. Not used with sqlite3.
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            # GETTING-STARTED: change 'db.sqlite3' to your sqlite3 database:
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static')

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_DIR, '../templates'),
)

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'staticfiles'),
)

LOGIN_URL = '/login/'

SENTRY_HASH = os.environ['SC_SENTRY_HASH']
SENTRY_FIVE_DIGIT = os.environ['SC_SENTRY_FIVE_DIGIT']
RAVEN_CONFIG = { 'dsn': 'https://%s@app.getsentry.com/%s' % (SENTRY_HASH, SENTRY_FIVE_DIGIT), }
