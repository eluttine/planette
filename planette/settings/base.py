"""
Django settings for planette project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'yi-(5bx=m0%=g7!j=)$2(!qdz212t^ta$dr^p*n)ctv6ax44d5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
]

# Application definition

INSTALLED_APPS = (
    #'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    #'django.contrib.sessions',
    #'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'rest_framework',
    'corsheaders',
    #'pagination',
    'tagging',
    'planet',
    'api',
    'storages',
)

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        # 'rest_framework.renderers.BrowsableAPIRenderer',
    )
}

MIDDLEWARE_CLASSES = (
    #'django.contrib.sessions.middleware.SessionMiddleware',
    #'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    #'django.contrib.auth.middleware.AuthenticationMiddleware',
    #'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    #'django.contrib.messages.middleware.MessageMiddleware',
    #'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'pagination.middleware.PaginationMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
)

ROOT_URLCONF = 'planette.urls'

WSGI_APPLICATION = 'planette.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

USE_I18N = True

USE_L10N = True

SITE_ID = 1


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

STATIC_URL = '/thumbnails/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
     os.path.join(PROJECT_ROOT, '../thumbnails'),
     #'/var/www/static/',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    #'django.contrib.auth.context_processors.auth',
    #'django.core.context_processors.debug',
    #'django.core.context_processors.i18n',
    #'django.core.context_processors.media',
    #'django.core.context_processors.static',
    #'django.core.context_processors.tz',
    #'django.core.context_processors.request',
    #'django.contrib.messages.context_processors.messages',
    #'planet.context_processors.context',
)

PLANET = {
    "USER_AGENT": "My Planet/1.0",
}

TEMPLATE_DIRS = (
    '/path/to/planet/project/templates',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    # some other template loaders here...
)
