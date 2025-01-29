from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
# Create your views here.

class CustomAuthToken(ObtainAuthToken):
    """
        Clase encargada de manejar la autenticación personalizada y retornar el token de autenticación
    """
    def post(self, request, *args, **kwargs):
        """
            Método que se encarga de manejar la petición POST y retornar el token de autenticación
        """
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
    
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 4  # Display 4 skills per page
    page_size_query_param = 'page_size'
    max_page_size = 100

    def paginate_queryset(self, queryset, request, view=None):
        # Default ordering if not already specified
        if not hasattr(queryset, 'ordered') or not queryset.ordered:
            queryset = queryset.order_by('id')  # Default to ordering by 'id'
        return super().paginate_queryset(queryset, request, view=view)