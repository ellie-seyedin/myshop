from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Brand, Feedback
from .forms import FeedbackForm
from django.contrib import messages
from django.views import View

class IndexView(View):
    def get(self, request):
        user = "elaheh"
        product_number = 4
        products = Product.objects.all().order_by('-id')[:4]
        return render(request, 
                   "products/home.html", {
                      "name" : user,
                      "number" : product_number,
                      "products" : products,
                      })
    def post(self, request):
     pass
def index(request):
          user = "elaheh"
          product_number = 4
          products = Product.objects.all().order_by('-id')[:4]
          return render(request, 
                   "products/home.html", {
                      "name" : user,
                      "number" : product_number,
                      "products" : products,
                      })
    

def product_category(request, product):
     if product == "suits" or product == "dresses" or product == "shirts" or product == "shoes":
         return HttpResponse(f"Here is the list of our {product}.")
     else:
        return HttpResponse("The page you are looking for doesn't exist.")
     
def signup(request):
    return render(request, "products/signup.html")

class ProductPageView(View):
    def get(self, request, product_brand, product_slug):
         product = Product.objects.get(slug = product_slug)
         if Feedback.objects.filter(product=product, id=1).exists():   
            my_feedback = Feedback.objects.get(product = product, id=1)
            form = FeedbackForm(instance = my_feedback)
         else:
            form = FeedbackForm()    
         reviews = Feedback.objects.filter(product = product)
         return render(request, "products/product.html", {
         "product":product,
          "form":form, 
          "reviews":reviews
    })

    def post(self, request, product_brand, product_slug):
        product = Product.objects.get(slug = product_slug)
        my_feedback = Feedback.objects.get(product = product)
        form = FeedbackForm(request.POST,instance = my_feedback)
        reviews = Feedback.objects.filter(product = product)
        if form.is_valid():
            form.save()
            messages.success(request, "Your feedback was submitted successfully.")

        return render(request, "products/product.html", {
         "product":product,
          "form":form, 
          "reviews":reviews
    })

   