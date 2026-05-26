# Integración de ChatGPT con GPT Actions para la Gestión de CV

Esta documentación describe cómo integrar tu **Custom GPT privado** de ChatGPT con el backend de tu CV para permitir consultas y modificaciones (CRUD) en tiempo real de tus datos profesionales mediante lenguaje natural.

---

## 1. Arquitectura y Seguridad

- **URL Base**: `/gpt-actions/`
- **Autenticación**: Cabecera `Authorization: Bearer <token>`
- **Aislamiento Estricto (Ownership)**: La API asocia automáticamente todas las lecturas y escrituras al `UserProfile` del usuario autenticado vía token. No es posible leer ni modificar datos de otros perfiles; de intentarse, el servidor responderá con código HTTP `404 Not Found` para proteger la privacidad.
- **Campos Seguros**: No se exponen subidas de archivos ni campos de administración del sistema. Los campos se limitan a datos de texto, fechas y números.
- **Estrategia de Borrado (DELETE)**:
  - **Experiencia Laboral**: Realiza un **soft delete** (marcando `publicado = False` en lugar de eliminar el registro físico de la base de datos).
  - **Proyectos, Educación, Skills y Cursos**: Realizan un **hard delete** (eliminación física permanente de la base de datos).

---

## 2. Cómo Obtener tu Token de Autenticación

El backend utiliza el sistema nativo `rest_framework.authtoken` de Django REST Framework. Tienes dos maneras de obtener o generar tu Token:

### Método A: Desde el Panel de Administración de Django
1. Accede al panel de administración de Django (ej. `https://backend.yampi.eu/admin/`).
2. Ve a la sección **Tokens** (bajo "AUTH TOKEN").
3. Haz clic en **Añadir Token**, selecciona tu usuario y guarda.
4. Copia la cadena alfanumérica generada (por ejemplo, `9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b`).

### Método B: Desde la Consola de Django (Django Shell)
Si tienes acceso a la terminal del servidor, puedes generarlo ejecutando:
```bash
python manage.py shell
```
Dentro de la consola interactiva de Python:
```python
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()
user = User.objects.get(username="tu_usuario")  # Reemplaza con tu usuario administrador
token, created = Token.objects.get_or_create(user=user)
print("Tu Token es:", token.key)
```

---

## 3. Configuración de la Action en ChatGPT

Para configurar tu Custom GPT privado con estas acciones, sigue estos pasos:

