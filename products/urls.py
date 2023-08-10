from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"), #Home page
    path('products/<product>', views.product_category, name="productcat"), #Suits product category
    path('signup', views.signup, name="signup"), #Signup page
    ]
