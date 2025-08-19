from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Región"
        verbose_name_plural = "Regiones"

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100)
    region = models.ForeignKey(
        Region, on_delete=models.CASCADE, related_name="cities"
    )

    class Meta:
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"
        unique_together = ("name", "region")

    def __str__(self):
        return f"{self.name}, {self.region.name}"


class Customer(models.Model):
    # Datos personales
    first_name = models.CharField("Nombre", max_length=100)
    last_name = models.CharField("Apellido", max_length=100)

    # Identificación
    tax_id = models.CharField("RUT", max_length=20, unique=True)

    # Contacto
    email = models.EmailField("Correo electrónico", unique=True)
    phone = models.CharField("Teléfono", max_length=20, blank=True, null=True)
    address = models.CharField("Dirección", max_length=255, blank=True, null=True)

    # Ubicación
    region = models.ForeignKey(
        Region, on_delete=models.SET_NULL, null=True, blank=True
    )
    city = models.ForeignKey(
        City, on_delete=models.SET_NULL, null=True, blank=True
    )

    # Info adicional
    created_at = models.DateTimeField("Fecha de creación", auto_now_add=True)
    updated_at = models.DateTimeField("Última actualización", auto_now=True)
    is_active = models.BooleanField("Activo", default=True)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ["first_name", "last_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.tax_id})"
