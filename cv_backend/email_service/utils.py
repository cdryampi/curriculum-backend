from django.core.mail import send_mail
from email_service.models import EmailConfig

def return_message(user_profile, name, email, message):
    """
    Envía un correo al propietario del perfil con el mensaje del usuario.
    """
    try:
        email_config = EmailConfig.objects.get(user_profile=user_profile)

        remitente = email_config.email_sender
        destinatario = user_profile.user.email
        asunto = f"Mensaje de contacto de {name}"

        mensaje = f"""
        De: {name} ({email})
        
        Mensaje:
        {message}

        ---------------------
        Mensaje enviado desde la página web.
        """

        send_mail(
            subject=asunto,
            message=mensaje,
            from_email=remitente,
            recipient_list=[destinatario],
            fail_silently=False,
        )

        return True

    except EmailConfig.DoesNotExist:
        raise Exception("No se ha configurado el email para este usuario.")

def send_back_email(user_profile, name, email, message):
    """
    Envía un correo de respuesta automática al usuario que envió el mensaje.
    """
    try:
        email_config = EmailConfig.objects.get(user_profile=user_profile)

        remitente = email_config.email_sender
        destinatario = email
        asunto = "Gracias por tu mensaje"

        mensaje = f"""
        Hola {name},

        {email_config.default_message}

        ---------------------
        Mensaje enviado automáticamente. No respondas a este correo.
        """

        send_mail(
            subject=asunto,
            message=mensaje,
            from_email=remitente,
            recipient_list=[destinatario],
            fail_silently=False,
        )

        return True

    except EmailConfig.DoesNotExist:
        raise Exception("No se ha configurado el email para este usuario.")
