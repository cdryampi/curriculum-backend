FROM python:3.12

WORKDIR /app/cv_backend

COPY . /app/

RUN pip install --no-cache-dir -r /app/cv_backend/requirements.txt

# Asegurar que pipeline.sh está en la imagen
RUN ls -l /app/cv_backend/  # Esto mostrará el contenido en Railway logs

# Asegurar permisos de ejecución para pipeline.sh
RUN chmod +x /app/pipeline.sh

# Ejecutar el pipeline antes de arrancar Gunicorn
RUN /app/pipeline.sh

EXPOSE 8000

CMD ["gunicorn", "cv_backend.wsgi:application", "--bind", "0.0.0.0:8000", "--log-file", "-"]
