#!/bin/bash
set -e  # Salir si cualquier comando falla

echo "==== Iniciando pipeline para Dokploy ===="

# Definir el módulo de configuración de Django
export DJANGO_SETTINGS_MODULE=cv_backend.settings
export PYTHONPATH=/app:/app/cv_backend

echo "Verificando estructura del proyecto..."
ls -la /app/

echo "Entrando en el directorio de la aplicación"
cd /app/cv_backend

echo "Verificando contenido del directorio cv_backend..."
ls -la

echo "==== Creando directorio de datos si no existe ===="
mkdir -p /app/cv_backend/data

echo "==== Ejecutando migraciones ===="
python manage.py migrate --noinput

echo "==== Ejecutando collectstatic ===="
python manage.py collectstatic --noinput

echo "==== Ajustando permisos para static y media ===="
# Crear directorios si no existen
mkdir -p static/
mkdir -p media/
mkdir -p data/

chmod -R 755 static/ || true
chmod -R 755 media/ || true
chmod -R 755 data/ || true

echo "Retornando al directorio raíz"
cd /app

echo "==== Ejecutando tareas de post-deploy ===="
if [ -f "post_deploy.py" ]; then
    python post_deploy.py
else
    echo "⚠️ No se encontró post_deploy.py, saltando..."
fi

echo "==== Pipeline completada con éxito ===="
