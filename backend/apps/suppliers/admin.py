from django.contrib import admin
from .models import Supplier, Region, City

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ["name", "tax_id", "email", "phone", "is_active", "region", "city"]
    list_filter = ["is_active", "region", "city"]
    search_fields = ["name", "email", "tax_id", "phone"]
    ordering = ["name"]

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ["name"]

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ["name", "region"]
    list_filter = ["region"]
