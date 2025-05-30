#!/bin/bash
# Script para probar el despliegue localmente antes de enviarlo a Dokploy

echo "🧪 Iniciando prueba local del contenedor..."

# Construir la imagen
echo "📦 Construyendo imagen Docker..."
docker build -t curriculum-backend-test .

if [ $? -ne 0 ]; then
    echo "❌ Error al construir la imagen"
    exit 1
fi

# Ejecutar el contenedor
echo "🚀 Ejecutando contenedor de prueba..."
docker run --rm -p 8000:8000 \
    -e SECRET_KEY=test-secret-key \
    -e DEBUG=True \
    -e ALLOWED_HOSTS=localhost,127.0.0.1 \
    -e URL_SERVER=http://localhost:8000 \
    --name curriculum-test \
    curriculum-backend-test

echo "✅ Prueba completada"
