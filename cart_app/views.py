from django.shortcuts import render, redirect, get_object_or_404
from .cartfunction import Cart
from product_app.models import Product


# Create your views here.


def cart_add(request, pk):
    if request.user.is_authenticated is False:
        return redirect("accounts_app:login_page")

    if request.method == "POST":
        product = get_object_or_404(Product, id=pk)
        color = request.POST.get("color")
        if not color:
            color = product.color.first().name
        override_quantity = request.POST.get("override")
        quantity = request.POST.get("quantity")
        cart = Cart(request)
        print(color)
        print(quantity)
        cart.add(product, color, quantity, override_quantity=override_quantity)
        return redirect("home_app:main")


def delete_product(request, pk):
    if request.user.is_authenticated is False:
        return redirect("home_app:main")

    cart = Cart(request)
    cart.delete(id=pk)

    return redirect("home_app:main")




