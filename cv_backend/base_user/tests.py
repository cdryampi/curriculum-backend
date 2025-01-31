from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from .models import UserProfile

User = get_user_model()

class UserTokenTest(TestCase):

    def test_token_is_created_for_new_user(self):
        """
        Verifica que al crear un usuario, se genere automáticamente un token de autenticación.
        """
        user = User.objects.create_user(username="testuser", password="testpassword")

        token = Token.objects.get(user=user) # recuperar el token del usuario, en teoría debería existir porque el signal lo crea automáticamente.

        self.assertIsNotNone(token)
        print(f"✔ Token generado correctamente: {token.key}")

    def test_profile_is_created_for_new_user(self):
        """
        Verifica que al crear un usuario, su perfil también se cree automáticamente.
        """
        user = User.objects.create_user(username="testuser2", password="testpassword")
        profile = UserProfile.objects.get(user=user)

        self.assertIsNotNone(profile)
        print(f"✔ Perfil generado correctamente para {user.username}")

    def test_user_can_authenticate_with_token(self):
        """
        Verifica que el usuario pueda autenticarse correctamente con su token.
        """
        user = User.objects.create_user(username="testuser3", password="testpassword")
        token = Token.objects.get(user=user)

        response = self.client.get("/base/userprofile/private/", HTTP_AUTHORIZATION=f"Token {token.key}")

        self.assertEqual(response.status_code, 200)
        print(f"✔ Autenticación con token exitosa para {user.username}")

