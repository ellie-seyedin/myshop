from django.urls import path
from . import views

urlpatterns = [
    path('products', views.index),
    path('products/<product>', views.product_category)
]
