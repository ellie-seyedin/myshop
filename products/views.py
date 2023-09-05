from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Brand, Feedback
from .forms import FeedbackForm
from django.contrib import messages


def index(request):
    user = "elaheh"
    products = Product.objects.all().order_by('-id')[:4]
    product_number = 4
    product1= products[0]
    #cross model query
    suits =Product.objects.filter(brand__title = "Ella", brand__id=1)
    print(suits)
    brnd = Brand.objects.get(title="Ella")
    suits = brnd.prd.all()
    print(suits)

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

def product_page(request, product_brand, product_slug):
    product = Product.objects.get(slug = product_slug)
    my_feedback = Feedback.objects.get(product = product, id=11)
    form = FeedbackForm(instance = my_feedback)
    reviews = Feedback.objects.filter(product = product)
    if request.method== "GET":

        return render(request, "products/product.html", {
        "product":product,
        "form":form, 
        "reviews":reviews
    })
    else:
        form = FeedbackForm(request.POST, instance = my_feedback)
        if form.is_valid():
            form.save()
            messages.success(request, "Your feedback was submitted successfully.")

        return render(request, "products/product.html", {
        "product":product,
        "form":form,
        "reviews" : reviews,
    })