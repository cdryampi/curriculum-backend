# base_user/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission
from .models import CustomUser, UserProfile

@receiver(post_save, sender=CustomUser)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        if UserProfile.objects.count() == 0:
            UserProfile.objects.create(user=instance)
        
        # Asignar el grupo basado en el rol
        if instance.role == 'admin':
            admin_group, created = Group.objects.get_or_create(name='Admin')
            instance.groups.add(admin_group)
            instance.profile.save()
        elif instance.role == 'guest':
            guest_group, created = Group.objects.get_or_create(name='Guest')
            instance.groups.add(guest_group)
            
            # Asignar permisos al grupo de invitados
            if not instance.is_superuser:
                permissions = [
                    Permission.objects.get(codename='can_create_guest_user_comment'),
                    Permission.objects.get(codename='can_edit_guest_user_comment'),
                    Permission.objects.get(codename='can_delete_guest_user_comment'),
                ]
                guest_group.permissions.add(*permissions)
            else:
                # Si es superusuario, no modifiques sus permisos
                pass
    
    # Guardar el objeto CustomUser solo si se creó un usuario "guest"
    if created and instance.role == 'guest':
        instance.save()