from django.contrib import admin
from .models import InventoryMovement

@admin.register(InventoryMovement)
class InventoryMovementAdmin(admin.ModelAdmin):
    list_display = ["product", "supplier", "movement_type", "quantity", "date"]
    list_filter = ["movement_type", "date", "supplier", "product"]
    search_fields = ["product__name", "supplier__name"]
    ordering = ["-date"]
