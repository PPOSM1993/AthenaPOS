from django.contrib import admin
from .models import Sale, SaleItem

class SaleItemInline(admin.TabularInline):
    model = SaleItem
    extra = 1
    readonly_fields = ["total_price", "unit_price"]

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ["id", "customer", "status", "payment_method", "subtotal", "total", "date"]
    list_filter = ["status", "payment_method", "date"]
    search_fields = ["customer__first_name", "customer__last_name", "customer__tax_id"]
    inlines = [SaleItemInline]

@admin.register(SaleItem)
class SaleItemAdmin(admin.ModelAdmin):
    list_display = ["sale", "product", "quantity", "unit_price", "total_price"]
    search_fields = ["product__name", "sale__customer__first_name", "sale__customer__last_name"]
