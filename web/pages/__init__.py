from .base_page import BasePage
from .login_page import LoginPage
from .main_page import MainPage
from .mont_page import MontPage
# Импортируем здесь все классы страниц, чтобы они были доступны из других модулей

__all__ = ['BasePage', 'LoginPage', 'MainPage', 'MontPage']
# Экспортируем все классы страниц, которые будут доступны при импорте из этого пакета
