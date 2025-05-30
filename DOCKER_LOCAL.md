# Local Development with Docker Compose

Esta guía describe cómo configurar un entorno de desarrollo local utilizando Docker Compose.

## Requisitos previos

- Docker y Docker Compose instalados en tu máquina local
- Git para clonar el repositorio

## Configuración local

1. Clona el repositorio:
   ```
   git clone <url-del-repositorio>
   cd curriculum-backend
   ```

2. Inicia los contenedores con Docker Compose:
   ```
   docker-compose up -d
   ```

3. Para ejecutar migraciones:
   ```
   docker-compose exec web python cv_backend/manage.py migrate
   ```

4. Para crear un superusuario:
   ```
   docker-compose exec web python cv_backend/manage.py createsuperuser
   ```

5. Accede a la aplicación en:
   - Web: http://localhost:8000
   - Admin: http://localhost:8000/admin

## Solución de problemas comunes

### Error al conectar con la base de datos

Si encuentras errores al conectar con PostgreSQL, asegúrate que:
1. El contenedor de la base de datos está en ejecución: `docker-compose ps`
2. Las variables de entorno en docker-compose.yml son correctas
3. Espera unos segundos después de iniciar los contenedores para que PostgreSQL esté completamente iniciado

### Errores de permisos en archivos media o static

Si tienes problemas con permisos en los volúmenes:
```
docker-compose exec web chmod -R 755 cv_backend/static/
docker-compose exec web chmod -R 755 cv_backend/media/
```

## Comandos útiles

- Ver logs: `docker-compose logs -f`
- Detener contenedores: `docker-compose down`
- Reconstruir la imagen: `docker-compose build`
- Ejecutar un comando Django: `docker-compose exec web python cv_backend/manage.py <comando>`
