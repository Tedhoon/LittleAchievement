from .base import *
import json

DEBUG = True

config_secret_develop = json.loads(open(CONFIG_SECRET_DEVELOP_FILE).read())

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# 외부 디비 연동시 쓸 것

'''

DB_PW = config_secret_develop['django']['db']['password']
DB_NAME = config_secret_develop['django']['db']['name']
DB_USER = config_secret_develop['django']['db']['user']
DB_HOST = config_secret_develop['django']['db']['host']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PW,
        'HOST': DB_HOST,
        'PORT': '5432',
    }
}
'''