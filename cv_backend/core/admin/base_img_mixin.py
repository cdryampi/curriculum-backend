from django.db.models import Q
from multimedia_manager.models import MediaFile

def filter_logo_queryset(model_name, model_id):
    queryset = MediaFile.objects.all()

    model_fields = {
        'UserProfile': 'foto_perfil',
        'StaticPage': 'imagen_pagina_estatica',
        'Skill': 'logo_skill',
        'Service': 'service_icons',
        'Project': 'project_image',
        'Meta': ['favicons', 'page_icons'],
        'ExperienciaLaboral': ['logo_empresa', 'logo_empresa_fondo'],
    }

    # Obtener campos específicos para el modelo
    fields = model_fields.get(model_name, [])

    # Añadir condiciones de filtrado basadas en los campos específicos
    if isinstance(fields, list):
        # Combinamos todas las condiciones con AND para cada campo relacionado
        q_objects = Q()
        for field in fields:
            q_objects &= (Q(**{f'{field}__id': model_id}) | Q(**{f'{field}__isnull': True}))
        queryset = queryset.filter(q_objects)
    else:
        # Aplicar filtro para un solo campo
        queryset = queryset.filter(
            Q(**{f'{fields}__id': model_id}) | Q(**{f'{fields}__isnull': True})
        )

    # Excluir campos no relacionados
    exclude_fields = []
    for key, value in model_fields.items():
        if key != model_name:
            if isinstance(value, list):
                exclude_fields.extend(value)
            else:
                exclude_fields.append(value)
    
    for field in exclude_fields:
        queryset = queryset.exclude(**{f'{field}__isnull': False})

    return queryset
