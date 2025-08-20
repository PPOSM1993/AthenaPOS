from rest_framework import viewsets, filters, status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from .models import Sale, SaleItem
from .serializers import SaleSerializer, SaleItemSerializer
from .pagination import StandardResultsSetPagination


class SaleViewSet(viewsets.ModelViewSet):
    """
    CRUD completo para Ventas.
    - Filtrado por cliente, fecha, estado y método de pago.
    - Soporta búsqueda por nombre o RUT del cliente.
    - Incluye items de venta.
    """
    queryset = Sale.objects.prefetch_related("items__product").all().order_by("-date")
    serializer_class = SaleSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["status", "payment_method", "date"]
    search_fields = ["customer__first_name", "customer__last_name", "customer__tax_id"]
    ordering_fields = ["date", "total", "customer__first_name"]

    def create(self, request, *args, **kwargs):
        """
        Crear venta o carrito temporal
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(
            {"message": "Venta creada exitosamente", "data": serializer.data},
            status=status.HTTP_201_CREATED,
        )

    def update(self, request, *args, **kwargs):
        """
        Actualiza venta y recalcula totales
        """
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(
            {"message": "Venta actualizada correctamente", "data": serializer.data},
            status=status.HTTP_200_OK,
        )

    def destroy(self, request, *args, **kwargs):
        """
        Eliminación lógica opcional
        """
        instance = self.get_object()
        instance.delete()
        return Response(
            {"message": "Venta eliminada exitosamente"},
            status=status.HTTP_204_NO_CONTENT,
        )


class SaleSearchView(generics.ListAPIView):
    """
    Búsqueda avanzada de ventas.
    - Por nombre o RUT del cliente
    - Por fecha o estado
    """
    serializer_class = SaleSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = Sale.objects.prefetch_related("items__product").all()
        q = self.request.query_params.get("q", "").strip()  # nombre o RUT cliente
        status_filter = self.request.query_params.get("status")
        date_filter = self.request.query_params.get("date")

        if q:
            queryset = queryset.filter(
                Q(customer__first_name__icontains=q) |
                Q(customer__last_name__icontains=q) |
                Q(customer__tax_id__icontains=q)
            )
        if status_filter:
            queryset = queryset.filter(status=status_filter)
        if date_filter:
            queryset = queryset.filter(date__date=date_filter)  # YYYY-MM-DD

        return queryset.order_by("-date")
