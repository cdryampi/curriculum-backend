#!/bin/bash
set -e  # Salir si cualquier comando falla

echo "==== Iniciando aplicación ===="

export DJANGO_SETTINGS_MODULE=cv_backend.settings
export PYTHONPATH=/app:/app/cv_backend

# Usar el puerto proporcionado por el entorno o 8000 por defecto
export PORT=${PORT:-8000}

echo "==== Ejecutando pipeline de inicialización ===="
# Ejecutar el pipeline si no se ha ejecutado ya
if [ ! -f "/app/cv_backend/data/db.sqlite3" ]; then
    echo "Base de datos no encontrada, ejecutando pipeline..."
    bash /app/pipeline.sh
else
    echo "Base de datos encontrada, omitiendo pipeline completo..."
    # Solo ejecutar migraciones por si hay cambios
    cd /app/cv_backend
    python manage.py migrate --noinput || true
    python manage.py collectstatic --noinput || true
fi

echo "==== Cambiando al directorio de la aplicación Django ===="
cd /app/cv_backend

echo "==== Iniciando Gunicorn ===="
exec gunicorn cv_backend.wsgi:application --bind 0.0.0.0:$PORT --log-file - --log-level info
