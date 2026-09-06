from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "section", "slug")
    list_filter = ("section",)
    search_fields = ("name",)
    prepopulated_fields = {
        "slug": ("name",)
    }
    ordering = ("section", "name")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "price",
        "stock",
        "is_available",
        "created_at",
    )

    list_filter = (
        "category__section",
        "category",
        "is_available",
    )

    search_fields = (
        "name",
        "description",
        "category__name",
    )

    list_editable = (
        "price",
        "stock",
        "is_available",
    )

    readonly_fields = (
        "created_at",
    )

    ordering = ("-created_at",)