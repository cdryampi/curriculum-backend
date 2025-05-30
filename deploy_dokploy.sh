#!/bin/bash
# Script para facilitar el despliegue con Dokploy

# Colores para output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${GREEN}=== Iniciando despliegue a Dokploy ===${NC}"

# Verificar instalación de Dokploy CLI
if ! command -v dokploy &> /dev/null; then
    echo -e "${RED}Error: dokploy-cli no está instalado.${NC}"
    echo -e "Instálalo con: ${YELLOW}npm install -g dokploy-cli${NC}"
    exit 1
fi

# Configurar variables
echo -e "${GREEN}Configurando variables de entorno...${NC}"
# Estas variables pueden ser establecidas automáticamente por Dokploy o definidas aquí
export REGISTRY_URL=${REGISTRY_URL:-"your-registry-url"}
export IMAGE_NAME=${IMAGE_NAME:-"curriculum-backend"}
export IMAGE_TAG=${IMAGE_TAG:-"latest"}
export APP_DOMAIN=${APP_DOMAIN:-"your-app-domain.com"}

# Construir la imagen
echo -e "${GREEN}Construyendo imagen Docker...${NC}"
docker build -t $REGISTRY_URL/$IMAGE_NAME:$IMAGE_TAG .

if [ $? -ne 0 ]; then
    echo -e "${RED}Error al construir la imagen Docker.${NC}"
    exit 1
fi

# Publicar la imagen
echo -e "${GREEN}Publicando imagen a $REGISTRY_URL...${NC}"
docker push $REGISTRY_URL/$IMAGE_NAME:$IMAGE_TAG

if [ $? -ne 0 ]; then
    echo -e "${RED}Error al publicar la imagen Docker.${NC}"
    exit 1
fi

# Desplegar con Dokploy
echo -e "${GREEN}Desplegando aplicación con Dokploy...${NC}"
dokploy deploy

if [ $? -ne 0 ]; then
    echo -e "${RED}Error al desplegar la aplicación.${NC}"
    exit 1
fi

echo -e "${GREEN}=== Despliegue completado con éxito ===${NC}"
echo -e "La aplicación estará disponible en: ${YELLOW}https://$APP_DOMAIN${NC}"
