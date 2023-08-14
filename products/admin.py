from django.contrib import admin
from .models import Shirt,Product

# Register your models here.

# add models to the admin panel
class productAdmin(admin.ModelAdmin):
    readonly_fields = ("slug",)
    list_display = ("title","id", "brand", "category", "is_best_seller")
    list_filter = ("is_best_seller",)
    search_fields = ("title", "category", "brand",)

admin.site.register(Shirt)
admin.site.register(Product, productAdmin)