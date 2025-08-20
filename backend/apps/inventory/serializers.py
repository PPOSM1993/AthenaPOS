from rest_framework import serializers
from .models import InventoryMovement

class InventoryMovementSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source="product.name", read_only=True)
    supplier_name = serializers.CharField(source="supplier.name", read_only=True)

    class Meta:
        model = InventoryMovement
        fields = "__all__"
        read_only_fields = ["created_at", "updated_at", "product_name", "supplier_name"]

    def validate_quantity(self, value):
        if value <= 0:
            raise serializers.ValidationError("La cantidad debe ser mayor a cero")
        return value

    def validate(self, data):
        """
        Validación extra: no permitir salida mayor al stock actual
        """
        if data["movement_type"] == "out" and data["quantity"] > data["product"].stock:
            raise serializers.ValidationError("No hay suficiente stock para esta salida")
        return data
