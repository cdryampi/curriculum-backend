FROM python:3.12-slim

# Instalar dependencias necesarias del sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libcairo2-dev \
    pkg-config \
    python3-dev \
    default-libmysqlclient-dev \
    postgresql-client \
    postgresql-server-dev-all \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Directorio de trabajo
WORKDIR /app

# Copiar y preinstalar dependencias
COPY cv_backend/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del proyecto al contenedor
COPY . /app/

# Asegurar permisos a scripts que se ejecutarán en hooks o como entrada
RUN chmod +x /app/pipeline.sh
RUN chmod +x /app/start.sh

# Exponer el puerto en el que corre Gunicorn
EXPOSE 8000

# Comando de inicio (Gunicorn envuelto por tu start.sh)
CMD ["bash", "start.sh"]
