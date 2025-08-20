from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import InventoryMovement
from .serializers import InventoryMovementSerializer
from .pagination import StandardResultsSetPagination

class InventoryMovementViewSet(viewsets.ModelViewSet):
    """
    CRUD completo para movimientos de inventario
    - Filtrado por producto, proveedor, tipo de movimiento y fecha
    - Búsqueda por nombre de producto
    """
    queryset = InventoryMovement.objects.select_related("product", "supplier").all()
    serializer_class = InventoryMovementSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["product", "supplier", "movement_type", "date"]
    search_fields = ["product__name", "supplier__name"]
    ordering_fields = ["date", "product__name", "quantity"]
