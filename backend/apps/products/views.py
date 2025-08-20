# products/views.py

from rest_framework import viewsets, filters, generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.db.models import Q

from .models import *
from .serializers import *
from .pagination import StandardResultsSetPagination


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name']

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all().order_by('name')
    serializer_class = GenreSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name']


class FormatViewSet(viewsets.ModelViewSet):
    queryset = Format.objects.all().order_by('name')
    serializer_class = FormatSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name']


class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all().order_by('name')
    serializer_class = PublisherSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'website']
    ordering_fields = ['name']

class ProductViewSet(viewsets.ModelViewSet):
    """
    CRUD completo para productos (libros, agendas, juegos, etc.)
    """
    queryset = Product.objects.select_related('publisher', 'category') \
                              .prefetch_related('genres', 'formats') \
                              .all() \
                              .order_by('-publication_date')
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = StandardResultsSetPagination

    # Filtros
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = {
        'publisher': ['exact'],
        'category': ['exact'],
        'genres__id': ['exact', 'in'],
        'formats__id': ['exact', 'in'],
        'language': ['exact', 'icontains'],
        'is_active': ['exact'],
    }

    # Búsqueda por texto
    search_fields = ['name', 'author', 'isbn', 'publisher__name', 'genres__name', 'formats__name']

    # Campos para ordenar
    ordering_fields = ['publication_date', 'name', 'sale_price', 'stock']
    ordering = ['-publication_date']  # Ordenamiento por defecto


class ProductSearchView(generics.ListAPIView):
    """
    Vista especializada para búsqueda libre de productos
    """
    queryset = Product.objects.filter(is_active=True).select_related('publisher').prefetch_related('genres')
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = self.queryset
        q = self.request.query_params.get('q', '').strip()
        if q:
            queryset = queryset.filter(
                Q(title__icontains=q) |
                Q(author__icontains=q) |
                Q(isbn__icontains=q) |
                Q(publisher__name__icontains=q) |
                Q(genres__name__icontains=q)
            ).distinct()
        return queryset.order_by('-release_date')
