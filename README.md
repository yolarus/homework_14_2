# Домашняя работа №16, урок 14.1.

## Описание
1. В классе Category атрибут products стал приватным, добавлены геттеры для получения списка продуктов в виде строки и списка, также добавлен метод для добавления нового продукта add_product
2. В классе Product атрибут price стал приватным, добавлены геттер и сеттер атрибута, также добавлен метод создания нового продукта new_product
3. Выполнено тестирование новых методов и корректировка старых тестов
4. Скорректирован файл README.md 
5. Выполнена проверка mypy и flake8

## Установка проекта
Клонирование проекта из [GitHub](https://github.com/yolarus/homework_14_2) по HTTPS-токену или SSH-ключу

## Запуск
~ python3 main.py

## Установка зависимостей
1. Перейти в настройки Pycharm -> Setting -> Project -> Python Interpreter 
2. Добавить локальный интерпретатор с менеджером пакетов Poetry
3. Выполнить команду в терминале PyCharm 'poetry install'

## Тестирование
1. Тесты находятся в директории "tests", запуск осуществляется командой
'pytest'. Тесты покрывают 100 % кода. 