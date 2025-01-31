from django.db import models
from base_user.models import UserProfile

class SocialMediaProfile(models.Model):
    """
    Modelo para gestionar perfiles de redes sociales de los usuarios.
    """
    # Definimos las opciones para los tipos de redes sociales
    SOCIAL_MEDIA_CHOICES = [
        ('facebook', 'Facebook'),
        ('twitter', 'Twitter'),
        ('instagram', 'Instagram'),
        ('linkedin', 'LinkedIn'),
        ('youtube', 'YouTube'),
        ('linkedin', 'LinkedIn'),
        ('github', 'GitHub'),
        ('stack_overflow', 'Stack Overflow'),
        ('dev_to', 'Dev.to')
        # Agrega más opciones según sea necesario
    ]

    user = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name='social_media_profiles'
    )
    social_media = models.CharField(
        max_length=20,
        choices=SOCIAL_MEDIA_CHOICES,
        verbose_name="Red Social",
        help_text="Selecciona la red social principal",
        default='Facebook'
    )
    profile_link = models.URLField(
        verbose_name="Enlace del Perfil",
        help_text="Enlace al perfil de la red social"
    )
    @property
    def red_social_readable(self):

        return self.SOCIAL_MEDIA_CHOICES.get(
            self.social_media,
            'Profesión no especificada'
        )
    
    class Meta:
        verbose_name = "Perfil de Red Social"
        verbose_name_plural = "Perfiles de Redes Sociales"

    def __str__(self):
        return f"{self.user.nombre}'s {self.social_media} profile"
