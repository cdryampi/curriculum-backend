import os
from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from django.core.cache import cache
from django.conf import settings
from multimedia_manager.models import MediaFile
from multimedia_manager.tasks import generate_images_task

@receiver(pre_save, sender=MediaFile)
def eliminar_imagenes_antes_actualizacion(sender, instance, **kwargs):
    """
    Antes de actualizar una imagen, eliminamos la versión anterior.
    """
    if instance.pk:  # Solo si el objeto ya existe
        try:
            old_instance = MediaFile.objects.get(pk=instance.pk)

            # Si el archivo cambió, eliminamos las versiones anteriores
            if old_instance.file and old_instance.file != instance.file:
                eliminar_imagenes_de_cache(old_instance)

                paths = [
                    old_instance.image_for_pc.path if old_instance.image_for_pc else None,
                    old_instance.image_for_tablet.path if old_instance.image_for_tablet else None,
                    old_instance.image_for_mobile.path if old_instance.image_for_mobile else None,
                    old_instance.file.path if old_instance.file else None
                ]

                for path in paths:
                    if path and os.path.exists(path):
                        os.remove(path)
                        print(f"🗑️ Eliminado: {path}")

        except MediaFile.DoesNotExist:
            pass  # Si no existe, no hay nada que borrar


@receiver(post_save, sender=MediaFile)
def generar_imagenes_post_save(sender, instance, created, **kwargs):
    """
    Lanza la tarea de Celery después de guardar la imagen.
    """
    if created or instance.file:  # Si es nuevo o si la imagen cambió
        generate_images_task(instance.id)


@receiver(post_delete, sender=MediaFile)
def eliminar_imagenes_post_delete(sender, instance, **kwargs):
    """
    Elimina los archivos físicos cuando se borra el objeto.
    """
    paths = [
        instance.image_for_pc.path if instance.image_for_pc else None,
        instance.image_for_tablet.path if instance.image_for_tablet else None,
        instance.image_for_mobile.path if instance.image_for_mobile else None,
        instance.file.path if instance.file else None
    ]

    for path in paths:
        if path and os.path.exists(path):
            os.remove(path)
            
    print(f"✅ Imágenes eliminadas para MediaFile {instance.id}")


def eliminar_imagenes_de_cache(instance):
    """
    Elimina los archivos en caché cuando se actualiza o borra una imagen.
    """
    cache_keys = [
        f"mediafile:{instance.id}:pc",
        f"mediafile:{instance.id}:tablet",
        f"mediafile:{instance.id}:mobile"
    ]

    for key in cache_keys:
        cache.delete(key)

    print(f"🧹 Caché eliminada para MediaFile {instance.id}")
