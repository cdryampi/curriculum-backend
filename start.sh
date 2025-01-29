#!/bin/bash
export DJANGO_SETTINGS_MODULE=cv_backend.settings
export PORT=${PORT:-8000}  # Usa el puerto de Railway o 8000 por defecto

pip install --no-cache-dir -r requirements.txt
gunicorn cv_backend.wsgi:application --bind 0.0.0.0:$PORT --log-file -