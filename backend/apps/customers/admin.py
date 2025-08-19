# apps/customers/admin.py
from django.contrib import admin
from .models import Region, City, Customer


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "region")
    list_filter = ("region",)
    search_fields = ("name",)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "tax_id", "email", "phone", "region", "city", "is_active")
    list_filter = ("region", "city", "is_active")
    search_fields = ("first_name", "last_name", "tax_id", "email", "phone")
    ordering = ("first_name", "last_name")
    readonly_fields = ("created_at", "updated_at")
    fieldsets = (
        ("Datos personales", {"fields": ("first_name", "last_name", "tax_id")}),
        ("Contacto", {"fields": ("email", "phone", "address")}),
        ("Ubicación", {"fields": ("region", "city")}),
        ("Otros", {"fields": ("is_active", "created_at", "updated_at")}),
    )
