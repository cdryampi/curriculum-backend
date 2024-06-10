from django.db import models
from base_user.models import UserProfile
from core.models import Tag
from django_ckeditor_5.fields import CKEditor5Field
from multimedia_manager.models import MediaFile


class ExperienciaLaboral(models.Model):

    """
        Modelo que representa a una experiencia laboral pasada, actual o futura.
    """
    
    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        verbose_name="Perfil de usuario",
        related_name="experiencias_laborales"
    )
    empresa = models.CharField(
        max_length=255,
        verbose_name="Empresa",
        help_text="Nombre de la empresa donde trabajaste."
    )
    posicion = models.CharField(
        max_length=255,
        verbose_name="Posición",
        help_text="Cargo o posición que ocupaste."
    )
    descripcion = CKEditor5Field(
        verbose_name="Descripción",
        null=True,
        blank=True,
        config_name='default'
    )
    fecha_inicio = models.DateField(
        verbose_name="Fecha de inicio",
        help_text="Cuándo comenzaste a trabajar aquí."
    )
    fecha_fin = models.DateField(
        null=True,
        blank=True,
        verbose_name="Fecha de fin",
        help_text="Cuándo terminaste de trabajar aquí. Dejar en blanco si aún trabajas aquí."
    )
    ubicacion = models.CharField(
        max_length=255,
        verbose_name="Ubicación",
        help_text="Ciudad o lugar de la empresa."
    )
    logo_empresa = models.ForeignKey(
        MediaFile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='logo_empresa',
        verbose_name="Logo de Empresa",
        help_text="Ingrese la foto del logo de la empresa."
    )
    logo_empresa_fondo = models.ForeignKey(
        MediaFile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='logo_empresa_fondo',
        verbose_name="Logo de Empresa fondo",
        help_text="Ingrese el fondo del logo de la empresa."
    )
    publicado = models.BooleanField(
        default=True,
        verbose_name="Mostrar experiencia",
        help_text= "¿Quieres mostrar esta experiencia laboral?"
    )
    tags = models.ManyToManyField(
        Tag,
        related_name="experiencias",
        blank=True,
        verbose_name="Tags"
    )

    class Meta:
        verbose_name = "Experiencia Laboral"
        verbose_name_plural = "Experiencias Laborales"
        ordering = ['-fecha_inicio'] 
    
    def __str__(self):

        return f"{self.posicion} en {self.empresa}"
