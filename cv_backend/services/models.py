from django.db import models
from base_user.models import UserProfile
from django_ckeditor_5.fields import CKEditor5Field
from multimedia_manager.models import MediaFile

class Service(models.Model):
    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name='services'
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Título"
    )
    description = CKEditor5Field(
        verbose_name="Descripción",
        null=True,
        blank=True,
    )
    icon = models.ForeignKey(
        MediaFile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='service_icons',
        verbose_name="Icono"
    )
    active = models.BooleanField(
        default=True,
        verbose_name="Activo"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
