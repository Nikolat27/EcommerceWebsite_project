import random
from datetime import datetime

from persiantools.jdatetime import JalaliDate

from product_app.models import Product
from .models import Order, OrderItem, Address, Cart, CartItem
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string


# Create your views here.

@login_required
def ajax_template_generator(request):
    cart = Cart.objects.get(request.user)
    data = render_to_string("AjaxTemplates/cart_template_ajax.html", context={"cart": cart})
    return data


@login_required
def cart_page(request):
    cart = Cart.objects.get(user=request.user)
    return render(request, "cart_app/cart_list.html", context={"cart_list": cart})


@login_required
def cart_add(request, pk):
    if request.method == "POST":
        cart, created = Cart.objects.get_or_create(user=request.user)
        product = get_object_or_404(Product, id=pk)
        color = request.POST.get("color")
        quantity = request.POST.get("quantity", 1)

        if color:
            item, created = CartItem.objects.get_or_create(cart=cart, product=product, color=color)
        else:
            color = product.color.first().title
            item, created = CartItem.objects.get_or_create(cart=cart, product=product, color=color)

        if item:
            item.price = product.discounted_price()
            item.quantity += quantity
            item.save()

        data = ajax_template_generator(request=request)
        return JsonResponse({"data": data, "bool": True})


@login_required
def cart_add_store(request, pk):
    cart, created = Cart.objects.create(user=request.user)
    product = get_object_or_404(Product, id=pk)
    color = product.color.first().title
    if cart:
        item, created = CartItem.objects.get_or_create(cart=cart, product=product, color=color)
        if item:
            item.price = product.discounted_price()
            item.quantity += 1
            item.save()
            data = ajax_template_generator(request=request)
            return JsonResponse({"data": data, "bool": True})


@login_required
def cart_update(request, pk):
    if request.method == "POST":
        cart_item = get_object_or_404(CartItem, id=pk)
        quantity = request.POST.get("quantity")
        cart_item.quantity = quantity
        cart_item.save()
        data = ajax_template_generator(request=request)
        return JsonResponse({"data": data, "bool": True})


@login_required
def remove_from_cart(request, pk):
    cart_item = get_object_or_404(CartItem, id=pk)
    cart_item.delete()
    data = ajax_template_generator(request=request)
    return JsonResponse({"data": data, "bool": True})


@login_required
def checkout(request):
    cart_list = Cart(request)
    return render(request, "cart_app/checkout.html", context={"cart_list": cart_list})


@login_required
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


@login_required
def order_detail(request, pk):
    order = Order.objects.get(id=pk)
    return render(request, "cart_app/order-user-panel.html", context={"order": order})


@login_required
def view_factor(request, pk):
    order = Order.objects.get(id=pk)
    order_items = OrderItem.objects.get(id=order.id)
    return render(request, "cart_app/factor.html", context={"order": order, "product": order_items})


@login_required
def purchases(request):
    return render(request, "cart_app/purchases.html")


@login_required
def address(request):
    addresses = Address.objects.filter(user=request.user)
    if request.method == "POST":
        f_name = request.POST.get("fname")
        l_name = request.POST.get("lname")
        state = request.POST.get("state")
        city = request.POST.get("city")
        address = request.POST.get("address")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        next_page = request.GET.get("next")
        postal_code = request.POST.get("postal_code")
        Address.objects.create(user=request.user, fname=f_name, lname=l_name, email=email, phone=phone, address=address,
                               city=city, state=state, postal_code=postal_code)
        if next_page:
            return redirect(next_page)
        return render(request, "cart_app/address.html", context={"addresses": addresses})
    return render(request, "cart_app/address.html", context={"addresses": addresses})


@login_required
def edit_address(request, pk):
    address = Address.objects.get(id=pk, user=request.user)
    if request.method == "POST":
        f_name = request.POST.get("fname")
        l_name = request.POST.get("lname")
        state = request.POST.get("state")
        city = request.POST.get("city")
        address = request.POST.get("address")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        postal_code = request.POST.get("postal_code")
        next_page = request.GET.get("next")
        if f_name:
            x = Address.objects.get(id=pk, user=request.user)
            x.fname = f_name
            x.save()

        if l_name:
            x = Address.objects.get(id=pk, user=request.user)
            x.lname = l_name
            x.save()

        if state:
            x = Address.objects.get(id=pk, user=request.user)
            x.state = state
            x.save()

        if city:
            x = Address.objects.get(id=pk, user=request.user)
            x.city = city
            x.save()

        if address:
            x = Address.objects.get(id=pk, user=request.user)
            x.address = address
            x.save()

        if phone:
            x = Address.objects.get(id=pk, user=request.user)
            x.phone = phone
            x.save()

        if email:
            x = Address.objects.get(id=pk, user=request.user)
            x.fname = f_name
            x.save()

        if postal_code:
            x = Address.objects.get(id=pk, user=request.user)
            x.email = email
            x.save()

        if next_page:
            return redirect(next_page)
        else:
            return redirect("home_app:main")
    return render(request, "cart_app/edit_address.html", context={"address": address})


def test1(request):
    today = datetime.today()
    product = Product.objects.get(id=1)
    j_date = JalaliDate.to_jalali(product.created_at.date())

    # Convert the JalaliDate to a string
    jalali_date_string = j_date.strftime('%Y-%m-%d')

    # Convert the string back to a datetime object
    jalali_date_object = datetime.strptime(jalali_date_string, '%Y-%m-%d')

    # Get the day of the week (Monday is 0 and Sunday is 6)
    day_of_week = jalali_date_object.weekday()

    # Create a list of weekdays as per your requirement
    weekdays = ['4 shanbe', '2 shanbe', '3 shanbe', '4 shanbe', '5 shanbe', 'jomeh', '3 shanbe']

    # Get the actual day of the week from the list
    actual_day = weekdays[day_of_week]

    # Print the result
    return HttpResponse(actual_day)
