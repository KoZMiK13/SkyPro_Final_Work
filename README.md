# SkyPro_Final_Work
Дипломная работа. Архитектура фреймворка

# Проект автоматизации тестирования сайта [Delivery](https://market-delivery.yandex.ru/)

## Задача 
Автоматизация UI и API тестов для сайта [Delivery](https://market-delivery.yandex.ru/)

## Структура проекта
- 'README.md' - описание структуры проектв.
- 'requirements.txt' - список зависимостей
- 'test_API.py' - API тесты
- 'test_UI.py' - UI тесты
- 'Pages' - папка с методами для UI тестов
    - 'MainPage.py' - содержит класс MainPage для работы с главной страницей сайта [Delivery](https://market-delivery.yandex.ru/)
- 'API' - папка с методами для API тестов
    'DeliveryAPI.py' - содержит класс DeliveryAPI для работы с API 
- 'run.sh' - файл для автоматизированного запуска тестов и формирования отчетов с сохранением истории тестирования

## Запуск тестов
- запуск только API тестов: 'python -m pytest -s test_API.py'
- запуск только UI тестов: 'python -m pytest -s test_UI.py'
- запуск всех тестов: 'python -m pytest -s'

## Запуск тестов и формирование отчетов
- запуск только API тестов с формированием отдельного отчета: `python -m pytest --alluredir allure-UI_result test_UI.py`
- запуск только UI тестов с формированием отдельного отчета: `python -m pytest --alluredir allure-API_result test_API.py`
- запуск всех тестов с формированием общего отчета: `python -m pytest --alluredir allure-ALL_result`

## Открытие отчетов
- открытие отчета по результатам API тестирования - `allure serve allure-API_result`
- открытие отчета по результатам UI тестирования - `allure serve allure-UI_result`
- открытие отчета по результатам общего тестирования - `allure serve allure-ALL_result`

## Запуск тестов, формирование и открытие общего отчета 
- Запуск тестов, формирование и открытие общего отчета с сохранением истории тестирования - `.run.sh`

### Найденные баги
- Ошибка "статус код 400" не отображается в запросе API при отправке поискового запроса с несуществующей системой координат  

