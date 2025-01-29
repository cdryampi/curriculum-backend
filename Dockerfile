FROM python:3.12

WORKDIR /app/cv_backend  # Ajusta si es necesario

COPY . /app/

RUN pip install --no-cache-dir -r /app/cv_backend/requirements.txt

EXPOSE 8000

CMD ["gunicorn", "cv_backend.wsgi:application", "--bind", "0.0.0.0:8000", "--log-file", "-"]
