from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    user = "elaheh"
    product_number = 4
    return render(request, "products/home.html", {"name" : user, "number" : product_number})

def product_category(request, product):
     if product == "suits" or product == "dresses" or product == "shirts" or product == "shoes":
         return HttpResponse(f"Here is the list of our {product}.")
     else:
        return HttpResponse("The page you are looking for doesn't exist.")
     
def signup(request):
    return render(request, "products/signup.html")

     
def shop(request):
    return render(request, "products/shop.html")

     
def contact(request):
    return render(request, "products/contact.html")

     
def profile(request):
    return render(request, "products/profile.html")
