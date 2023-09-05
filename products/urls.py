from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name="home"), #Home page
    path('products/<product>', views.product_category, name="productcat"), #Suits product category
    path('signup', views.signup, name="signup"), #Signup page
    path('products/<product_brand>/<product_slug>', views.ProductPageView.as_view(), name="product_page")
    ]
