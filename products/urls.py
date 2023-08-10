from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"), #Home page
    path('products/<product>', views.product_category), #Suits product category
    path('signup', views.signup, name="signup"), #Signup page
    path('shop', views.shop, name="shop"), #Shop page
    path('contact', views.contact, name="contact"), #Contact page
    path('profile', views.profile, name="profile"), #Profile page

]
