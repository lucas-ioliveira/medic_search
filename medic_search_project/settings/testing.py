from .settings import *

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default': {
        # pip install mysqlclient
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Nome do seu banco de dados',
        'USER': 'Nome do usuário',
        'PASSWORD': 'Senha',
        'HOST': 'Nome do host de conexão ao banco',
        'PORT': 'Número da porta de comunicação',
    }
}