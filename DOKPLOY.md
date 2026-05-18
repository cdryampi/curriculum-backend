# Curriculum Backend - Dokploy Deployment Guide (SQLite)

Este repositorio contiene el backend para un sistema de gestión de currículum vitae, adaptado para ser desplegado con Dokploy usando SQLite como base de datos.

## Requisitos previos

- Cuenta en Dokploy
- Docker instalado localmente (para pruebas)
- Acceso a un registro de contenedores (Container Registry)

## Variables de entorno necesarias

La aplicación requiere las siguientes variables de entorno:

```
SECRET_KEY=tu_clave_secreta
DEBUG=False
URL_SERVER=https://backend.yampi.eu
ALLOWED_HOSTS=backend.yampi.eu,localhost,127.0.0.1
PUBLIC_PROFILE_USERNAME=tu_usuario_publico
CORS_ALLOWED_ORIGINS=https://cdryampi.github.io,https://yampi.eu,https://www.yampi.eu
CORS_ALLOW_ALL_ORIGINS=False
CSRF_TRUSTED_ORIGINS=https://backend.yampi.eu,https://cdryampi.github.io,https://yampi.eu,https://www.yampi.eu
CONTACT_THROTTLE_RATE=5/hour

# Configuración de reCAPTCHA
RECAPTCHA_PUBLIC_KEY=tu_clave_publica_recaptcha
RECAPTCHA_PRIVATE_KEY=tu_clave_privada_recaptcha

# Configuración de correo electrónico
EMAIL_HOST=smtp.proveedor.com
EMAIL_PORT=587
EMAIL_HOST_USER=tu@email.com
EMAIL_HOST_PASSWORD=tu_contraseña
DEFAULT_FROM_EMAIL=tu@email.com

# Opcional: directorio personalizado para la base de datos SQLite
DB_DIR=/app/cv_backend/data
```

## Diferencias con PostgreSQL

Esta configuración utiliza SQLite en lugar de PostgreSQL:

- ✅ **Ventajas**: Más simple, no requiere servidor de base de datos separado
- ⚠️ **Limitaciones**: No recomendado para alta concurrencia, un solo archivo de BD
- 📦 **Persistencia**: Se utiliza un volumen persistente para mantener los datos

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
- `pipeline.sh`: Script que configura la aplicación durante el primer arranque
- `start.sh`: Script que inicia la aplicación y ejecuta el pipeline si es necesario
- `post_deploy.py`: Script que ejecuta tareas de post-despliegue

## Volúmenes persistentes

La aplicación utiliza tres volúmenes persistentes:

- `app-data`: Para la base de datos SQLite y datos de aplicación (500Mi)
- `media-files`: Para archivos multimedia subidos por los usuarios (2Gi)
- `static-files`: Para archivos estáticos de la aplicación (1Gi)

## Monitoreo de salud

Dokploy monitoreará la salud de la aplicación accediendo a la ruta `/admin/login/`.

## Pruebas locales

Antes de desplegar a Dokploy, puedes probar localmente:

```bash
# En Windows (PowerShell)
.\test_local.sh

# En Unix/Linux/macOS
bash test_local.sh
```

## Migración desde PostgreSQL

Si vienes de una configuración con PostgreSQL:

1. Exporta tus datos: `python manage.py dumpdata > datos.json`
2. Cambia la configuración a SQLite
3. Ejecuta migraciones: `python manage.py migrate`
4. Importa datos: `python manage.py loaddata datos.json`

## Soporte

Para cualquier problema o consulta, por favor crea un issue en este repositorio.
