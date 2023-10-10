from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string

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
        cart.add(product=product, color=color, quantity=quantity, override_quantity=override_quantity)
        cart = Cart(request)
        data = render_to_string("AjaxTemplates/add-to-cart-product-detail.html", {"cart": cart}, request)

        return JsonResponse({"bool": True, "data": data, "totalcartitems": int(cart.len())})


def delete_product(request, pk):
    if request.user.is_authenticated is False:
        return redirect("home_app:main")

    cart = Cart(request)
    cart.delete(id=pk)
    data = render_to_string("AjaxTemplates/delete-cart-Ajax.html", {"cart": cart})
    return JsonResponse({"bool": True, "data": data, "totalcartitems": int(cart.len())})


