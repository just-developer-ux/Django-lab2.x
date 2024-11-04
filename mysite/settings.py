"""
Налаштування Django для проекту mysite.

Згенеровано «django-admin startproject» за допомогою Django 5.1.2.

Додаткову інформацію про цей файл див
https://docs.djangoproject.com/en/5.1/topics/settings/

Повний список налаштувань та їх значень див
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# Будування шляхів всередині проекту: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Налаштування швидкого запуску розробки - непридатні для виробництва
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# ПОПЕРЕДЖЕННЯ БЕЗПЕКИ: зберігайте секретний ключ, який використовується у виробництві, в таємниці!
SECRET_KEY = 'django-insecure-x3ma9ckg)z874o376ka3b6fms9yb659oe(2fkt_o28zy3-c=9m'

# ПОПЕРЕДЖЕННЯ ПРО БЕЗПЕКУ: не запускайте з увімкненим налагодженням у робочому режимі!
DEBUG = True

# Дозволені хости
ALLOWED_HOSTS = []


# Визначення програми
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app_blog',
]

# Додаткові бібліолеки необхідні для роботи додатку
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Основний конфігуратор посилань
ROOT_URLCONF = 'mysite.urls'

# Налаштування шаблонів
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

# Посилання на додаток WSGI
WSGI_APPLICATION = 'mysite.wsgi.application'


# Налаштування бази даних
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Перевірка паролів
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


# Налаштування мов
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Налаштування статичних файлів (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Тип поля первинного ключа за замовчуванням
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
