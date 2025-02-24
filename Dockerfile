FROM python:3.12

WORKDIR /app/cv_backend

# Copiar todo el código dentro del contenedor
COPY . /app/

# Instalar dependencias
RUN pip install --no-cache-dir -r /app/cv_backend/requirements.txt

# Asegurar permisos de ejecución para pipeline.sh
RUN chmod +x /app/pipeline.sh

# Exponer puerto para Railway
EXPOSE 8000

# Ejecutar Django + Celery juntos usando un script de inicio
CMD ["/bin/bash", "-c", "/app/pipeline.sh && gunicorn cv_backend.wsgi:application --bind 0.0.0.0:8000 --log-file - & celery -A cv_backend worker --loglevel=info --pool=solo"]
