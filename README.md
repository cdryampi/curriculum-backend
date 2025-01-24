# CV Backend - Proyecto Django

Este es un proyecto Django que sirve como backend para un sistema de currículum en línea. Proporciona una API RESTful para gestionar información personal, proyectos, experiencia laboral, educación, habilidades, comentarios y más.

---

## Tabla de Contenidos

1. [Requisitos Previos](#requisitos-previos)
2. [Configuración del Proyecto](#configuración-del-proyecto)
3. [Estructura del Proyecto](#estructura-del-proyecto)
4. [Configuración de CKEditor 5](#configuración-de-ckeditor-5)
5. [Personalización del Panel de Administración](#personalización-del-panel-de-administración)
6. [Despliegue en Producción](#despliegue-en-producción)

---

## Requisitos Previos

Antes de comenzar, asegúrate de tener instalado lo siguiente:

- **Python 3.8 o superior**.
- **Pipenv** o **pip** para gestionar dependencias.
- **Git** (opcional, para clonar el repositorio).

---

## Configuración del Proyecto

Sigue estos pasos para configurar y ejecutar el proyecto en tu entorno local:

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/tu-usuario/cv_backend.git
   cd cv_backend
   ```
2. **Crear entorno virtual**:
   ```bash
        python -m venv venv
        source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```
3. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Crear archivo `.env`**:
   ```bash
   SECRET_KEY=tu_clave_secreta_aqui
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   URL_SERVER=http://localhost:8000
   RECAPTCHA_PUBLIC_KEY=tu_clave_publica_recaptcha
   RECAPTCHA_PRIVATE_KEY=tu_clave_privada_recaptcha
   ```
5. **Aplicar migraciones**:
   ```bash
   python manage.py migrate
   ```
6. **Ejecutar los comandos de creación de datos de prueba**:
   ```bash
   python manage.py add_users_data
   python manage.py assign_group_permissions
   ```
7. **Iniciar el servidor de desarrollo**:
   ```bash
   python manage.py runserver
   ```

## Estructura del Proyecto

El proyecto está estructurado de la siguiente manera:

```plaintext
cv_backend/
├── base_user/ # Aplicación para gestionar usuarios
├── core/ # Aplicación principal del proyecto con modelos y vistas comunes
├── comments/ # Aplicación para gestionar comentarios **(en desarrollo)**
├── education/ # Aplicación para gestionar educación y formación
├── experience/ # Aplicación para gestionar experiencia laboral
├── projects/ # Aplicación para gestionar proyectos personales
├── skills/ # Aplicación para gestionar habilidades y competencias
├── static/ # Archivos estáticos (CSS, JS, imágenes, etc.)
├── redes_sociales/ # Aplicación para gestionar redes sociales **(en desarrollo)**
├── services/ # Aplicación para gestionar servicios y productos **(en desarrollo)**
├── multimedia_manager/ # Aplicación para gestionar archivos multimedia
├── media/ # Archivos multimedia subidos por los usuarios
├── static_pages/ # Aplicación para gestionar páginas estáticas
├── utils/ # Módulos y funciones de utilidad
```

## Configuración de CKEditor 5

El proyecto utiliza CKEditor 5 para la edición de texto enriquecido en los campos de texto de los modelos. Para configurar CKEditor 5, sigue estos pasos:

```bash
CKEDITOR_5_CONFIGS = {
    'default': {
        'toolbar': ['undo', 'redo', '|', 'heading', '|', 'bold', 'italic', 'strikethrough', 'underline', 'link', 'bulletedList', 'numberedList', '|', 'outdent', 'indent', '|', 'blockQuote', 'insertTable', 'mediaEmbed', 'imageUpload', '|', 'removeFormat', 'sourceEditing'],
        'image': {
            'toolbar': ['imageTextAlternative', '|', 'imageStyle:inline', 'imageStyle:block', 'imageStyle:side']
        },
        'table': {
            'contentToolbar': ['tableColumn', 'tableRow', 'mergeTableCells']
        },
        'simpleUpload': {
            'uploadUrl': 'URL_TO_YOUR_UPLOAD_ENDPOINT',
            'headers': {
                'X-CSRFToken': 'CSRF_TOKEN'
            }
        },
        'height': '400px',
        'width': 'auto',
    }
}
```

## Personalización del Panel de Administración

El panel de administración está personalizado usando Jazzmin. Puedes modificar la configuración en settings.py bajo la clave JAZZMIN_SETTINGS.

```bash
JAZZMIN_SETTINGS = {
    "site_title": "Admin de Mi Currículum",
    "site_header": "Mi Currículum",
    "site_brand": "Mi Currículum",
    "welcome_sign": "Bienvenido al Panel de Administración",
    "search_model": "auth.User",
    "user_avatar": None,
}
```
