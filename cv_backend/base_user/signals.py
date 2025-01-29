from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission
from .models import CustomUser, UserProfile
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=CustomUser)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Crea o actualiza el perfil de usuario y asigna grupos y permisos basados en el rol.
    """
    # Crear perfil si no existe
    if created:
        # Si no hay un perfil asociado al usuario, crear uno
        UserProfile.objects.get_or_create(user=instance)

        # Asignar grupos basados en el rol del usuario
        if instance.role == 'admin':
            # Crear o recuperar el grupo "Admin"
            admin_group, _ = Group.objects.get_or_create(name='Admin')
            instance.groups.add(admin_group)

        elif instance.role == 'guest':
            # Crear o recuperar el grupo "Guest"
            guest_group, _ = Group.objects.get_or_create(name='Guest')
            instance.groups.add(guest_group)

            # Asignar permisos al grupo de invitados (si no es superusuario)
            if not instance.is_superuser:
                # Lista de permisos requeridos para el grupo "Guest"
                permissions = [
                    'can_create_guest_user_comment',
                    'can_edit_guest_user_comment',
                    'can_delete_guest_user_comment',
                ]
                # Iterar sobre los permisos y asignarlos al grupo
                for perm_codename in permissions:
                    try:
                        permission = Permission.objects.get(codename=perm_codename)
                        guest_group.permissions.add(permission)
                    except Permission.DoesNotExist:
                        # Registro de advertencia si el permiso no existe
                        print(f"Warning: Permission with codename '{perm_codename}' does not exist.")

    # Actualizar perfil existente si es necesario
    else:
        if hasattr(instance, 'profile'):
            instance.profile.save()

@receiver(post_save, sender=CustomUser)
def create_auth_token(sender, instance, created, **kwargs):
    """
    Crea un token de autenticación para el usuario.
    """
    if created:
        Token.objects.create(user=instance)