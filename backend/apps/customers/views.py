# customers/views.py
from rest_framework import viewsets, filters, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from .serializers import CustomerSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint para gestionar Clientes
    - CRUD completo (listar, crear, actualizar, eliminar)
    - Búsqueda por nombre, apellido, email y RUT
    - Filtros dinámicos por tipo de cliente o región
    """
    queryset = Customer.objects.all().order_by("-created_at")
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]

    # Agregamos filtros y búsquedas
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["region", "city"]  # filtros exactos
    search_fields = ["first_name", "last_name", "email", "tax_id"]  # búsquedas parciales
    ordering_fields = ["first_name", "last_name", "created_at"]  # ordenar por campos

    def create(self, request, *args, **kwargs):
        """
        Sobrescribimos create para manejar errores de validación
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(
            {"message": "Cliente creado exitosamente", "data": serializer.data},
            status=status.HTTP_201_CREATED,
        )

    def update(self, request, *args, **kwargs):
        """
        Sobrescribimos update para devolver mensajes más claros
        """
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(
            {"message": "Cliente actualizado correctamente", "data": serializer.data},
            status=status.HTTP_200_OK,
        )

    def destroy(self, request, *args, **kwargs):
        """
        Eliminación lógica opcional: se puede cambiar a 'is_active = False'
        si queremos mantener historial
        """
        instance = self.get_object()
        instance.delete()
        return Response(
            {"message": "Cliente eliminado exitosamente"},
            status=status.HTTP_204_NO_CONTENT,
        )
