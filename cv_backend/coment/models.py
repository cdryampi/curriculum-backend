from django.db import models
from django.conf import settings

from django.utils.translation import gettext_lazy as _
from django_ckeditor_5.fields import CKEditor5Field

from django.contrib.auth.models import Permission

from django.contrib.auth import get_user_model



class Comment(models.Model):
    """
        Clase que representa a un comenantario
    """
    content = CKEditor5Field(
        verbose_name=_("Contenido"),
        help_text=_("Ingresa el texto del comentario."),
        null=True,
        blank=True,
        config_name='default'
    )
    publicado = models.BooleanField(
        default=True,
        verbose_name="Mostrar comentario",
        help_text= "¿Quieres mostrar el comentario?"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Fecha de creación")
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Fecha de actualización")
    )

    class Meta:
        abstract = True
        verbose_name = _("Comentario")
        verbose_name_plural = _("Comentarios")

class RegisteredUserComment(Comment):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_comments",
        verbose_name=_("Usuario"), help_text=_("El usuario que publicó el comentario.")
    )
    parent_comment = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.CASCADE, related_name="replies",
        verbose_name=_("Comentario padre"), help_text=_("Respuesta a un comentario existente.")
    )

    class Meta:
        verbose_name = _("Comentario de Usuario Registrado")
        verbose_name_plural = _("Comentarios de Usuarios Registrados")

        permissions = [
            ("can_create_guest_user_comment", "Can create registered user comment"),
            ("can_edit_guest_user_comment", "Can edit registered user comment"),
            ("can_delete_guest_user_comment", "Can delete registered user comment"),
        ]

class GuestUserComment(Comment):
    username = models.CharField(
        max_length=255,
        verbose_name=_("Nombre de usuario"),
        help_text=_("Introduce tu nombre de usuario.")
    )
    email = models.EmailField(
        blank=True,
        null=True,
        verbose_name=_("Correo electrónico"),
        help_text=_("Introduce tu correo electrónico (opcional).")
    )

    class Meta:
        verbose_name = _("Comentario de Usuario Invitado")
        verbose_name_plural = _("Comentarios de Usuarios Invitados")
