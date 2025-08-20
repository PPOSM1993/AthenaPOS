from django.contrib import admin
from .models import Category, Publisher, Product, Genre, Format


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(Format)
class FormatAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
    ordering = ("name",)


# --- INLINES PARA M2M ---
class ProductGenreInline(admin.TabularInline):
    model = Product.genres.through
    extra = 1
    verbose_name = "Género"
    verbose_name_plural = "Géneros"


class ProductFormatInline(admin.TabularInline):
    model = Product.formats.through
    extra = 1
    verbose_name = "Formato"
    verbose_name_plural = "Formatos"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id", "name", "product_type", "category", "publisher", "author",
        "isbn", "stock", "sale_price", "discount_percentage", "is_active",
        "get_genres", "get_formats",
    )
    list_filter = ("product_type", "category", "publisher", "is_active", "genres", "formats")
    search_fields = ("name", "author", "isbn")
    ordering = ("name",)
    readonly_fields = ("created_at", "updated_at")

    fieldsets = (
        ("Información General", {
            "fields": (
                "name", "product_type", "category", "publisher", "author", "isbn",
                "description", "language", "pages", "publication_date",
                "image", "is_active"
            )
        }),
        ("Stock y Precios", {
            "fields": (
                "stock", "purchase_price", "vat_percentage",
                "sale_price", "discount_percentage"
            )
        }),
        ("Tiempos", {
            "fields": ("created_at", "updated_at")
        }),
    )

    inlines = [ProductGenreInline, ProductFormatInline]  # 👈 Aquí agregamos los inlines

    def get_genres(self, obj):
        return ", ".join([g.name for g in obj.genres.all()])
    get_genres.short_description = "Géneros"

    def get_formats(self, obj):
        return ", ".join([f.name for f in obj.formats.all()])
    get_formats.short_description = "Formatos"
