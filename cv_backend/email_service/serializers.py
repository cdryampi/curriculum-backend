from rest_framework import serializers

class SendEmailSerializer(serializers.Serializer):
    """
    Serializador para enviar un correo al usuario del perfil autenticado y responder automáticamente.
    """
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    message = serializers.CharField()
