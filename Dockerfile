FROM python:3.12-slim

# Instalar dependencias necesarias
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libcairo2-dev \
    pkg-config \
    python3-dev \
    default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copiar archivos de requisitos primero para aprovechar la caché de Docker
COPY cv_backend/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de los archivos
COPY . /app/

# Asegurar permisos de ejecución para scripts
RUN chmod +x /app/pipeline.sh
RUN chmod +x /app/start.sh

# Exponer el puerto que utilizará la aplicación
EXPOSE 8000

# No ejecutamos el pipeline aquí ya que Dokploy tiene su propio ciclo de vida
# En su lugar, lo manejaremos en dokploy.yaml

# Usar el script de inicio como punto de entrada
CMD ["bash", "start.sh"]
