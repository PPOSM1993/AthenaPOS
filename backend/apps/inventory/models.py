from django.db import models
from apps.products.models import Product
from apps.suppliers.models import Supplier
from django.utils import timezone

class InventoryMovement(models.Model):
    MOVEMENT_TYPES = (
        ("in", "Entrada"),
        ("out", "Salida"),
    )

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="movements")
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, blank=True)
    movement_type = models.CharField(max_length=3, choices=MOVEMENT_TYPES)
    quantity = models.IntegerField()
    note = models.TextField(blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Movimiento de Inventario"
        verbose_name_plural = "Movimientos de Inventario"
        ordering = ["-date"]

    def __str__(self):
        return f"{self.product.name} - {self.movement_type} - {self.quantity}"

    def save(self, *args, **kwargs):
        """
        Actualiza stock del producto al guardar un movimiento
        """
        super().save(*args, **kwargs)
        if self.movement_type == "in":
            self.product.stock += self.quantity
        elif self.movement_type == "out":
            self.product.stock -= self.quantity
        self.product.save()
