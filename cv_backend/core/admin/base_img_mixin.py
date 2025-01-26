from django.db.models import Q
from multimedia_manager.models import MediaFile


def filter_logo_queryset(model_name, model_id=None, user=None):
    """
    Filtra el queryset de MediaFile basado en:
    - El modelo relacionado (`model_name`).
    - El ID del modelo relacionado (`model_id`).
    - El usuario autenticado (`user`).
    """
    if not user or not user.is_authenticated:
        print("El usuario no está autenticado. Retornando queryset vacío.")
        return MediaFile.objects.none()

    # Define los campos relacionados para cada modelo
    model_fields = {
        'UserProfile': 'foto_perfil',
        'CustomUser': 'foto_perfil_invitado',
        'StaticPage': 'imagen_pagina_estatica',
        'Skill': 'logo_skill',
        'Service': 'service_icons',
        'Project': 'project_image',
        'Meta': ['favicons', 'page_icons'],
        'ExperienciaLaboral': ['logo_empresa', 'logo_empresa_fondo'],
    }

    # Verifica que el modelo esté definido en los campos
    fields = model_fields.get(model_name)
    if not fields:
        print(f"Modelo {model_name} no está definido en los campos relacionados.")
        return MediaFile.objects.none()

    # Filtra por los archivos creados por el usuario
    queryset = MediaFile.objects.filter(creado_por=user)
    print(f"Queryset inicial filtrado por usuario: {queryset}")

    # Aplica el filtro basado en el modelo relacionado
    if model_id:
        if isinstance(fields, list):
            # Para modelos con múltiples relaciones
            query = Q()
            for field in fields:
                query |= Q(**{f"{field}__id": model_id})
        else:
            # Para un único campo relacionado
            query = Q(**{f"{fields}__id": model_id})

        print(f"Query generado: {query}")
        queryset = queryset.filter(query)
        print(f"Queryset después de aplicar el filtro del modelo: {queryset}")
    else:
        print("model_id es None. No se aplicará filtro adicional.")

    return queryset
