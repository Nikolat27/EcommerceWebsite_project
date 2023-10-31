import random
import uuid

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from persiantools.jdatetime import JalaliDate
import datetime
from .cartfunction import Cart
from product_app.models import Product
from .models import Order, OrderItem


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


def checkout(request):
    cart_list = Cart(request)
    return render(request, "cart_app/checkout.html", context={"cart_list": cart_list})


def order_creation(request):
    if request.method == "POST":
        cart = Cart(request)
        f_name = request.POST.get("f_name")
        l_name = request.POST.get("l_name")
        state = request.POST.get("state")
        city = request.POST.get("city")
        address = request.POST.get("address")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        opn = request.POST.get("optional_note")
        postal_code = request.POST.get("postal_code")
        order_number = random.randint(1000, 10000000)
        print(order_number)
        order = Order.objects.create(user=request.user, total_price=cart.total(), f_name=f_name, l_name=l_name,
                                     phone_number=phone, email=email, state=state, city=city, postal_code=postal_code
                                     , optional_notes=opn, address=address, order_number=order_number)
        for item in cart:
            OrderItem.objects.create(order=order, product=item['product'], color=item['color'],
                                     quantity=item['quantity'], price=item['price'])
            cart.remove_cart()

            return redirect("cart_app:order_detail", order.id)


def order_detail(request, pk):
    order = Order.objects.get(id=pk)
    return render(request, "cart_app/order-user-panel.html", context={"order": order})


def test1(request):
    # x = JalaliDate(datetime.date(2023, 10, 30))
    x = JalaliDate.to_jalali(2023, 5, 30)
    return HttpResponse(x)
