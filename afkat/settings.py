"""
Django settings for afkat project.

Generated by 'django-admin startproject' using Django 5.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
from datetime import timedelta
from pathlib import Path

import environ
import sentry_sdk

from sentry_sdk.integrations.django import DjangoIntegration
sentry_sdk.init(
    dsn="https://d8f1bd59fec9bf8736045bc9feae82c0@o4509159271301120.ingest.de.sentry.io/4509159313047632",
    # Add data like request headers and IP for users,
    # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
    integrations=[DjangoIntegration()],
    send_default_pii=True,
    traces_sample_rate=1.0,
)

env = environ.Env()
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

AUTH_USER_MODEL = "afkat_auth.User"
SITE_ID = 1
LOGIN_REDIRECT_URL = "home"
LOGOUT_REDIRECT_URL = "home"

# Application definition
LOCAL_APPS = [
    'afkat_home',
    'afkat_auth',
    'afkat_game',
    'afkat_art'
]
THIRD_PARTY_APPS = [
    'rest_framework',
    'corsheaders',
    'rest_framework_simplejwt',
    'rest_framework.authtoken',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth.registration',
    'dj_rest_auth',
    'debug_toolbar',
    'django_registration',
    'django_browser_reload',
    'django_filters',
    'crispy_forms',
    'crispy_bootstrap5',
    'django_countries',
    'phonenumber_field',
    'drf_yasg',
]
INSTALLED_APPS = [
                     'django.contrib.admin',
                     'django.contrib.auth',
                     'django.contrib.contenttypes',
                     'django.contrib.sessions',
                     'django.contrib.messages',
                     'django.contrib.staticfiles',
                     'django.contrib.sites',
                 ] + THIRD_PARTY_APPS + LOCAL_APPS

THIRD_PARTY_MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]
MIDDLEWARE = [
                 'django.middleware.security.SecurityMiddleware',
                 'django.contrib.sessions.middleware.SessionMiddleware',
                 'corsheaders.middleware.CorsMiddleware',
                 'django.middleware.common.CommonMiddleware',
                 'django.middleware.csrf.CsrfViewMiddleware',
                 'django.contrib.auth.middleware.AuthenticationMiddleware',
                 # "django.contrib.auth.middleware.LoginRequiredMiddleware",
                 'django.contrib.messages.middleware.MessageMiddleware',
                 'django.middleware.clickjacking.XFrameOptionsMiddleware',

             ] + THIRD_PARTY_MIDDLEWARE

# CSRF_COOKIE_SECURE = False  # Set to True in production
# CSRF_USE_SESSIONS = False
# CSRF_COOKIE_HTTPONLY = False
CSRF_TRUSTED_ORIGINS = ['http://localhost:8000', 'http://127.0.0.1:8000',
                        "https://789c-2a01-9700-4201-300-189-e28-fad2-71b.ngrok-free.app"]
# SESSION_COOKIE_SECURE = False

ROOT_URLCONF = 'afkat.urls'
MEDIA_ROOT = BASE_DIR / "media"
MEDIA_URL = "/media/"

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'afkat.wsgi.application'
INTERNAL_IPS = ['127.0.0.1']

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # 'default': dj_database_url.config(
    #     default = 'postgres://postgres:' + env("DB_PASSWORD") + '@localhost:5432/afkat',
    #     conn_max_age = 600,
    #     conn_health_checks = True,
    # )
    'default': {
        **env.db(),
        'CONN_MAX_AGE': 600,
        'CONN_HEALTH_CHECKS': True,
    }
}
# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Cache configuration
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
        'TIMEOUT': 300,  # 5 minutes
    }
}

DEBUG_TOOLBAR_CONFIG = {
    "DISABLE_PANELS": [
        "debug_toolbar.panels.redirects.RedirectsPanel",
        # Disable profiling panel due to an issue with Python 3.12:
        # https://github.com/jazzband/django-debug-toolbar/issues/1875
        "debug_toolbar.panels.profiling.ProfilingPanel",
    ],
    "SHOW_TEMPLATE_CONTEXT": True,
}
REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'rest_framework.views.exception_handler',
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAuthenticated',),
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 'rest_framework.authentication.SessionAuthentication',
        # 'rest_framework.authentication.BaseAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
    ],
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        "rest_framework.throttling.UserRateThrottle",
    ],
    'DEFAULT_THROTTLE_RATES':{
        'anon': '10/minute',
        'user': '50/minute'
    },
    "DEFAULT_FILTER_BACKENDS": [
                "django_filters.rest_framework.DjangoFilterBackend",
                "rest_framework.filters.SearchFilter",
                "rest_framework.filters.OrderingFilter",
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
}

REST_AUTH = {
    'USE_JWT': True,
    'JWT_AUTH_COOKIE': 'afkat-auth',
    'JWT_AUTH_REFRESH_COOKIE': 'afkat-refresh-token',
    "JWT_AUTH_HTTPONLY": False,  # Makes sure refresh token is sent


    'LOGIN_SERIALIZER': 'afkat_auth.serializers.UserLoginSerializer',
    'REGISTER_SERIALIZER': 'afkat_auth.serializers.CustomRegisterSerializer',
    'USER_DETAILS_SERIALIZER': 'afkat_auth.serializers.UserProfileSerializer',
}

ACCOUNT_LOGIN_METHODS = {'email'}
# ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "none"

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes = 10),
    "REFRESH_TOKEN_LIFETIME": timedelta(days = 5),
}

# CONN_MAX_AGE = 600
# CONN_HEALTH_CHECKS = True
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"
ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_OPEN = True

CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]
CORS_ALLOW_HEADERS = [
    'ngrok-skip-browser-warning',
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'access-control-allow-origin',
]
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True

CORS_ORIGIN_WHITELIST = (
    'http://localhost:3000',  # for localhost (REACT Default)
    'http://localhost:5173',  # for localhost (REACT Default)
    'http://192.168.0.50:3000',  # for network
    'http://localhost:8080',  # for localhost (Developlemt)
    'http://192.168.0.50:8080',  # for network (Development)
)


# AUTHENTICATION_BACKENDS = [
#     # Needed to login by username in Django admin, regardless of allauth
#     # 'django.contrib.auth.backends.ModelBackend',
#
#     # allauth specific authentication methods, such as login by e-mail
#     # 'allauth.account.auth_backends.AuthenticationBackend',
# ]

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Basic' : {
            'type': 'basic',
        }
    }
}

# Delete in deployment
DATA_UPLOAD_MAX_MEMORY_SIZE =1 * 1024 * 1024 * 1024 # No limit (or set to e.g., 2 * 1024 * 1024 * 1024 for 2GB)
FILE_UPLOAD_MAX_MEMORY_SIZE = 1 * 1024 * 1024 * 1024  # Also remove file size memory buffer limit
