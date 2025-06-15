from django.contrib import admin

from .models import Category, Product, Tag


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at", "updated_at"]
    search_fields = ["name"]
    ordering = ["name"]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at", "updated_at"]
    search_fields = ["name"]
    ordering = ["name"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "price", "created_at", "updated_at"]
    list_filter = ["created_at", "tags", "category"]
    search_fields = ["name", "description"]
    filter_horizontal = ["tags"]

    def get_queryset(self, request):
        return super().get_queryset(request).select_related("category")
