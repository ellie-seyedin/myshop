from django.contrib import admin
from .models import Product, Brand, Address, Category, Feedback

# Register your models here.

# add models to the admin panel
class productAdmin(admin.ModelAdmin):
    readonly_fields = ("slug",)
    list_display = ("title","id", "brand", "is_best_seller")
    list_filter = ("is_best_seller",)
    search_fields = ("title", "category", "brand",)

admin.site.register(Brand)
admin.site.register(Feedback)
admin.site.register(Category)
admin.site.register(Product, productAdmin)
admin.site.register(Address)