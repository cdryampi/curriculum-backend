#!/bin/bash
echo "==== Iniciando pipeline para Dokploy ===="

# Definir el módulo de configuración de Django
export DJANGO_SETTINGS_MODULE=cv_backend.settings
export PYTHONPATH=/app  # Asegurar que Python encuentra el módulo de Django

echo "Entrando en el directorio de la aplicación"
cd /app/cv_backend

echo "==== Ejecutando migraciones ===="
python manage.py migrate --noinput

echo "==== Ejecutando collectstatic ===="
python manage.py collectstatic --noinput

echo "==== Ajustando permisos para static y media ===="
# Crear directorios si no existen
mkdir -p static/
mkdir -p media/

chmod -R 755 static/
chmod -R 755 media/

echo "Retornando al directorio raíz"
cd /app

echo "==== Ejecutando tareas de post-deploy ===="
if [ -f "post_deploy.py" ]; then
    python post_deploy.py
else
    echo "⚠️ No se encontró post_deploy.py, saltando..."
fi

echo "==== Pipeline completada ===="
