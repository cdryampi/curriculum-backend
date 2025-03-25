from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from multimedia_manager.models import MediaFile, DocumentFile
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from colorfield.fields import ColorField


class CustomUser(AbstractUser):
    ROLES = [
        ('admin', 'Admin'),
        ('guest', 'Guest'),
        ('test', 'Test'),
    ]
    
    role = models.CharField(
        max_length=10,
        choices=ROLES,
        default='guest'
    )
    profile_image = models.ForeignKey(
        MediaFile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='foto_perfil_invitado',
        verbose_name=_("Foto de perfil"),
        help_text=_("Ingrese la foto de perfil para los comentarios.")
    )

    def get_absolute_url(self):
        return None
    
    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'

    def __str__(self):
        return self.username
    


class UserProfile(models.Model):
    """
        Modelo que representa a un usuario y su información personal.
    """
    PROFESIONES =[
        ('programador_web', 'Programador web'),
        ('administrador_sistemas', 'Administrador de sistemas'),
        ('programador_mobile', 'Programador Mobile'),
    ]

    nombre = models.CharField(
        max_length=100,
        blank=True, null=True,
        verbose_name="Nombre",
        help_text="Ingrese su nombre."
    )

    foto = models.ForeignKey(
        MediaFile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='foto_perfil',
        verbose_name="Foto de perfil",
        help_text="Ingrese la foto de perfil del CV."
    )
    apellido = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Apellido",
        help_text="Ingrese su apellido."
    )
    correo_electronico = models.EmailField(
        verbose_name="Correo Electrónico",
        help_text="Ingrese su correo electrónico.",
        unique=True,
        blank=True,
        null=True
    )
    resumen_habilidades = CKEditor5Field(
        verbose_name="Resumen profesional",
        help_text="Resume de forma breve tu perfil profesional.",
        null=True,
        blank=True,
        config_name='default'
    )
    description = CKEditor5Field(
        verbose_name="Descripción",
        help_text="Resume tu persona y tus aficiones.",
        null=True,
        blank=True,
        config_name='default'
    )
    profesion = models.CharField(
        max_length=100,
        choices=PROFESIONES,
        default="programador_web",
        verbose_name="Profesión",
        help_text="Escoge la profesión que quieras."
    )

    ciudad = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Ciudad",
        help_text="Ingrese la ciudad de residencia."
    )
    direccion = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name="Dirección",
        help_text="Ingrese su dirección."
    )
    telefono = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        verbose_name="Teléfono",
        help_text="Ingrese su número de teléfono."
    )
    edad = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="Edad",
        help_text="Ingrese su edad."
    )
    disponibilidad = models.BooleanField(
        default=True,
        verbose_name="¿Disponible?",
        help_text="¿Estás disponible para trabajar?"
    )
    resume_file = models.ForeignKey(
        DocumentFile,
        on_delete=models.SET_NULL,
        related_name='resume_files',
        null=True,
        blank=True,
        verbose_name="Archivo de Currículum"
    )
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile',
    )
    
    @property
    def profesion_readable(self):
        return self.PROFESIONES.get(self.profesion, 'Profesión no especificada')
    
    @property
    def get_meta(self):
        if self.meta:
            return self.meta
        return None
    
    @property
    def get_keywords(self):
        if self.keywords:
            return self.keywords
        return None
    
    @property
    def get_socials_media(self):
        if self.social_media_profiles:
            return self.social_media_profiles
        return None
    
    @property
    def get_education(self):
        if self.education:
            return self.education
        return None
    
    @property
    def get_skills(self):
        if self.skills:
            return self.skills
        return None
    
    @property
    def get_courses(self):
        if self.courses:
            return self.courses
        return None

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj
    
    def get_absolute_url(self):
        return None
    
    def __str__(self):
        return f"Perfil de Usuario para {self.user}"

    class Meta:
        verbose_name = "Perfil de Usuario"
        verbose_name_plural = "Perfil de Usuarios"

class Keywords(models.Model):
    """
        Clase que representa a un KeyWord para el SEO.
    """
    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name='keywords'
    )
    keyword = models.CharField(
        max_length=100,
        verbose_name="Palabra Clave"
    )

    class Meta:
        verbose_name = "Palabra Clave"
        verbose_name_plural = "Palabras Claves"

    def __str__(self):
        return f"{self.keyword} (Perfil de {self.user_profile})"

class Meta(models.Model):
    """
        Clase que representa a la información auxliar para el Seo de la web.
    """
    user_profile = models.OneToOneField(
        UserProfile,
        on_delete=models.CASCADE,
        related_name='meta'
    )
    meta_title = models.CharField(
        max_length=255,
        verbose_name="Título Meta"
    )
    meta_description = CKEditor5Field(
        verbose_name="Descripción",
        null=True,
        blank=True,
        config_name='default'
    )
    page_icon = models.ForeignKey(
        MediaFile,
        on_delete=models.SET_NULL,
        related_name='page_icons',
        null=True,
        blank=True,
        verbose_name="Icono de la Página"
    )
    favicon = models.ForeignKey(
        MediaFile,
        on_delete=models.SET_NULL,
        related_name='favicons',
        null=True,
        blank=True,
        verbose_name="Favicon"
    )
    meta_color = ColorField(
        default='#FF0000',
        verbose_name="Color de la Página",
        help_text="Escoge un color para la página."
    )


    class Meta:
        verbose_name = "Meta Datos"
        verbose_name_plural = "Meta Datos"

    def __str__(self):
        return f"Meta Datos de {self.user_profile}"