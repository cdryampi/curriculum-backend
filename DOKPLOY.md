# Curriculum Backend - Dokploy Deployment Guide

Este repositorio contiene el backend para un sistema de gestión de currículum vitae, adaptado para ser desplegado con Dokploy.

## Requisitos previos

- Cuenta en Dokploy
- Docker instalado localmente (para pruebas)
- Acceso a un registro de contenedores (Container Registry)

## Variables de entorno necesarias

La aplicación requiere las siguientes variables de entorno:

```
SECRET_KEY=tu_clave_secreta
DEBUG=False
URL_SERVER=https://tu-dominio.com
ALLOWED_HOSTS=tu-dominio.com,www.tu-dominio.com
DATABASE_URL=postgres://usuario:contraseña@host:puerto/nombre_bd
RECAPTCHA_PUBLIC_KEY=tu_clave_publica_recaptcha
RECAPTCHA_PRIVATE_KEY=tu_clave_privada_recaptcha
EMAIL_HOST=smtp.proveedor.com
EMAIL_PORT=587
EMAIL_HOST_USER=tu@email.com
EMAIL_HOST_PASSWORD=tu_contraseña
```

## Despliegue con Dokploy

1. Asegúrate de tener instalada la CLI de Dokploy:
   ```
   npm install -g dokploy-cli
   ```

2. Inicia sesión en Dokploy:
   ```
   dokploy login
   ```

3. Construye la imagen y despliega la aplicación:
   ```
   dokploy deploy
   ```

## Estructura del proyecto

- `Dockerfile`: Configuración para construir la imagen del contenedor
- `dokploy.yaml`: Configuración para el despliegue en Dokploy
- `pipeline.sh`: Script que se ejecuta durante el despliegue para configurar la aplicación
- `start.sh`: Script que inicia la aplicación
- `post_deploy.py`: Script que ejecuta tareas de post-despliegue

## Volúmenes persistentes

La aplicación utiliza dos volúmenes persistentes:

- `media-files`: Para archivos multimedia subidos por los usuarios
- `static-files`: Para archivos estáticos de la aplicación

## Monitoreo de salud

Dokploy monitoreará la salud de la aplicación accediendo a la ruta `/admin/login/`.

## Escalado

La aplicación está configurada para escalar automáticamente entre 1 y 2 instancias según la carga.

## Soporte

Para cualquier problema o consulta, por favor crea un issue en este repositorio.
