#!/bin/bash
export DJANGO_SETTINGS_MODULE=cv_backend.settings

# Usar el puerto proporcionado por el entorno o 8000 por defecto
export PORT=${PORT:-8000}

# Cambiar al directorio de la aplicación Django
cd /app/cv_backend

# Iniciar Gunicorn
gunicorn cv_backend.wsgi:application --bind 0.0.0.0:$PORT --log-file -
