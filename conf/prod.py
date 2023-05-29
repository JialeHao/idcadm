from conf.base import *


DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file':  BASE_DIR / 'conf' / 'mysql.cnf',
        },
    }
}
