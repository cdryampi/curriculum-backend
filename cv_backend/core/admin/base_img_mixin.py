from django.db.models import Q
from multimedia_manager.models import MediaFile

def filter_logo_queryset(model_name, model_id=None, user=None):
    """
    Filtra el queryset de MediaFile basado en el modelo relacionado, el ID del modelo,
    y el usuario autenticado.
    """
    queryset = MediaFile.objects.all()

    # Define los campos relacionados para cada modelo
    model_fields = {
        'UserProfile': 'foto_perfil',  # Relación inversa hacia UserProfile
        'CustomUser': 'foto_perfil_invitado',
        'StaticPage': 'imagen_pagina_estatica',
        'Skill': 'logo_skill',
        'Service': 'service_icons',
        'Project': 'project_image',
        'Meta': ['favicons', 'page_icons'],
        'ExperienciaLaboral': ['logo_empresa', 'logo_empresa_fondo'],
    }

    # Obtén el campo relacionado para el modelo especificado
    fields = model_fields.get(model_name)
    if not fields:
        print(f"Modelo {model_name} no definido en model_fields.")
        return MediaFile.objects.none()

    # Aplica el filtro basado en el modelo y sus campos relacionados
    if isinstance(fields, list):
        query = Q()
        for field in fields:
            query |= Q(**{f'{field}__id': model_id})
    else:
        query = Q(**{f'{fields}__id': model_id})

    # Filtra el queryset inicial con la relación definida
    print(f"Aplicando query: {query}")
    queryset = queryset.filter(query)

    # Filtrar por usuario autenticado (si aplica)
    if user and user.is_authenticated:
        queryset = queryset.filter(creado_por=user)

    print(f"Queryset final: {queryset}")
    return queryset

