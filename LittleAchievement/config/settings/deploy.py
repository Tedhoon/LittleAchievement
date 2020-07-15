from .base import *
import json

DEBUG = False

ALLOWED_HOSTS = ['domain','.amazonaws.com','localhost','127.0.0.1']


# 아래는 auto scaling setting 

'''
import requests
EC2_PRIVATE_IP=None
try:
    EC2_PRIVATE_IP=requests.get('http://169.254.169.254/latest/meta-data/local-ipv4', timeout = 0.01).text
except requests.exceptions.RequestException:    
    pass

if EC2_PRIVATE_IP:    
    ALLOWED_HOSTS.append(EC2_PRIVATE_IP)
'''

config_secret_deploy = json.loads(open(CONFIG_SECRET_DEPLOY_FILE).read())

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# 외부 db참조시 쓸 것
'''
DB_PW = config_secret_deploy['django']['db']['password']
DB_NAME = config_secret_deploy['django']['db']['name']
DB_USER = config_secret_deploy['django']['db']['user']
DB_HOST = config_secret_deploy['django']['db']['host']

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

WSGI_APPLICATION = 'config.wsgi.application'