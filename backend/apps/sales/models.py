from django.db import models
from apps.customers.models import Customer
from apps.products.models import Product
from django.core.validators import MinValueValidator


class Sale(models.Model):
    STATUS_CHOICES = (
        ("pending", "Pendiente"),     # carrito temporal
        ("completed", "Completada"),  # venta confirmada
        ("canceled", "Cancelada"),
    )
    PAYMENT_METHODS = (
        ("cash", "Efectivo"),
        ("card", "Tarjeta"),
        ("other", "Otro"),
    )

    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS, default="cash")
    
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    vat_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=19)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    notes = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"
        ordering = ["-date"]

    def __str__(self):
        return f"Venta #{self.id} - {self.customer}"

    def update_totals(self):
        """
        Calcula subtotal, IVA y total sumando los SaleItem.
        """
        items = self.items.all()
        self.subtotal = sum([item.total_price for item in items])
        self.total = self.subtotal + (self.subtotal * self.vat_percentage / 100)
        self.save()


class SaleItem(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        verbose_name = "Item de venta"
        verbose_name_plural = "Items de venta"

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"

    def save(self, *args, **kwargs):
        """
        Calcula el total por línea y actualiza la venta automáticamente.
        """
        if self.product:
            self.unit_price = self.product.sale_price
        self.total_price = self.unit_price * self.quantity
        super().save(*args, **kwargs)

        # Actualizamos los totales de la venta
        self.sale.update_totals()
