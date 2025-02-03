from django.db import models
from core.models import Tag

from multimedia_manager.models import MediaFile
from django_ckeditor_5.fields import CKEditor5Field
from base_user.models import UserProfile

from django.utils.translation import gettext_lazy as _




class Project(models.Model):
    """
        Modelo que representa a un Proyecto proficional o personal.
    """
    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        verbose_name="Perfil de usuario",
        related_name="proyectos"
    )

    title = models.CharField(
        max_length=200,
        verbose_name="Título",
        help_text="Añade un título a tu proyecto."
    )

    description = CKEditor5Field(
        verbose_name=_("Descripción"),
        help_text=_("Introduce una descripción."),
        null=True,
        blank=True,
        config_name='default'
    )

    start_date = models.DateField(
        verbose_name="Fecha de Inicio"
    )

    end_date = models.DateField(
        null=True,
        blank=True,
        verbose_name="Fecha de Fin"
    )

    link = models.URLField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name="Enlace del Proyecto"
    )

    image = models.ForeignKey(
        MediaFile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Imagen del Proyecto",
        related_name="project_image"
    )

    tags = models.ManyToManyField(
        Tag,
        blank=True,
        verbose_name="Etiquetas"
    )

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"

    def __str__(self):
        return self.title
