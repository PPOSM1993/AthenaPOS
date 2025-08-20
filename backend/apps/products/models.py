from django.db import models
from apps.customers.models import Region  # si quieres relacionar promociones por región
from django.core.validators import MinValueValidator, MaxValueValidator
from stdnum import isbn  # Validación de ISBN chileno/internacional


class Category(models.Model):
    """
    Categorías de productos: Libro, Agenda, Juego de Mesa, Marcador, etc.
    """
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    def __str__(self):
        return self.name


class Publisher(models.Model):
    """
    Editoriales de libros
    """
    name = models.CharField(max_length=150, unique=True)

    class Meta:
        verbose_name = "Editorial"
        verbose_name_plural = "Editoriales"

    def __str__(self):
        return self.name


class Genre(models.Model):
    """
    Géneros de libros: Novela, Ciencia Ficción, Infantil, etc.
    """
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Género"
        verbose_name_plural = "Géneros"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Format(models.Model):
    """
    Formato de productos: Físico, Digital, Audiolibro, etc.
    """
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Formato"
        verbose_name_plural = "Formatos"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Product(models.Model):
    PRODUCT_TYPES = (
        ("book", "Libro"),
        ("agenda", "Agenda"),
        ("game", "Juego de Mesa"),
        ("stationery", "Artículos de Papelería"),
        ("other", "Otro"),
    )

    name = models.CharField("Nombre del producto", max_length=255)
    product_type = models.CharField(
        "Tipo de producto", max_length=20, choices=PRODUCT_TYPES, default="other"
    )
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True
    )
    publisher = models.ForeignKey(
        Publisher, on_delete=models.SET_NULL, null=True, blank=True
    )
    author = models.CharField("Autor", max_length=255, blank=True, null=True)
    isbn = models.CharField("ISBN", max_length=20, blank=True, null=True, unique=True)
    description = models.TextField("Descripción", blank=True, null=True)
    language = models.CharField("Idioma", max_length=50, blank=True, null=True)
    pages = models.PositiveIntegerField("Número de páginas", blank=True, null=True)
    publication_date = models.DateField("Fecha de publicación", blank=True, null=True)

    # Nuevos campos
    genres = models.ManyToManyField(Genre, verbose_name="Géneros", blank=True)
    formats = models.ManyToManyField(Format, verbose_name="Formatos", blank=True)

    stock = models.PositiveIntegerField("Stock", default=0)
    purchase_price = models.DecimalField(
        "Precio de compra", max_digits=10, decimal_places=2, default=0
    )
    vat_percentage = models.DecimalField(
        "IVA (%)", max_digits=5, decimal_places=2, default=19,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    sale_price = models.DecimalField(
        "Precio de venta", max_digits=10, decimal_places=2, default=0
    )
    discount_percentage = models.DecimalField(
        "Descuento (%)", max_digits=5, decimal_places=2, default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    image = models.ImageField("Imagen del producto", upload_to="products/", blank=True, null=True)
    is_active = models.BooleanField("Activo", default=True)
    created_at = models.DateTimeField("Fecha de creación", auto_now_add=True)
    updated_at = models.DateTimeField("Última actualización", auto_now=True)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ["name"]

    def __str__(self):
        return self.name

    def clean(self):
        """
        Validación de ISBN si es libro
        """
        if self.product_type == "book" and self.isbn:
            if not isbn.is_valid(self.isbn):
                from django.core.exceptions import ValidationError
                raise ValidationError("El ISBN ingresado no es válido.")
