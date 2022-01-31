import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG_SETTING')

ALLOWED_HOSTS = ['*']

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'alumni.apps.AlumniConfig',
    'playerprogress.apps.PlayerprogressConfig',
    #'postgradprep.apps.PostgradprepConfig',
    'playerresources.apps.PlayerresourcesConfig',
    'sitemanagement.apps.SitemanagementConfig',
    'teammanagement.apps.TeammanagementConfig',

    'django_cleanup.apps.CleanupConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'hempfieldbaseball.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'hempfieldbaseball.wsgi.application'


# Database
DATABASES = {
    'default': {
       'NAME': os.environ.get('DATABASE_NAME'),
       'ENGINE': 'django.db.backends.mysql',
       'USER': os.environ.get('DATABASE_USER'),
       'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
       'HOST': os.environ.get('DATABASE_HOST'),
       'PORT': os.environ.get('DATABASE_PORT')
    },
}

DATABASE_ROUTERS = [
    # 'hempfieldbaseball.database_routers.blog.BlogRouter',
    # 'hempfieldbaseball.database_routers.playerprogress.PlayerprogressRouter'
]


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_ROOT = os.environ.get('STATIC_ROOT')

STATIC_URL = '/static/dist/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static/dist/'),
]

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
