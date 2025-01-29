# Usa una imagen base con Python
FROM python:3.12

WORKDIR /app

# Copia todo el proyecto
COPY . /app/

# Instala las dependencias desde cv_backend/
RUN pip install --no-cache-dir -r /app/cv_backend/requirements.txt

# Exponer el puerto que Railway usa
EXPOSE 8000

# Ejecutar Gunicorn
CMD ["gunicorn", "cv_backend.cv_backend.wsgi:application", "--bind", "0.0.0.0:8000", "--log-file", "-"]