1. Ve a [ChatGPT](https://chatgpt.com) y selecciona **Explore GPTs** -> **Create a GPT** (o edita uno existente).
2. En la pestaña **Configure**, añade el nombre, descripción e instrucciones básicas.
3. Haz clic en **Create new action** (Crear nueva acción) en la parte inferior.
4. Configura los siguientes parámetros:
   - **Authentication** (Autenticación):
     - **Type**: `API Key`
     - **Auth Type**: `Bearer`
     - **API Key**: *[Pega el Token que obtuviste en el paso anterior]*
   - **Schema**:
     - Selecciona **Import from URL** y proporciona `https://tu-dominio.com/gpt-actions/schema/` o copia y pega el contenido completo de `curriculum-backend/docs/gpt-actions-openapi.yaml` directamente en el editor.
5. Guarda la Action. Asegúrate de configurar la visibilidad de tu Custom GPT a **Only me** (Solo yo) o **Only people with a link** (Solo personas con el enlace) para mantener tu token y acceso completamente privado.

---

## 4. Instrucciones del Sistema recomendadas para el Custom GPT

Copia y pega el siguiente bloque de instrucciones en la pestaña **Instructions** del editor de tu Custom GPT:

```txt
Eres el gestor privado del CV de Yampi. Tu propósito es ayudar al usuario a leer y modificar los datos profesionales de su currículum mediante lenguaje natural a través de las acciones API proporcionadas.

Sigue rigurosamente estas pautas operativas:
1. Usa las acciones exclusivamente para leer o modificar datos del CV.
2. Antes de realizar cualquier acción de escritura (crear, actualizar o borrar registros), resume de forma clara y concisa el cambio exacto que vas a realizar y solicita confirmación explícita del usuario.
3. No inventes fechas, empresas, tecnologías, ni identificadores (IDs).
4. Cuando tengas que modificar o borrar un elemento existente (por ejemplo, una experiencia laboral, skill o proyecto), primero realiza una llamada de listado (GET) para identificar el registro correcto y su correspondiente ID numérico.
5. Después de realizar una modificación exitosa, vuelve a consultar el recurso afectado para confirmar visualmente el resultado y reporta el cambio al usuario.
6. El formato obligatorio para todos los campos de tipo fecha es estrictamente YYYY-MM-DD (por ejemplo, 2024-01-15). Transforma cualquier fecha relativa o difusa que te indique el usuario a este formato antes de enviarla.
7. No intentes modificar campos de archivos multimedia, logos, PDFs o campos que no estén explícitamente expuestos en el schema OpenAPI.
```

---

## 5. Endpoints Disponibles

| Método | Endpoint | Acción | Operación OpenAPI (`operationId`) |
| :--- | :--- | :--- | :--- |
| **GET** | `/gpt-actions/profile/` | Leer perfil | `getProfile` |
| **PATCH** | `/gpt-actions/profile/` | Actualizar perfil | `updateProfile` |
| **GET** | `/gpt-actions/experiences/` | Listar experiencias | `listExperiences` |
| **POST** | `/gpt-actions/experiences/` | Crear experiencia | `createExperience` |
| **GET** | `/gpt-actions/experiences/{id}/` | Detalle experiencia | `getExperience` |
| **PATCH** | `/gpt-actions/experiences/{id}/` | Actualizar experiencia | `updateExperience` |
| **DELETE** | `/gpt-actions/experiences/{id}/` | Soft delete experiencia | `deleteExperience` |
| **GET** | `/gpt-actions/projects/` | Listar proyectos | `listProjects` |
| **POST** | `/gpt-actions/projects/` | Crear proyecto | `createProject` |
| **GET** | `/gpt-actions/projects/{id}/` | Detalle proyecto | `getProject` |
| **PATCH** | `/gpt-actions/projects/{id}/` | Actualizar proyecto | `updateProject` |
| **DELETE** | `/gpt-actions/projects/{id}/` | Hard delete proyecto | `deleteProject` |
| **GET** | `/gpt-actions/education/` | Listar educación | `listEducation` |
| **POST** | `/gpt-actions/education/` | Crear educación | `createEducation` |
| **GET** | `/gpt-actions/education/{id}/` | Detalle educación | `getEducation` |
| **PATCH** | `/gpt-actions/education/{id}/` | Actualizar educación | `updateEducation` |
| **DELETE** | `/gpt-actions/education/{id}/` | Hard delete educación | `deleteEducation` |
| **GET** | `/gpt-actions/skills/` | Listar habilidades | `listSkills` |
| **POST** | `/gpt-actions/skills/` | Crear habilidad | `createSkill` |
| **GET** | `/gpt-actions/skills/{id}/` | Detalle habilidad | `getSkill` |
| **PATCH** | `/gpt-actions/skills/{id}/` | Actualizar habilidad | `updateSkill` |
| **DELETE** | `/gpt-actions/skills/{id}/` | Hard delete habilidad | `deleteSkill` |
| **GET** | `/gpt-actions/courses/` | Listar cursos | `listCourses` |
| **POST** | `/gpt-actions/courses/` | Crear curso | `createCourse` |
| **GET** | `/gpt-actions/courses/{id}/` | Detalle curso | `getCourse` |
| **PATCH** | `/gpt-actions/courses/{id}/` | Actualizar curso | `updateCourse` |
| **DELETE** | `/gpt-actions/courses/{id}/` | Hard delete curso | `deleteCourse` |
| **GET** | `/gpt-actions/schema/` | Obtener el OpenAPI YAML | *(Público, para importación)* |
