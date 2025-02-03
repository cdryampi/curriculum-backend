from django.db import models
from base_user.models import UserProfile
from django_ckeditor_5.fields import CKEditor5Field
from multimedia_manager.models import MediaFile
from utils.utils import truncate_html_content
from core.models import Tag

class Education(models.Model):
    """
        Clase que representa a una formación en una institución.
    """
    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name='education'
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Título",
        help_text="Título del grado o curso formal."
    )
    subtitle = models.CharField(
        max_length=255,
        verbose_name="Subtítulo",
        help_text="Subtítulo del grado o curso formal (por ejemplo, licenciatura, maestría).",
        null=True,
        blank=True
    )
    institution = models.CharField(
        max_length=255,
        verbose_name="Institución",
        help_text="Nombre de la institución educativa."
    )
    start_year = models.PositiveIntegerField(
        verbose_name="Año de Inicio",
        help_text="Año en que se inició el grado o curso."
    )
    end_year = models.PositiveIntegerField(
        verbose_name="Año de Finalización",
        help_text="Año en que se completó el grado o curso. Deja en blanco si todavía estás cursando.",
        null=True,
        blank=True
    )
    description = CKEditor5Field(
        verbose_name="Descripción",
        help_text="Descripción detallada de la educación formal.",
        null=True,
        blank=True,
        config_name='default'
    )
    tags = models.ManyToManyField(
        Tag,
        related_name="destacados",
        blank=True,
        verbose_name="Tags"
    )
    @property
    def get_short_description_preview(self):

        return truncate_html_content(self.description, 10)
            
    class Meta:
        verbose_name = "Educación"
        verbose_name_plural = "Educaciones"
        ordering = ['-end_year']

    def __str__(self):
        return f"{self.title} - {self.institution}"

class Skill(models.Model):
    """
        Clase que representa a una habilidad.
    """
    CATEGORY_CHOICES = [

        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('mobile', 'Mobile'),
        ('sysadmin', 'Sysadmin'),
        ('office', 'Ofimática'),
        ('other', 'Otros'),

    ]

    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name='skills'
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Título",
        help_text="Título de la habilidad (por ejemplo, Python, Comunicación)."
    )
    logo = models.ForeignKey(
        MediaFile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='logo_skill',
        verbose_name="Imagen del logo",
        help_text="Ingrese la imagen de la skill."
    )
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        verbose_name="Categoría",
        help_text="Selecciona la categoría de la habilidad (por ejemplo, Frontend, Backend)."
    )
    proficiency = models.PositiveIntegerField(
        verbose_name="Porcentaje de Maestría",
        help_text="Porcentaje de maestría en la habilidad (por ejemplo, 85%)."
    )

    class Meta:
        verbose_name = "Habilidad"
        verbose_name_plural = "Habilidades"
    
    @property
    def get_category_readable(self):
        return dict(self.CATEGORY_CHOICES).get(
            self.category, 'categoría no encontrada'
        )
    
    def __str__(self):
        return self.title

class Course(models.Model):
    """
        Modelo que representa un Curso no formal o semiformal.
    """
    PLATFORM_CHOICES = [
        ('Udemy', 'Udemy'),
        ('Platzi', 'Platzi'),
        ('OPENWEBINARS', 'OPENWEBINARS'),
        ('SEPE', 'SEPE'),
    ]

    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name='courses'
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Título",
        help_text="Título del curso no formal."
    )
    platform = models.CharField(
        max_length=255,
        choices=PLATFORM_CHOICES,
        verbose_name="Plataforma",
        help_text="Nombre de la plataforma donde se impartió el curso (por ejemplo, Udemy, Coursera)."
    )
    completion_year = models.PositiveIntegerField(
        verbose_name="Año de Finalización",
        help_text="Año en que se completó el curso."
    )
    certificate_url = models.URLField(
        verbose_name="URL del Certificado",
        help_text="URL del certificado del curso (si aplica).",
        null=True,
        blank=True
    )
    description = CKEditor5Field(
        verbose_name="Descripción",
        help_text="Descripción breve del curso.",
        null=True,
        blank=True,
        config_name='default'
    )

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
    
    @property
    def get_platform_readable(self):
        return dict(self.PLATFORM_CHOICES).get(
            self.platform, 'Plataforma no encontrada.'
        )
    def __str__(self):
        return f"{self.title} - {self.platform}"
