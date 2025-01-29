#!/bin/bash
echo "==== Iniciando pipeline ===="

echo "Entrado en el directorio de la aplicación"

if [ -d "cv_backend" ]; then
    cd cv_backend
fi

echo "==== Ejecutando migraciones ===="

python manage.py migrate --noinput

echo "==== Ejecutando collectstatic ===="

python manage.py collectstatic --noinput

echo "==== Ajustando permisos para static y media ===="

chmod -R 755 static/
chmod -R 755 media/

echo "retornando al directorio raíz"

cd ..

echo "==== Ejecutando tareas de post-deploy ===="

if [ -f "post_deploy.py" ]; then
    python post_deploy.py
else
    echo "⚠️ No se encontró post_deploy.py, saltando..."
fi

echo "==== Pipeline completada ===="
echo "==== Iniciando servidor ===="