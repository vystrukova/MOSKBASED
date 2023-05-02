from .api_client import *
from .info import *
from .sed_api import *
from .user_fixture import *
# Импортируем здесь все классы страниц, чтобы они были доступны из других модулей

__all__ = ['ApiClient', 'Info', 'SedApi', 'user_fixture', 'autorized_client']
# Экспортируем все классы, которые будут доступны при импорте из этого пакета