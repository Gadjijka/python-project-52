#!/usr/bin/env bash
# Выход при ошибке
set -o errexit

# Установка зависимостей с помощью poetry
poetry install

# Применение миграций
python manage.py migrate

# Компиляция сообщений для локалей
python manage.py compilemessage
