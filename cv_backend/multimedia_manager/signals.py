from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MediaFile

@receiver(post_save, sender=MediaFile)
def generate_media_files(sender, instance, created, **kwargs):
    """
    Signal que genera las versiones de imágenes después de crear un MediaFile.
    """
    if created:  # Solo si es un nuevo objeto
        instance.generate_images()
