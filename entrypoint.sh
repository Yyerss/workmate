#!/bin/sh

# Применение миграций базы данных
echo "Applying database migrations..."
python manage.py migrate --noinput

# Запуск Gunicorn
echo "Starting server..."
exec gunicorn config.wsgi:application --bind 0.0.0.0:8000