from django.contrib import admin
from .models import Shirt

# Register your models here.

# add models to the admin panel
admin.site.register(Shirt)