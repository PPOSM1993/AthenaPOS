from rest_framework import serializers
from .models import Supplier, Region, City

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = "__all__"
        read_only_fields = ["created_at", "updated_at"]

    def validate_email(self, value):
        if Supplier.objects.filter(email=value).exists():
            raise serializers.ValidationError("Este correo ya está registrado.")
        return value

    def validate_phone(self, value):
        if Supplier.objects.filter(phone=value).exists():
            raise serializers.ValidationError("Este teléfono ya está registrado.")
        return value

    def validate_tax_id(self, value):
        if value and Supplier.objects.filter(tax_id=value).exists():
            raise serializers.ValidationError("Este RUT ya está registrado.")
        return value
