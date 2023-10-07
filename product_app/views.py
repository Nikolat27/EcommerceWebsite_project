from django.shortcuts import render, get_object_or_404
from .models import Product, Color


# Create your views here.


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    # related_products = Product.objects.filter(category__title=product.category.first().title)[:8]
    related_products = Product.objects.filter(category__in=product.category.all()).distinct()
    return render(request, "product_app/product_detail.html", context={"product": product, "related_products": related_products})
