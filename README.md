## Тесты на Python3 (PyTest + Selenium + Appium + requests)

- Для создания виртуальной среды выполните следующие команды:
> pip install virtualenv

> virtualenv venv

- Для установки зависимостей выполните следующие команды:
> pip install -r requirements.txt

> pip freeze > requirements.txt

- Для запуска Appium тестов используйте команды:
> cd mw

> pytest -s -v

### Генерация отчетов Allure:

1. Создайте папку, в которую allure будет складывать необходимые для генерации отчета файлы. Например, папка reports в директории проекта.

![image](https://user-images.githubusercontent.com/106829774/235541700-7c61779f-c788-42ee-bc81-b2a0676ee939.png)

2. Для генерации отчета используйте следующую команду:

> pytest --alluredir=reports

- По завершении выполнения тестов выполните команду для формирования отчета на основе имеющихся файлов с результатами:

> allure serve reports
