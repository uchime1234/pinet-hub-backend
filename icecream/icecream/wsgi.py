"""
WSGI config for icecream project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

from pathlib import Path
import os

from django.core.wsgi import get_wsgi_application


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'gitrepo',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders'
]



MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
]


CORS_ALLOWED_ORIGINS = [
    'http://localhost:5173'
]

CORS_ALLOW_ALL_ORIGINS = True


CORS_ALLOW_ALL_CREDENTIALS = True

CORS_ALLOW_HEADERS = [
    'authorization',
    'content-type',
]


CORS_ALLOW_METHODS = [
     'GET',
     'POST',
     'OPTIONS',

]

MEDIA_URL = "/media/" # to handle image upload
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

REST_FRAMEWORK = {'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.AllowAny'], 
                  'DEFAULT_AUTHENTICATION_CLASSES': ['rest_framework.authentication.SessionAuthentication', 'rest_framework.authentication.BasicAuthentication' ],
                  'DEFAULT_RENDERER_CLASSES': [
                      'rest_framework.renderers.JSONRenderer',
                      'rest_framework.renderers.BrowsableAPIRenderer'
                  ]
                  }


ROOT_URLCONF = 'myfirstproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR, 'temeplates'],
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

WSGI_APPLICATION = 'myfirstproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'uchimevictor',
        'HOST': '127.0.0.1',
        'PORT': '5432'

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










os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'icecream.settings')

application = get_wsgi_application()
