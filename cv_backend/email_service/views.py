from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from base_user.models import UserProfile
from .utils import return_message, send_back_email
from .serializers import SendEmailSerializer

class SendEmailView(generics.CreateAPIView):
    """
    Vista para enviar un correo al usuario del perfil autenticado y responder automáticamente.
    """
    serializer_class = SendEmailSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)  # Valida los datos antes de continuar

        name = serializer.validated_data["name"]
        email = serializer.validated_data["email"]
        message = serializer.validated_data["message"]

        try:
            user_profile = UserProfile.objects.get(user=request.user)
        except UserProfile.DoesNotExist:
            return Response({"error": "Perfil de usuario no encontrado"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            return_message(user_profile, name, email, message)
            send_back_email(user_profile, name, email, message)
            return Response({"mensaje": "Correo enviado con éxito"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
