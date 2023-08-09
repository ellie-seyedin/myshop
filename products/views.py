from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Welcome to my website!")

# def suits(request, product):
#      if product == "suits" or product == "dresses" or product == "shirts" or product == "shoes":
#          return HttpResponse(f"Here is the list of our {product}.")
#      else:
#         return HttpResponse("The page you are looking for doesn't exist.")