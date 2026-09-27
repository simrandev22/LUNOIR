from django.contrib import admin
from .models import Shoe


@admin.register(Shoe)
class ShoeAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "gender",
        "category",
        "price",
    )

    list_filter = (
        "gender",
        "category",
    )

    search_fields = (
        "name",
        "description",
    )