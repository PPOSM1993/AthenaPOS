from rest_framework import serializers
from .models import Category, Publisher, Product, Genre, Format
from stdnum import isbn


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = "__all__"


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class FormatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Format
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source="category", write_only=True, required=False
    )

    publisher = PublisherSerializer(read_only=True)
    publisher_id = serializers.PrimaryKeyRelatedField(
        queryset=Publisher.objects.all(), source="publisher", write_only=True, required=False
    )

    # Nuevos campos: géneros y formatos
    genres = GenreSerializer(many=True, read_only=True)
    genre_ids = serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.all(), source="genres", many=True, write_only=True, required=False
    )

    formats = FormatSerializer(many=True, read_only=True)
    format_ids = serializers.PrimaryKeyRelatedField(
        queryset=Format.objects.all(), source="formats", many=True, write_only=True, required=False
    )

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "product_type",
            "category",
            "category_id",
            "publisher",
            "publisher_id",
            "author",
            "isbn",
            "description",
            "language",
            "pages",
            "publication_date",
            "genres",
            "genre_ids",
            "formats",
            "format_ids",
            "stock",
            "purchase_price",
            "vat_percentage",
            "sale_price",
            "discount_percentage",
            "image",
            "is_active",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["created_at", "updated_at"]

    def validate(self, data):
        """
        Validaciones generales
        """
        product_type = data.get("product_type", getattr(self.instance, "product_type", None))
        isbn_value = data.get("isbn", getattr(self.instance, "isbn", None))
        purchase_price = data.get("purchase_price", getattr(self.instance, "purchase_price", None))
        sale_price = data.get("sale_price", getattr(self.instance, "sale_price", None))
        discount = data.get("discount_percentage", getattr(self.instance, "discount_percentage", None))
        stock = data.get("stock", getattr(self.instance, "stock", None))
        author = data.get("author", getattr(self.instance, "author", None))
        publisher = data.get("publisher", getattr(self.instance, "publisher", None))

        # Validación ISBN solo si es un libro
        if product_type == "book":
            if not isbn_value:
                raise serializers.ValidationError("Los libros deben tener un ISBN.")
            if not isbn.is_valid(isbn_value):
                raise serializers.ValidationError("El ISBN ingresado no es válido.")
            if not author:
                raise serializers.ValidationError("Los libros deben tener un autor.")
            if not publisher:
                raise serializers.ValidationError("Los libros deben tener una editorial.")

        # Precio de venta no puede ser menor que el de compra
        if sale_price is not None and purchase_price is not None:
            if sale_price < purchase_price:
                raise serializers.ValidationError("El precio de venta no puede ser menor al precio de compra.")

        # Descuento entre 0 y 100
        if discount is not None and (discount < 0 or discount > 100):
            raise serializers.ValidationError("El descuento debe estar entre 0 y 100%.")

        # Stock no negativo
        if stock is not None and stock < 0:
            raise serializers.ValidationError("El stock no puede ser negativo.")

        return data


    def create(self, validated_data):
        genres = validated_data.pop("genres", [])
        formats = validated_data.pop("formats", [])
        product = super().create(validated_data)
        if genres:
            product.genres.set(genres)
        if formats:
            product.formats.set(formats)
        return product

    def update(self, instance, validated_data):
        genres = validated_data.pop("genres", None)
        formats = validated_data.pop("formats", None)
        product = super().update(instance, validated_data)
        if genres is not None:
            product.genres.set(genres)
        if formats is not None:
            product.formats.set(formats)
        return product