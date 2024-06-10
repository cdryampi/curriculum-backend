from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

# Create your views here.
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 4  # Display 4 skills per page
    page_size_query_param = 'page_size'
    max_page_size = 100

    def paginate_queryset(self, queryset, request, view=None):
        # Default ordering if not already specified
        if not hasattr(queryset, 'ordered') or not queryset.ordered:
            queryset = queryset.order_by('id')  # Default to ordering by 'id'
        return super().paginate_queryset(queryset, request, view=view)