from django.db import models
from django.conf import settings
from django_ckeditor_5.fields import CKEditor5Field
from base_user.models import UserProfile
# Create your models here.

class EmailConfig(models.Model):
    """
        Clase que representa la configuración de los correos electrónicos asignados a un usuario.
    """
    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name='email_config'
    )
    email_sender = models.EmailField(
        "Mensaje por defecto",
        help_text='Introduce el correo electrónico que se usará para enviar los correos.'
    )
    default_message = models.CharField(
        max_length=100,
        help_text='Introduce el nombre que se mostrará como remitente de los correos.',
        default='Gracias por tu mensaje, te responderemos pronto.'
    )


    def __str__(self):
        return f"Configuración de {self.user_profile.user}"

    def save(self, *args, **kwargs):
        """
        Asegura que solo se pueda crear una configuración por usuario.
        También valida que el email no sea usado por otro usuario.
        """
        if not self.pk and EmailConfig.objects.filter(user_profile=self.user_profile).exists():
            raise Exception("Cada usuario solo puede tener una configuración de email.")

        if EmailConfig.objects.filter(email_sender=self.email_sender).exclude(user_profile=self.user_profile).exists():
            raise Exception("Este email ya está en uso por otro usuario.")

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Configuración de Correo"
        verbose_name_plural = "Configuraciones de Correo"
