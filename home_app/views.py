from django.http import HttpResponse
from django.shortcuts import render

from product_app.models import Product


# Create your views here.


def home_app(request):
    products = Product.objects.all()

    return render(request, "home_app/index.html", context={"products": products})
