from rest_framework import serializers
from .models import *
import re
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ["id", "name"]


class CitySerializer(serializers.ModelSerializer):
    region = RegionSerializer(read_only=True)

    class Meta:
        model = City
        fields = ["id", "name", "region"]


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields =  '__all__'
        read_only_fields = ["id", "created_at", "updated_at"]

    # Validación del email
    def validate_email(self, value):
        try:
            validate_email(value)
        except ValidationError:
            raise serializers.ValidationError("El correo electrónico no es válido.")

        if (
            Customer.objects.filter(email=value)
            .exclude(pk=self.instance.pk if self.instance else None)
            .exists()
        ):
            raise serializers.ValidationError("Este correo ya está registrado.")
        return value

    # Validación del RUT / Tax ID (Chile)
    def validate_tax_id(self, value):
        if not re.match(r"^\d{7,8}-[\dkK]$", value):
            raise serializers.ValidationError("El RUT debe tener el formato XXXXXXXX-X")
        return value

    # Validación de número de teléfono
    def validate_phone(self, value):
        if not re.match(r"^\+?\d{9,15}$", value):
            raise serializers.ValidationError(
                "El teléfono debe contener entre 9 y 15 dígitos (puede incluir prefijo +)."
            )
        return value

    # Validación de tipo de cliente
    def validate_customer_type(self, value):
        if value not in ["persona", "empresa"]:
            raise serializers.ValidationError(
                "El tipo de cliente debe ser 'persona' o 'empresa'."
            )
        return value
