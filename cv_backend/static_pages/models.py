from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from multimedia_manager.models import MediaFile
from django.utils.text import slugify
from base_user.models import UserProfile
# Create your models here.
class StaticPage(models.Model):
    """
        Clase que representa a una pagina estatica básica.
    """
    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        verbose_name="Perfil de usuario",
        related_name="paginas_estaticas",
    )
    title = models.CharField(
        max_length=100,
        verbose_name="Título",
        help_text="Añade un título para la página estática."
    )
    slug = models.SlugField(
        unique=True,
        editable=False
    )
    content = CKEditor5Field(
        null=True,
        blank=True,
        verbose_name="Contenido",
        help_text="Añade una descripción principal para la página estatica"
    )
    image = models.ForeignKey(
        MediaFile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='imagen_pagina_estatica',
        verbose_name="Imagen principal para la página estática.",
        help_text="Ingrese la imagen que complemente la descripción."
    )
    publicado = models.BooleanField(
        default=False,
        help_text="Indica si tu página estatica esta publicada.",
        verbose_name="Publicado"
    )

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        # Generar el slug automáticamente si no está establecido
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)