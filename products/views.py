from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


def index(request):
    user = "elaheh"
    products = Product.objects.all().order_by('-id')[:4]
    product_number = 4
    product1= products[0]
    return render(request, 
                  "products/home.html", {
                      "name" : user,
                      "number" : product_number,
                      "products" : products,
                      "product1" : product1,
                      })

def product_category(request, product):
     if product == "suits" or product == "dresses" or product == "shirts" or product == "shoes":
         return HttpResponse(f"Here is the list of our {product}.")
     else:
        return HttpResponse("The page you are looking for doesn't exist.")
     
def signup(request):
    return render(request, "products/signup.html")

