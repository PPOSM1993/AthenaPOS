from rest_framework import serializers
from .models import Sale, SaleItem
from apps.products.models import Product


class SaleItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleItem
        fields = ["id", "product", "quantity", "unit_price", "total_price"]
        read_only_fields = ["unit_price", "total_price"]

    def validate_quantity(self, value):
        product = self.initial_data.get("product")
        if product:
            product_obj = Product.objects.get(pk=product)
            if value > product_obj.stock:
                raise serializers.ValidationError(
                    f"No hay suficiente stock para {product_obj.name}. Stock disponible: {product_obj.stock}"
                )
        return value

    def create(self, validated_data):
        item = super().create(validated_data)
        # Actualiza los totales de la venta automáticamente
        item.sale.update_totals()
        return item

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        instance.sale.update_totals()
        return instance


class SaleSerializer(serializers.ModelSerializer):
    items = SaleItemSerializer(many=True)

    class Meta:
        model = Sale
        fields = [
            "id", "customer", "date", "status", "payment_method",
            "subtotal", "vat_percentage", "total", "notes", "items"
        ]
        read_only_fields = ["subtotal", "total", "date"]

    def create(self, validated_data):
        items_data = validated_data.pop("items", [])
        sale = Sale.objects.create(**validated_data)
        for item_data in items_data:
            SaleItem.objects.create(sale=sale, **item_data)
        sale.update_totals()
        return sale

    def update(self, instance, validated_data):
        items_data = validated_data.pop("items", None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if items_data is not None:
            # Opcional: eliminamos items no enviados y actualizamos/creamos los nuevos
            instance.items.all().delete()
            for item_data in items_data:
                SaleItem.objects.create(sale=instance, **item_data)
            instance.update_totals()

        return instance
