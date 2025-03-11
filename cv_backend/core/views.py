from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.views.generic import TemplateView
from rest_framework import status
# Create your views here.

class IndexView(TemplateView):
    """
        Clase encargada de mostrar la página de inicio con los endpoints disponibles
    """
    def get(self, request, *args, **kwargs):
        """
            Método que se encarga de manejar la petición GET y retornar la página de inicio
                path('userprofile/<int:id>/', UserProfileDetailView.as_view(), name='userprofile-detail'),
                path('userprofile/', UserProfileListView.as_view(), name='userprofile-list'),
                path('userprofile/private/', UserProfilePrivateView.as_view(), name='userprofile-private'),
        """

        END_POINTS = {
            'Ver perfil de un usuario': 
            {
                'id':1,
                'url': '/userprofile/<int:id>/',
                'method': 'GET',
                'description': 'Muestra el perfil de un usuario específico',
                'params': 'id: int',
                'warning': 'Solo los usuarios autenticados pueden acceder a este endpoint'
            },

            'Ver lista de perfiles de usuario': 
            {
                'id':2,
                'url': '/userprofile/',
                'method': 'GET',
                'description': 'Muestra la lista de perfiles de usuario',
                'warning': 'Solo los usuarios autenticados pueden acceder a este endpoint'
            },
            'Ver perfil propio':
            {
                'id':3,
                'url': '/userprofile/private/',
                'method': 'GET',
                'description': 'Muestra el perfil del usuario autenticado',
                'warning': 'Solo los usuarios autenticados pueden acceder a este endpoint'
            },
        }
        is_login = False
        if request.user.is_authenticated:
            is_login = True

        return render(request, 'index.html', {'endpoints': END_POINTS, 'is_login': is_login})
    
class CustomAuthToken(ObtainAuthToken):
    """
    Vista personalizada para la autenticación con tokens.
    """
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        
        if not serializer.is_valid():
            return Response(
                {"error": "Credenciales inválidas"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        user = serializer.validated_data['user']

        # Si el usuario está inactivo, evitar que inicie sesión
        if not user.is_active:
            return Response(
                {"error": "Este usuario está inactivo."},
                status=status.HTTP_403_FORBIDDEN
            )

        # Generar o recuperar el token
        token, created = Token.objects.get_or_create(user=user)

        return Response(
            {
                "token": token.key,
                "user_id": user.pk,
                "username": user.username,
                "email": user.email,
            },
            status=status.HTTP_200_OK
        )
    
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 4  # Display 4 skills per page
    page_size_query_param = 'page_size'
    max_page_size = 100

    def paginate_queryset(self, queryset, request, view=None):
        # Default ordering if not already specified
        if not hasattr(queryset, 'ordered') or not queryset.ordered:
            queryset = queryset.order_by('id')  # Default to ordering by 'id'
        return super().paginate_queryset(queryset, request, view=view)