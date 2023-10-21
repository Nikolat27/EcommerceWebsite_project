from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string

from .cartfunction import Cart
from product_app.models import Product


# Create your views here.

def cart_list(request):
    cart_list = Cart(request)
    return render(request, "cart_app/cart_list.html", context={"cart_list": cart_list})


def cart_add(request, pk):
    if request.user.is_authenticated is False:
        return redirect("accounts_app:login_page")

    if request.method == "POST":
        product = get_object_or_404(Product, id=pk)
        color = request.POST.get("color")
        if not color:
            color = product.color.first().title
        quantity = request.POST.get("count")
        cart = Cart(request)
        print(color)
        print(quantity)
        cart.add(product=product, color=color, quantity=quantity)
        data = render_to_string("AjaxTemplates/add-to-cart-product-detail.html", {"cart": cart})

        return JsonResponse({"bool": True, "data": data, "totalcartitems": int(cart.len())})


def cart_update(request, pk):
    if request.user.is_authenticated is False:
        return redirect("accounts_app:login_page")

    if request.method == "POST":
        product = get_object_or_404(Product, id=pk)
        color = request.POST.get("color")
        if not color:
            color = product.color.first().title
        new_quantity = request.POST.get("count")
        cart = Cart(request)
        if new_quantity:
            cart.update(product=product, color=color, new_quantity=new_quantity)
        else:
            print("there is not new_quantity")

        return redirect("cart_app:cart_list")


def delete_product(request, pk):
    if request.user.is_authenticated is False:
        return redirect("home_app:main")

    cart = Cart(request)
    cart.delete(id=pk)
    data = render_to_string("AjaxTemplates/delete-cart-Ajax.html", {"cart": cart})
    return JsonResponse({"bool": True, "data": data, "totalcartitems": int(cart.len())})


def delete_cart_list(request, pk):
    if request.user.is_authenticated is False:
        return redirect("home_app:main")

    cart_list = Cart(request)
    cart_list.delete(id=pk)
    return redirect("cart_app:cart_list")

